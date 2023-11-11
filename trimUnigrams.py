def has_numbers(s):
    return any(char.isdigit() for char in s)

def isEnglish(s):
    return s.isascii()

def hadSymbol(s):
    special_characters = "~`^,!?@$%^&*()-+_=<>/|:;\""
    return any(c in special_characters for c in s)

def twoUpperCase(s):
    if(len(s)>1):
        return s[0].isupper() and s[1].isupper()
    else:
        return False

def createNewBigrams():
    i = 0
    approve = []
    with open("wp_1gram.txt", encoding="utf8") as file:
        for line in file:
            x = line.replace('\n', '')
            a = x.split('\t')
            a[0] = int(a[0])
            if (has_numbers(a[1]) == False) and (isEnglish(a[1])) and (hadSymbol(a[1]) == False) and (twoUpperCase(a[1]) == False):
                approve.append(line)
            if (i % 10000000 == 0):
                print(i)
            i+=1
    print("Finished")
    return approve

f = open("new_wp_1gram.txt", 'w')
new_list = createNewBigrams()
for line in new_list:
    f.write(line)
f.close()
