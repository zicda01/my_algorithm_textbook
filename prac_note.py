# import sys
# sys.stdin = open("input.txt", "r")

def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x)-ord('0')      # in ASCII, '0' = 48, '1' = 49, '2' = 50
    return i

s = '123'
a = atoi(s)
print(a + 1)            # 124