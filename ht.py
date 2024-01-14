import hello

def test_hello():
    assert hello.hello_world() == "Hello World!"
    
def test_helloN():
    assert hello.hello_world_n(3) == "Hello World! Hello World! Hello World!"