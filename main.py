__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile
from pathlib import Path

working_directory = Path(__file__).absolute().parent

cache_directory = working_directory / "cache"
testzip_path = working_directory / "data.zip"


def clean_cache():
    current_dirlist = os.listdir()
    if "cache" not in current_dirlist:
        os.mkdir("cache")
    else:
        for file in os.listdir(cache_directory):
            os.remove(os.path.join(cache_directory, file))


def cache_zip(zipfile_path, cachedir_path):
    with ZipFile(zipfile_path, "r") as zip:
        print("Unzipping files now, please stand by...")
        zip.extractall(cachedir_path)
        print(f"All files unzipped succesfully in {cachedir_path}")


def cached_files():
    cache_list = os.listdir(cache_directory)
    return_list = []
    for file in cache_list:
        return_list.append(f"{cache_directory}\{file}")
    return return_list


def find_password(cached_list):
    for file in cached_list:
        opened_file = open(file)
        for line in opened_file:
            if "password" in line:
                return line[10:-1]
        opened_file.close()
