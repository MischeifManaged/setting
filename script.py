import sys 
import requests

#print(sys.version)
print(sys.executable)

def greet(who_to_target):
    greeting = "Hello, {}".format(who_to_target)
    return greeting

r = requests.get('https://coreyms.com')
print(r.status_code)
