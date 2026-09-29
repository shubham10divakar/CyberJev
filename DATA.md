# Data sources, licences and attribution

The files in `data/`, `data_heldout/` and `data_val/` are **built from the public datasets
below** by `python scripts/prepare_data.py` (current version: v6; details and checks in
[`plan/03_data.md`](plan/03_data.md)). Each example keeps a `source` field naming its dataset.
Every source keeps its **own licence**; this repository's Apache-2.0 licence covers the code
only.

- **Research use.** The built data is shared to make the results reproducible. Three sources
  state **no licence** (marked below); treat their rows as research-only and check with their
  authors before any other use.
- **Share-alike / attribution.** Rows from CC-BY, CC-BY-SA and ODC-BY sources remain under
  those terms: attribute the original authors, and share CC-BY-SA-derived rows alike.
- **Citation.** If you use the built data, please cite the original datasets and the
  Cyber-Jev paper (**in preparation**, see [README](README.md#citation)).

## `http_attack`

| Role | Dataset | Licence |
|---|---|---|
| train / calib / test | [bridge4/CSIC2010_dataset_classification](https://huggingface.co/datasets/bridge4/CSIC2010_dataset_classification) (CSIC 2010 HTTP dataset) | CSIC 2010 research terms |
| train / calib / test | [shengqin/web-attacks](https://huggingface.co/datasets/shengqin/web-attacks) | **none stated** |
| train / calib / test | [notesbymuneeb/ai-waf-dataset](https://huggingface.co/datasets/notesbymuneeb/ai-waf-dataset) | MIT |
| train / calib / test | [gretelai/synthetic_text_to_sql](https://huggingface.co/datasets/gretelai/synthetic_text_to_sql) (benign SQL) | Apache-2.0 |
| held-out | [zrmarine/sql_injection](https://huggingface.co/datasets/zrmarine/sql_injection) | **none stated** |
| held-out | [vyykaaa/dataset-web-attack](https://huggingface.co/datasets/vyykaaa/dataset-web-attack) | **none stated** |
| val | [puyang2025/waf_data_v2](https://huggingface.co/datasets/puyang2025/waf_data_v2) | MIT |
| val | [xlangai/spider](https://huggingface.co/datasets/xlangai/spider) (benign SQL) | CC-BY-SA-4.0 |

## `prompt_injection`

| Role | Dataset | Licence |
|---|---|---|
| train / calib / test | [S-Labs/prompt-injection-dataset](https://huggingface.co/datasets/S-Labs/prompt-injection-dataset) | MIT |
| train / calib / test | [neuralchemy/Prompt-injection-dataset](https://huggingface.co/datasets/neuralchemy/Prompt-injection-dataset) | Apache-2.0 |
| train / calib / test | [Simsonsun/JailbreakPrompts](https://huggingface.co/datasets/Simsonsun/JailbreakPrompts) | MIT |
| train / calib / test | [walledai/WildJailbreak](https://huggingface.co/datasets/walledai/WildJailbreak) (WildJailbreak eval split, AllenAI) | ODC-BY |
| train / calib / test | [Lakera/mosscap_prompt_injection](https://huggingface.co/datasets/Lakera/mosscap_prompt_injection) | MIT |
| train / calib / test | [saidutta69/awesome-chatgpt-prompts-clean](https://huggingface.co/datasets/saidutta69/awesome-chatgpt-prompts-clean) | CC0-1.0 |
| train / calib / test | [databricks/databricks-dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | CC-BY-SA-3.0 |
| train / calib / test | [yanismiraoui/prompt_injections](https://huggingface.co/datasets/yanismiraoui/prompt_injections) | Apache-2.0 |
| train / calib / test | [dmtrdr/russian_prompt_injections](https://huggingface.co/datasets/dmtrdr/russian_prompt_injections) | Apache-2.0 |
| train / calib / test | [mteb/MKQARetrieval](https://huggingface.co/datasets/mteb/MKQARetrieval) (MKQA questions, Apple) | CC-BY-3.0 |
| held-out | [deepset/prompt-injections](https://huggingface.co/datasets/deepset/prompt-injections) | Apache-2.0 |
| held-out | [jackhhao/jailbreak-classification](https://huggingface.co/datasets/jackhhao/jailbreak-classification) | Apache-2.0 |
| val | [TrustAIRLab/in-the-wild-jailbreak-prompts](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts) | MIT |

## `phishing_url`

| Role | Dataset | Licence |
|---|---|---|
| train / calib / test | [flwrlabs/fed-phishing-urls](https://huggingface.co/datasets/flwrlabs/fed-phishing-urls) | Apache-2.0 |
| held-out | [saidutta69/PhishTrap](https://huggingface.co/datasets/saidutta69/PhishTrap) | MIT |
| held-out | [phishdestroy/destroylist](https://huggingface.co/datasets/phishdestroy/destroylist) (pinned revision `42163edf`) | MIT |
| val | [JPxxx/url-benchmark-dataset](https://huggingface.co/datasets/JPxxx/url-benchmark-dataset) | Apache-2.0 |

Licences are as stated on each dataset card on 2026-09-29.
