import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_equal(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        }
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_empty(self):
        node = HTMLNode(props={
        }
        )
        self.assertEqual(node.props_to_html(), "")

    def test_None(self):
        node = HTMLNode(props=None
        )
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", None, {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")