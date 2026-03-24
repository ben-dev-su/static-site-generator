from enum import Enum
import re

from textnode import TextType, TextNode
from split_delimiter import split_nodes_delimiter


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes: list[TextNode] | None):
    if old_nodes is None:
        return []

    new_nodes = []

    for node in old_nodes:
        if node is None:
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        seq = []
        for i in range(len(images)):
            seq = remaining_text.split(f"![{images[i][0]}]({images[i][1]})", 1)

            if seq[0] != "":
                new_nodes.append(TextNode(seq[0], TextType.TEXT))
            new_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))

            remaining_text = seq[1]

        if seq[1] != "":
            new_nodes.append(TextNode(seq[1], TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    if old_nodes is None:
        return []

    new_nodes = []

    for node in old_nodes:
        if node is None:
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)
            continue

        seq = []
        remaining_text = node.text
        for i in range(len(links)):
            seq = remaining_text.split(f"[{links[i][0]}]({links[i][1]})", 1)

            if seq[0] != "":
                new_nodes.append(TextNode(seq[0], TextType.TEXT))
            new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))

            remaining_text = seq[1]

        if seq[1] != "":
            new_nodes.append(TextNode(seq[1], TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown: str):
    if not markdown:
        return []

    blocks = []

    for block in markdown.split("\n\n"):
        if not block:
            continue

        stripped_block = block.strip()

        if not stripped_block:
            continue
        blocks.append(stripped_block)

    return blocks


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block: str):
    heading_re = r"^#{1,6}\s[a-zA-Z\d]"

    # check headings blocks
    if re.match(heading_re, markdown_block):
        return BlockType.HEADING

    # check code blocks
    lines = markdown_block.split("\n")
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    # check quote blocks
    if markdown_block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    # check unordered list block
    if markdown_block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST

    # check ordered list block
    if markdown_block.startswith("1. "):
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                return BlockType.PARAGRAPH
            count += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
