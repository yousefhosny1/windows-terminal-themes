from converters import ITermToWindowsConverter
import argparse
import os

parser = argparse.ArgumentParser(description='Iterm2 theme converter')

# Add the argument
parser.add_argument('path', type=str, help='Path to .itermcolors file')

# Parse the arguments
args = parser.parse_args()

if __name__ == "__main__":
    for file in os.listdir('iterm2-themes'):
        ITermToWindowsConverter.convert(f"{args.path}")
