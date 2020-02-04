# Irfansha Shaik, 03.02.2020, Aarhus

'''
Emilie Lykke Thonsgaard
Irfansha Shaik
'''

# A naive script for submitting username and accessing the response from the url:
# http://lbs-2020-02.askarov.net:3030/

'''
todos:
- Instead of checking where the username is admin
  we will check if the key characters one by one (by sql injection).
  But we need to consider if the characters are alpha-numeric or more.
'''

import requests
import time

def get_usernames():
  users = []
  users.append("admin")
  return users

def test_username(username):
  payload= {'username': username, 'Submit':'submit'}
  #r = requests.get('http://lbs-2020-02.askarov.net:3030/', data=data)
  start_time = time.time()
  s = requests.post('http://lbs-2020-02.askarov.net:3030/reset/', payload)
  time_taken = (time.time() - start_time)
  # We need to assert if the resultant string is a success
  #print(r1.text)
  return time_taken

def main():
  usernames = get_usernames()
  for user_name in usernames:
    user_time = test_username(user_name)
    print(user_time)

if __name__== "__main__":
  main()
