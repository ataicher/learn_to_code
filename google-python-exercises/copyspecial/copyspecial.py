#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def printspecial(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    match = re.search(r'\w+__\w+__\.\w+', filename)
    if match:
      path = os.path.join(dir, filename)
      print os.path.abspath(path)

def copyspecial(dirs, todir):
  if not os.path.exists(todir):
    os.mkdir(todir)
  for dir in dirs:
    filenames = os.listdir(dir)
    for filename in filenames:
      match = re.search(r'\w+__\w+__\.\w+', filename)
      if match:
        source = os.path.join(dir, filename)
        source = os.path.abspath(source)
        dest = os.path.abspath(todir)
        shutil.copy(source, dest)

def zipspecial(dirs, tozip):
  cmd = 'zip -j ' + tozip 
  for dir in dirs:
    filenames = os.listdir(dir)
    for filename in filenames:
      match = re.search(r'\w+__\w+__\.\w+', filename)
      if match:
        source = os.path.join(dir, filename)
        source = os.path.abspath(source)
        cmd = cmd + ' ' + source
  #print 'about to execute shell command:', cmd
  #return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('there was an error:' + output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  #todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
    copyspecial(args, todir)

  #tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    zipspecial(args, tozip)
    
  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  dir = args[0]
  #printspecial(dir)

if __name__ == "__main__":
  main()
