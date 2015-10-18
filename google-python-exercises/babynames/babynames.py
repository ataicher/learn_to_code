#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  
  # open file and generate text string
  f = open(filename, 'rU')
  text = f.read()

  # find the year
  match = re.search('Popularity in \d\d\d\d', text)
  year = match.group()[14:]

  # get the string containing number, boy name, and girl name
  match = re.findall(r'<td>\d+</td><td>\w+</td><td>\w+</td>', text)
  
  name_dict = {}
  for str in match:
    
    # extract number
    start_ind = 4
    end_ind = start_ind
    while str[end_ind] != '<':
      end_ind += 1
    num = str[4:end_ind]
    
    # extract boy name
    start_ind = end_ind + 9
    end_ind = start_ind
    while str[end_ind] != '<':
      end_ind += 1
    boy_name = str[start_ind:end_ind]
    if boy_name in name_dict.keys():
      if int(name_dict[boy_name]) > int(num):
        name_dict[boy_name] = num
    else:
      name_dict[boy_name] = num  

    # extract girl name
    start_ind = end_ind + 9
    end_ind = start_ind
    while str[end_ind] != '<':
      end_ind += 1
    girl_name = str[start_ind:end_ind]
    if girl_name in name_dict.keys():
      if int(name_dict[girl_name]) > int(num):
        name_dict[girl_name] = num
    else:
      name_dict[girl_name] = num 
  
  # create alphabitically sorted name rank list 
  name_rank_list = [year]
  for name in name_dict.keys():
    name_rank_list.append(name + ' ' + name_dict[name])
  return sorted(name_rank_list)
    
def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  for filename in args:
    name_rank_list = extract_names(filename)
    if summary:
      f = open(filename + '.summary', 'w')
      for str in name_rank_list:
        f.write(str + '\n')
    else:
      for str in name_rank_list:
        print str
  # +++your code here+++
  extract_names(args[0])
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
