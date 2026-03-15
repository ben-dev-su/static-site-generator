import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_values(self):
        a = {"href": "www.google.com", "target": "_blank"}
        node = HTMLNode(tag="<a>", props=a)
        self.assertEqual(node.props_to_html(), 'href="www.google.com" target="_blank"')

    def test_props_to_html_multiple(self):
        a = {
            "href": "www.google.com",
            "target": "_self",
            "class": "link",
            "name": "google_link",
            "title": "Google Link",
        }
        node = HTMLNode(tag="<a>", props=a)
        self.assertEqual(
            node.props_to_html(),
            'href="www.google.com" target="_self" class="link" name="google_link" title="Google Link"',
        )

    def test_props_to_html_single(self):
        a = {"href": "www.google.com"}
        node = HTMLNode(tag="<a>", props=a)
        self.assertEqual(node.props_to_html(), 'href="www.google.com"')

    # def test_props_contains_javascript(self):
    #     p = {"href": "javascript:alert('Hello World!');"}
    #     node = HTMLNode(props=p)
    #     with self.assertRaises(ValueError):
    #         node.props_to_html()


if __name__ == "__main__":
    unittest.main()
