"""
Code that has been copied from the www is mentioned in the references file.
Make sure to check it to get credit.

"""

import pathlib
import os
import re

# rewrite for later: add recursive walk through patch directories
#snipped for later use
#   for x in os.walk(cwd):
#       print(x)
#   3-Tuple: dirpath, dirnames, filenames
print("Current directory:", pathlib.Path.cwd())
os.chdir(os.path.join(pathlib.Path.cwd(), "patchfolder"))
print("Working directory:", pathlib.Path.cwd())

currentDir = pathlib.Path.cwd()

# print(os.listdir()) # list all files/dirs in current directory

# Grab files *.patch$ in current dir only
patchfiles = [file for file in os.listdir() 
        if os.path.isfile(os.path.join(currentDir, file))
        if re.search(".patch$", file)
        ]


#seek a patch file for ^+++ b/ and return all occourances
# "diff" seem not to be included in all patches
def returnDiff(self):
    difflist = []
    for line in self:
        if re.search(r"^\+{3}\sb\/", line): 
            line = line.strip('\n') #strip line break
            difflist.append(line)
    return(difflist)




# bring patch file names and target files together in a dictionary
d = {}
for patchfile in patchfiles:
    #print("patchfile:", patchfile) 'DEBUG
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        diffs = returnDiff(file)
    d[patchfile] = diffs

print('\n' * 3)


# sort by target file to patch
sorted_d = sorted(d.items(), key=lambda kv: kv[1])

# Print to screen
#for x in sorted_d:
#    print(x)



"""
for patchfiles,diffs in d.items():
    print(patchfiles)
    print(diffs)
    print()
"""

# for later: split patches that affect multiple targets into files
# grab patches with more than one target
for i in d:
    if len(d[i]) > 1:
        print(len(d[i]), i)


