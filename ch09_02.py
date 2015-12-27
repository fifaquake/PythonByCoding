try:
    a = 18
    b = 0
    c = a / b
    print('result', str(c))
except ZeroDivisionError as e:
    print('Error: division by zero')
    print(e)
finally:
    print('Done')

print('exit form program')