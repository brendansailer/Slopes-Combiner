#!/usr/bin/env python3

import os
from sys import argv
from lxml import etree

PREFIX = '{http://www.topografix.com/GPX/1/1}'

def combine_gpx(base_filename, other_filenames):
    """
    Make a combination of a bunch of GPX files by adding <trk> from all the
    files in `other_filenames` to the root of the file at `base_filename` and
    returning a string of the resulting XML.
    """

    base_file = open(base_filename)
    tree = etree.parse(base_file)
    base_file.close()
    root = tree.getroot()

    for filename in other_filenames:
        other_file = open(filename)
        other_tree = etree.parse(other_file)
        root.append(other_tree.getroot().find(PREFIX + 'trk'))

    return etree.tostring(tree)


if __name__ == '__main__':
    dirname = argv[-1]
    filenames = os.listdir(dirname)

    gpx_filenames = [os.path.join(dirname, f) for f in filenames if os.path.splitext(f)[1] == '.gpx']

    print(combine_gpx(gpx_filenames[0], gpx_filenames[1:]))
