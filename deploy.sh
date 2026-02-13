#!/bin/bash
# Quick deployment script for GitHub Pages

echo "🚀 Deploying Convolution Calculator to GitHub Pages"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Convolution Calculator"
else
    echo "✅ Git repository already initialized"
fi

echo ""
echo "📝 Next steps:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   https://github.com/new"
echo ""
echo "2. Name it: convolution-calculator"
echo ""
echo "3. Run these commands:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/convolution-calculator.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "4. Enable GitHub Pages:"
echo "   - Go to repository Settings → Pages"
echo "   - Select branch: main"
echo "   - Click Save"
echo ""
echo "5. Your site will be live at:"
echo "   https://YOUR_USERNAME.github.io/convolution-calculator/"
echo ""
echo "✨ Done!"
