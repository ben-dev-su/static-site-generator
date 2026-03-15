from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    TEXT = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode):
    text_type: TextType = text_node.text_type

    tag = text_type.value
    value = text_node.text

    match text_type:
        case TextType.TEXT | TextType.BOLD | TextType.ITALIC | TextType.CODE:
            return LeafNode(tag, value)
        case TextType.LINK:
            if text_node.url is None:
                text_node.url = ""
            return LeafNode(
                text_type.value, value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            if text_node.url is None:
                text_node.url = ""
            return LeafNode(
                text_type.value,
                "",
                {"src": text_node.url, "alt": text_node.text},
            )
        case _:
            raise Exception(f"Unknown TextType for TextNode: {TextNode}")
