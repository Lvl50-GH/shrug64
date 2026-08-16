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
