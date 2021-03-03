import pytest

@pytest.mark.float
@pytest.mark.parametrize('temp', [38])
def test_temp(temp):
    assert temp < 37

@pytest.mark.float
def test_of_average():
    numbers = [13.3, 50.6, 17.4]
    assert sum(numbers) / len(numbers) > 20

@pytest.mark.float
def test_of_maximum():
    values = [2.8, 3.6, 7.9, 4.6, 5.7]
    assert min(values) > 2

@pytest.mark.dicts
def test_Kate_prof():
    professions = {'Mari': 'doctor', 'Kate': 'nurse'}
    assert professions['Kate'] == 'nurse'

@pytest.mark.dicts
def test_bonuses():
    bonus = {'Kate': 2000, 'Margo': 13800, 'Poline': 7000, \
             'Dave': 72000, 'Kris': 32500, 'Jane': 5000}
    assert sum(bonus.values()) < 150000

@pytest.mark.dicts
def test_need_to_do():
    tasks = {'done':['math', 'eng'], 'need':['literature']}
    assert tasks['need'] == []