import unittest
import re


class TestRegrex(unittest.TestCase):

    def test_match(self):
        # Testowanie metody re.match
        pattern = r"^Python"
        string = "Python jest świetny"
        result = re.match(pattern, string)
        self.assertIsNotNone(result)
        self.assertEqual(result.group(), "Python")

    def test_no_match(self):
        pattern = r"^Java"
        string = "Python jest świetny"
        result = re.match(pattern, string)
        self.assertIsNone(result)

    def test_search(self):
        # Testowanie metody re.search
        pattern = r"świetny"
        string = "Python jest świetny"
        result = re.search(pattern, string)
        self.assertIsNotNone(result)
        self.assertEqual(result.group(), "świetny")

    def test_findall(self):
        # Testowanie metody re.findall
        pattern = r"\d+"
        string = "Mam 2 jabłka i 3 gruszki"
        result = re.findall(pattern, string)
        self.assertEqual(result, ["2", "3"])

    def test_sub(self):
        # Testowanie metody re.sub
        pattern = r"jabłko|gruszka|gruszkę"
        string = "Mam jabłko i gruszkę"
        replacement = "owoc"
        result = re.sub(pattern, replacement, string)
        self.assertEqual(result, "Mam owoc i owoc")

    def test_groups(self):
        # Testowanie grup przechwytujących
        pattern = r"(\d+)-(\d+)-(\d+)"
        string = "Data: 2023-03-15"
        result = re.search(pattern, string)
        self.assertIsNotNone(result)
        self.assertEqual(result.group(1), "2023")
        self.assertEqual(result.group(2), "03")
        self.assertEqual(result.group(3), "15")

    def test_complex_pattern(self):
        # Testowanie adresu email
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        valid_emails = ["test@example.com", "user.name@domain.co.uk"]
        invalid_emails = ["invalid@", "@example.com", "user@.com"]

        for email in valid_emails:
            self.assertIsNotNone(re.match(pattern, email), f"{email} powinien być prawidłowy")

        for email in invalid_emails:
            self.assertIsNone(re.match(pattern, email), f"{email} nie powinien być prawidłowy")

    def test_multiple_patterns(self):
        test_cases = [
            {"pattern": r"\d+", "string": "123", "expected": True},
            {"pattern": r"[a-z]+", "string": "ABC", "expected": False},
            {"pattern": r"[A-Za-z]+", "string": "Abc", "expected": True}
        ]

        for tc in test_cases:
            with self.subTest(pattern=tc["pattern"], string=tc["string"]):
                result = bool(re.match(tc["pattern"], tc["string"]))
                self.assertEqual(result, tc["expected"])

if __name__ == "__main__":
    unittest.main()