"""
Code that has been copied from the www is mentioned in the references file.
Make sure to check it to get credit.


# find all patches in directory
# grab those with multiple targets and split them
#
# profit!

"""

import pathlib
import os
import re
import subprocess
from shutil import which


print("Current directory:", pathlib.Path.cwd())
os.chdir(os.path.join(pathlib.Path.cwd(), "patchfolder"))
print("Working directory:", pathlib.Path.cwd())

currentDir = pathlib.Path.cwd()

# Grab active patches in current directory
print("Grabbing all .patch files")
patchfiles = [file for file in os.listdir()
              if os.path.isfile(os.path.join(currentDir, file))
              if re.search(".patch$", file)
              ]

# seek a patch file for ^+++ b/ and return all occurrences
# "diff" seem not to be included in all patches


def returnDiffAsList(self):
    difflist = []
    for line in self:
        if re.search(r"^\+{3}\s", line):
            line = line.strip('\n')  # strip line break
            difflist.append(line)
    return(difflist)


def returnSingleDiff(self):
    for line in self:
        if re.search(r"^\+{3}\s", line):
            output = line.strip('\n')  # strip line break
    return(output)


# bring patch file names and target files together in a dictionary
d_raw = {}
print("Collect target file and link to filename")
for patchfile in patchfiles:
    # print("patchfile:", patchfile) 'DEBUG
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        diffs = returnDiffAsList(file)
    d_raw[patchfile] = diffs

if which("splitdiff"):  # check if splitdiff is available
    print("splitdiff found")
    print("splitting patches with multiple file targets into individual patches")
    for patchfile in d_raw:  # grab patches with more than one target
        if len(d_raw[patchfile]) > 1:
            subprocess.call(["splitdiff", "-a", patchfile])  # split them
            # disable old file by renaming
            os.rename(patchfile, patchfile + ".disabled")
    print("Done. Old files renamed.")

else:
    print("splitdiff not found. Install \"patchutils\" and try again.")
    print("Skipping splitting")

# scan for patchfiles again
print("Selection all .patch files (again)")
patchfiles_splitted = [file for file in os.listdir()
                       if os.path.isfile(os.path.join(currentDir, file))
                       if re.search(".patch$", file)
                       ]

# again bring patchfiles and
print("Scan for targets again and link information")
d_splitted = {}
for patchfile in patchfiles_splitted:
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        d_splitted[patchfile] = returnSingleDiff(file)

# sort by target file to patch
print("Sorting patches by target file")
sorted_d = sorted(d_splitted.items(), key=lambda kv: kv[1])

print("Patches and target files")
for x in sorted_d:
    print(x)
# print(d_splitted)


"""
for patchfiles,diffs in d_raw.items():
    print(patchfiles)
    print(diffs)
    print()
"""
