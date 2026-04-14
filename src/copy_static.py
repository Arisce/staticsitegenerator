import os
import shutil

def copy_static_to_public(src, dst):
    # delete destination if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)

    # recreate destination
    os.mkdir(dst)

    # loop through source
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        # if file -> copy
        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)

        # if directory -> recurse
        else:
            copy_static_to_public(src_path, dst_path)