from main import welcome 
import pytest

@pytest.mark.one 
def test_welcome(): 
    assert welcome(name='ahmed')=='hello ahmed'