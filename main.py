from converters import ITermToWindowsConverter
import os

if __name__ == "__main__":
    for file in os.listdir('iterm2-themes'):
        ITermToWindowsConverter.convert(f"iterm2-themes/{file}")
