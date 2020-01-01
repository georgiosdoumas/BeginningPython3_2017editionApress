#!/usr/bin/python3.6
import unittest, mymath   # mymath.py should exist in the same folder
from subprocess import Popen, PIPE

class ProductTestCase(unittest.TestCase):
    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = mymath.product(x, y)
                self.assertEqual(p, x * y, 'Integer multiplication failed')
    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 5
                p = mymath.product(x, y)
                self.assertEqual(p, x * y, 'Float multiplication failed')
    def test_with_PyChecker(self):
        cmd = '/usr/bin/pychecker', '-Q', mymath.__file__.rstrip('c')
        pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pychecker.stdout.read(), b'')
    def test_with_PyLint(self):
        cmd = '/usr/bin/pylint-3.6', '-rn', 'mymath'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        self.assertEqual(pylint.stdout.read(), b'')

if __name__ == '__main__':
    unittest.main()
