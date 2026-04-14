import unittest
from block import block_to_block_type, BlockType

class TestBlock(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Hello"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```Some code```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> a\n> b"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- a\n- b"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. a\n2. b"), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("just text"), BlockType.PARAGRAPH)