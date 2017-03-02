'''
Created on 28 Feb 2017

@author: Willie
'''
import sys
import argparse
import urllib.request
import re

def main():    
    # parse the command line arguments to get the input filename
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()

    # now the filename arguments is in args.input
    filename = args.input
    fh2 =urllib.request.urlopen(filename)
    buffer = fh2.read().decode('utf-8')

    # break the buffer into lines
    lines = buffer.split('\n')
    # the first line is the size of the LED array
    size = int(lines[0])

    print (size)
    for i, line in enumerate(lines[1:-1]):
        print (i, line)
    fh2.close()
    # I construct a class to do the testing
    #tester = LEDTester(size)

    # now loop over each line (except the first) and process the commands (turn on/off, switch)
    #for i, line in enumerate(lines[1:]):
        #tester.execute_command(line)

    # at the end, count the number of lights that are on
    # print("{} {}".format(filename, tester.count_lighting()))
    #return
main()    
    
if __name__ == '__main__':
    pass