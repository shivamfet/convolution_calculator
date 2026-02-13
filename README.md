# Convolution Output Dimension Calculator 🔍

A comprehensive toolkit for understanding and calculating convolution output dimensions in Convolutional Neural Networks (CNNs).

## 📁 Project Structure

```
convolution_calculator/
├── README.md                          # This file
├── conv_calculator_animated.html      # ⭐ Interactive animated visualizer (RECOMMENDED)
├── conv_calculator_gui.html           # Interactive web GUI with real-time updates
├── conv_output_calculator.py          # Command-line interactive calculator
├── conv_examples.py                   # Pre-configured example scenarios
├── conv_calculator_gui.py             # Desktop GUI (requires tkinter)
└── README_CONV_CALCULATOR.md          # Detailed documentation
```

## 🚀 Quick Start

### **Option 1: Animated Visualizer** ⭐ RECOMMENDED

The most intuitive way to understand convolutions:

```bash
open conv_calculator_animated.html
```

**Features:**
- ✅ Watch the filter slide over the input step-by-step
- ✅ Separate controls for rows and columns
- ✅ Animation with adjustable speed
- ✅ Visual arrows showing input → output mapping
- ✅ Support for non-square inputs and filters
- ✅ Real-time validation

### **Option 2: Static Web GUI**

Fast, responsive calculator with visual representation:

```bash
open conv_calculator_gui.html
```

**Features:**
- ✅ Real-time dimension calculations
- ✅ Color-coded parameters
- ✅ Visual representation of layers
- ✅ Quick presets

### **Option 3: Command-Line Calculator**

For terminal enthusiasts:

```bash
python3 conv_output_calculator.py
```

**Features:**
- ✅ Interactive input prompts
- ✅ Step-by-step calculation display
- ✅ Validation of configurations
- ✅ Repeat calculations easily

### **Option 4: View Examples**

See pre-configured common scenarios:

```bash
python3 conv_examples.py
```

## 📐 The Formula

```
Output = ((Input - Filter + 2 × Padding) / Stride) + 1
```

**Where:**
- **Input**: Height or width of input image
- **Filter**: Height or width of convolution kernel
- **Stride**: Step size when moving the filter
- **Padding**: Pixels added around the border

## 🎓 Key Concepts

### Input Dimensions
- **Height (Rows)**: Vertical size of the input
- **Width (Columns)**: Horizontal size of the input
- Can be rectangular (e.g., 100×200)

### Filter/Kernel
- **Height (Rows)**: Vertical size of the filter
- **Width (Columns)**: Horizontal size of the filter
- Common sizes: 1×1, 3×3, 5×5, 7×7
- Can be non-square (e.g., 3×5)

### Stride
- How many pixels the filter moves each step
- **Stride = 1**: Dense convolution, overlapping receptive fields
- **Stride = 2**: Downsampling, reduces output by ~half
- **Stride > 2**: Aggressive downsampling

### Padding
- Extra pixels added around the input border
- **Padding = 0** (Valid): No padding, output smaller than input
- **Padding = ⌊filter_size / 2⌋** (Same): With stride=1, output equals input
- Allows filter to process edge pixels

## 💡 Common Use Cases

### Same Padding (Preserve Dimensions)
```
Input:   32×32
Filter:  3×3
Stride:  1
Padding: 1
Output:  32×32 ✓
```

### Downsampling (Reduce by Half)
```
Input:   64×64
Filter:  4×4
Stride:  2
Padding: 1
Output:  32×32 ✓
```

### Max Pooling
```
Input:   56×56
Filter:  2×2
Stride:  2
Padding: 0
Output:  28×28 ✓
```

### Non-Square Processing
```
Input:   100×200
Filter:  3×5
Stride:  1
Padding: 0
Output:  98×196 ✓
```

## 🎯 Understanding the Animation

The animated visualizer shows **exactly** how convolution works:

1. **Filter Placement**: Red rectangle shows current filter position
2. **Input Processing**: Blue cells are original input, purple is padding
3. **Output Generation**: Green cells show computed output features
4. **Sliding Motion**: Watch the filter move across rows, then down
5. **Arrow Connection**: Shows which input region creates which output

### Animation Flow:
```
1. Filter starts at top-left (0, 0)
2. Slides right by stride amount
3. Reaches end of row
4. Moves down by stride amount
5. Starts next row from left
6. Repeats until entire input is covered
```

## 🔧 Requirements

- **HTML versions**: Any modern web browser (Chrome, Firefox, Safari, Edge)
- **Python versions**: Python 3.x (no additional packages needed)
- **Desktop GUI**: Python with tkinter (may not be available in all environments)

## 📊 Examples Included

The `conv_examples.py` file includes:

1. **Standard MNIST**: 28×28 → 24×24
2. **Same Padding**: 32×32 → 32×32
3. **Downsampling**: 64×64 → 32×32
4. **Large Image**: 224×224 → 112×112
5. **Non-Square**: 100×200 → 98×196

## 🎨 Visual Legend

- 🔵 **Blue**: Input image dimensions
- 🔴 **Red**: Filter/kernel dimensions
- 🟠 **Orange**: Stride parameter
- 🟣 **Purple**: Padding region
- 🟢 **Green**: Output features (generated)
- ⬜ **Gray**: Output features (pending)

## 📝 Tips

1. **Start Simple**: Begin with square inputs and filters to understand basics
2. **Experiment**: Try different stride and padding combinations
3. **Watch Animation**: Use the animated version to see the actual convolution process
4. **Validate**: The tools automatically detect invalid configurations
5. **Learn Patterns**: Use presets to understand common CNN architectures

## 🐛 Troubleshooting

**Problem**: Output dimensions are not integers
**Solution**: Adjust stride, padding, or filter size so (Input - Filter + 2×Padding) is divisible by Stride

**Problem**: Desktop GUI won't launch
**Solution**: Use the HTML versions instead - they work everywhere!

**Problem**: Animation is too fast/slow
**Solution**: Use the speed slider in the animation controls

## 📚 Learn More

This tool helps visualize concepts from:
- Convolutional Neural Networks (CNNs)
- Deep Learning
- Computer Vision
- Image Processing

Understanding these dimensions is crucial for:
- Designing CNN architectures
- Debugging dimension mismatches
- Calculating memory requirements
- Understanding receptive fields

## 🤝 Usage

Feel free to use these tools for:
- Learning deep learning concepts
- Teaching CNN fundamentals
- Debugging your neural network architectures
- Understanding convolution operations

---

**Created**: February 2026
**Purpose**: Educational tool for understanding CNN convolution operations
**Best Tool**: `conv_calculator_animated.html` for visual learning! 🎬
