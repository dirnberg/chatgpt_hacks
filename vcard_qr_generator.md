## QR Code Generator for vCard Information

This script generates a QR code image for each vCard data object in a given JSON array. The script takes a JSON array as an argument, with each object in the array containing vCard information for a person. The vCard information includes fields such as first name, last name, company, position, phone numbers, email, address, and URL.

The script extracts the relevant fields from each vCard data object, concatenates them into a vCard information string, and uses it to create a QR code object with qrcode library. The generated QR code is saved as a PNG image file, with a filename format of vcard_QR_{first_name}_{last_name}.png.

The script generates a QR code image for each vCard data object in the input JSON array. The images are saved as PNG files in the current directory, with filenames starting with "vcard_QR_" followed by the person's first name and last name.

# Requirements
Python 3.x

qrcode

You can install qrcode using pip:

```bash
pip install qrcode
```

# Usage
```bash
python3 vcard_qr_generator.py --vcard '[{"first_name": "Jane", "last_name": "Doe", "company": "XYZ Corporation", "position": "Director", "mobile_number": "+1 555-987-6543", "tel_number": "+1 555-123-4567", "email": "jane.doe@xyzcorp.com", "address": "123 Main St, Anytown, USA", "url": "https://www.xyzcorp.com"}, {"first_name": "John", "last_name": "Smith", "company": "ABC Inc", "position": "Manager", "mobile_number": "+1 555-123-4567", "tel_number": "+1 555-987-6543", "email": "john.smith@abcinc.com", "address": "456 Oak St, Anytown, USA", "url": "https://www.abcinc.com"}]'
```
```bash
Arguments
--vcard: The vCard information in JSON array format, containing one or more vCard data objects. Each object should include fields such as first name, last name, company, position, phone numbers, email, address, and URL. If not provided, default values will be used for each field.
Output
```


