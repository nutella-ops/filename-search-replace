#!/usr/bin/python3
import os

userRaw = input("search/replace: ")
userParse = userRaw.split('/')
currentDir = os.getcwd()
dirFiles = os.listdir(currentDir)
script = "replace.py"
dirFiles.remove(script)

for fileName in dirFiles:
    os.rename(fileName, fileName.replace(userParse[0], userParse[1]))