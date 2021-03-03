import pytest

@pytest.mark.parametrize('temp', [38])
def test_temp(temp):
    assert temp < 37

