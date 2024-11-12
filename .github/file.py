import sys
from os import WCONTINUED


def file():
    '''Asks for an input which is a file'''
    filename = input("Enter complete file name whose contents you want: ")
    try:
        '''will try to open file, the with makes the file close once its been run through
        this will go through each line, and split the values apart using strip and split. After this
        the code will then check if the length of the line is 2, if it is not it will skip that one and
        say that it does not contain two values. If the line does have 2 values, then it will try to take
        each value and add them up. If one of them is not a float and there is a float error, then it will
        print that one of the inputs on the line was not a float. Finally there is a check on the bottom
        that checks if the name of the file is available. If the file is not existent then the code will return
        that the file does not exist'''
        with open(filename, 'r') as infile:
            i = 1
            for line_num in infile:
                line_split = line_num.strip().split()
                if len(line_split) !=2:
                    print("Line {} does not contain two values".format(i))
                    continue
                try:
                    num_1 = float(line_split[0])
                    num_2 = float(line_split[1])
                    val = num_1 + num_2
                    print("Line {}'s sum is: {}".format(i,val))
                except ValueError:
                    print("Error, sums could not be added up")
                i+=1
    except FileNotFoundError:
        print("Could not find file {}".format(filename))


if __name__ == '__main__':
    file()

