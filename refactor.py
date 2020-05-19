"""
Code that has been copied from the www is mentioned in the references file.
Make sure to check it to get credit.


# find all patches in directory
# grab those with multiple targets and split them
# print a (pretty) table with patches to files linked to each other
#
# profit!

"""

import pathlib
import os
import re
import subprocess
from shutil import which
import readline

readline.set_completer_delims(' \t\n=')
readline.parse_and_bind("tab: complete")

print("Current directory:", pathlib.Path.cwd())

os.chdir(os.path.join(pathlib.Path.cwd(),
                      input("Select patch folder (you can tab-complete): ")))
print("Working directory is now:", pathlib.Path.cwd())


print("Grabbing all .patch files")
PatchFilesInFolder = [file for file in os.listdir()
                      if os.path.isfile(os.path.join(pathlib.Path.cwd(), file))
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
    # a patch file for '^+++ ' and return the occurrence
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

# scan for PatchFilesInFolder
# again
print("Selection all .patch files (again)")
patchfiles_splitted = [file for file in os.listdir()
                       if os.path.isfile(os.path.join(pathlib.Path.cwd(), file))
                       if re.search(".patch$", file)
                       ]

# again bring PatchFilesInFolder
# and
print("Scan for targets again and link information")
d_splitted = {}
for patchfile in patchfiles_splitted:
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        d_splitted[patchfile] = returnSingleDiff(file)

# sort by target file to patch
print("Sorting patches by target file")
sorted_d = sorted(d_splitted.items(), key=lambda kv: kv[1])

#Print table, format values should be dynamic in future
for patch in sorted_d:
    print('{:<95s}{:<70s}'.format(patch[0], patch[1]))