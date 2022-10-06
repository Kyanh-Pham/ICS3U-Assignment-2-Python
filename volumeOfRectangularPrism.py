#!/usr/bin/env python3

# Created by: Kyanh Pham
# Created on: Oct 2022
# This program calculates the volume of a rectangular prism
# with length, width, and height inputted from user


def main():
    # This function calculates volume
    print("This will calculate the volume of a rectangular prism or cube.")

    # Input
    length = float(input("Enter the length (cm): "))
    width = float(input("Enter the width (cm): "))
    height = float(input("Enter the height (cm): "))

    # Process
    volume = length * width * height

    # Output
    print("Volume is {0} cm³.".format(volume))

    print("\nDone.")


if __name__ == "__main__":
    main()
