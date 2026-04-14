import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello World"
        self.assertEqual(extract_title(md), "Hello World")

    def test_extract_title_multiline(self):
        md = "Some text\n# Title\nMore text"
        self.assertEqual(extract_title(md), "Title")

    def test_extract_title_error(self):
        md = "No title here"
        with self.assertRaises(Exception):
            extract_title(md)