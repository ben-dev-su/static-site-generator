import re
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from helper import markdown_to_blocks, block_to_block_type, text_to_textnodes, BlockType
from textnode import text_node_to_html_node, TextNode, TextType

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
