#!/usr/bin/python

import os
import sys
import argparse


destdir = "src/documentation"


def get_roles(directory):
    _roles = []

    _rolesdir = "%s/roles/" % directory
    for _role in os.listdir(_rolesdir):
        _roledir = "%s/%s" % (_rolesdir, _role)
        if not os.path.isdir(_roledir) or \
           not os.path.isdir("%s/meta" % _roledir) or \
           not os.path.isdir("%s/tasks" % _roledir):
            continue
        if _role.startswith("ipa"):
            _role = _role[3:]
        _roles.append(_role)

    return sorted(_roles)


def get_module_readmes(directory):
    _readmes = []

    for _item in os.listdir(directory):
        if _item.startswith("README-") and \
           _item.endswith(".md"):
            _item = _item[7:-3]
            _readmes.append(_item)

    return sorted(_readmes)


def readlines(file_in):
    try:
        in_f = open(file_in, "r")
    except IOError:
        print("Failed to open '%s' for reading" % file_in)
        sys.exit(1)

    lines = in_f.readlines()
    in_f.close()

    return lines


def open_outfile(file_out):
    try:
        out_f = open(file_out, "w")
    except IOError:
        print("Failed to open '%s' for writing" % file_out)
        sys.exit(1)

    print("Writing %s" % file_out)

    return out_f


valid_code_block_declarations = [
    "```\n",
    "```ini\n",
    "```yaml\n",
    "```json\n",
    "```bash\n"
]

def convert_write(filename, lines, out_f):
    in_raw = False
    for line in lines:
        if in_raw:
            out_f.write(line)
            if line == "```\n":
                in_raw = False
                out_f.write("{% endraw %}\n")
        else:
            if line.startswith("```"):
                if line not in valid_code_block_declarations:
                    print("%s: Unknown code block declaration: %s" %
                          (filename, repr(line)))
                in_raw = True
                out_f.write("{% raw %}\n")
            out_f.write(line)


def copy_role_doc(srcdir, role):
    file_in = "%s/roles/ipa%s/README.md" % (srcdir, role)
    file_out = "src/documentation/roles/%s.md" % role

    lines = readlines(file_in)
    out_f = open_outfile(file_out)

    out_f.write("---\nlayout: page\ntitle: ipa%s\n---\n" % role)

    if " role" in lines[0] and lines[1].startswith("==="):
        lines = lines[2:]

    convert_write(file_in, lines, out_f)
    out_f.close()


def copy_module_doc(srcdir, module):
    file_in = "%s/README-%s.md" % (srcdir, module)
    file_out = "src/documentation/plugins/%s.md" % module

    lines = readlines(file_in)
    out_f = open_outfile(file_out)

    out_f.write("---\nlayout: page\ntitle: ipa%s\n---\n" % module)

    if (" module" in lines[0] or " Module" in lines[0]) and \
       lines[1].startswith("==="):
        lines = lines[2:]

    convert_write(file_in, lines, out_f)
    out_f.close()


parser = argparse.ArgumentParser(usage="update_docs.py <ansible-freeipa repo directory>")
options, args = parser.parse_known_args()

if len(args) != 1:
    parser.print_help()
    sys.exit(1)

srcdir = args[0]

if not os.path.isdir("%s/roles" % srcdir) or \
   not os.path.isdir("%s/plugins/modules" % srcdir) or \
   not os.path.isfile("%s/utils/ansible-freeipa.spec.in" % srcdir):
    print("The given path is not a valid ansible-freeipa repository!")
    sys.exit(-1)

roles = get_roles(srcdir)
module_readmes = get_module_readmes(srcdir)

for role in roles:
    copy_role_doc(srcdir, role)

for readme in module_readmes:
    copy_module_doc(srcdir, readme)
