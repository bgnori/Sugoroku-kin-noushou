#!/usr/bin/python
# -*- coding=utf8 -*-

import sys
import mechanize

option_settings = {
  "mygaiji": "checked", 
  "myhansp": "checked",
  "myhanpar": "checked",
  "myzensp": "checked",
  "my78hosetsu_tekiyo": "checked",
  "myhosetsu_tekiyo": "checked",
  "my78": "checked",
  "myjyogai": "checked",
  "mysimplesp": "checked",
  "mypre": "checked",
}

class FormWrapper(object):
  ''' I prefer control object over value for access by name.'''
  def __init__(self, target):
    self.target = target

  def __getattr__(self, name):
    return self.target.find_control(name)

  def __getitem__(self, name):
    return self.target.find_control(name)


br = mechanize.Browser()
br.open("http://www.aozora.jp/tools/checker.cgi")

print >> sys.stderr, br.title().decode('shiftjis')

forms =  list(br.forms())
assert len(forms) == 1
form = forms[0]

w = FormWrapper(form)
w.mytext.value = sys.stdin.read().decode('utf8').encode('shiftjis')
for k, v in option_settings.items():
  op = w[k]
  if (v == "checked"):
    op.value=['on']

import urllib
url, data, hdrs = form.click_request_data()
r = urllib.urlopen(url, data)

print >> sys.stderr, r.info()
dat = r.read().decode('shiftjis')
f = open('header.html', 'w')
sys.stdout.write(dat.encode('utf8'))


