import math
A, B, V = map(int,input().split()) # A는 올라가는 미터 B는 미끄러지는 미터 V는 높이
print(math.ceil((V-A)/(A-B)) + 1)