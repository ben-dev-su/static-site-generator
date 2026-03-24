import unittest

from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        self.maxDiff = None
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        valid_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(valid_nodes, nodes)

    def test_text_to_textnodes_empty(self):
        nodes = text_to_textnodes("")

        valid_nodes = []

        self.assertListEqual(valid_nodes, nodes)

    def test_text_to_texnodes_no_text_nodes(self):
        text = "**text**_italic_`code block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        valid_nodes = [
            TextNode("text", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode("code block", TextType.CODE),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(valid_nodes, nodes)

    def test_text_to_texnodes_only_text(self):
        text = "[value for value in iterable] [value if condition else condition for value in iterable]"
        nodes = text_to_textnodes(text)

        valid_nodes = [
            TextNode(text, TextType.TEXT),
        ]

        self.assertListEqual(valid_nodes, nodes)

    def test_text_to_textnodes_mixed_double(self):
        self.maxDiff = None
        text = "This is **text****text** with an _italic__italic_ word and a `code block``code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)[link](https://boot.dev)"
        nodes = text_to_textnodes(text)

        valid_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertListEqual(valid_nodes, nodes)
