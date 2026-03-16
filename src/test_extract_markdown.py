import unittest

from helper import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link](https://youtu.be/dQw4w9WgXcQ?si=K9TuIWn_QJebW1tF)"
        )
        self.assertListEqual(
            [("link", "https://youtu.be/dQw4w9WgXcQ?si=K9TuIWn_QJebW1tF")], matches
        )

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [link1](https://youtu.be/dQw4w9WgXcQ?si=K9TuIWn_QJebW1tF) and another [link2](https://youtu.be/EE-xtCF3T94?si=1uBkGcnM_XsNkn_V)"
        )
        self.assertListEqual(
            [
                ("link1", "https://youtu.be/dQw4w9WgXcQ?si=K9TuIWn_QJebW1tF"),
                ("link2", "https://youtu.be/EE-xtCF3T94?si=1uBkGcnM_XsNkn_V"),
            ],
            matches,
        )

    def test_extract_multiple_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image1](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://wallhaven.cc/w/8gkeej)"
        )
        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://wallhaven.cc/w/8gkeej"),
            ],
            matches,
        )

    def test_extract_links_no_link(self):
        matches = extract_markdown_links("This is text with without a link")
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_images_no_image(self):
        matches = extract_markdown_images("This is text with without a link")
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_image_wrong_markdown(self):
        matches = extract_markdown_images(
            "This is text with an !image2](https://wallhaven.cc/w/8gkeej)"
        )
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_links_wrong_markdown(self):
        matches = extract_markdown_images(
            "This is text with an [image2]https://wallhaven.cc/w/8gkeej)"
        )
        self.assertListEqual(
            [],
            matches,
        )

    def test_extract_links_but_image(self):

        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_images_but_link(self):
        matches = extract_markdown_images(
            "This is text with an [link](https://youtu.be/dQw4w9WgXcQ?si=K9TuIWn_QJebW1tF)"
        )
        self.assertListEqual([], matches)
