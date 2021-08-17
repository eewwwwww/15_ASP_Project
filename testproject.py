import unittest
import mean as prog

class TestMyProgram(unittest.TestCase):

    def test_total(self):
        data = [3637.2, 2782.2, 2939.2]
        result = prog.EvaluateMarks.total(data)
        self.assertEqual(result, 9358.599999999999)

    def test_mean(self):
        data = [322.81, 278.22, 293.92]
        result = prog.EvaluateMarks.mean(data)
        self.assertEqual(result, 298.31666666666666)

if __name__ == '__main__':
    unittest.main()
