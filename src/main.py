import sys

from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from generate_page import generate_page, generate_pages_recursive

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static_to_public("static", "docs")

    generate_pages_recursive(
        "content",
        "template.html",
        "docs",
        basepath
    )

main()

# chmod +x main.sh
# ./main.sh