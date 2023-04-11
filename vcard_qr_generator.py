# usage
# python3 vcard_qr_generator.py --vcard '[{"first_name": "Jane", "last_name": "Doe", "company": "XYZ Corporation", "position": "Director", "mobile_number": "+1 555-987-6543", "tel_number": "+1 555-123-4567", "email": "jane.doe@xyzcorp.com", "address": "123 Main St, Anytown, USA", "url": "https://www.xyzcorp.com"}, {"first_name": "John", "last_name": "Smith", "company": "ABC Inc", "position": "Manager", "mobile_number": "+1 555-123-4567", "tel_number": "+1 555-987-6543", "email": "john.smith@abcinc.com", "address": "456 Oak St, Anytown, USA", "url": "https://www.abcinc.com"}]'

import argparse
import json
import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create an argparse object and define the vcard argument
parser = argparse.ArgumentParser(description='Generate a QR code for vcard information')
parser.add_argument('--vcard', type=str, default='[{"first_name": "", "last_name": "NN", "company": "", "position": "", "mobile_number": "", "tel_number": "", "email": "", "address": "", "url": ""}]', help='vCard information in JSON array format')

# Parse the command-line arguments
args = parser.parse_args()

# Load the vcard data from the JSON array
vcard_data_array = json.loads(args.vcard)

# Loop through each vCard data object in the array
for vcard_data in vcard_data_array:
    # Extract the relevant fields from the vcard data
    first_name = vcard_data['first_name']
    last_name = vcard_data['last_name']
    company = vcard_data['company']
    position = vcard_data['position']
    mobile_number = vcard_data['mobile_number']
    tel_number = vcard_data['tel_number']
    email = vcard_data['email']
    address = vcard_data['address']
    url = vcard_data['url']

    # Concatenate vCard information into a string
    vcard_info = f"BEGIN:VCARD\nVERSION:3.0\nN:{last_name};{first_name};;;\nORG:{company}\nTITLE:{position}\nTEL;TYPE=CELL:{mobile_number}\nTEL;TYPE=WORK:{tel_number}\nEMAIL:{email}\nADR;TYPE=HOME:;;{address};;;;\nURL:{url}\nEND:VCARD"

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
    img.save(f"vcard_QR_{first_name}_{last_name}.png", dpi=(600, 600))
