import os
import shutil

from copystatic import copy_static_recursevly

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    if not os.path.exists(dir_path_static):
        raise Exception("Not static folder found")

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    os.mkdir(dir_path_public)

    print("Copying static files to public directory...")
    copy_static_recursevly(dir_path_static, dir_path_public)


if __name__ == "__main__":
    main()
