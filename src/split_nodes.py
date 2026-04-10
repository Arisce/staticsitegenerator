import re

from textnode import TextNode, TextType

def split_nodes_image(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(r"!\[([^\]]+)\]\(([^)]+)\)", text))

        if not matches:
            new_nodes.append(node)
            continue
        
        last_index = 0

        for match in matches:
            start, end = match.span()
            alt_text = match.group(1)
            url = match.group(2)

            # text before image
            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))

            # image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            last_index = end

        # remaining text
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))

    return new_nodes

import re
from textnode import TextNode, TextType


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # skip non-text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = list(re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text))

        if not matches:
            new_nodes.append(node)
            continue

        last_index = 0

        for match in matches:
            start, end = match.span()
            link_text = match.group(1)
            url = match.group(2)

            # text before match
            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))

            # the link node
            new_nodes.append(TextNode(link_text, TextType.LINK, url))

            last_index = end

        # remaining text after last match
        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))

    return new_nodes