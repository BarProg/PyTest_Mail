import pytest

def test_need_to_do():
    tasks = {'done':['math', 'eng'], 'need':['literature']}
    assert tasks['need'] == []