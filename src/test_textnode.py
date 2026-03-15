import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")
        self.assertEqual(html_node.to_html(), "<i>This is a italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
        node = TextNode("This is a anchor node", TextType.LINK, "www.google.de")
        # {"href": "www.google.com"}
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a anchor node")
        self.assertEqual(
            html_node.to_html(), '<a href="www.google.de">This is a anchor node</a>'
        )

    def test_image(self):
        node = TextNode(
            "This is a image node", TextType.IMAGE, "www.google.de/img1.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.to_html(),
            '<img src="www.google.de/img1.png" alt="This is a image node"></img>',
        )


if __name__ == "__main__":
    unittest.main()
