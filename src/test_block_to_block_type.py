import unittest

from helper import block_to_block_type, BlockType


# paragraph
# heading
# code
# quote
# unordered_list
# ordered_list
class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        md_block = "Hello World"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_heading(self):
        for level in range(1, 6):
            md_block = "#" * level + " Hello World"
            block_type = block_to_block_type(md_block)
            with self.subTest(heading_level=level, level=level):
                self.assertEqual(BlockType.HEADING, block_type)

    def test_block_to_block_type_not_code(self):
        md_block = "```Hello World```"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_not_code_new_line_end(self):
        md_block = """```
        Hello World
        ```
        """
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_not_code_new_line_start(self):
        md_block = """
        ```
        Hello World
        ```
        """
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_code(self):
        md_block = """```
        Hello World
```"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_block_to_block_type_not_code_empty(self):
        md_block = """```

```"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.CODE, block_type)

    def test_block_to_block_type_simple_quote(self):
        md_block = ">All's well that ends better."
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_block_to_block_type_simple_quote_with_space(self):
        md_block = "> All's well that ends better."
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_block_to_block_type_quote_multiline(self):
        md_block = """>Home is behind, the world ahead,
>and there are many paths to tread
>through shadows to the edge of night,
>until the stars are all alight."""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_block_to_block_type_quote_multiline_with_spaces(self):
        md_block = """> Home is behind, the world ahead,
> and there are many paths to tread
> through shadows to the edge of night,
> until the stars are all alight."""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.QUOTE, block_type)

    def test_block_to_block_type_not_quote_with_paragraph(self):
        md_block = """>Home is behind, the world ahead,
>and there are many paths to tread
Hello World
>through shadows to the edge of night,
>until the stars are all alight."""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_not_quote_empty(self):
        md_block = ""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_not_quote_starts_paragraph(self):
        md_block = """Home is behind, the world ahead,
>and there are many paths to tread
>Hello World
>through shadows to the edge of night,
>until the stars are all alight."""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_u_list_simple(self):
        md_block = "- item"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_block_to_block_type_u_list_empty(self):
        md_block = ""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_u_list_no_space(self):
        md_block = "-item"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_u_list_multiline(self):
        md_block = """- item1
- item2
- item3
- item4"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.UNORDERED_LIST, block_type)

    def test_block_to_block_type_no_u_list_multiline(self):
        md_block = """- item1
- item2
random
- item3
- item4"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_simple(self):
        md_block = "1. item"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_block_to_block_type_o_list_empty(self):
        md_block = ""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_no_space(self):
        md_block = "1.item"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_no_dot(self):
        md_block = "1 item"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_no_number(self):
        md_block = ". item"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_hypgen(self):
        md_block = "-. item"
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_multiline(self):
        md_block = """1. item1
2. item2
3. item3
4. item4"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.ORDERED_LIST, block_type)

    def test_block_to_block_type_no_o_list_multiline(self):
        md_block = """1. item1
2. item2
random
3. item3
4. item4"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_wrong_count(self):
        md_block = """1. item1
2. item2
5. item3
6. item4"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)

    def test_block_to_block_type_o_list_stats_with_zero(self):
        md_block = """0. item1
2. item2
5. item3
6. item4"""
        block_type = block_to_block_type(md_block)
        self.assertEqual(BlockType.PARAGRAPH, block_type)
