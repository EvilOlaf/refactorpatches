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


from prettytable import PrettyTable
from pathlib import Path
import os
import re
import subprocess
from shutil import which
import readline
import sys

try:
    assert sys.version_info >= (3, 8, 3)
except:
    print("\n===============================================================")
    print("This script has been written and tested with Python 3.8.2 only.")
    print("Feel free to try with other versions.")
    print("===============================================================")

# a better code structure....
# add command line parameters
# target folder
# what to do with it
# possibility to add absolute path
# fix patches where no targets found
# necessary information if patch creates a new file or editing an existing one?

# 1. ask user what to do
# 1.1 print list of patches sorted by their first target
# 1.2 print list of patches after splitting and sorting by their targets
# 1.3 print list of targets that are affected by 2 or more patches
# 2. ask user for directory
# 3. do the work
# 4. ask if save we should save the output to file
# 5. goto 1 or exit


# Definitions


def returnAllDiffsAsTuple(self):
    # seek a patch file for '^+++ ' and return all occurrences
    # "diff" seem not to be included in all patches
    difflist = []
    for line in self:
        if re.search(r"^\+{3}\s", line):
            # append and strip line break
            difflist.append(line.strip('\n').strip("+++ b"))
    return(tuple(difflist))


def returnSingleDiff(self):
    # seek a patch file for '^+++ ' and return the occurrence
    for line in self:
        if re.search(r"^\+{3}\s", line):
            return(line.strip('\n').strip("+++ b"))


# Main loop
print("""
Patch comparison

Options:
1 = print a list of patches sorted by their first target file

    Example:
        mypatch.patch -> mycode.c, mycode.h, myothercode.c, ...

2 = split patches targeting multiple files into seperated patches and then
    print a list sorted by the target file.
    Optionally show target files only that are altered by multiple patches.

    Example:
        mypatch.patch                                   -> mycode.c
        my2ndpatch.patch                                -> mycode.c
        my_other_patch_that_fixes_something_else.patch  -> mycode.c

0 = Exit
""")


while True:
    mainInput = input("Enter a number: ")  # Select what to do
    if not mainInput == "0":  # for any step we need a working directory
        print("Current directory:", Path.cwd())
        foldersInCwd = ([a for a in os.listdir(".") if os.path.isdir(a)])
        print()
        for folder in foldersInCwd:
            print(folder)
        print()

        # necessary for tab completion user input
        readline.set_completer_delims(' \t\n=')
        readline.parse_and_bind("tab: complete")

        try:
            os.chdir(os.path.join(Path.cwd(),
                                  input("Select patch folder (you can tab-complete): ")))
        except:
            print("That did not work :(")
            exit()
        print("Working directory is now:", Path.cwd())
        print()

        # for any step we need the patchlist beforehand
        print("Grabbing all .patch files", end='')
        PatchFilesInFolder = [file for file in os.listdir()
                              if os.path.isfile(os.path.join(Path.cwd(), file))
                              if re.search(".patch$", file)
                              ]
        print(" - OK. Found", len(PatchFilesInFolder), "patches.")

        # create dictionary with
        # value : patchfile name
        # key/s : target file/s
        # for any step we need this dictionary
        patchDictBefore = {}
        print("Collect target file and link to filename", end='')
        for patchfile in PatchFilesInFolder:
            with open(patchfile, encoding="utf-8", errors="replace") as file:
                diffs = returnAllDiffsAsTuple(file)
                patchDictBefore[patchfile] = diffs
        print(" - OK")

    if mainInput == "1":  # print list of patches sorted by their first target
        sortedpatchDictBefore = sorted(
            patchDictBefore.items(), key=lambda kv: kv[1])
        print("\nOutput is sorted by target file. If a patch contains")
        print("multiple targets the first match is relevant.\n\n")
        for item in sortedpatchDictBefore:
            print(item[0], "->", item[1])
        print("\n\n")

    elif mainInput == "2":  # print list of patches after breaking them down
        # into their targets and sort it their targets
        if which("splitdiff"):  # check if splitdiff is available
            print("Splitting patches with multiple targets into individual patches.")
            warning = input("This cannot be undone. Proceed? (y/n): ")
            if not warning == "y":
                print("Aborting...")
                exit()

            print("OK. Started splitting...")
            for patchfile in patchDictBefore:  # grab patches with more than one target
                if len(patchDictBefore[patchfile]) > 1:
                    subprocess.call(
                        ["splitdiff", "-a", patchfile])  # split them
                    # disable old file by renaming
                    os.rename(patchfile, patchfile + ".splitted")
            print("Done. Old files have been renamed to \"*.splitted\"")

            print("Grabbing all .patch files", end='')
            patchfiles_splitted = [file for file in os.listdir()
                                   if os.path.isfile(os.path.join(Path.cwd(), file))
                                   if re.search(".patch$", file)
                                   ]
            print(" Done.")

            # bring patches and target files together
            print("Collect target file and link to filename", end='')
            splittedPatchDict = {}
            for patchfile in patchfiles_splitted:
                with open(patchfile, encoding="utf-8", errors="replace") as file:
                    splittedPatchDict[patchfile] = returnSingleDiff(file)
            print(" Done.")

            sortedSplittedPatchDict = sorted(
                splittedPatchDict.items(), key=lambda kv: kv[1])
            print("\nOutput is sorted by target file.\n\n")
#            for item in sortedSplittedPatchDict:
#                print(item[0], "->", item[1])
            x = PrettyTable()
            x.field_names = ["Patch file", "target file"]
            x.align["Patch file"] = "l"
            x.align["target file"] = "l"
            for item in sortedSplittedPatchDict:
                x.add_row([item[0], item[1]])
            print(x)
            print("\n\n")

            print("I can filter this list and show only files that are")
            print("target of multiple patches so you could merge them.")
            if input("Should I do that? (y/n) ") == "y":
                def yield_lines():
                    for line in sortedSplittedPatchDict:
                        yield line
                gen1 = yield_lines()

                # prefeed comparator
                patchTupleA = next(gen1)
                patchTupleB = next(gen1)
                patcha = patchTupleA[0]
                patchb = patchTupleB[0]
                targetA = patchTupleA[1]
                targetB = patchTupleB[1]
                for _ in gen1:
                    if targetA == targetB:
                        print("Match found:", patcha, patchb, "->", targetA)
                #        while True:
                #            merge = input("Merge? (y/n)")
                #            if merge == "y":
                #                print("Okay")
                #                pass
                #                break
                #            elif merge == "n":
                #                print("Skipping")
                #                break
                #            else:
                #                print("y or n???")
                    else:
                        pass
                    targetA = targetB  # shift b to a
                    patchTupleA = patchTupleB
                    patcha = patchb
                    patchTupleB = next(gen1)  # refill b
                    patchb = patchTupleB[0]
                    targetB = patchTupleB[1]
            print("\n\n")

        else:
            print(
                "\"splitdiff\" not found. Install \"patchutils\" package and try again.")
            print("Exiting")
            exit()

    elif mainInput == "0":
        print("Aight, exiting. Thank you for flying with Werner Enterprises.")
        exit()

    else:
        mainInput = input("Invalid input. Enter a number: ")


exit()


# Print table, format values should be dynamic in future
# for patch in sorted_d:

#    print('{:<95s}{:<70s}'.format(patch[0], patch[1]))


# search for target file matches

"""
        x = PrettyTable()
        x.field_names = ["Patch file", "target file"]
        x.align["Patch file"] = "l"
        x.align["target file"] = "l"
        for item in sortedpatchDictBefore:
            x.add_row([item[0], item[1]])
        print(x)
"""
