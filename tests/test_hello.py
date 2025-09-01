import unittest
from test.hello import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("W0rld"), "Hello, World!")
        self.assertEqual(hello("テスト"), "Hello, テスト!")

if __name__ == "__main__":
    unittest.main()
