import unittest
import marks as prog


def test_total(self):
    data = [45, 60, 70, 40, 80, 90, 55, 75, 20, 65]
    result = prog.EvaluateMarks.total(data)
    self.assertEqual(result, 500)

def test_mean(self):
        data = [45, 60, 70, 40, 80, 90, 55, 75, 20, 65]
        result = prog.EvaluateMarks.mean(data)
        self.assertEqual(result, 60)

if __name__ == '__main__':
    unittest.main()