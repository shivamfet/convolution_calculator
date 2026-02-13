#!/usr/bin/env python3
"""
Interactive GUI for Convolution Output Dimension Calculator
Features:
- Visual representation of input, filter, and output
- Real-time updates with sliders
- Color-coded results (valid/invalid)
- Step-by-step calculation display
"""

import tkinter as tk
from tkinter import ttk
import math


class ConvCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Convolution Output Calculator")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')

        # Initialize variables
        self.input_h = tk.IntVar(value=64)
        self.input_w = tk.IntVar(value=64)
        self.filter_h = tk.IntVar(value=3)
        self.filter_w = tk.IntVar(value=3)
        self.stride = tk.IntVar(value=1)
        self.padding = tk.IntVar(value=1)

        self.setup_ui()
        self.update_calculation()

    def setup_ui(self):
        """Setup the user interface."""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        title_frame.pack(fill=tk.X, pady=(0, 10))
        title_frame.pack_propagate(False)

        title_label = tk.Label(
            title_frame,
            text="🔍 Interactive Convolution Output Calculator",
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=15)

        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left panel - Controls
        left_panel = tk.Frame(main_frame, bg='#f0f0f0')
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))

        self.create_controls(left_panel)

        # Right panel - Visualization and Results
        right_panel = tk.Frame(main_frame, bg='#f0f0f0')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_visualization(right_panel)
        self.create_results(right_panel)

    def create_controls(self, parent):
        """Create input controls."""
        controls_frame = tk.LabelFrame(
            parent,
            text="📊 Input Parameters",
            font=('Arial', 14, 'bold'),
            bg='white',
            fg='#2c3e50',
            padx=20,
            pady=20
        )
        controls_frame.pack(fill=tk.BOTH, padx=5, pady=5)

        # Input Height
        self.create_slider(
            controls_frame, "Input Height:", self.input_h, 1, 512, 0,
            color='#3498db'
        )

        # Input Width
        self.create_slider(
            controls_frame, "Input Width:", self.input_w, 1, 512, 1,
            color='#3498db'
        )

        # Separator
        ttk.Separator(controls_frame, orient='horizontal').grid(
            row=2, column=0, columnspan=3, sticky='ew', pady=20
        )

        # Filter Height
        self.create_slider(
            controls_frame, "Filter Height:", self.filter_h, 1, 15, 3,
            color='#e74c3c'
        )

        # Filter Width
        self.create_slider(
            controls_frame, "Filter Width:", self.filter_w, 1, 15, 4,
            color='#e74c3c'
        )

        # Separator
        ttk.Separator(controls_frame, orient='horizontal').grid(
            row=5, column=0, columnspan=3, sticky='ew', pady=20
        )

        # Stride
        self.create_slider(
            controls_frame, "Stride:", self.stride, 1, 8, 6,
            color='#f39c12'
        )

        # Padding
        self.create_slider(
            controls_frame, "Padding:", self.padding, 0, 10, 7,
            color='#9b59b6'
        )

        # Preset buttons
        ttk.Separator(controls_frame, orient='horizontal').grid(
            row=8, column=0, columnspan=3, sticky='ew', pady=20
        )

        preset_label = tk.Label(
            controls_frame,
            text="🎯 Quick Presets:",
            font=('Arial', 12, 'bold'),
            bg='white'
        )
        preset_label.grid(row=9, column=0, columnspan=3, pady=(0, 10))

        presets = [
            ("MNIST 28×28", 28, 28, 5, 5, 1, 0),
            ("CIFAR 32×32", 32, 32, 3, 3, 1, 1),
            ("ImageNet 224×224", 224, 224, 8, 8, 2, 3),
            ("HD 720p", 720, 1280, 7, 7, 2, 3),
        ]

        for i, (name, ih, iw, fh, fw, s, p) in enumerate(presets):
            btn = tk.Button(
                controls_frame,
                text=name,
                command=lambda ih=ih, iw=iw, fh=fh, fw=fw, s=s, p=p:
                    self.set_preset(ih, iw, fh, fw, s, p),
                bg='#34495e',
                fg='white',
                font=('Arial', 10),
                relief=tk.FLAT,
                padx=10,
                pady=5,
                cursor='hand2'
            )
            btn.grid(row=10+i, column=0, columnspan=3, sticky='ew', pady=2)

    def create_slider(self, parent, label, variable, from_, to, row, color='#3498db'):
        """Create a labeled slider."""
        # Label
        lbl = tk.Label(
            parent,
            text=label,
            font=('Arial', 11, 'bold'),
            bg='white',
            fg='#2c3e50'
        )
        lbl.grid(row=row, column=0, sticky='w', pady=5)

        # Value display
        value_lbl = tk.Label(
            parent,
            textvariable=variable,
            font=('Arial', 11, 'bold'),
            bg=color,
            fg='white',
            width=5,
            relief=tk.FLAT,
            padx=5,
            pady=2
        )
        value_lbl.grid(row=row, column=1, padx=10)

        # Slider
        slider = ttk.Scale(
            parent,
            from_=from_,
            to=to,
            orient=tk.HORIZONTAL,
            variable=variable,
            command=lambda x: self.update_calculation()
        )
        slider.grid(row=row, column=2, sticky='ew', pady=5)

        parent.grid_columnconfigure(2, weight=1)

    def create_visualization(self, parent):
        """Create visualization canvas."""
        viz_frame = tk.LabelFrame(
            parent,
            text="🎨 Visual Representation",
            font=('Arial', 14, 'bold'),
            bg='white',
            fg='#2c3e50',
            padx=10,
            pady=10
        )
        viz_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.canvas = tk.Canvas(
            viz_frame,
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def create_results(self, parent):
        """Create results display."""
        results_frame = tk.LabelFrame(
            parent,
            text="📈 Calculation Results",
            font=('Arial', 14, 'bold'),
            bg='white',
            fg='#2c3e50',
            padx=20,
            pady=15
        )
        results_frame.pack(fill=tk.X, padx=5, pady=5)

        # Formula display
        self.formula_text = tk.Text(
            results_frame,
            height=8,
            font=('Courier', 10),
            bg='#ecf0f1',
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        self.formula_text.pack(fill=tk.X, pady=(0, 10))

        # Result display
        self.result_frame = tk.Frame(results_frame, bg='white')
        self.result_frame.pack(fill=tk.X)

        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=('Arial', 16, 'bold'),
            bg='white',
            pady=10
        )
        self.result_label.pack()

    def set_preset(self, ih, iw, fh, fw, s, p):
        """Set preset values."""
        self.input_h.set(ih)
        self.input_w.set(iw)
        self.filter_h.set(fh)
        self.filter_w.set(fw)
        self.stride.set(s)
        self.padding.set(p)
        self.update_calculation()

    def calculate_output(self, input_dim, filter_dim, stride, padding):
        """Calculate output dimension."""
        return ((input_dim - filter_dim + 2 * padding) / stride) + 1

    def update_calculation(self):
        """Update all calculations and visualizations."""
        # Get values
        ih = self.input_h.get()
        iw = self.input_w.get()
        fh = self.filter_h.get()
        fw = self.filter_w.get()
        s = self.stride.get()
        p = self.padding.get()

        # Calculate outputs
        oh = self.calculate_output(ih, fh, s, p)
        ow = self.calculate_output(iw, fw, s, p)

        # Update formula text
        self.formula_text.delete(1.0, tk.END)
        self.formula_text.insert(tk.END, "Formula: Output = ((Input - Filter + 2×Padding) / Stride) + 1\n\n")
        self.formula_text.insert(tk.END, f"Height Calculation:\n")
        self.formula_text.insert(tk.END, f"  = (({ih} - {fh} + 2×{p}) / {s}) + 1\n")
        self.formula_text.insert(tk.END, f"  = ({ih - fh + 2*p} / {s}) + 1\n")
        self.formula_text.insert(tk.END, f"  = {oh}\n\n")
        self.formula_text.insert(tk.END, f"Width Calculation:\n")
        self.formula_text.insert(tk.END, f"  = (({iw} - {fw} + 2×{p}) / {s}) + 1\n")
        self.formula_text.insert(tk.END, f"  = ({iw - fw + 2*p} / {s}) + 1\n")
        self.formula_text.insert(tk.END, f"  = {ow}")

        # Check validity
        is_valid = (oh > 0 and ow > 0 and oh == int(oh) and ow == int(ow))

        # Update result label
        if is_valid:
            self.result_label.config(
                text=f"✓ Output: {int(oh)} × {int(ow)} | Features: {int(oh * ow):,}",
                fg='#27ae60',
                bg='#d4edda'
            )
            self.result_frame.config(bg='#d4edda')
        else:
            self.result_label.config(
                text=f"✗ Output: {oh:.2f} × {ow:.2f} (INVALID - Not integers!)",
                fg='#c0392b',
                bg='#f8d7da'
            )
            self.result_frame.config(bg='#f8d7da')

        # Update visualization
        self.draw_visualization(ih, iw, fh, fw, s, p, oh, ow, is_valid)

    def draw_visualization(self, ih, iw, fh, fw, s, p, oh, ow, is_valid):
        """Draw the visualization."""
        self.canvas.delete('all')

        # Get canvas size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width < 100:  # Canvas not ready yet
            canvas_width = 700
            canvas_height = 300

        # Calculate scaling
        max_dim = max(ih, iw, oh, ow) if is_valid else max(ih, iw)
        scale = min(100, 200 / max_dim) if max_dim > 0 else 1

        # Positions
        input_x = 100
        filter_x = input_x + iw * scale + 80
        output_x = filter_x + fw * scale + 80
        y_center = canvas_height // 2

        # Draw input image
        input_y = y_center - (ih * scale) // 2
        self.draw_rectangle(
            self.canvas, input_x, input_y,
            iw * scale, ih * scale,
            '#3498db', f'Input\n{ih}×{iw}'
        )

        # Draw padding if exists
        if p > 0:
            pad_scale = p * scale
            self.canvas.create_rectangle(
                input_x - pad_scale, input_y - pad_scale,
                input_x + iw * scale + pad_scale, input_y + ih * scale + pad_scale,
                outline='#9b59b6', width=3, dash=(5, 5)
            )
            self.canvas.create_text(
                input_x + iw * scale // 2, input_y - pad_scale - 15,
                text=f'Padding: {p}',
                font=('Arial', 10, 'bold'),
                fill='#9b59b6'
            )

        # Draw filter
        filter_y = y_center - (fh * scale) // 2
        self.draw_rectangle(
            self.canvas, filter_x, filter_y,
            fw * scale, fh * scale,
            '#e74c3c', f'Filter\n{fh}×{fw}'
        )

        # Draw stride indicator
        if s > 1:
            stride_y = filter_y + fh * scale + 30
            arrow_length = s * scale
            self.canvas.create_line(
                filter_x, stride_y,
                filter_x + arrow_length, stride_y,
                arrow=tk.LAST, width=3, fill='#f39c12'
            )
            self.canvas.create_text(
                filter_x + arrow_length // 2, stride_y - 15,
                text=f'Stride: {s}',
                font=('Arial', 10, 'bold'),
                fill='#f39c12'
            )

        # Draw arrow
        self.canvas.create_text(
            (filter_x + output_x) // 2, y_center,
            text='⟹',
            font=('Arial', 30),
            fill='#2c3e50'
        )

        # Draw output
        if is_valid:
            output_y = y_center - (oh * scale) // 2
            self.draw_rectangle(
                self.canvas, output_x, output_y,
                ow * scale, oh * scale,
                '#27ae60', f'Output\n{int(oh)}×{int(ow)}'
            )
        else:
            self.canvas.create_text(
                output_x, y_center,
                text='❌\nInvalid\nConfiguration',
                font=('Arial', 14, 'bold'),
                fill='#c0392b',
                justify=tk.CENTER
            )

    def draw_rectangle(self, canvas, x, y, w, h, color, label):
        """Draw a labeled rectangle."""
        # Draw rectangle
        canvas.create_rectangle(
            x, y, x + w, y + h,
            fill=color, outline='#2c3e50', width=2
        )

        # Draw label
        canvas.create_text(
            x + w // 2, y + h // 2,
            text=label,
            font=('Arial', 12, 'bold'),
            fill='white',
            justify=tk.CENTER
        )


def main():
    root = tk.Tk()
    app = ConvCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
