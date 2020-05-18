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

# Grab files *.patch$ in current dir
patchfiles = [file for file in os.listdir() 
        if os.path.isfile(os.path.join(currentDir, file))
        if re.search(".patch$", file)
        ]


#seek file for diff and return all of them
def returnDiff(self):
    difflist = []
    for line in self:
        if re.search("^diff\s", line):
       #if "diff --git" in line:
            difflist.append(line)
    #print("difflist:", difflist) #DEBUG
    return(difflist)

"""
def dumpclean(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print(k)
                dumpclean(v)
            else:
                print('%s : %s' % (k, v))
    elif isinstance(obj, list):
        for v in obj:
            if hasattr(v, '__iter__'):
                dumpclean(v)
            else:
                print(v)
    else:
        print(obj)
#dumpclean(d)
"""

#DEBUG
#for file in patchfiles:
#    print(file)

# collect information about patchfiles and diffs
d = {} #empty dictionary
for patchfile in patchfiles:
    #print("patchfile:", patchfile) 'DEBUG
    with open(patchfile, encoding="utf-8", errors="replace") as file:
        diffs = returnDiff(file)
    d[patchfile] = diffs

print()
print()


# sort by diff
sortedd = sorted(d.items(), key=lambda kv: kv[1])

for x in sortedd:
    print(x)

#print(sorted_x)

"""
for patchfiles,diffs in d.items():
    print(patchfiles)
    print(diffs)
    print()
"""




