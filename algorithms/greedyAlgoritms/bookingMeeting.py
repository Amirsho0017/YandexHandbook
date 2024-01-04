number = int(input())

times = []
while number > 0:
    number -= 1
    l, r = map(int, input().split())
    times.append([l, r])

times.sort(key=lambda x: x[1])  # Sort intervals based on the ending time

resp = [times[0]]
for i in range(1, len(times)):
    if times[i][0] > resp[-1][1]:
        resp.append(times[i])

print(len(resp))
