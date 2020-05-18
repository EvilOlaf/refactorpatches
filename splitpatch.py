"""
split a .patch file with multiple targets into individual files
"""

#No longer needed: splitdiff -a from patchutils does the job.




"""
import sys
import re


def splitpatch(self):
    #    try:
    with open(self, encoding="utf-8", errors="replace") as file:
        #content = file.read()  # put patch to string in memory
        #print(content)
        print(file.read())
        #exit()
        splitContent = re.split(r"\n^diff\s", content)
        for i in splitContent:
            print(i)
            print('\n' * 3)


#            delimiter = "diff "
#            content = ([e+delimiter for e in content.split(delimiter) if e])
"""            for i in content:
                print(i)
                print('\n' * 3)"""
#    except:
#        print("Nope.")


# DEBUG
splitpatch("test.patch")
# DEBUG
"""