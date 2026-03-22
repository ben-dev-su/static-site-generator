import unittest

from helper import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_new_line(self):
        md = """
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [],
        )

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [],
        )

    def test_markdown_to_blocks_new_line_at_start_and_end(self):
        md = """

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items


"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_new_lines_everywhere(self):
        md = """

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line








- This is a list
- with items


"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_no_new_lines(self):
        md = """
This is **bolded** paragraph
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph\nThis is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_single_line(self):
        md = "This is **bolded** paragraph"
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            ["This is **bolded** paragraph"],
        )
