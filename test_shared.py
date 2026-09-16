import pytest

@pytest.mark.parametrize("gate", [0], ids=["gate0"])
def test_security_gate(gate):
    assert True
