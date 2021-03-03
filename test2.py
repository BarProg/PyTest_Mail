import pytest
import math

def test_of_average():
    numbers = [13.3, 50.6, 17.4]
    assert sum(numbers) / len(numbers) > 20
