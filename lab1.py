import requests

print(requests.__version__)
response = requests.get('http://www.google.com/')
response_github = requests.get('https://github.com/HyZ7846/CMPUT404lab1')
#print(response.text)
print(response_github.text)
