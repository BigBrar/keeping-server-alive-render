import requests
import time

# Your server URL
URL = "https://backend-pspcl-power-supply-check.onrender.com/"

def ping_server():
    try:
        response = requests.get(URL, timeout=10)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Pinged {URL} - Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error pinging {URL}: {e}")

if __name__ == "__main__":
    ping_server()
