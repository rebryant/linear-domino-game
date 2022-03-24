#!/usr/bin/python

#####################################################################################
# Copyright (c) 2022 Marijn Heule, Randal E. Bryant, Carnegie Mellon University
# Last edit: March 23, 2022
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
########################################################################################

# Time the execution of a program.  Force termination if that program exceeds a time limit

import sys
import subprocess
import datetime
import os.path

def usage(name):
    print("Usage: %s TLIM PATH Args ..." % name)
    print("    TLIM:    Runtime limit (in seconds)")
    print("    PATH:    Path of executable program")
    print("    Args ... Arguments to pass to invoked program")

def runprog(timelimit, path, arglist):
    alist = [path] + arglist
    start = datetime.datetime.now()
    p = subprocess.Popen(alist)
    try:
        p.wait(timeout=timelimit)
    except subprocess.TimeoutExpired:
        p.kill()
        print("Execution of %s FAILED.  Timed out after %d seconds" % (path, timelimit))
        sys.exit(1)
    delta = datetime.datetime.now() - start
    secs = delta.seconds + 1e-6 * delta.microseconds
    print("Program %s completed with exit code %d" % (path, p.returncode))
    print("Total time: %.3f seconds" % secs)
    return
    
def run(name, arglist):
    if len(arglist) < 2:
        usage(name)
        return
    try:
        timelimit = float(arglist[0])
    except:
        print("Invalid time limit '%s'" % arglist[0])
        usage(name)
        return
    path = arglist[1]
    if not os.path.exists(path):
        print("Invalid path '%s'" % path)
        usage(name)
        return
    arglist = arglist[2:]
    runprog(timelimit, path, arglist)
          

name = sys.argv[0]
arglist = sys.argv[1:]
run(name, arglist)
    
    
