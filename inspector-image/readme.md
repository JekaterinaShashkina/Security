# Inspector Image

A program for analyzing images. It allows extracting data from metadata (EXIF) and checking for steganography. Steganography is the technique of hiding data within an ordinary, nonsecret file or message to avoid detection; the hidden data is then extracted at its destination.

# Installation

1. Make sure you have Python 3 installed.
2. Install the necessary dependencies using the command: pip install exifread

# How to use

Use the command

To find the location where this photo was taken
**python inspector_image.py -map image.jpeg**

To show the pgp key which is hidden in the image
**python inspector_image.py -steg image.jpeg**

# Error

If the program is run without specifying a flag, it will display a message with command line usage instructions.
