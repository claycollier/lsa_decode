#!/usr/bin/env python3

import argparse

def main():
     parser = argparse.ArgumentParser(description='Decodes LSA secret data.')
     parser.add_argument('-f', "--infile", type=argparse.FileType('r'), 
               metavar='filename', 
               help="Specify the file to read. Defaults to stdin.", default='-')
     args = parser.parse_args()

     text = decode(args.infile)
     if text != '':
          print(text)

def decode(input_file):
     out = list()
     try:
          for line in input_file:
               chars = line.split()
               for char in chars:
                    try:
                         byte = int(char, 16)
                         out.append(chr(byte))
                    except ValueError as err:
                         print('Invalid input value: %s' % err)
                         return ''
     except KeyboardInterrupt:
          return ''

     return ''.join(out)

if __name__ == '__main__':
     main()
