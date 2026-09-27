import pytest

pytest.importorskip("datasets")  # data builders need the `train` extra

from cyberjev.data import csic_to_text  # noqa: E402

# In CSIC, headers are joined by a literal backslash-n; only the body follows a real newline.


def test_csic_get_keeps_request_line_and_decodes():
    raw = (r"GET http://localhost:8080/tienda1/buscar.jsp?q=%27+OR+1%3D1 HTTP/1.1"
           r"\nUser-Agent: Mozilla/5.0\nHost: localhost:8080\nConnection: close\n")
    assert csic_to_text(raw) == "GET /tienda1/buscar.jsp?q=' OR 1=1 HTTP/1.1"


def test_csic_post_keeps_body():
    raw = (r"POST /tienda1/publico/vaciar.jsp HTTP/1.1\nUser-Agent: Mozilla/5.0"
           r"\nContent-Length: 17" "\nB2=Vaciar+carrito")
    assert csic_to_text(raw) == "POST /tienda1/publico/vaciar.jsp HTTP/1.1\nbody: B2=Vaciar carrito"
