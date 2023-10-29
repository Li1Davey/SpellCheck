'''
David Sanchez
'''

#_Main--------------------------------------------
file = 'wp_2gram.txt'
fp = open(file, encoding="utf8")
limit = 10
total = 0
for line in fp.readlines():
    if(limit > 0):
        x = line.replace('\n', '')
        a = x.split('\t')
        total += int(a[0])
        print(a)
    limit-=1
print(total)