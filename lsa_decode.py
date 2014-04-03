#!/usr/bin/env python3

import sys
import argparse

def main():
     parser = argparse.ArgumentParser(description='Decodes LSA secret data.')
     parser.add_argument('-f', "--infile", type=argparse.FileType('r'), 
               metavar='filename', help="Specify the file to read", default='-')
     args = parser.parse_args()

     text = decode(args.infile)
     if text != '':
          print(text)

def decode(input_file):
     out = list()
     for line in input_file:
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
