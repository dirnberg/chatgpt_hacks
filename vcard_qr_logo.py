#Usage

#pip install argparse Pillow qrcode

#python3 vcard_qr_logo.py --qr_path Jane_Doe.png 

import argparse
import json
from PIL import Image
import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create an argparse object and define the vcard argument
parser = argparse.ArgumentParser(description='Generate a QR code with logo')
parser.add_argument('--qr_path', type=str, default='vcard_qr.png', help='Path to the input QR code image')
# Parse the command-line arguments
args = parser.parse_args()

# Load the QR code image
qr_img = Image.open(args.qr_path)

# Open logo image
logo_img = Image.open("logo.png")

# Resize logo to 300 dpi
logo_img = logo_img.resize((int(300 * logo_img.size[0] / logo_img.info['dpi'][0]),
                            int(300 * logo_img.size[1] / logo_img.info['dpi'][1])),
                           resample=Image.LANCZOS)
logo_img.info['dpi'] = (300, 300)

# Convert logo to RGBA mode for transparency
logo_img = logo_img.convert("RGBA")

# Calculate position to place logo in the center of QR code
x_pos = int((qr_img.size[0] - logo_img.size[0]) / 2)
y_pos = int((qr_img.size[1] - logo_img.size[1]) / 2)

# Convert QR code to RGBA mode for transparency
qr_img = qr_img.convert("RGBA")

# Overlay logo on top of QR code
qr_img.alpha_composite(logo_img, dest=(x_pos, y_pos))

# Generate new output PNG image
output_path = args.qr_path.split('.')[0] + "_logo.png"
qr_img.save(output_path, dpi=(600, 600))
