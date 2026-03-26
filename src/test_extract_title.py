import unittest

from inline_markdown import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Tolkien Fan Club"
        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")

    def test_extract_title_white_space(self):
        md = "#  Tolkien Fan Club \n"
        title = extract_title(md)
        self.assertEqual(title, " Tolkien Fan Club ")

    def test_extract_title_no_title(self):
        md = """
## No Title
        """
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_none(self):
        md = None
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_level2(self):
        md = "## Tolkien Fan Club"
        with self.assertRaises(ValueError):
            extract_title(md)

    def test_extract_title_multiline(self):
        md = """
# Tolkien Fan Club

- Find Ring
- Fly with the eagles to that mountain
- Destroy Ring

"""

        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")

    def test_extract_title_from_middle(self):
        md = """
## Sub Title

- Find Ring
- Fly with the eagles to that mountain
- Destroy Ring

# Tolkien Fan Club

"""

        title = extract_title(md)
        self.assertEqual(title, "Tolkien Fan Club")
