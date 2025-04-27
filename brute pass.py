import socket
import time

# Constants
HOST = '127.0.0.1'
PORT = 8888
DELAY = 1.2

def try_pin(pin):
    # Format PIN to ensure 3 digits with leading zeros
    pin_str = f"{pin:03d}"
    data = f"magicNumber={pin_str}"
    
    # Create HTTP request
    request = (
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
        f"{data}"
    )