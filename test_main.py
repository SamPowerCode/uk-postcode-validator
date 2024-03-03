import unittest
from main import (
    format_uk_postcode,
    validate_uk_postcode,
)


class PostcodeTest(unittest.TestCase):
    def test_format_uk_postcode_success(self):
        postcode = "aa9a9aa"
        result = format_uk_postcode(postcode)
        self.assertEqual(result, "AA9A 9AA")

        postcode = "aa9a-9aa"
        result = format_uk_postcode(postcode)
        self.assertEqual(result, "AA9A 9AA")
    
    def test_format_uk_postcode_fail(self):
        postcode = ""
        result = format_uk_postcode(postcode)
        self.assertEqual(result, " ")

    def test_validate_uk_postcode_success(self):
        postcode = "aa9a9aa"
        result = validate_uk_postcode(postcode)
        self.assertEqual(result, True)

    def test_validate_uk_postcode_fail(self):
        postcode = "aa9aa"
        result = validate_uk_postcode(postcode)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
