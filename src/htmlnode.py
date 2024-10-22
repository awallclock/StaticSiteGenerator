class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemenented")

    def props_to_html(self):
        if self.props is None:
            return ""
        formatted = ""
        for prop in self.props:
            formatted += f' {prop}="{self.props[prop]}"'
        return formatted

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {
            self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode needs a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode needs a tag")
        if not self.children:
            raise ValueError("ParentNode needs children")

        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
