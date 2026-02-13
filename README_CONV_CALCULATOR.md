# Convolution Output Dimension Calculator

This tool calculates the output dimensions of an image after applying a convolutional operation with specified parameters.

## Files

1. **conv_output_calculator.py** - Interactive calculator with detailed step-by-step calculations
2. **conv_examples.py** - Demonstrates common convolution scenarios

## Formula

The output dimension is calculated using:

```
Output = ((Input - Filter + 2 × Padding) / Stride) + 1
```

Where:
- **Input**: Height or width of input image
- **Filter**: Height or width of convolution filter/kernel
- **Stride**: Step size for moving the filter
- **Padding**: Number of pixels added around the input

## Usage

### Interactive Calculator

Run the main calculator to input your own values:

```bash
python3 conv_output_calculator.py
```

You'll be prompted to enter:
- Input image dimensions (height × width)
- Filter/kernel dimensions (height × width)
- Stride value
- Padding value

### View Examples

To see pre-configured examples:

```bash
python3 conv_examples.py
```

## Example Calculations

### Example 1: Basic Convolution
```
Input:   28 × 28
Filter:  5 × 5
Stride:  1
Padding: 0
Output:  24 × 24
```

### Example 2: Same Padding
```
Input:   32 × 32
Filter:  3 × 3
Stride:  1
Padding: 1
Output:  32 × 32  (same as input)
```

### Example 3: Downsampling with Stride
```
Input:   64 × 64
Filter:  3 × 3
Stride:  2
Padding: 1
Output:  32 × 32  (half the input size)
```

## Understanding the Parameters

### Padding Types

- **Valid (padding=0)**: No padding, output is smaller than input
- **Same (padding=⌊filter/2⌋)**: Output has same dimensions as input (with stride=1)
- **Full**: Maximum padding for complete coverage

### Common Stride Values

- **Stride=1**: Preserves spatial dimensions (with appropriate padding)
- **Stride=2**: Reduces dimensions by half (common for downsampling)
- **Stride>2**: More aggressive downsampling

### Typical Filter Sizes

- **1×1**: Pointwise convolution (channel mixing)
- **3×3**: Most common, good balance of receptive field and computation
- **5×5, 7×7**: Larger receptive field, more parameters
- **11×11**: Used in early CNN layers (e.g., AlexNet)

## Requirements

- Python 3.x
- No external dependencies required

## Notes

- The calculator validates that output dimensions are positive integers
- Non-integer outputs indicate an invalid configuration
- For valid convolutions, adjust stride, padding, or filter size to get integer outputs
