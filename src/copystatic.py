import os
import shutil


def copy_static_recursevly(src_dir_path, dst_dir_path):
    if not os.path.exists(dst_dir_path):
        os.mkdir(dst_dir_path)

    content = os.listdir(src_dir_path)
    if not content:
        return

    for element in content:

        from_path = os.path.join(src_dir_path, element)
        dest_path = os.path.join(dst_dir_path, element)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_static_recursevly(from_path, dest_path)
