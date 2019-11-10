#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program do a for loop


def main():

    # variables
    red = 0
    green = 0
    blue = 0

    # input
    input("Press enter to start. ")

    # process
    for green in range(255):
        for red in range(255):
            for blue in range(255):
                print("RGB: (" + str(red) + ", " + str(green) + ", " +
                      str(blue) + ")")


if __name__ == "__main__":
    main()
