import pytest
from seasons import get_minutes

def test_invalid():
    with pytest.raises(TypeError):
        get_minutes(12-12-2012) == "Invalid date"
