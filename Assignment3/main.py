'''
Created on 28 Feb 2017

@author: Willie
'''
import sys
import argparse
import urllib.request
import re

def filter(x):
    x = int(x)
    x = 0 if (x < 0) else x
    x = size if (x > size) else x
    return x
    
    pass
def main():    
    # parse the command line arguments to get the input filename
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()

    # now the filename arguments is in args.input
    filename = args.input
    #Open that file and read it in to the buffer
    fh2 =urllib.request.urlopen(filename)
    buffer = fh2.read().decode('utf-8')

    # break the buffer into lines
    lines = buffer.split('\n')
    # the first line is the size of the LED array
    global size
    size = int(lines[0])

    print (size)
    for i, line in enumerate(lines[1:-1]):
        print (i, line)
        # Regex expression to find the command and co-ordinates
        m = re.match(r'(((\D+ \D+)|(\D+)) (.?\d+)(.?)(.?\d+) through (.?\d+)(.?)(.?\d+))',line)
        print("matched: ", m is not None, m.groups())
        # Is this a valid matched line of input? skip line if false.
        mtest = m is not None
        if (mtest == 'false'):
            continue
        #Assign variables to the command & co-ordinates
        cmd,x1,y1,x2,y2 = m.group(2),m.group(5),m.group(7),m.group(8),m.group(10)
        filter(x1)
        filter(x2)
        filter(y1)
        filter(y2)
        
        print(cmd,":",x1,y1,x2,y2,mtest)
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