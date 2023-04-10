# usage
# python3 vcard_qr_generator.py --vcard '{"first_name": "Jane", "last_name": "Doe", "company": "XYZ Corporation", "position": "Director", "mobile_number": "+1 555-987-6543", "tel_number": "+1 555-123-4567", "email": "jane.doe@xyzcorp.com"}'

import argparse
import json
import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create an argparse object and define the vcard argument
parser = argparse.ArgumentParser(description='Generate a QR code for vcard information')
parser.add_argument('--vcard', type=str, default='{"first_name": "", "last_name": "NN", "company": "", "position": "", "mobile_number": "", "tel_number": "", "email": ""}', help='vCard information in JSON format')

# Parse the command-line arguments
args = parser.parse_args()

# Load the vcard data from the JSON string
vcard_data = json.loads(args.vcard)

# Extract the relevant fields from the vcard data
first_name = vcard_data['first_name']
last_name = vcard_data['last_name']
company = vcard_data['company']
position = vcard_data['position']
mobile_number = vcard_data['mobile_number']
tel_number = vcard_data['tel_number']
email = vcard_data['email']

# Concatenate vCard information into a string
vcard_info = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nORG:{company}\nTITLE:{position}\nTEL;TYPE=CELL:{mobile_number}\nTEL;TYPE=WORK:{tel_number}\nEMAIL:{email}\nEND:VCARD"

# Create QR code object with vCard information
qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=60,  # 1 inch = 60 pixels at 600dpi
    border=4,
)
qr.add_data(vcard_info)
qr.make(fit=True)

# Create and save QR code image as PNG
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{first_name}_{last_name}.png", dpi=(600, 600))
