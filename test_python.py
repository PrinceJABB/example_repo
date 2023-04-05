

import numpy as np

class TestClass:
    def __init__(self):
        self._inner_function()

    def test_method(self):
        print("test_method")

    def _inner_function(self):
        print("inner_function")

if __name__ == "__main__":
    test = TestClass()
    test.test_method()