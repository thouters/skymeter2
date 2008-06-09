#!/usr/bin/env python
#   PySkymeter 2.1.0, 2008/03/25
#   Skymeter, raadpleegt de Volumepagina van skynet selfcare,
#   verwerkt deze en bekomt de nuttige informatie.
#   
#   Copyright (C) 2005 Thomas Langewouters. 
#   
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#   
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import re, os, time
import urllib, urllib2
__version__ = "2.1.0"

class SkymeterError(Exception):
    def __init__(self, errorstring):
        self.error = errorstring

class Meter:
    unitmap = {'GB':1024,'MB':1}
    def __init__(self,data):
        (self.value,self.total) = map(lambda s: self.string2num(s), data)

    def __repr__(self):
        return "%10s: %2.f%%: %s of %s" % \
            (   self.__class__.__name__,
                (float(self.value) / self.total)*100,
                self.num2string(self.value),
                self.num2string(self.total)     )

    def string2num(self,s):
        c = 0
        s = s.split(' ')
        for m in filter(lambda p: s.count(p[0]),self.unitmap.iteritems()):
           c += float(s[s.index(m[0]) -1]) * m[1]
        return c
     
    def num2string(self,n):
        s = "%d GB" % (n/1024)
        if (n % 1024):
            s +=" %d MB" % (n%1024)
        return s

class BasicMeter(Meter):
    pass
class PackMeter(Meter):
    pass

class skymeter:
    confmap = {'user': 'username' ,'pass':'password'}
    conffile = "~/.skymeterrc"
    username = ''
    password = ''
    data = []
    time = None
    timeformat = "%a, %d %b %Y %H:%M:%S"
    _version = "2.1.0"
    
    def __init__(self):
        try:
            f = open(os.path.expanduser(self.conffile),"r")
            s = f.read().split('\n')
            f.close()
        except:
            return

        s = filter(lambda x:(x[0:4] in self.confmap.keys()),s)
        s = map(lambda y:(self,self.confmap[y[0:4]],y[4:].strip()),s)
        for kv in s:
            setattr(*kv)

    def testCreds(self):
        # FIXME: test more thoroughly!
        if self.username == "" or self.password == "":
           raise SkymeterError("Invalid Credentials!") 

    def savecred(self):
        self.testCreds()
        try:
            f = open(os.path.expanduser(self.conffile),"w")
            f.write("user %s\npass %s" %(self.username,self.password))
            f.close()
        except:
           raise SkymeterError("File I/O error") 

    def GetData(self):
        self.data = []
        self.testCreds()

        baseurl = "https://e-care.skynet.be/index.cfm"
        postdata = { "form_login":self.username, "form_password":self.password,
                     "Langue_Id":"2", "fuseaction":"CheckLoginConnection" }
        try:
            buffer = urllib2.urlopen(baseurl +"?function=connection.getVolume",
                                urllib.urlencode(postdata)).read()
        except:
            raise SkymeterError("Network failure")

        if buffer.find("Basic monthly volume:") == -1:
            raise SkymeterError("Authentication failure")

        bas = r"Monthly volume used\s*<strong>([^<]+)<\/strong>" + \
                 r"\s+out of\s+<strong>([^<]+)"
        pack = r"You used\s*<strong>\s*([^<]+)\s*<\/strong>\s*" + \
                 r"out\s*of\s*<strong>\s*([^<]+)\s*<\/strong>"
        bas = re.compile(bas)
        pack = re.compile(pack)
        try:
            self.data.append(BasicMeter(bas.search(buffer).groups()))
            if buffer.find("Volume Pack in current use: ") != -1:
                self.data.append(PackMeter(pack.search(buffer).groups()))
        except:
            raise SkymeterError("Parse failure")
        self.time = time.localtime()
        return self.data
    
    def prettyPrint(self):
        now = time.strftime(self.timeformat, self.time)
        s = "Volume meters for %s on %s\n" % (self.username, now)
        s += "\n".join(map(lambda y: repr(y), self.data))
        return s

if __name__ == '__main__':
    try:
        s = skymeter()
        s.GetData()
        print s.prettyPrint()
    except SkymeterError, e:
        print "An error occured: %s" % e.error 
