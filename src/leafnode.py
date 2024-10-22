from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode needs a value")
        if self.tag is None:
            return self.value
        formatted = HTMLNode.props_to_html(self)
        return f"<{self.tag}{formatted}>{self.value}</{self.tag}>"
