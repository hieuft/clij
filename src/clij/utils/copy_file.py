import shutil
from .get_file_extension import get_file_ext

def copy_file_to_dest(source_file: str, dest_file: str) -> str:
    shutil.copy2(source_file, dest_file)

def copy_file_to_dir(source_file: str, dest_dir: str, new_name: str) -> str:
    file_ext = get_file_ext(source_file)
    dest_file = f"{dest_dir}{new_name}{file_ext}"

    copy_file_to_dest(source_file, dest_file)
