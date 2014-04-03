#!/usr/bin/env python3

import sys

def main():
     try:
          filename = sys.argv[1]
     except IndexError:
          print('Usage: %s filename' % sys.argv[0])
          sys.exit(1)

     text = decode(filename)
     if text != '':
          print(text)

def decode(fname):
     try:
          infile = open(fname, 'r')
     except IOError as e:
          print(e)
          return ''

     out = list()
     for line in infile:
          chars = line.split()
          for c in chars:
               try:
                    byte = int(c, 16)
                    out.append(chr(byte))
               except ValueError as e:
                    print('Invalid input value: %s' % e)
                    return ''

     return ''.join(out)

if __name__ == '__main__':
     main()
