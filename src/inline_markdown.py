import re
from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode] | None, delimiter: str, text_type: TextType
):
    if old_nodes is None:
        return []
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text_parts = node.text.split(delimiter)
        if len(text_parts) % 2 == 0:
            raise Exception(f"Invalid markdown. no matching delimiters for {node.text}")

        for i in range(len(text_parts)):
            if text_parts[i] == "":
                continue

            if i % 2 != 0:
                new_nodes.append(TextNode(text_parts[i], text_type))
            else:
                new_nodes.append(TextNode(text_parts[i], TextType.TEXT))

    return new_nodes


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


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
