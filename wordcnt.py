#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/


import sys

def print_words(filename) :
  count=worddict(filename)
  for i in count :
    print i,"-->",count[i]

def print_top(filename) :
  count=worddict(filename)
  topc=0;
  for i in count :
    if count[i]>topc :
      topc=count[i]
      topw=i
  print topw, '-->', topc

def worddict(filename):
  f=open(filename,'rU')
  count={}
  w=[]
  k=[]
  for i in f :
    k= i.lower()
    w=k.split()
    for word in w :
      if word in count.keys():
         count[word]+=1
      else :
         count[word]=1
  return count


def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
