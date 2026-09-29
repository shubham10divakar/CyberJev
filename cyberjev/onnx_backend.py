"""ONNX Runtime backend for CPU inference.

    python scripts/onnx_cpu.py --model runs/cyber-jev-v2-l6   # writes model.onnx, model.int8.onnx

`OnnxModel` quacks like the PyTorch model as far as `cyberjev.model.score` needs
(`model(**enc).logits`, `.eval()`), so the Decider runs on either. Needs `onnxruntime`
(the `onnx` extra); exporting also needs `onnx`.
"""

from pathlib import Path
from types import SimpleNamespace

import torch

INT8, FP32 = "model.int8.onnx", "model.onnx"


def available() -> bool:
    try:
        import onnxruntime  # noqa: F401
    except ImportError:
        return False
    return True


def find(folder: Path) -> Path | None:
    """The ONNX file to load from a model folder: int8 if present, else fp32, else None."""
    for name in (INT8, FP32):
        if (Path(folder) / name).exists():
            return Path(folder) / name
    return None


def export(model, tok, path: Path) -> None:
    """Export a PyTorch cross-encoder with dynamic batch and sequence length."""
    enc = tok(["question: q option: o"], ["GET / HTTP/1.1"], return_tensors="pt")
    names = [n for n in ("input_ids", "attention_mask", "token_type_ids") if n in enc]
    dyn = {n: {0: "batch", 1: "seq"} for n in names} | {"logits": {0: "batch"}}
    torch.onnx.export(model.cpu().eval(), tuple(enc[n] for n in names), str(path),
                      input_names=names, output_names=["logits"], dynamic_axes=dyn,
                      opset_version=17, dynamo=False)


def quantize(fp32: Path, int8: Path) -> None:
    """Dynamic int8 weight quantization (activations stay fp32)."""
    from onnxruntime.quantization import QuantType, quantize_dynamic

    quantize_dynamic(str(fp32), str(int8), weight_type=QuantType.QInt8)


class OnnxModel:
    def __init__(self, path: Path, threads: int | None = None):
        import onnxruntime as ort

        so = ort.SessionOptions()
        if threads:
            so.intra_op_num_threads = threads
        so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        self.path = Path(path)
        self.session = ort.InferenceSession(str(path), so, providers=["CPUExecutionProvider"])
        self.inputs = [i.name for i in self.session.get_inputs()]

    def eval(self):
        return self

    def __call__(self, **enc):
        feed = {k: v.cpu().numpy() for k, v in enc.items() if k in self.inputs}
        return SimpleNamespace(logits=torch.from_numpy(self.session.run(None, feed)[0]))
