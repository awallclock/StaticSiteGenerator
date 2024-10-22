from textnode import TextNode, TextType
from htmlnode import HTMLNode


def main():
    test_props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    test = HTMLNode("taggggg", "vallllue", "chillllldren", test_props)
    print(test.__repr__())


main()
