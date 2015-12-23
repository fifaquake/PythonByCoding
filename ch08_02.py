import sys

print('opening files...')
f1 = open('mydoc1', 'r')
f2 = open('mydoc2', 'r')


def reading_data(f):
    while True:
        data = f.readline()
        if (data == '') or (data is None):
            break
        sys.stdout.write(data)

reading_data(f1)
reading_data(f2)

f1.close()
f2.close()