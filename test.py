import unittest
import main

class TestMain(unittest.TestCase):
    def testMain(self):
        print("Testing main.py")
        main.run()
        print("Done testing main.py")

if __name__ == '__main__':
    unittest.main()

