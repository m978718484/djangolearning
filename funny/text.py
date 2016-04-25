v = open('text.txt')
lines = v.readlines()
v.close()

for line in lines:
        a = line.decode('utf8')
        a = a.encode('utf8')
        print a.decode('utf8')

