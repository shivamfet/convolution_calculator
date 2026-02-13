#!/usr/bin/env python3
"""
Convolutional Layer Output Dimension Calculator

This script calculates the output dimensions of an image after applying
a convolutional operation with specified parameters.

Formula:
Output = ((Input - Filter + 2 * Padding) / Stride) + 1
"""

import math


def calculate_output_dimension(input_dim, filter_dim, stride, padding):
    """
    Calculate output dimension for a convolutional layer.

    Args:
        input_dim: Input dimension (height or width)
        filter_dim: Filter/kernel dimension (height or width)
        stride: Stride value
        padding: Padding value

    Returns:
        Output dimension after convolution
    """
    output = ((input_dim - filter_dim + 2 * padding) / stride) + 1
    return output


def visualize_calculation(input_h, input_w, filter_h, filter_w, stride, padding):
    """
    Calculate and display the output dimensions with detailed information.
    """
    # Calculate output dimensions
    output_h = calculate_output_dimension(input_h, filter_h, stride, padding)
    output_w = calculate_output_dimension(input_w, filter_w, stride, padding)

    print("\n" + "="*60)
    print("CONVOLUTION OUTPUT DIMENSION CALCULATOR")
    print("="*60)

    print("\nInput Parameters:")
    print(f"  • Input Image Dimensions:  {input_h} × {input_w}")
    print(f"  • Filter/Kernel Size:      {filter_h} × {filter_w}")
    print(f"  • Stride:                  {stride}")
    print(f"  • Padding:                 {padding}")

    print("\n" + "-"*60)
    print("Calculation Formula:")
    print("  Output = ((Input - Filter + 2 × Padding) / Stride) + 1")

    print("\n" + "-"*60)
    print("Height Calculation:")
    print(f"  Output Height = (({input_h} - {filter_h} + 2 × {padding}) / {stride}) + 1")
    print(f"  Output Height = (({input_h} - {filter_h} + {2*padding}) / {stride}) + 1")
    print(f"  Output Height = ({input_h - filter_h + 2*padding} / {stride}) + 1")
    print(f"  Output Height = {(input_h - filter_h + 2*padding) / stride} + 1")
    print(f"  Output Height = {output_h}")

    print("\nWidth Calculation:")
    print(f"  Output Width  = (({input_w} - {filter_w} + 2 × {padding}) / {stride}) + 1")
    print(f"  Output Width  = (({input_w} - {filter_w} + {2*padding}) / {stride}) + 1")
    print(f"  Output Width  = ({input_w - filter_w + 2*padding} / {stride}) + 1")
    print(f"  Output Width  = {(input_w - filter_w + 2*padding) / stride} + 1")
    print(f"  Output Width  = {output_w}")

    print("\n" + "="*60)
    print("RESULT:")
    print("="*60)

    # Check if output dimensions are valid (should be positive integers)
    if output_h > 0 and output_w > 0:
        if output_h == int(output_h) and output_w == int(output_w):
            print(f"\n✓ Output Image Dimensions: {int(output_h)} × {int(output_w)}")
            print(f"✓ Total output features:   {int(output_h * output_w)}")
            print("\n✓ Valid configuration!")
        else:
            print(f"\n✗ Output Dimensions: {output_h} × {output_w}")
            print("\n⚠ WARNING: Output dimensions are not integers!")
            print("  This configuration will not work properly.")
            print("  Adjust stride, padding, or filter size.")
    else:
        print(f"\n✗ Invalid configuration!")
        print(f"  Output dimensions are negative or zero: {output_h} × {output_w}")

    print("="*60 + "\n")

    return output_h, output_w


def get_positive_int(prompt):
    """Get a positive integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("  ⚠ Please enter a positive integer!")
        except ValueError:
            print("  ⚠ Invalid input! Please enter a number.")


def get_non_negative_int(prompt):
    """Get a non-negative integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("  ⚠ Please enter a non-negative integer!")
        except ValueError:
            print("  ⚠ Invalid input! Please enter a number.")


def main():
    """Main function to run the calculator."""
    print("\n" + "="*60)
    print("WELCOME TO CONVOLUTION OUTPUT DIMENSION CALCULATOR")
    print("="*60)
    print("\nThis tool helps you calculate the output dimensions of an image")
    print("after applying a convolutional layer with specified parameters.\n")

    while True:
        print("\nPlease enter the following parameters:")
        print("-" * 60)

        # Get input dimensions
        input_h = get_positive_int("Input Image Height:        ")
        input_w = get_positive_int("Input Image Width:         ")

        # Get filter dimensions
        filter_h = get_positive_int("Filter/Kernel Height:      ")
        filter_w = get_positive_int("Filter/Kernel Width:       ")

        # Get stride
        stride = get_positive_int("Stride:                    ")

        # Get padding
        padding = get_non_negative_int("Padding:                   ")

        # Calculate and display results
        visualize_calculation(input_h, input_w, filter_h, filter_w, stride, padding)

        # Ask if user wants to try again
        choice = input("Do you want to calculate another configuration? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nThank you for using the calculator! Goodbye.\n")
            break


if __name__ == "__main__":
    main()
