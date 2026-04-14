from markdown_to_blocks import markdown_to_blocks
from block import block_to_block_type, BlockType
from htmlnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode_to_html import text_node_to_html_node
from textnode import TextNode, TextType

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            lines = block.split("\n")
            cleaned = [line.strip() for line in lines]
            text = " ".join(cleaned)
            children_nodes = text_to_children(text)
            node = ParentNode("p", children_nodes)

        elif block_type == BlockType.HEADING:
            count = 0
            for c in block:
                if c == "#":
                    count += 1
                else:
                    break
            text = block[count+1:]
            children_nodes = text_to_children(text)
            node = ParentNode(f"h{count}", children_nodes)

        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            cleaned_lines = [line.strip() for line in lines[1:-1]]
            text = "\n".join(cleaned_lines) + "\n"
            text_node = TextNode(text, TextType.TEXT)
            child = text_node_to_html_node(text_node)
            node = ParentNode("pre", [ParentNode("code", [child])])

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            cleaned = [line.lstrip("> ").strip() for line in lines]
            text = " ".join(cleaned)
            children_nodes = text_to_children(text)
            node = ParentNode("blockquote", children_nodes)

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            items = []
            for line in lines:
                text = line[2:]
                items.append(ParentNode("li", text_to_children(text)))
            node = ParentNode("ul", items)

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            items = []
            for i, line in enumerate(lines):
                text = line[len(f"{i+1}. "):]
                items.append(ParentNode("li", text_to_children(text)))
            node = ParentNode("ol", items)

        children.append(node)

    return ParentNode("div", children)