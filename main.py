import requests
import hashlib
import sys

# send request to api using first 5 chars of hashed password
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)

  # basic check to make sure request worked
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  
  return res


# loop through returned hashes and see if our password matches
def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())

  # compare each hash tail with ours
  for h, count in hashes:
    if h == hash_to_check:
      return count
  
  return 0

# hash password and split into first 5 chars + rest
def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]

  # send only first part to api for security
  response = request_api_data(first5_char)

  return get_password_leaks_count(response, tail)


# main loop to check multiple passwords from command line
def main(args):
  for password in args:
    count = pwned_api_check(password)

    # print result based on whether password was found
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  
  return 'done!'


if __name__ == '__main__':
  # take passwords from command line input
  sys.exit(main(sys.argv[1:]))
  
# example usage (testing multiple passwords):
# python main.py password123 BIGMONEY2002 ryetoast
