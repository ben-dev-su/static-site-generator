import os

from inline_markdown import extract_title
from markdown_blocks import markdown_to_html_node


def generate_page_recursively(from_dir_path, template_path, dest_dir_path, basepath):
    dir_content = os.listdir(from_dir_path)
    if not dir_content:
        return

    for element in dir_content:
        from_path = os.path.join(from_dir_path, element)
        dest_path = os.path.join(dest_dir_path, element.replace(".md", ".html"))
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_page_recursively(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"* {from_path} {template_path} -> {dest_path}")

    if not os.path.exists(from_path):
        raise Exception(f"No file at {from_path} exists")

    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    parent_node = markdown_to_html_node(markdown)
    html = parent_node.to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    create_dest(dest_path, template)


def create_dest(dest_path, html):
    dest_dir_path = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, "w")
    to_file.write(html)
    to_file.close()
