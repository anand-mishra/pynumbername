import unittest

import env

from src import numbername

class TestNumberName(unittest.TestCase):
    def test_ones(self):
        self.assertEqual(numbername.to_number_name(0), '') 
        self.assertEqual(numbername.to_number_name(1), 'one') 
        self.assertEqual(numbername.to_number_name(2), 'two') 
        self.assertEqual(numbername.to_number_name(3), 'three') 
        self.assertEqual(numbername.to_number_name(4), 'four') 
        self.assertEqual(numbername.to_number_name(5), 'five') 
        self.assertEqual(numbername.to_number_name(6), 'six') 
        self.assertEqual(numbername.to_number_name(7), 'seven') 
        self.assertEqual(numbername.to_number_name(8), 'eight') 
        self.assertEqual(numbername.to_number_name(9), 'nine') 
        self.assertEqual(numbername.to_number_name(9), 'nine') 

    def test_tens(self):
        self.assertEqual(numbername.to_number_name(10), 'ten') 
        self.assertEqual(numbername.to_number_name(11), 'eleven') 
        self.assertEqual(numbername.to_number_name(12), 'twelve') 
        self.assertEqual(numbername.to_number_name(13), 'thirteen') 
        self.assertEqual(numbername.to_number_name(14), 'fourteen') 
        self.assertEqual(numbername.to_number_name(15), 'fifteen') 
        self.assertEqual(numbername.to_number_name(16), 'sixteen') 
        self.assertEqual(numbername.to_number_name(17), 'seventeen') 
        self.assertEqual(numbername.to_number_name(18), 'eighteen') 
        self.assertEqual(numbername.to_number_name(19), 'nineteen') 
        self.assertEqual(numbername.to_number_name(20), 'twenty') 
        self.assertEqual(numbername.to_number_name(30), 'thirty') 
        self.assertEqual(numbername.to_number_name(40), 'forty') 
        self.assertEqual(numbername.to_number_name(50), 'fifty') 
        self.assertEqual(numbername.to_number_name(60), 'sixty') 
        self.assertEqual(numbername.to_number_name(70), 'seventy') 
        self.assertEqual(numbername.to_number_name(80), 'eighty') 
        self.assertEqual(numbername.to_number_name(90), 'ninety') 
        self.assertEqual(numbername.to_number_name(25), 'twenty five') 
        self.assertEqual(numbername.to_number_name(88), 'eighty eight') 
        self.assertEqual(numbername.to_number_name(67), 'sixty seven') 
        self.assertEqual(numbername.to_number_name(99), 'ninety nine') 

    def test_hundred(self):
        self.assertEqual(numbername.to_number_name(100), 'one hundred')
        self.assertEqual(numbername.to_number_name(110), 'one hundred ten')
        self.assertEqual(numbername.to_number_name(112), 'one hundred twelve')
        self.assertEqual(numbername.to_number_name(999), 'nine hundred '
            'ninety nine')
        self.assertEqual(numbername.to_number_name(501), 'five hundred one')


    def test_thousands(self):
        self.assertEqual(numbername.to_number_name(1000), 'one thousand')
        self.assertEqual(numbername.to_number_name(9999), 'nine thousand '
            'nine hundred ninety nine')
        self.assertEqual(numbername.to_number_name(5000), 'five thousand')
        self.assertEqual(numbername.to_number_name(5001), 'five thousand one')
        self.assertEqual(numbername.to_number_name(5050), 'five thousand fifty')
        self.assertEqual(numbername.to_number_name(5011), 'five thousand eleven')

    def test_mixed(self):
        self.assertEqual(numbername.to_number_name(5000000), 'five million')
        self.assertEqual(numbername.to_number_name(70023), 'seventy thousand '
            'twenty three')
        self.assertEqual(numbername.to_number_name(1230001), 'one million '
            'two hundred thirty thousand one')
        self.assertEqual(numbername.to_number_name(1231001), 'one million '
            'two hundred thirty one thousand one')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestNumberName)
    unittest.TextTestRunner(verbosity=2).run(suite)
