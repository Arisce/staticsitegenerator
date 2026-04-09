import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from textnode_to_html import text_node_to_html_node
from split_delimiter import split_nodes_delimiter

class Test_Split_Delimiter(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("Hello `world` test", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(result[0].text, "Hello ")
        self.assertEqual(result[1].text, "world")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " test")

    def test_multiple_delimiters(self):
        node = TextNode("This is **bold** and `code`", TextType.TEXT)

        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[3].text_type, TextType.CODE)