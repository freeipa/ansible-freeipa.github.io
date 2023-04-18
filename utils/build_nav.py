#!/usr/bin/python

import os
import sys
import yaml

nav_in="src/_data/nav_in.yml"
nav_out="src/_data/nav.yml"


def get_file_header(filename):
    header = {}
    with open(filename, "r") as f_in:
        lines = f_in.readlines()

        if len(lines) > 0 and lines[0] == "---\n":
            for line in lines[1:]:
                if ": " in line:
                    key, text = line.split(": ")
                    if key in header:
                        print("Duplicate key in header: %s: %s" % (filename,
                                                                   key))
                    header[key] = text.strip()
                elif line == "---\n":
                    return(header)
                else:
                    print("Invalid header: %s" % filename)
                    sys.exit(-1)
    return None


def get_file_title(filename):
    header = get_file_header(filename)

    if header is not None and "title" in header:
        return header["title"]
    return None


def autosubdir(item, subdir):
    dirs = {}
    files = {}

    for name in os.listdir(subdir):
        _path = os.path.join(subdir, name)
        if name.startswith("."):
            pass
        if os.path.islink(_path):
            print("Ignoring %s" % _path)
        else:
            if os.path.isdir(_path):
                dirs[name] = _path
            else:
                files[name] = _path

    if "index.md" not in files:
        print("Missing index.md in %s" % subdir)
        sys.exit(-1)
    del files["index.md"]

    if len(dirs) + len(files) > 0:
        item["subitems"] = []

    for _dir in sorted(dirs):
        index_md = os.path.join(dirs[_dir], "index.md")
        _title = get_file_title(index_md)
        if _title is None:
            print("Missing title in %s" % index_md)
            sys.exit(-1)
        _item = {}
        _item["path"] = "%s/" % _dir
        _item["title"] = _title
        item["subitems"].append(_item)
        autosubdir(_item, dirs[_dir])

    for _file in sorted(files):
        if not _file.endswith(".md"):
            print("Ignoring %s" % files[_file])
            continue
        _title = get_file_title(files[_file])
        if _title is None:
            print("Missing title in %s" % files[_file])
            sys.exit(-1)
        _item = {}            
        _item["path"] = "%s.html" % os.path.splitext(_file)[0]
        _item["title"] = _title
        item["subitems"].append(_item)


with open(nav_in, "r") as f_in:
    try:
        data = yaml.safe_load(f_in)
    except yaml.YAMLError as e:
        print(e)
        sys.exit(-1)
    else:
        for item in data:
            if "autosubitems" in item and item["autosubitems"]:
                subdir = "src/%s" % item["path"]
                autosubdir(item, subdir)

with open(nav_out, "w") as f_out:
    yaml.safe_dump(data, f_out)
