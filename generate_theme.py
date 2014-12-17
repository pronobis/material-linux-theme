#!/usr/bin/env python

# material-linux - Auto-generated set of consistent themes for a Linux
#                  desktop based on the Android Material color palette.
#
# Copyright (C) 2014 Andrzej Pronobis
# Author: Andrzej Pronobis <a.pronobis@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
from x256 import x256
from material import material_palette
from palette import selected_palette, colors


def main():

    # Resolve colors
    print("Resolving colors in selected palette:")
    for name, value in selected_palette.iteritems():
        parts = value.split('-')
        x = '-'.join(parts[:-1])
        y = ''.join(parts[-1:])
        if (len(x) > 0) and (x in material_palette):
            z = material_palette[x][y]
            print("-> Replacing %s with %s" % (value, z))
            selected_palette[name] = z
        else:
            print("-> Skipping %s" % value)

    print("\nResolving colors other colors:")
    for name, value in colors.iteritems():
        z = selected_palette[value]
        colors[name] = z
        print("-> Replacing %s with %s" % (name, z))

    # Compile color tags
    colors2 = {}
    # Palette
    for color, value in selected_palette.iteritems():
        colors2["[material:" + color + "]"] = value
    # Palette 256
    for color, value in selected_palette.iteritems():
        x = x256.from_hex(value[1:])
        colors2["[material256:" + color + "]"] = str(x)
    # Other colors
    for color, value in colors.iteritems():
        colors2["[material:" + color + "]"] = value
    # Other colors 256
    for color, value in colors.iteritems():
        x = x256.from_hex(value[1:])
        colors2["[material256:" + color + "]"] = str(x)
    pattern = re.compile(r'(' + '|'.join(
        re.escape(key) for key in colors2.keys()) + r')')

    # Get def files
    script_dir = os.path.dirname(__file__)
    def_dir = os.path.join(script_dir, './defs')
    out_dir = os.path.join(script_dir, './out')
    def_files = [f for f in os.listdir(def_dir)
                 if os.path.isfile(os.path.join(def_dir, f))]
    print("\nParsing files: %s" % def_files)

    # Process files
    for df in def_files:
        in_file = open(os.path.join(def_dir, df))
        out_file = open(os.path.join(out_dir, df), 'w')
        for line in in_file:
            result = pattern.sub(lambda x: colors2[x.group()], line)
            out_file.write(result)
        out_file.close()
        in_file.close()

if __name__ == '__main__':
    main()
