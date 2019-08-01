"""                 ЗАДАНИЕ1            """
# 1.Ввести три числа. Посчитать кол-во отрицательных чисел
def count_negative():

    m = int (input("Введите первое число: \n"))
    n = int (input("Введите второе число: \n"))
    p = int (input("Введите третье число: \n"))
    string = (m,n,p)

    print (len([x for x in string if int(x)<0]))

count_negative()

# 2.Имеется ли среди трёх чисел пара равных
def equal_couple():
    print ("Введите три числа \n")
    l = input().split()
    for i in set(l):
        if l.count(i) >= 2:
            print (i,l.count(i))
    else: print ("Nothing equal")

equal_couple()

# 3.Найти среднее геометрическое,если не равны нулю, в противном случае среднее арифмитическое
"""def geo_ari(lst):
    s=0
    for i in lst:
        if i != 0:
            s+=i 
        return s/len(lst)
    print (s/len(lst))   
    for i in set(l):
        if i != 0:
            print (ll)
            print ("KGFG")
        #return geo
    print ("KGFG")
    geo = sum(l)/len(l)
    print (geo)

geo_ari([2,7,13])
"""

# 4.По номеру месяца вывести пору года
def period(number):
    if number in [12,1,2]:
        print ("It's winter!")
    elif number in [3,4,5]:
        print ("It's spring!")
    elif number in [6,7,8]:
        print ("It's summer!")
    elif number in [9,10,11]:
        print ("It's autumn!")
period(7)

# 11. Найти наибольшее число
def maxvalue(a,b,c):
    d=max(a,b,c)
    print ("Наибольшее число из трёх это {} ".format(d))

maxvalue(43,1043,786)

# 13. <Мы нашли К грибов в лесу>
def mushroom(k):
    a = ('гриб', 'гриба', 'грибов')
    if k == 1:
        print ("Мы нашли %s %s в лесу" % (k,a[0]))
    elif k in [2,3,4]:
        print ("Мы нашли %s %s в лесу" % (k,a[1]))
    elif k in [5,6,7,8,9]:
        print("Мы нашли %s %s в лесу" % (k,a[2]))
    else:
        print('Вы ввели не натуральное число!')

mushroom(76)

# 14. Вывести возраст
def age(k):
    a = ('год', 'года', 'лет')
    if k in [1,21,31,41,51,61,71,81,91]:
        print ("Мне %s %s" % (k,a[0]))
    elif k in [2,22,32,42,52,62,72,82,92,3,23,33,43,53,63,73,83,93,4,24,34,44,54,64,74,84,94]:
        print ("Мне %s %s" % (k,a[1]))
    elif k in [5,25,35,45,55,65,75,85,95,6,26,36,46,56,66,76,86,96,7,27,37,47,57,67,77,87,97,8,28,38,48,58,68,78,88,98,9,29,39,49,59,69,79,89,99]:
        print("Мне %s %s" % (k,a[2]))
    else:
        print('Вы ввели не целое число!')
age(98)

