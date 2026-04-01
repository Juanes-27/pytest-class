from smath import subtract

def setup_function(function):
    print(f" Running Setup: {function.__name__} ")
    function.x = 10
    
def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x
    
### Run to see failed test
#def test_hello_subtract():
#   assert subtract(test_hello_subtract.x) == 12


def test_hello_subtract2():
    assert subtract(test_hello_subtract2.x) == 9