import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(test_nodes, new_nodes)

    def test_bold_node(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(test_nodes, new_nodes)

    def test_italic_node(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(test_nodes, new_nodes)

    def test_multiple_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        node2 = TextNode(
            "This is another text with a `better code block`", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
        test_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is another text with a ", TextType.TEXT),
            TextNode("better code block", TextType.CODE),
        ]
        self.assertListEqual(test_nodes, new_nodes)

    def test_delimiters_not_matching(self):
        node = TextNode("Text with a **bold* word", TextType.TEXT)
        with self.assertRaises(Exception):
            _ = split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_not_text_type(self):
        node = TextNode("_italic_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([node], "**", TextType.TEXT)
        test_nodes = [
            TextNode("_italic_", TextType.ITALIC),
        ]
        self.assertListEqual(test_nodes, new_nodes)

    def test_empty_node(self):
        new_nodes = split_nodes_delimiter([], "**", TextType.TEXT)
        test_nodes = []
        self.assertListEqual(test_nodes, new_nodes)

    def test_delimiter_at_the_start(self):
        node = TextNode("`This is a code block` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_nodes = [
            TextNode("This is a code block", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertListEqual(test_nodes, new_nodes)

    def test_mulitple_delimiter_in_a_node(self):
        node = TextNode(
            "This is a `code block`, and this is another `cooler code block`",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        test_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(", and this is another ", TextType.TEXT),
            TextNode("cooler code block", TextType.CODE),
        ]
        self.assertListEqual(test_nodes, new_nodes)
