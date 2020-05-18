"""
split a .patch file with multiple targets into individual files
"""

import sys

def splitpatch(self):
#    try:
        with open(self, encoding="utf-8", errors="replace") as file:
            content = file.read() # put patch to string in memory
            delimiter = "diff "
            content = ([e+delimiter for e in content.split(delimiter) if e])
            for i in content:
                print(i)
#    except:
#        print("Nope.")


# DEBUG
splitpatch("test.patch")
# DEBUG
