import requests

# user_info = {'name': ['letian', 'letian2'], 'password': '123'}
# json_data = {'a': 1, 'b': 4}
file_data = {'image': open('Lenna.png', 'rb')}
user_info = {'info': 'Lenna'}

r = requests.post("http://127.0.0.1:6000/upload", data=user_info, files=file_data)

print(r.headers)
print(r.text)
