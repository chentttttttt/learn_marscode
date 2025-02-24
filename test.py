import unittest
from homework import process_array

class TestProcessArray(unittest.TestCase):

    def test_empty_array(self):
        # 测试空数组
        result = process_array([])
        self.assertEqual(result['mean'], 0)
        self.assertIsNone(result['max'])
        self.assertIsNone(result['min'])
        self.assertIsNone(result['mode'])
        self.assertIsNone(result['median'])

    def test_single_element_array(self):
        # 测试单元素数组
        result = process_array([5])
        self.assertEqual(result['mean'], 5)
        self.assertEqual(result['max'], 5)
        self.assertEqual(result['min'], 5)
        self.assertEqual(result['mode'], 5)
        self.assertEqual(result['median'], 5)

    def test_normal_array(self):
        # 测试正常数组
        arr = [1, 2, 3, 4, 5]
        result = process_array(arr)
        self.assertEqual(result['mean'], 3)
        self.assertEqual(result['max'], 5)
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['mode'], [1, 2, 3, 4, 5])
        self.assertEqual(result['median'], 3)

    def test_even_length_array(self):
        # 测试偶数长度数组
        arr = [1, 2, 3, 4]
        result = process_array(arr)
        self.assertEqual(result['mean'], 2.5)
        self.assertEqual(result['max'], 4)
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['mode'], [1, 2, 3, 4])
        self.assertEqual(result['median'], 2.5)

    def test_odd_length_array(self):
        # 测试奇数长度数组
        arr = [1, 2, 3, 4, 5, 6, 7]
        result = process_array(arr)
        self.assertEqual(result['mean'], 4)
        self.assertEqual(result['max'], 7)
        self.assertEqual(result['min'], 1)
        self.assertEqual(result['mode'], [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(result['median'], 4)

if __name__ == '__main__':
    unittest.main()
