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
found = result.find('font')

if found:
  print found
  sys.exit(1)

f = file(dst)
f.write(result.text)
f.close()

