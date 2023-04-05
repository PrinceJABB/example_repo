

import numpy as np

class TestClass:
    def __init__(self):
        self._inner_function()

    def test_nomethbod(self):
        print("test_nomethbod")

    def _inner_function(self):
        print("inner_function")

if __name__ == "__main__":
    test = TestClass()
    test.test_nomethbod()
    print('not good')