import sys
import re



def extract_names(filename):
   result=[]
   f=open(filename,'rU')
   for i in f:
      match=re.search(r'Popularity in (\d\d\d\d)',i)
      if match :

         result.append(match.group(1)+)
         break
   names=[]
   for i in f:
     match=re.search(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',i)
     if match :
        names.append(match.group(2)+"-->"+match.group(1))
        names.append(match.group(3)+"-->"+match.group(1))
   names.sort()
   return result+names


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)


  summary = False
  if args[0] == '--summaryfile':
     summary = True
     del args[0]

# +++your code here+++
  l=extract_names(args[0])
  print l

# For each filename, get the names, then either print the text output
# or write it to a summary file




if __name__ == '__main__':
  main()
