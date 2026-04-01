from greeting import my_name
import pytest

@pytest.fixture
def juanes():
    return "My name is: Juanes"

@pytest.fixture
def ari():
    return "My name is: Ari"

def test_juanes(juanes):
    assert juanes == my_name("Juanes")
    
def test_ari(ari):
    assert ari == my_name("Ari")