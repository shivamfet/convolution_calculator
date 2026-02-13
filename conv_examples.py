#!/usr/bin/env python3
"""
Example demonstrations of convolution output dimension calculations
"""

from conv_output_calculator import visualize_calculation


def run_examples():
    """Run several example scenarios."""

    print("\n" + "="*60)
    print("EXAMPLE SCENARIOS")
    print("="*60)

    examples = [
        {
            "name": "Example 1: Standard MNIST-like convolution",
            "input_h": 28,
            "input_w": 28,
            "filter_h": 5,
            "filter_w": 5,
            "stride": 1,
            "padding": 0
        },
        {
            "name": "Example 2: Same padding (output = input)",
            "input_h": 32,
            "input_w": 32,
            "filter_h": 3,
            "filter_w": 3,
            "stride": 1,
            "padding": 1
        },
        {
            "name": "Example 3: Stride 2 for downsampling",
            "input_h": 64,
            "input_w": 64,
            "filter_h": 4,
            "filter_w": 4,
            "stride": 2,
            "padding": 1
        },
        {
            "name": "Example 4: Large image with stride 2",
            "input_h": 224,
            "input_w": 224,
            "filter_h": 8,
            "filter_w": 8,
            "stride": 2,
            "padding": 3
        },
        {
            "name": "Example 5: Non-square image and filter",
            "input_h": 100,
            "input_w": 200,
            "filter_h": 3,
            "filter_w": 5,
            "stride": 1,
            "padding": 0
        }
    ]

    for i, example in enumerate(examples, 1):
        print(f"\n{'='*60}")
        print(example["name"])
        visualize_calculation(
            example["input_h"],
            example["input_w"],
            example["filter_h"],
            example["filter_w"],
            example["stride"],
            example["padding"]
        )

        if i < len(examples):
            input("\nPress Enter to see next example...")


if __name__ == "__main__":
    run_examples()
