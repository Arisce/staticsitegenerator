import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestText_to_TextNodes(unittest.TestCase):
    def test_full_pipeline(self):
            text = "This is **bold** and `code`"

            nodes = text_to_textnodes(text)

            self.assertEqual(nodes[1].text_type, TextType.BOLD)
            self.assertEqual(nodes[3].text_type, TextType.CODE)