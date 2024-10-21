from textnode import TextNode, TextType


def main():
    test = TextNode("this is a text node", TextType.BOLD, "http://awallclock.com")
    print(test)


main()
