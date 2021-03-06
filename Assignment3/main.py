'''
Created on 28 Feb 2017

@author: Willie
'''
import sys
import argparse
import urllib.request
import re
# rectify out of bounds co-ordinates.
def filter(x):
    x = int(x)
    x = 0 if (x < 0) else x
    x = size-1 if (x > size) else x
    return x
 
#Turn on function, change array values to a 1.
def turn_on(x1,x2,y1,y2):  
    for i in range (x1,x2+1):
        for j in range (y1,y2+1):
            array2d[i][j] = 1
                                
#Turn off function, change array values to a 0.
def turn_off(x1,x2,y1,y2):  
    for i in range (x1,x2+1):
        for j in range (y1,y2+1):
            array2d[i][j] = 0
            
#Switch 0 to 1 OR 1 to 0 in the defined area.
def switch(x1,x2,y1,y2):  
    for i in range (x1,x2+1):
        for j in range (y1,y2+1):
            if array2d[i][j]==1:
                array2d[i][j]=0
            else:
                array2d[i][j]=1
                
def main():  
    global size # length of x and y
    global array2d  # create a 2 dimensional list
    # parse the command line arguments to get the input filename
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()

    # filename contains the arg inputs
    filename = args.input
    #Open that file and read it in to the buffer
    fh2 =urllib.request.urlopen(filename)
    buffer = fh2.read().decode('utf-8')

    # break the buffer into lines
    lines = buffer.split('\n')
    
    #Line 0 contains the X & Y lengths (array size).
    size = int(lines[0])
    #Initialize array with all zeros.
    array2d = [ [0]*size for _ in range(size) ]
    #Loop through lines one at a time
    for i, line in enumerate(lines[1:-1]):
        #print (i, line)
        # Regex expression to find the command and co-ordinates
        m = re.match(r'(((\D+ \D+)|(\D+)) (.?\d+)(.?)(.?\d+) through (.?\d+)(.?)(-?\d+))',line)
        #print("matched: ", m is not None, m.groups())
        # Is this a valid matched line of input? skip line if false.
        mtest = m is not None
        if (mtest == 'false'):
            continue
        #Assign variables to the command & co-ordinates
        cmd,x1,y1,x2,y2 = m.group(2),m.group(5),m.group(7),m.group(8),m.group(10)
        #sanitize the co-ordinates by calling filter function.
        x1 = filter(x1)
        x2 = filter(x2)
        y1 = filter(y1)
        y2 = filter(y2)

        # Run the commands
        if cmd == "turn on":
            turn_on(x1,x2,y1,y2)
        elif cmd == "turn off":
            turn_off(x1,x2,y1,y2)
        elif cmd == "switch":
            switch(x1,x2,y1,y2)
        else:
            x1=x1
    #Print the filename and total leds that are lit   
    total = sum(x.count(1) for x in array2d)
    print (filename, " ", total , " leds are lit")

#Call main function from script  
if __name__ == '__main__':
    main()