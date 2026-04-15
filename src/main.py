from textnode import TextNode, TextType
from copy_static import copy_static_to_public
from generate_page import generate_page, generate_pages_recursive

def main():
    copy_static_to_public("static", "public")
    generate_pages_recursive(
        "content",
        "template.html",
        "public"
    )

main()

# chmod +x main.sh
# ./main.sh