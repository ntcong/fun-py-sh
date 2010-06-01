#!/usr/bin/env python

from __future__ import print_function

import sys 
import getopt

VERSION = '1.0'
display_return = True

def print_usage():
    print('echo - display line of text')
#    print 'USAGE: echo [OPTION] [STRING]'
#    print '            -n  --no-newline        do not output trailing newline'
#    print '            -v  --version           output version information and exit'
#    print '            -h  --help              display this help and exit'
    
    
def main():
    global display_return
    try:
        opts, args = getopt.getopt(sys.argv[1:],'nhv',['no-newline','help','version'])
    except getopt.GetoptError, err:
        print(str(err))
        print_usage()
        return 
    for arg,val in opts:
        if arg in ('-h','--help'):
            print_usage()
            return
        elif arg in ('-v','--version'):
            print(VERSION)
            return
        elif arg in ('-n','--no-newline'):
            display_return = False
    
    for val in args:
        print(val, end=" ")
    if display_return:
        print("")
    
if __name__=="__main__":
    main()


