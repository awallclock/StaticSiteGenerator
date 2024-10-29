import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("THIS DO BE A TEST NODE", TextType.ITALIC)
        node2 = TextNode("THIS DO BE A TEST NODE", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("YAAAS QUEEEEN", TextType.LINK,
                        "https://poopfarts.edu")
        node2 = TextNode("YAAAS QUEEEEN", TextType.LINK,
                         "https://poopfarts.edu")
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("THIS DO BE A TEST NODE", TextType.ITALIC)
        node2 = TextNode("THIS DO BE A TEST NODE", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff2(self):
        node = TextNode("THIS DO BE A TEST NODE",
                        TextType.ITALIC, "https://lol.com")
        node2 = TextNode("THIS DO BE A TEST NODE", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)


class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("Regular text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Regular text")

    def test_bold(self):
        node = TextNode("Text that should be bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Text that should be bold")

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")

    def test_link(self):
        node = TextNode("Link text", TextType.LINK, "www.urmom.gov")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props, {"href": "www.urmom.gov"})

    def test_image(self):
        node = TextNode("lol", TextType.IMAGE, "lmao.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "lmao.jpg", "alt": "lol"})


if __name__ == "__main__":
    unittest.main()
