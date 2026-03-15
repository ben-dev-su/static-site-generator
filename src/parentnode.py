from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError()

        if not self.children:
            raise ValueError("Parent node must have children.")

        html = ""
        for child in self.children:
            html += child.to_html()

        if not self.props:
            return f"<{self.tag}>{html}</{self.tag}>"

        props = super().props_to_html()
        return f"<{self.tag} {props}>{html}</{self.tag}>"
