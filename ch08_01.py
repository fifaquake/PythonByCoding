print('Creating files...')

f1 = open('mydoc1', 'w')

f2 = open('mydoc2', 'a')


print('writing data into files...')
for index in range(1, 12):
    data = ''
    name = 'user ' + str(index - 1)
    email = 'user ' + str(index - 1) + '@email.com'
    if index == 1:
        data = '{0:3s} {1:10s} {2:15s}\n'.format('No', 'Name', 'Email')
    else:
        data = '{0:3s} {1:10s} {2:15s}\n'.format(str(index - 1), name, email)

    f1.write(data)
    f2.write(data)

print('close file...')
f1.close()
f2.close()
