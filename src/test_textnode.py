import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Goodbye", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_equal_text_type(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_equal_url(self):
        node1 = TextNode("hello", TextType.LINK, "https://a.com")
        node2 = TextNode("hello", TextType.LINK, "https://a.com")
        self.assertEqual(node1, node2)

    def test_not_equal_url_vs_default(self):
        node1 = TextNode("hello", TextType.LINK, "https://a.com")
        node2 = TextNode("hello", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url_vs_none(self):
        node1 = TextNode("hello", TextType.LINK, "https://a.com")
        node2 = TextNode("hello", TextType.LINK, None)
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()