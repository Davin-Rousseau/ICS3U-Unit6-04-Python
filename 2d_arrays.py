#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on: Dec 2019
# This program uses a 2D array to print average

import random


def average_of_numbers(passed_in_2D_list, rows, columns):
    # this function adds up all the elements in  a 2D array
    # and takes average

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element
    total = total / (rows + columns)

    return total


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    input_1 = input("How many rows would you like: ")
    input_2 = input("How many columns would you like: ")
    try:
        rows = int(input_1)
        columns = int(input_2)
        for loop_counter_rows in range(0, rows):
            temp_column = []
            for loop_counter_columns in range(0, columns):
                a_random_number = random.randint(0, 50+1)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")
        average_number = average_of_numbers(a_2d_list, rows, columns)
        print("The average of all number in 2d array: {0} "
              .format(average_number))
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
