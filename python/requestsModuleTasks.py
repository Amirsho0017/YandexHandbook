from requests import get

server_addr = input()
key = input()

response = get(f"http://{server_addr}")
data = eval(response.content.decode('UTF-8'))

if data.get(key):
    print(data[key])
else:
    print('No data')

server_address = input()

response = get(f"http://{server_address}")
data = response.content.decode('utf-8')
li = [i for i in data if isinstance(i, int)]
print(sum(li))
