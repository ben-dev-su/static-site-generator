import re

from textnode import TextType, TextNode


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
            new_nodes.append(TextNode(node.text, node.text_type))
            continue

        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(TextNode(node.text, node.text_type))
            continue

        remaining_text = node.text
        for i in range(len(images)):
            seq = remaining_text.split(f"![{images[i][0]}]({images[i][1]})", 1)

            if seq[0] != "":
                new_nodes.append(TextNode(seq[0], TextType.TEXT))
            new_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))

            remaining_text = seq[1]

    return new_nodes


def split_nodes_link(old_nodes):
    if old_nodes is None:
        return []

    new_nodes = []

    for node in old_nodes:
        if node is None:
            continue

        if node.text_type != TextType.TEXT:
            new_nodes.append(TextNode(node.text, node.text_type))
            continue

        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(TextNode(node.text, node.text_type))
            continue

        remaining_text = node.text
        for i in range(len(links)):
            seq = remaining_text.split(f"[{links[i][0]}]({links[i][1]})", 1)

            if seq[0] != "":
                new_nodes.append(TextNode(seq[0], TextType.TEXT))
            new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))

            remaining_text = seq[1]

    return new_nodes
