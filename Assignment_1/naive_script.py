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
'''

import requests


def test_username():
  payload= {'username': 'admin', 'Submit':'submit'}
  #r = requests.get('http://lbs-2020-02.askarov.net:3030/', data=data)
  r1 = requests.post('http://lbs-2020-02.askarov.net:3030/reset/', payload)
  print(r1.text)

def main():
  test_username()

if __name__== "__main__":
  main()
