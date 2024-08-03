from colorama import Fore
x = [" Hi dear!This app is just for entertainment.”,”we are going to help you to find a good name for your  friendship:) ",
     ]
x2 = [Fore.LIGHTGREEN_EX, Fore.RESET, Fore.MAGENTA, Fore.CYAN]
for i in x:
    print(i)
n1 = str(input(Fore.RESET+"enter first name : "))
n2 = str(input("enter seconds name : "))
pl = []
pl2 = []
j = []
name = [len(n1),len(n2)]
def ship_name_developer(name1, name2):
    for jk in n1:
        pl.append(jk)
    for v in n2:
        pl2.append(v)
    for k in range(min(name)):
        if pl[k] in pl2:
            j.append(pl[k])
    length_n1 = len(name1)
    length_n2 = len(name2)
    a = length_n1 // 2
    b = length_n2 // 2
    tim = n1[:a] + n2[:b]
    if len(j) < 3:
        print(tim, "is good option")
    else:
        print(Fore.MAGENTA, tim, "or", Fore.CYAN, j[0]+j[1]+j[2])
ship_name_developer(n1, n2)