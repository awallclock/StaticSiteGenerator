import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        # testing Parent Node
        child_node = LeafNode("b", "child")
        parent_node = ParentNode("i", [child_node])
        self.assertEqual(parent_node.to_html(), "<i><b>child</b></i>")

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("i", "THIS IS ITALIC")
        child_node = ParentNode("div", [grandchild])
        parent_node = ParentNode("span", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<span><div><i>THIS IS ITALIC</i></div></span>"
        )

    def test_to_html_with_many_childs(self):
        parent_node = ParentNode(
            "p",
            [
                LeafNode(None, "Normal text"),
                LeafNode("b", "Bold text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p>Normal text<b>Bold text</b><i>Italic text</i>Normal text</p>",
        )

    def test_deep_parents(self):
        child_node = ParentNode("b", [LeafNode("i", "UH TEST?")])
        parent_node = ParentNode(
            "p", [child_node, LeafNode(
                None, "NORMAL TEXT"), LeafNode("i", "ITALICS")]
        )
        self.assertEqual(
            parent_node.to_html(),
            "<p><b><i>UH TEST?</i></b>NORMAL TEXT<i>ITALICS</i></p>",
        )


if __name__ == "__main__":
    unittest.main()
