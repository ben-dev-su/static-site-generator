import os
import shutil
import sys

from copystatic import copy_static_recursevly
from generator import generate_page_recursively, generate_page

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if not os.path.exists(dir_path_static):
        raise Exception("Not static folder found")

    print("=============================")
    print("Deleting public directory...")
    print("=============================")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print()

    os.mkdir(dir_path_public)

    print("===========================================")
    print("Copying static files to public directory...")
    print("===========================================")
    copy_static_recursevly(dir_path_static, dir_path_public)

    print()

    print("=====================")
    print("Generating content...")
    print("=====================")
    generate_page_recursively(
        dir_path_content, "./template.html", dir_path_public, basepath
    )
    print()


if __name__ == "__main__":
    main()
