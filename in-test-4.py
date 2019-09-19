
# неубывание 1+2+3 / 3+4+5
def calc1(check):
    results = {}
    for n in range(10000,99999):
        s = str(n)
        n1 = int(s[0]) + int(s[1]) + int(s[2])
        n2 = int(s[2]) + int(s[3]) + int(s[4])
        if (n1 > n2):
            res = str(n2) + str(n1)
        else:
            res = str(n1) + str(n2)
        if res in check:
            results[res] = res
            print(s, res)
    return results

# неубывание 1 + 3 + 5 // 2 + 4
def calc2(check):
    results = {}
    for n in range(10000,99999):
        s = str(n)
        n1 = int(s[0]) + int(s[2]) + int(s[4])
        n2 = int(s[1]) + int(s[3])
        if (n1 > n2):
            res = str(n2) + str(n1)
        else:
            res = str(n1) + str(n2)
        if res in check:
            results[res] = res
            print(s, res)
    return results

# невозрастание 1 + 3 + 5 // 2 + 4
def calc3(check):
    results = {}
    for n in range(10000,99999):
        s = str(n)
        n1 = int(s[0]) + int(s[2]) + int(s[4])
        n2 = int(s[1]) + int(s[3])
        if (n1 < n2):
            res = str(n2) + str(n1)
        else:
            res = str(n1) + str(n2)
        if res in check:
            results[res] = res
            print(s, res)
    return results

check1 = ['2525', '256', '2520', '2528', '2825', '2025', '625', '106']
check2 = ['30', '1528', '116', '1519', '2019', '1920', '1915', '316', '2815']
check3 = ['10', '1528', '116', '1519', '2019', '1920', '1915', '316', '2815']
check4 = ['1220', '120', '210', '2012', '1920', '2019', '212', '2919', '1929']

print(calc1(check1))
print(calc2(check2))
print(calc3(check3))
print(calc3(check4))
