import unittest

from alphabet import determine_alphabet


class TestAlphabet(unittest.TestCase):

	def test_size(self):
		# Assume alphabet is normal latin alphabet
		given = [
			"aaa",
			"abb",
			"abc"
		]
		# Validate that we're in the right order
		self.assertEqual(given, sorted(given))

		expected = ['a','b','c']
		self.assertEqual(determine_alphabet(given), expected)

	def test_size_reverse(self):
		# Assume alphabet is normal latin alphabet
		given = [
			"abc",
			"bc",
			"c"
		]
		# Validate that we're in the right order
		self.assertEqual(given, sorted(given))

		expected = ['a','b','c']
		self.assertEqual(determine_alphabet(given), expected)

	def test_missing(self):
		# Assume alphabet is normal latin alphabet
		given = [
			"aaa",
			"baa",
			"caa"
		]
		# Validate that we're in the right order
		self.assertEqual(given, sorted(given))

		expected = ['a','b','c']
		self.assertEqual(determine_alphabet(given), expected)

	def test_suffix_order(self):
		# Assume alphabet is normal latin alphabet
		given = [
			"aca",
			"acb",
			"acc",
		]
		# Validate that we're in the right order
		self.assertEqual(given, sorted(given))

		expected = ['a','b','c']
		self.assertEqual(determine_alphabet(given), expected)

	def test_prefix_order(self):
		# Assume alphabet is normal latin alphabet
		given = [
			"caa",
			"cab",
			"cac",
		]
		# Validate that we're in the right order
		self.assertEqual(given, sorted(given))

		expected = ['a','b','c']
		self.assertEqual(determine_alphabet(given), expected)

	def test_entire_prefix(self):
		# Assume alphabet is normal latin alphabet
		given = [
			"cbaa",
			"cbab",
			"cbac",
		]
		# Validate that we're in the right order
		self.assertEqual(given, sorted(given))

		expected = ['a','b','c']
		self.assertEqual(determine_alphabet(given), expected)

	@unittest.skip("Making bad assumptions")
	def test_bad_assumptions(self):
		# We cannot infer letter prioritization from this list
		# While a comes before ab, we cannot make any assertions on 'b'
		given = [
			"a",
			"ab",
			"abc",
		]
		# Validate that we're in the right order
		self.assertEqual(given, sorted(given))

		expected = ['a','b','c']
		self.assertEqual(determine_alphabet(given), expected)



if __name__ == '__main__':
    unittest.main()