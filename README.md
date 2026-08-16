# shrug64
64 Bit Encoded Shrug Emoji

Found buried deep in the bowels of AWS debugging messages:

This text string: 

wq9cXyjjg4QpXy/Crw==

When parsed through base64 provides the classic "Shrug" text emoji


  ̄\_(ツ)_/ ̄


Script is a simple python interpretation. Requires a Linux system, Python 3 and the "base64" module. 
Basically just a Python wrapped for "base64 -d" on Linux

Don't download the script and name it base64.py, since base64 is a known function/utility. 

Given the sample repo, usage is almost the same as the command line utility. 

python shrug64.py -d ./shrug.txt (or any other plain text file with base64 encoded content to decode

You can also use the -e command line setting to output base64 ENCODED text in a file to standard output. 

You could write a similar script to use OpenSSH to encrypt a file, or even scramble a file with ROT13 or simple ciphers, etc. 
This isn't meant to be a god tier script, just a fun script based on some Easter egg seen in the wild. 
