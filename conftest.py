import pytest

@pytest.fixture
def values_of_bonus():
    bonus = {'Kate':2000, 'Margo':13800, 'Poline':7000, \
             'Dave':72000, 'Kris':32500, 'Jane':5000}
    return sum(bonus.values())

