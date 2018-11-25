#!/usr/bin/python3

import sys
import getopt
import os
import re
import shutil

def main(argv):

    usagemessage = "{}: usage: {} -v|-n [ -o dir ] dirs_to_walk".format(sys.argv[0],sys.argv[0])
    
    dryrun = False
    verbose = False
    targetdir = os.path.join(os.environ['HOME'],"targetdir")

    try:
        opts, dirs_to_walk = getopt.getopt(argv,"o:nv")
    except getopt.GetoptError:
        print(usagemessage)
        sys.exit(1)

    for opt, value in opts:
        if opt == 'n':
            dryrun = True
        if opt == 'v':
            verbose = True
        if opt == 'o':
            targetdir = value

    if not dirs_to_walk:
        print(usagemessage)
        sys.exit(2)

    if not os.path.exists(targetdir):
        os.mkdir(targetdir)

    for mypath in dirs_to_walk:
        onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and not f.startswith(".")]
        print(len(onlyfiles))
        for myfile in onlyfiles:
            mymatch = re.match(r'.*([A-Za-z0-9])',myfile[::-1])
            if not mymatch: 
                continue
            firstchar = mymatch.group(1)
            targetsubdir = os.path.join(targetdir,firstchar.lower())
            if not os.path.exists(targetsubdir):
                os.mkdir(targetsubdir)
            if verbose or dryrun:
                print("I want to move {} to {}".format(os.path.join(mypath,myfile),targetsubdir))
            if not dryrun:
                shutil.move(os.path.join(mypath,myfile),targetsubdir)


if __name__ == "__main__":
    main(sys.argv[1:])
