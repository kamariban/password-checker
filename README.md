# Password Leak Checker

## Overview
This is a Python script that checks whether a password has appeared in known data breaches. It uses the Have I Been Pwned service to verify if a password has been exposed before.

---

## How It Works
- The password is converted into a SHA-1 hash  
- Only the first 5 characters of the hash are sent in the request  
- The API returns possible matches  
- The script checks the rest of the hash locally  
- If found, it returns how many times the password has appeared in breaches
---

## Requirements
- Python 3.x  
- requests  

Install dependencies:  
pip install requests  


## Notes
- The full password is NEVER sent over the network  
- Only part of a hashed version is used  
- Nothing is stored or logged  
