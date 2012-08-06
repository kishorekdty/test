
import sys
import re
import os
import shutil
import commands

def gpath(dirname):
  result = []
  paths = os.listdir(dirname) 
  for fname in paths:
    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result


def copy(paths, to_dir):
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, fname))
 


def tozip(paths, zipfile):
 
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print "Command " + cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

 
  paths = []
  for dirname in args:
    paths.extend(gpath(dirname))

  if todir:
    copy(paths, todir)
  if tozip:
    tozip(paths, tozip)
 
if __name__ == "__main__":
  main()
