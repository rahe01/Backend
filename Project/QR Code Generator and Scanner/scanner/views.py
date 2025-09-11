from django.shortcuts import render
import qrcode
from .models import QRCode
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings
from pathlib import Path
import os

# Generate QR Code
def generate_qr(req):
    qr_image_url = None

    if req.method == 'POST':
        mobile_number = req.POST.get('mobile_number')
        data = req.POST.get('qr_data')

        # Validate mobile number
        if not mobile_number or len(mobile_number) != 11 or not mobile_number.isdigit():
            return render(req, 'scanner/generate.html', {'error': 'Invalid Mobile Number'})

        # Generate QR Code
        qr_content = f"{data}|{mobile_number}"
        qr = qrcode.make(qr_content)

        qr_image_io = BytesIO()
        qr.save(qr_image_io, format="PNG")
        qr_image_io.seek(0)

        # Ensure qr_codes folder exists inside MEDIA_ROOT
        qr_storage_path = Path(settings.MEDIA_ROOT) / 'qr_codes'
        os.makedirs(qr_storage_path, exist_ok=True)

        fs = FileSystemStorage(location=qr_storage_path, base_url='/media/qr_codes/')
        filename = f"{data}_{mobile_number}.png"

        qr_image_content = ContentFile(qr_image_io.read(), name=filename)
        filepath = fs.save(filename, qr_image_content)
        qr_image_url = fs.url(filename)

        # Save in database (if QRCode model has an ImageField)
        QRCode.objects.create(
            data=data,
            mobile_number=mobile_number,
            image=filepath  # assumes you have "image = models.ImageField(upload_to='qr_codes/')" in your model
        )

    return render(req, 'scanner/generate.html', {'qr_image_url': qr_image_url})


# Scan QR Code page
def scan_qr(req):
    return render(req, 'scanner/scan.html')
