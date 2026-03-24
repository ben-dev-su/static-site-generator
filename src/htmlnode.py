class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,  # noqa: F821
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""

        items = []
        for k, v in self.props.items():
            items.append(f'{k}="{v}"')
        return " ".join(items)

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


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


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str | None,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError()

        if not self.tag:
            return self.value

        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        props = super().props_to_html()
        return f"<{self.tag} {props}>{self.value}</{self.tag}>"
