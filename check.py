#!/usr/bin/python
# -*- coding=utf8 -*-
'''
usage
	python check.py $< -o $@
'''

import sys
from BeautifulSoup import BeautifulSoup


assert len(sys.argv) == 4

src = sys.argv[1]
dst = sys.argv[3]
print >>sys.stderr, src, dst

f = file(src)
soup = BeautifulSoup(f.read())
f.close()

result = soup.find('pre')
found = None
while not found:
  found = result.find('font')
  for name, value in found.attrs:
    if name == u'color' and value == 'red':
      print found
      sys.exit(1)
  found = None

f = file(dst, 'w')
f.write(result.text.encode('utf8'))
f.close()

