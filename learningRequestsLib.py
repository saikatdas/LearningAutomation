#learning requests lib in python
import requests
r = requests.get('http://www.saikatdas.in')
print(r.status_code)
