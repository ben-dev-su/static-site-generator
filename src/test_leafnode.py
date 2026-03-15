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


if __name__ == "__main__":
    unittest.main()
