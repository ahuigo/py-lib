#!/usr/bin/env python3

import zlib,sys,os  # A compression / decompression library
argv = sys.argv
if len(argv)<2:
    quit("git-object.py .git/objects/55/xxxxxxxxx")
filename = argv[1]
compressed_contents = open(filename, 'rb').read()
txt = zlib.decompress(compressed_contents)
print(txt)
print(txt.decode())
