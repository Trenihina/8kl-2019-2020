def rule0(strForCheck:str):
    ch1 = strForCheck[2] in ['E', 'H', 'B']
    ch2 = strForCheck[0] in ['D', 'H', 'B', 'C'] and strForCheck[0] != strForCheck[2]
    ch3 = strForCheck[1] in ['D', 'E','C'] and strForCheck[1] != strForCheck[0]
    return ch1 and ch2 and ch3

# Цепочка из четырёх бусин, помеченных латинскими буквами, формируется по следующему правилу:
# – на втором месте цепочки стоит одна из бусин A, B, C;
# – в конце– одна из бусин B, D, C, которой нет на втором месте;
# – в начале – одна из бусин A, D, E, которой нет на четвёртом есте;
# – на третьем месте – одна из бусин C, D, E, не стоящая на первом месте.
# Определите, какие из перечисленных цепочек созданы по этому правилу?
# BADC  EACB  DBCE  AAEB  EAED  ECCD  EABC  ACDD  ABCB
# В ответе перечислите все такие цепочки через запятую.
def rule1(strForCheck:str):
    ch1 = strForCheck[1] in ['A', 'B', 'C']
    ch2 = strForCheck[3] in ['B', 'D','C'] and strForCheck[3] != strForCheck[1]
    ch3 = strForCheck[0] in ['A', 'D','E'] and strForCheck[0] != strForCheck[3]
    ch4 = strForCheck[2] in ['C', 'D','E'] and strForCheck[2] != strForCheck[0]
    return ch1 and ch2 and ch3 and ch4


'''3. Цепочка из трёх бусин, помеченных латинскими буквами, формируется по следующему правилу:
– в середине цепочки стоит одна из бусин A, D, F;
– на первом месте – одна из бусин C, B, A, которой нет на втором месте;
– в конце – одна из бусин C, B, D, F, не стоящая на первом месте.
Определите, какие из перечисленных цепочек созданы по этому правилу?
CAA  BDF  CFC  AAD  BFF  CDA  CDB  DAC  ACD
В ответе перечислите все такие цепочки через запятую.
'''
def rule2(strForCheck:str):
    ch1 = strForCheck[1] in ['A', 'D', 'F']
    ch2 = strForCheck[0] in ['C', 'B', 'A'] and strForCheck[0] != strForCheck[1]
    ch31 = strForCheck[2] in ['C', 'B', 'D', 'F']
    ch32 = strForCheck[2] != strForCheck[0]
    ch3  = ch31 and ch32
    # ch3 = strForCheck[2] in ['C', 'B', 'D', 'F'] and strForCheck[2] != strForCheck[0]
    return ch1 and ch2 and ch3

'''
Цепочка из трёх бусин, помеченных латинскими буквами, формируется по следующему правилу:
– в начале цепочки стоит одна из бусин D, B, C;
– на третьем месте – одна из бусин A, C, D, E, которой нет на первом месте;
– в середине – одна из бусин А, B, C, E, не стоящая на третьем месте.
Определите, какие из перечисленных цепочек созданы по этому правилу?
BCE  DAB  CCE  DCD  CAA  BAC  ABC  DCB  DAE
В ответе перечислите все такие цепочки через запятую.
'''

def rule3(strForCheck:str):
    ch1 = strForCheck[0] in ['D', 'B', 'C']
    ch2 = strForCheck[2] in ['A', 'C', 'D','E'] and strForCheck[2] != strForCheck[0]
    ch3 = strForCheck[1] in ['A', 'B', 'C', 'E'] and strForCheck[1] != strForCheck[2]
    return ch1 and ch2 and ch3

'''
Цепочка из трёх бусин, помеченных латинскими буквами, формируется по следующему правилу:
– в середине цепочки стоит одна из бусин C, D, H;
– на первом месте – одна из бусин A, B, C, которой нет на втором месте;
– в конце – одна из бусин А, B, D, H, не стоящая на первом месте.
Определите, какие из перечисленных цепочек созданы по этому правилу?
AHA  CCD  BHH  ADC  ADB  ACD  BDH  DCA  CAD
В ответе перечислите все такие цепочки через запятую.
'''
def rule4(strForCheck:str):
    ch1 = strForCheck[1] in ['C', 'D', 'H']
    ch2 = strForCheck[0] in ['A', 'B', 'C'] and strForCheck[0] != strForCheck[1]
    ch3 = strForCheck[2] in ['A', 'B', 'D', 'H'] and strForCheck[2] != strForCheck[0]
    return ch1 and ch2 and ch3

# строки для проверки
inp1 = ['BADC', 'EACB', 'DBCE', 'AAEB', 'EAED', 'ECCD', 'EABC', 'ACDD', 'ABCB']
inp2 = ['CAA', 'BDF', 'CFC', 'AAD', 'BFF', 'CDA', 'CDB', 'DAC', 'ACD']
inp3 = ['BCE', 'DAB', 'CCE', 'DCD', 'CAA', 'BAC', 'ABC', 'DCB', 'DAE']
inp4 = ['AHA', 'CCD', 'BHH', 'ADC', 'ADB', 'ACD', 'BDH', 'DCA', 'CAD']

inp0 = ['HDE', 'DDH', 'BHE', 'BEE', 'HDH', 'HBB', 'ECB', 'HED', 'CEB']

print('Вариант 1')
for chain in inp1:
    print(chain+':', rule1(chain))

print('Вариант 2')
for chain in inp2:
    print(chain+':', rule2(chain))

print('Вариант 3')
for chain in inp3:
    print(chain+':', rule3(chain))
    
print('Вариант 4')
for chain in inp4:
    print(chain+':', rule4(chain))