# Irfansha Shaik, 03.02.2020, Aarhus

'''
Emilie Lykke Thonsgaard
Irfansha Shaik
'''

# A naive script for submitting username and accessing the response from the url:
# http://lbs-2020-02.askarov.net:3030/

'''
todos:
- Write a function for submitting username: test_username
  Input: string (username)
  Proc: we submit the username in the website and time the invocation
  Ouput: float (the time taken to complete invocation)
- Now need to time the calls
  - We want to use inbuild time functions in python.
  - First we consider the module timeit.
'''

import requests

def get_usernames():
  users = []
  users.append("admin")
  return users

def test_username(username):
  payload= {'username': username, 'Submit':'submit'}
  #r = requests.get('http://lbs-2020-02.askarov.net:3030/', data=data)
  r1 = requests.post('http://lbs-2020-02.askarov.net:3030/reset/', payload)
  # We need to assert if the resultant string is a success
  #print(r1.text)
  return 0

def main():
  usernames = get_usernames()
  for user_name in usernames:
    user_time = test_username(user_name)
    #print(user_time)

if __name__== "__main__":
  main()
