# Password Leak Checker

## Overview
This is a simple Python script that checks whether a password has appeared in known data breaches. It uses the Have I Been Pwned service to see if a password has been exposed before.

---

## How It Works
- The password is converted into a SHA-1 hash
- Only part of that hash is sent when making the request
- The script compares the response to see if the password has been found before
- It returns how many times the password has appeared in breaches

---

