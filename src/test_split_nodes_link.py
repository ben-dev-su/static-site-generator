import unittest

from textnode import TextType, TextNode
from helper import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    def test_split_link(self):
        node = TextNode(
            "This is text with an [House with Chimaeras](https://en.wikipedia.org/wiki/House_with_Chimaeras) and another [gargoyle](https://en.wikipedia.org/wiki/Gargoyle)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "House with Chimaeras",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "gargoyle", TextType.LINK, "https://en.wikipedia.org/wiki/Gargoyle"
                ),
            ],
            new_nodes,
        )

    def test_split_link_empty_nodes(self):
        new_nodes = split_nodes_link([])
        self.assertListEqual(
            [],
            new_nodes,
        )

    def test_split_link_multiple_nodes(self):

        node = TextNode(
            "This is text with an [House with Chimaeras](https://en.wikipedia.org/wiki/House_with_Chimaeras) and another [gargoyle](https://en.wikipedia.org/wiki/Gargoyle)",
            TextType.TEXT,
        )

        node2 = TextNode(
            "This is text with an [House with Chimaeras](https://en.wikipedia.org/wiki/House_with_Chimaeras) and another [gargoyle](https://en.wikipedia.org/wiki/Gargoyle)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node, node2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "House with Chimaeras",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "gargoyle", TextType.LINK, "https://en.wikipedia.org/wiki/Gargoyle"
                ),
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "House with Chimaeras",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "gargoyle", TextType.LINK, "https://en.wikipedia.org/wiki/Gargoyle"
                ),
            ],
            new_nodes,
        )

    def test_split_link_bold_and_text_node(self):

        node = TextNode(
            "This is text with an [House with Chimaeras](https://en.wikipedia.org/wiki/House_with_Chimaeras) and another [gargoyle](https://en.wikipedia.org/wiki/Gargoyle)",
            TextType.TEXT,
        )

        bold_node = TextNode("**bold text**", TextType.BOLD)

        new_nodes = split_nodes_link([node, bold_node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "House with Chimaeras",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "gargoyle", TextType.LINK, "https://en.wikipedia.org/wiki/Gargoyle"
                ),
                TextNode("**bold text**", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_split_link_just_bold_node(self):
        node = TextNode(
            "**bold text**",
            TextType.BOLD,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("**bold text**", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_split_images_with_empty_node(self):
        node = TextNode(
            "This is text with an [House with Chimaeras](https://en.wikipedia.org/wiki/House_with_Chimaeras) and another [gargoyle](https://en.wikipedia.org/wiki/Gargoyle)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link(
            [node, None]  # pyright: ignore[reportArgumentType]
        )
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode(
                    "House with Chimaeras",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "gargoyle", TextType.LINK, "https://en.wikipedia.org/wiki/Gargoyle"
                ),
            ],
            new_nodes,
        )

    def test_split_images_with_no_image(self):
        node = TextNode(
            "This is a text",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_at_the_beginning_and_end(self):
        node = TextNode(
            "[House with Chimaeras](https://en.wikipedia.org/wiki/House_with_Chimaeras) and another [gargoyle](https://en.wikipedia.org/wiki/Gargoyle)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "House with Chimaeras",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "gargoyle", TextType.LINK, "https://en.wikipedia.org/wiki/Gargoyle"
                ),
            ],
            new_nodes,
        )

    def test_split_link_back_to_back(self):
        node = TextNode(
            "[House with Chimaeras](https://en.wikipedia.org/wiki/House_with_Chimaeras)[gargoyle](https://en.wikipedia.org/wiki/Gargoyle)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "House with Chimaeras",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
                TextNode(
                    "gargoyle", TextType.LINK, "https://en.wikipedia.org/wiki/Gargoyle"
                ),
            ],
            new_nodes,
        )

    def test_split_link_no_text(self):
        node = TextNode(
            "[](https://en.wikipedia.org/wiki/House_with_Chimaeras)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "",
                    TextType.LINK,
                    "https://en.wikipedia.org/wiki/House_with_Chimaeras",
                ),
            ],
            new_nodes,
        )

    def test_split_link_no_link(self):
        node = TextNode(
            "[]()",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("", TextType.LINK, ""),
            ],
            new_nodes,
        )

    def test_split_link_not_an_link(self):
        node = TextNode(
            "![notimage](www.google.com)",
            TextType.TEXT,
        )

        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("![notimage](www.google.com)", TextType.TEXT),
            ],
            new_nodes,
        )
