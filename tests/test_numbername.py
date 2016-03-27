import unittest

import env

from numbername import to_number_name

class TestNumberName(unittest.TestCase):
    def test_ones(self):
        self.assertEqual(to_number_name(0), 'zero')
        self.assertEqual(to_number_name(1), 'one')
        self.assertEqual(to_number_name(2), 'two')
        self.assertEqual(to_number_name(3), 'three')
        self.assertEqual(to_number_name(4), 'four')
        self.assertEqual(to_number_name(5), 'five')
        self.assertEqual(to_number_name(6), 'six')
        self.assertEqual(to_number_name(7), 'seven')
        self.assertEqual(to_number_name(8), 'eight')
        self.assertEqual(to_number_name(9), 'nine')
        self.assertEqual(to_number_name(9), 'nine')

    def test_tens(self):
        self.assertEqual(to_number_name(10), 'ten')
        self.assertEqual(to_number_name(11), 'eleven')
        self.assertEqual(to_number_name(12), 'twelve')
        self.assertEqual(to_number_name(13), 'thirteen')
        self.assertEqual(to_number_name(14), 'fourteen')
        self.assertEqual(to_number_name(15), 'fifteen')
        self.assertEqual(to_number_name(16), 'sixteen')
        self.assertEqual(to_number_name(17), 'seventeen')
        self.assertEqual(to_number_name(18), 'eighteen')
        self.assertEqual(to_number_name(19), 'nineteen')
        self.assertEqual(to_number_name(20), 'twenty')
        self.assertEqual(to_number_name(30), 'thirty')
        self.assertEqual(to_number_name(40), 'forty')
        self.assertEqual(to_number_name(50), 'fifty')
        self.assertEqual(to_number_name(60), 'sixty')
        self.assertEqual(to_number_name(70), 'seventy')
        self.assertEqual(to_number_name(80), 'eighty')
        self.assertEqual(to_number_name(90), 'ninety')
        self.assertEqual(to_number_name(25), 'twenty five')
        self.assertEqual(to_number_name(88), 'eighty eight')
        self.assertEqual(to_number_name(67), 'sixty seven')
        self.assertEqual(to_number_name(99), 'ninety nine')

    def test_hundred(self):
        self.assertEqual(to_number_name(100), 'one hundred')
        self.assertEqual(to_number_name(110), 'one hundred ten')
        self.assertEqual(to_number_name(112), 'one hundred twelve')
        self.assertEqual(to_number_name(999), 'nine hundred '
            'ninety nine')
        self.assertEqual(to_number_name(501), 'five hundred one')


    def test_thousands(self):
        self.assertEqual(to_number_name(1000), 'one thousand')
        self.assertEqual(to_number_name(9999), 'nine thousand '
            'nine hundred ninety nine')
        self.assertEqual(to_number_name(5000), 'five thousand')
        self.assertEqual(to_number_name(5001), 'five thousand one')
        self.assertEqual(to_number_name(5050), 'five thousand fifty')
        self.assertEqual(to_number_name(5011), 'five thousand eleven')

    def test_mixed(self):
        self.assertEqual(to_number_name(5000000), 'five million')
        self.assertEqual(to_number_name(70023), 'seventy thousand '
            'twenty three')
        self.assertEqual(to_number_name(1230001), 'one million '
            'two hundred thirty thousand one')
        self.assertEqual(to_number_name(1231001), 'one million '
            'two hundred thirty one thousand one')
        self.assertEqual(to_number_name(10 ** 63), 'one vigintillion')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumberName)
    unittest.TextTestRunner(verbosity=2).run(suite)
