import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_should_not_none(self):
        node = TextNode("This is a url node", TextType.LINK, "www.link.com/image1")
        self.assertIn(node.text_type, [TextType.IMAGE, TextType.LINK])
        self.assertIsNotNone(
            node.url, "Url attribute is None, besides TextType is Link."
        )

    def test_url_should_none(self):
        node = TextNode("This is a url node", TextType.TEXT)
        self.assertNotEqual(TextType.LINK, node.text_type)
        self.assertNotEqual(TextType.IMAGE, node.text_type)
        self.assertIsNone(
            node.url,
            "Url attribute is not None, besides TextType is not Link or Image.",
        )


if __name__ == "__main__":
    unittest.main()
