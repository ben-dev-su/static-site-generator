import unittest

from markdown_blocks import markdown_to_html_node
from htmlnode import HTMLNode


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings_in_heading_no_blank_line(self):
        md = """
# this is a level 1 heading with **bolded** text
## this is l2
##### this is l5
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is a level 1 heading with <b>bolded</b> text\n## this is l2\n##### this is l5</h1></div>",
        )

    def test_headings_1(self):
        md = """
# this is a level 1 heading with **bolded** text
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is a level 1 heading with <b>bolded</b> text</h1></div>",
        )

    def test_headings_2(self):
        md = "## level 2 heading"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>level 2 heading</h2></div>",
        )

    def test_headings_3(self):
        md = "### this is a level 3 heading here"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>this is a level 3 heading here</h3></div>",
        )

    def test_headings_4(self):
        md = """
#### This is level 4 heading with _italic_ text and `code` here
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>This is level 4 heading with <i>italic</i> text and <code>code</code> here</h4></div>",
        )

    def test_headings_5(self):
        md = """
##### This is level 5 heading
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>This is level 5 heading</h5></div>",
        )

    def test_headings_6(self):
        md = """
###### This is level 6 heading
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is level 6 heading</h6></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_codeblock_empty(self):
        md = """
```
```
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code></code></pre></div>",
        )

    def test_blockquote(self):
        md = """
>Hello
>World
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Hello World</blockquote></div>",
        )

    def test_blockquote_with_inline(self):
        md = """
>This is **bolded** paragraph
>This is _italic_ and this is `code`
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph This is <i>italic</i> and this is <code>code</code></blockquote></div>",
        )

    def test_blockquote_with_empty_line(self):
        md = """
>This is **bolded** paragraph
>
>This is _italic_ and this is `code`
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> paragraph This is <i>italic</i> and this is <code>code</code></blockquote></div>",
        )

    def test_empty(self):
        md = ""
        node = markdown_to_html_node(md)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_blockquote_with_space(self):
        md = """
> Hello
>World
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Hello World</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Hello **World**
- World
- _Italic_ item
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Hello <b>World</b></li><li>World</li><li><i>Italic</i> item</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
1. Hello **World**
2. World
3. _Italic_ item
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Hello <b>World</b></li><li>World</li><li><i>Italic</i> item</li></ol></div>",
        )
