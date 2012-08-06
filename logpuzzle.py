
import os
import re
import sys
import urllib


def url_sort_key(url):
 
  match = re.search(r'-(\w+)-(\w+)\.\w+', url)
  if match:
    return match.group(2)
  else:
    return url

def read(filename):
  
  underbar = filename.index('_')
  host = filename[underbar + 1:]
  url = {}
  f = open(filename)
  for line in f:
    match = re.search(r'"GET (\S+)', line)
    if match:
      path = match.group(1)
      if 'puzzle' in path:
        url['http://' + host + path] = 1

  return sorted(url.keys(), key=url_sort_key)
 


def download(img_urls, dest):
  
  if not os.path.exists(dest):
    os.makedirs(dest)

  index = file(os.path.join(dest, 'index.html'), 'w')
  index.write('<html><body>\n')

  i = 0
  for img_url in img_urls:
    local_name = 'img%d' % i
    print 'Downloading...', img_url
    urllib.urlretrieve(img_url, os.path.join(dest, local_name))
    index.write('<img src="%s">' % (local_name,))
    i += 1

  index.write('\n</body></html>\n')
  index.close()
 

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read(args[0])

  if todir:
    download(img_urls, todir)
  
if __name__ == '__main__':
  main()
