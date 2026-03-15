from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError()

        if self.tag == "":
            return self.value

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        props = super().props_to_html()
        return f"<{self.tag} {props}>{self.value}</{self.tag}>"
