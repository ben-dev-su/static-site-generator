import os
import shutil

from copystatic import copy_static_recursevly
from generator import generate_page_recursively, generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"


def main():
    if not os.path.exists(dir_path_static):
        raise Exception("Not static folder found")

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    os.mkdir(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_recursevly(dir_path_static, dir_path_public)

    generate_page_recursively(dir_path_content, "./template.html", dir_path_public)

    # generate_page("content/index.md", "./template.html", "public/index.html")
    # generate_page(
    #     "content/blog/glorfindel/index.md",
    #     "./template.html",
    #     "public/blog/glorfindel/index.html",
    # )
    # generate_page(
    #     "content/blog/tom/index.md", "./template.html", "public/blog/tom/index.html"
    # )
    # generate_page(
    #     "content/blog/majesty/index.md",
    #     "./template.html",
    #     "public/blog/majesty/index.html",
    # )
    # generate_page(
    #     "content/contact/index.md", "./template.html", "public/contact/index.html"
    # )


if __name__ == "__main__":
    main()
