#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# script to register Python 2.0 or later for use with win32all
# and other extensions that require Python registry settings
#
# written by Joakim Löw for Secret Labs AB / PythonWare
#
# source:
# http://www.pythonware.com/products/works/articles/regpy20.htm
 
import sys
 
from _winreg import *
 
# tweak as necessary
version = sys.version[:3]
installpath = sys.prefix
 
regpath = "SOFTWARE\\Python\\Pythoncore\\%s\\" % (version)
installkey = "InstallPath"
pythonkey = "PythonPath"
pythonpath = "%s;%s\\Lib\\;%s\\DLLs\\" % (
    installpath, installpath, installpath
)
 
def RegisterPy():
    try:
        reg = OpenKey(HKEY_CURRENT_USER, regpath)
    except EnvironmentError:
        try:
            reg = CreateKey(HKEY_CURRENT_USER, regpath)
            SetValue(reg, installkey, REG_SZ, installpath)
            SetValue(reg, pythonkey, REG_SZ, pythonpath)
            CloseKey(reg)
        except:
            print "*** Unable to register!"
            return
        print "--- Python", version, "is now registered!"
        return
    if (QueryValue(reg, installkey) == installpath and
        QueryValue(reg, pythonkey) == pythonpath):
        CloseKey(reg)
        print "=== Python", version, "is already registered!"
        return
    CloseKey(reg)
    print "*** Unable to register!"
    print "*** You probably have another Python installation!"
 
def UnRegisterPy():
    try:
        reg = OpenKey(HKEY_LOCAL_MACHINE, regpath)
    except EnvironmentError:
        print "*** Python not registered?!"
        return
    try:
        DeleteKey(reg, installkey)
        DeleteKey(reg, pythonkey)
        DeleteKey(HKEY_LOCAL_MACHINE, regpath)
    except:
        print "*** Unable to un-register!"
    else:
        print "--- Python", version, "is no longer registered!"
 
if __name__ == "__main__":
    # Register python's distribution
    RegisterPy()
    # If you want to unregister python's distribution, just comment the upper line and uncomment the following line
    #UnRegisterPy() 
