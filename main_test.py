import pytest
from main import int_to_roman

# do not change this file

def test_int_to_roman():
    assert int_to_roman(3) == "III"
    assert int_to_roman(9) == "IX"
    assert int_to_roman(58) == "LVIII"
    assert int_to_roman(400) == "CD"
    assert int_to_roman(1994) == "MCMXCIV"
    assert int_to_roman(3999) == "MMMCMXCIX"
