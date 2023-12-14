import requests

server_address = input()

total_sum = 0

response = requests.get(f"http://{server_address}")
while True:
    data = int(response.content.decode('utf-8'))
    if data == 0:
        break
    else:
        total_sum += data

print(total_sum)
