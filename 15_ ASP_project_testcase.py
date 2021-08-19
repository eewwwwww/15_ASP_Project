import unittest
import result as prog

class TestMyProgram(unittest.TestCase):

    def test_total(self):
        data = [11163284, 9816149, 6549149, 4971870, 1180258, 951180, 680019, 292835, 166877, 123098, 86302, 42084, 14585 ]
        result = prog.EvaluateMarks.total(data)
        self.assertEqual(result, 36037690)

    def test_mean(self):
        data = [11163284, 9816149, 6549149, 4971870, 1180258, 951180, 680019, 292835, 166877, 123098, 86302, 42084, 14585]
        result = prog.EvaluateMarks.mean(data)
        self.assertEqual(result, 2772130.0)

if __name__ == '__main__':
    unittest.main()