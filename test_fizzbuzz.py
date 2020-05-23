import unittest


# input หาร 3 ลงตัว จะได้ fizz
# input หาร 5 ลงตัว จะได้ buzz
# input หาร 3 และ 5 ลงตัวจะได้ fizzbuzz
# นอกนั้นจะได้เลขตัวเดิม

class TestFizzBuzz(unittest.TestCase):
    def test_get_one_when_input_is_one(self):
        result = fizzbuzz(1)
        self.assertEqual(result, 1)

    def test_get_four_when_input_is_four(self):
        result = fizzbuzz(4)
        self.assertEqual(result, 4)

    def test_get_fizz_when_input_is_three(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')

    def test_get_fizz_when_input_is_six(self):
        result = fizzbuzz(6)
        self.assertEqual(result, 'fizz')


def fizzbuzz(number):
    if number % 3 == 0:
        return 'fizz'

    return number


unittest.main()
