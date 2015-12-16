import time

now = time.time()

print(now)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(now)))
print(time.timezone)