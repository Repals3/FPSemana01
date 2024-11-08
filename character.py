monster1 = str(input("What is your monster name? "))
HP1=int(input("Health points? "))
lvl1=int(input("Level? "))

monster2 = str(input("What is your monster name? "))
HP2=int(input("Health points? "))
lvl2=int(input("Level? "))

monster3 = str(input("What is your monster name? "))
HP3=int(input("Health points? "))
lvl3=int(input("Level? "))


print(monster1)
print(HP1)
print(lvl1)

print(monster2)
print(HP2)
print(lvl2)

print(monster3)
print(HP3)
print(lvl3)

array=[
    [monster1,(HP1,lvl1)],
    [monster2,(HP2,lvl2)],
    [monster3,(HP3,lvl3)]
]

print(array)

def arrumação_monsterlvl(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j][1][1]<array[j+1][1][1]:
                array[j],array[j+1] = array[j+1], array[j]

arrumação_monsterlvl(array)

for i in array:
    print(i[0])