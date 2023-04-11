# Usage: python3 vcard_qr_logo.py --prefix vcard_QR_ --folder ./QRcodes

import argparse
import json
import os
import re
from PIL import Image
import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create an argparse object and define the vcard argument
parser = argparse.ArgumentParser(description='Generate a QR code with logo')
parser.add_argument('--prefix', type=str, default='vcard_QR_', help='Prefix for input QR code image filenames')
parser.add_argument('--folder', type=str, default='.', help='Path to folder containing input QR code images')

# Parse the command-line arguments
args = parser.parse_args()

# Get a list of all PNG files in the specified folder with the specified prefix
qr_files = [f for f in os.listdir(args.folder) if f.endswith('.png') and f.startswith(args.prefix)]

# Loop through each QR code file
for qr_file in qr_files:
    # Load the QR code image
    qr_img = Image.open(os.path.join(args.folder, qr_file))

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
    output_path = os.path.join(args.folder, qr_file.split('.')[0] + "_logo.png")
    qr_img.save(output_path, dpi=(600, 600))
