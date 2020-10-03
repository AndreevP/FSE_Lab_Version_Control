from storage import Storage

def test_add():
    pass

def test_remove():
    pass

def test_set():
    st = Storage({'a': 1})
    code = st.set('a', 2)
    assert code == 0, "Expected to recieve the zero success code, as the key is present, but got {}".format(code)
    assert st.get('a') == 2, "Expected to obtain the value that was set"
    code = st.set('b', 1)
    assert code == 1, "Expected to recieve an error code, as the key is not present, but got {}".format(code)
    assert st.get('b') is None, "An unexisting key should not be added after the set operation" 

def test_get():
    st = Storage({'a': 1, 'b': 2})
    key = 'b'
    val = st.get(key)
    assert val == 2, "Value for the key {} is not equal to expected".format(key)
    key = 'c'
    val = st.get(key)
    assert val is None, "Value for an unexisting key is not None"

def run_tests():
    test_add()
    test_remove()
    test_set()
    test_get()

if __name__ == "__main__":
    run_tests()
