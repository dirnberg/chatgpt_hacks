# QR Code Logo Generator

This script generates a new QR code image by overlaying a logo on top of an existing QR code image. The script takes a folder path and a prefix as arguments, and processes all PNG files in the folder with filenames starting with the prefix. The logo image is hard-coded as "logo.png" and must be present in the same directory as the script.

The QR code images are assumed to be in 300 dpi and will be converted to RGBA mode for transparency. The logo image is also converted to RGBA mode and resized to 300 dpi before being overlaid on the QR code image in the center. The output image is saved as a new PNG file with the suffix "_logo" added to the original filename.

Usage

```bash
python3 vcard_qr_logo.py --prefix vcard_QR_ --folder ./QRcodes
```

Arguments
--prefix: The prefix for the input QR code image filenames (default is "vcard_QR_")
--folder: The path to the folder containing the input QR code images (default is current directory)

# Requirements
```bash
pip install pillow qrcode
```

This will install both Pillow and qrcode packages. You can run this command in your terminal or command prompt to install the packages.

(done with chatgpt)
prompt: write python code to get a qr code from vcard information
