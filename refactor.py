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
patchfiles = [file for file in os.listdir()
              if os.path.isfile(os.path.join(currentDir, file))
              if re.search(".patch$", file)
              ]

# seek a patch file for ^+++ b/ and return all occurrences
# "diff" seem not to be included in all patches


def returnDiff(self):
    difflist = []
    for line in self:
        if re.search(r"^\+{3}\sb\/", line):
            line = line.strip('\n')  # strip line break
            difflist.append(line)
    return(difflist)


# bring patch file names and target files together in a dictionary
d_raw = {}
for patchfile in patchfiles:
    # print("patchfile:", patchfile) 'DEBUG
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        diffs = returnDiff(file)
    d_raw[patchfile] = diffs

print('\n' * 3)

if which("splitdiff"):  # check if splitdiff is available
    print("splitdiff found")

    for patchfile in d_raw:  # grab patches with more than one target
        if len(d_raw[patchfile]) > 1:
            subprocess.call(["splitdiff", "-a", patchfile])  # split them
            # disable old file by renaming
            os.rename(patchfile, patchfile + ".disabled")

else:
    print("splitdiff not found. Install \"patchutils\" and try again.")

# scan for patchfiles again
patchfiles_splitted = [file for file in os.listdir()
                       if os.path.isfile(os.path.join(currentDir, file))
                       if re.search(".patch$", file)
                       ]

# again bring patchfiles and
d_splitted = {}
for patchfile in patchfiles_splitted:
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        diffs = returnDiff(file)
    d_splitted[patchfile] = diffs

# sort by target file to patch
sorted_d = sorted(d_splitted.items(), key=lambda kv: kv[1])

# Print to screen
for x in sorted_d:
   print(x)


"""
for patchfiles,diffs in d_raw.items():
    print(patchfiles)
    print(diffs)
    print()
"""
