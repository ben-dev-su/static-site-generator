import re

from enum import Enum
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if not block:
            continue

        stripped_block = block.strip()

        if not stripped_block:
            continue
        filtered_blocks.append(stripped_block)

    return filtered_blocks


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


# 1. first markdown to blocks
# 2. figure out the type of block
# 3. create nodes out of the block; this will be our parent node
# 4. parse inline content of one block, and create text nodes. these will be our leaf nodes
# 5. append leaf nodes to parent nodes
# 4. create to_html nodes the parent node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children_nodes = []
    for block in blocks:
        node = block_type_block_to_parent_node(block)
        children_nodes.append(node)

    allvater_node = ParentNode(tag="div", children=children_nodes)

    return allvater_node


def block_type_block_to_parent_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.PARAGRAPH:
            return block_to_paragraph(block)
        case BlockType.HEADING:
            return block_to_heading(block)
        case BlockType.CODE:
            return block_to_codeblock(block)
        case BlockType.QUOTE:
            return block_to_quote(block)
        case BlockType.UNORDERED_LIST:
            return block_to_unordered_list(block)
        case BlockType.ORDERED_LIST:
            return block_to_ordered_list(block)
        case _:
            raise Exception("No valid block")


def block_to_paragraph(block):
    new_block = block.replace("\n", " ")
    leafs = block_to_leaf_nodes(new_block)
    return ParentNode(tag="p", children=leafs)


def block_to_heading(block):
    # every heading has a space between # and the heading text
    # splittin the block on the first space will give us the
    # # and the text
    splits = block.split(" ", 1)
    leafs = block_to_leaf_nodes(splits[1])
    len_hash = len(splits[0])
    return ParentNode(tag=f"h{len_hash}", children=leafs)


def block_to_codeblock(block):
    text = block.removeprefix("```\n").removesuffix("```")
    text_node = TextNode(text, TextType.TEXT)
    leaf = text_node_to_html_node(text_node)
    code_node = ParentNode(tag="code", children=[leaf])
    return ParentNode(tag="pre", children=[code_node])


def block_to_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:

        if line.startswith("> "):
            line = line.strip("> ")

        if line.startswith(">"):
            line = line.strip(">")

        if line == "":
            continue
        new_lines.append(line)

    new_block = " ".join(new_lines)
    leafs = block_to_leaf_nodes(new_block)
    return ParentNode(tag="blockquote", children=leafs)


def block_to_unordered_list(block):
    lines = block.split("\n")
    leafs = []
    for line in lines:
        line = line.strip("- ")
        nodes = block_to_leaf_nodes(line)
        leafs.append(ParentNode(tag="li", children=nodes))
    return ParentNode(tag="ul", children=leafs)


def block_to_ordered_list(block):
    lines = block.split("\n")
    leafs = []
    for line in lines:
        line = line[3:]
        nodes = block_to_leaf_nodes(line)
        leafs.append(ParentNode(tag="li", children=nodes))
    return ParentNode(tag="ol", children=leafs)


def block_to_leaf_nodes(block: str):
    text_nodes = text_to_textnodes(block)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf = text_node_to_html_node(text_node)
        leaf_nodes.append(leaf)
    return leaf_nodes
