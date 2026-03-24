import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_two_child_and_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        first_child_node = ParentNode("span", [grandchild_node])
        second_child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><span><b>grandchild</b></span></div>",
        )

    def test_to_html_without_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_without_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_without_child_grandchild_child(self):
        grandchild_node = LeafNode("b", "grandchild")
        first_child_node = ParentNode("span", [grandchild_node])
        second_child_node = LeafNode("b", "grandchild")
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><b>grandchild</b></div>",
        )

    def test_to_html_child_raw_value(self):
        child_node = LeafNode("", "child")
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), "<p>child</p>")

    def test_to_html_without_child_grandchild_child_with_props(self):
        grandchild_node = LeafNode("a", "Click mich!", {"href": "www.google.com"})
        first_child_node = ParentNode("span", [grandchild_node])
        second_child_node = LeafNode("a", "Click mich!", {"href": "www.google.com"})
        parent_node = ParentNode("div", [first_child_node, second_child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><a href="www.google.com">Click mich!</a></span><a href="www.google.com">Click mich!</a></div>',
        )

    def test_to_html_parent_with_props_and_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(), '<div class="container"><span>child</span></div>'
        )

    def test_to_html_children_none(self):
        node = ParentNode("div", None)  # type: ignore
        with self.assertRaises(ValueError):
            node.to_html()
