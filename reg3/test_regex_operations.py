import re
import unittest

class TestRegexOperations(unittest.TestCase):
    def test_match(self):
        # Testuje dopasowanie ciągu cyfr na początku tekstu
        pattern = r'\d+'
        text = "12345abc"
        match = re.match(pattern, text)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(), "12345")

    def test_search(self):
        # Testuje wyszukiwanie ciągu cyfr gdziekolwiek w tekście
        pattern = r'\d+'
        text = "abc 678 def"
        search_result = re.search(pattern, text)
        self.assertIsNotNone(search_result)
        self.assertEqual(search_result.group(), "678")

    def test_substitution(self):
        # Testuje zastąpienie ciągu cyfr słowem 'number'
        pattern = r'\d+'
        repl = "number"
        text = "I have 2 apples and 3 oranges"
        result = re.sub(pattern, repl, text)
        self.assertEqual(result, "I have number apples and number oranges")

    def test_findall(self):
        # Testuje wyszukanie wszystkich wyrazów o dokładnie 3 literach
        pattern = r'\b\w{3}\b'
        text = "The cat sat on the mat"
        found = re.findall(pattern, text)
        self.assertListEqual(found, ['The', 'cat', 'sat', 'the', 'mat'])

    def test_compile(self):
        # Testuje kompilację wyrażenia regularnego i użycie skompilowanego wzorca
        pattern_str = r'\w+'
        compiled_pattern = re.compile(pattern_str)
        self.assertIsNotNone(compiled_pattern)
        self.assertTrue(hasattr(compiled_pattern, "search"))

        text = "Hello world"
        match = compiled_pattern.match(text)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(), "Hello")

if __name__ == '__main__':
    unittest.main()
