lsa_decode
==========

Simple Python decoder for retrieving stored passwords from Windows dial up networking settings

See also: http://www.passcape.com/index.php?section=docsys&cmd=details&id=23

Passcape Software (www.passcape.com) provides a program to extract stored, encrypted password information 
from the Windows registry. This is useful for extracting a forgotten password for a VPN or other dialup connection.

Unfortunately, the hex-formatted output isn't immediately readable. This script reads the raw data format output 
by Passcape's tool, converts it to readable ASCII/UTF-8, and writes it out to the console.

The script reads from stdin if no file is specified on the command line.

sample.txt contains sample output from Passcape's extraction tool.
