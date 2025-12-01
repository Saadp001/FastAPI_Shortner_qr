from urllib.parse import urlparse
import hashlib
import qrcode
import os

def get_domain_prefix(url: str) -> str:
    domain = urlparse(url).netloc
    domain_name = domain.split(".")[0]
    return domain_name[:3].lower()

def get_hash_suffix(url: str) -> str:
    hash_value = hashlib.sha256(url.encode()).hexdigest()
    return hash_value[:3]

def generate_short_code(url: str) -> str:
    return get_domain_prefix(url) + get_hash_suffix(url)




def generate_qr(short_url: str) -> str:
    # File path
    qr_path = f"qr_codes/{short_url}.png"

    # If QR already exists, don't regenerate
    if os.path.exists(qr_path):
        return qr_path

    # Generate QR image
    img = qrcode.make(short_url)
    img.save(qr_path)

    return qr_path
