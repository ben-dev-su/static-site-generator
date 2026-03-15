import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_without_props(self):
        node = LeafNode("a", "Click mich!")
        self.assertEqual(node.to_html(), "<a>Click mich!</a>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode(
            "a", "Click mich!", {"href": "www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(), '<a href="www.google.com" target="_blank">Click mich!</a>'
        )

    def test_no_value_raise_error(self):
        node = LeafNode("a", "", {"href": "www.google.com", "target": "_blank"})
        with self.assertRaises(ValueError):
            node.to_html()

        node.value = None

        with self.assertRaises(ValueError):
            node.to_html()

    def test_returns_raw_value_if_no_tag(self):
        node = LeafNode("", "RAW VALUE", {"href": "www.google.com", "target": "_blank"})
        self.assertEqual("RAW VALUE", node.to_html())


if __name__ == "__main__":
    unittest.main()
