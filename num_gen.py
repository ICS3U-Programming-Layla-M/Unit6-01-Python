#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 10, 2021
# This program generates 10 random number into an array/list between 0 and 100
# and displays the average

import random
import constants


def main():
    # create an empty list
    number_array = []

    for counter in range(constants.MIN_NUM, constants.MAX_ARRAY_SIZE):
        # generate random number from 0 to 100 and add it to the list
        number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        number_array.append(number)

        # display the random number added and at which position/index
        print("{0} added to the list at position {1}.\
". format(number, counter))
        counter = counter + 1
    print()

    for counter in range(constants.MIN_NUM, constants.MAX_ARRAY_SIZE):
        # calculate the sum of the numbers in the list
        if counter == 0:
            sum = number_array[counter]
        else:
            sum = sum + number_array[counter]
        counter = counter + 1

    # calculate and display the average of the numbers in the list
    average = sum/constants.MAX_ARRAY_SIZE
    print("The average is: {}". format(average))


if __name__ == "__main__":
    main()
