import unittest

from textnode import TextNode, TextType


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
        node = TextNode("YAAAS QUEEEEN", TextType.LINK, "https://poopfarts.edu")
        node2 = TextNode("YAAAS QUEEEEN", TextType.LINK, "https://poopfarts.edu")
        self.assertEqual(node, node2)

    def test_diff(self):
        node = TextNode("THIS DO BE A TEST NODE", TextType.ITALIC)
        node2 = TextNode("THIS DO BE A TEST NODE", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff2(self):
        node = TextNode("THIS DO BE A TEST NODE", TextType.ITALIC, "https://lol.com")
        node2 = TextNode("THIS DO BE A TEST NODE", TextType.ITALIC, None)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
