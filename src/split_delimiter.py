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
