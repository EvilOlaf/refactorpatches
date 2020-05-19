"""
    Refactor patch folders
    Copyright (C) 2020 Werner

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""


from pathlib import Path
import os
import re
import subprocess
from shutil import which
import readline

# necessary for tab completion user input
readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

print("Current directory:", Path.cwd())

os.chdir(os.path.join(Path.cwd(),
                      input("Select patch folder (you can tab-complete): ")))
print("Working directory is now:", Path.cwd())


print("Grabbing all .patch files")
PatchFilesInFolder = [file for file in os.listdir()
                      if os.path.isfile(os.path.join(Path.cwd(), file))
                      if re.search(".patch$", file)
                      ]


def returnAllDiffsAsTuple(self):
    # seek a patch file for '^+++ ' and return all occurrences
    # "diff" seem not to be included in all patches
    difflist = []
    for line in self:
        if re.search(r"^\+{3}\s", line):
            difflist.append(line.strip('\n'))  # append and strip line break
    return(tuple(difflist))


def returnSingleDiff(self):
    # seek a patch file for '^+++ ' and return the occurrence
    for line in self:
        if re.search(r"^\+{3}\s", line):
            return(line.strip('\n'))


# bring patch file names and target files together in a dictionary
patchDictBefore = {}
print("Collect target file and link to filename")
for patchfile in PatchFilesInFolder:
    # print("patchfile:", patchfile) 'DEBUG
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        diffs = returnAllDiffsAsTuple(file)
    patchDictBefore[patchfile] = diffs

if which("splitdiff"):  # check if splitdiff is available
    print("splitdiff found")
    print("splitting patches with multiple file targets into individual patches")
    for patchfile in patchDictBefore:  # grab patches with more than one target
        if len(patchDictBefore[patchfile]) > 1:
            subprocess.call(["splitdiff", "-a", patchfile])  # split them
            # disable old file by renaming
            os.rename(patchfile, patchfile + ".disabled")
    print("Done. Old files renamed.")

else:
    print("splitdiff not found. Install \"patchutils\" and try again.")
    print("Skipping splitting")

# scan for patches again
print("Selection all .patch files (again)")
patchfiles_splitted = [file for file in os.listdir()
                       if os.path.isfile(os.path.join(Path.cwd(), file))
                       if re.search(".patch$", file)
                       ]

# again bring patches and target files together
print("Scan for targets again and link information")
d_splitted = {}
for patchfile in patchfiles_splitted:
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        d_splitted[patchfile] = returnSingleDiff(file)

# sort by target file to patch
print("Sorting patches by target file")
sorted_d = sorted(d_splitted.items(), key=lambda kv: kv[1])

#Print table, format values should be dynamic in future
#for patch in sorted_d:
#    print('{:<95s}{:<70s}'.format(patch[0], patch[1]))


# search for target file matches

def yield_lines():
    for line in sorted_d:
        yield line

gen1 = yield_lines()

for _ in gen1:
    a = next(gen1)
    b = next(gen1)
    if a == b:
        print("Match")
    print(a[1], b[1])
    break


"""
print(next(gen1))
print(next(gen1))
print(next(gen1))"""