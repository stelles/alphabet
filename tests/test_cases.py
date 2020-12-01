import unittest

from alphabet import Alphabet


class TestCases(unittest.TestCase):


	def test_example(self):
		# Example given by instructions
		given = [
			"bca",
			"aaa",
			"acb"
		]
		expected = ['b','a','c']
		self.assertEqual(Alphabet.determine_alphabet(given), expected)

	def test_me(self):
		## My own personal example
		given = [
			"ssm",
			"sam",
			"smm",
			"ass", # Unlucky
			"asa",
			"asm"
		]
		expected = ['s','a','m']
		self.assertEqual(Alphabet.determine_alphabet(given), expected)

if __name__ == '__main__':
    unittest.main()