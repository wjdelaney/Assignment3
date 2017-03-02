'''
Created on 28 Feb 2017

@author: Willie
'''
import sys
import argparse
def main():    
    # parse the command line arguments to get the input filename
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()

    # now the filename arguments is in args.input
    filename = args.input

    # read_file reads the contents of the buffer into a single string
    buffer = read_file(filename=filename)

    # break the buffer into lines
    lines = buffer.split('\n')

    # the first line is the size of the LED array
    size = int(lines[0])

    # I construct a class to do the testing
    tester = LEDTester(size)

    # now loop over each line (except the first) and process the commands (turn on/off, switch)
    for i, line in enumerate(lines[1:]):
        tester.execute_command(line)

    # at the end, count the number of lights that are on
    print("{} {}".format(filename, tester.count_lighting()))
    return
if __name__ == '__main__':
    pass