cook_book = {}

with open('menu.txt', encoding='utf-8') as fail:
    lines = fail.readlines()
    non=(line for line in lines if not line.isspace())
    with open('new_menu.txt', 'w', encoding='utf-8') as n_f:
         n_f.writelines(non)

with open('new_menu.txt', encoding='utf-8') as f:
    while True:
        dish = f.readline().strip()
        #print(dish)
        if not dish:
            break
        n = f.readline().strip()
        #print(k)
        cook_book[dish]=[]
        for i in range(int(n)):
            ing = {}
            list = f.readline().strip().split('|')
            #print(list)
            ing['ingredient_name']=list[0]
            ing['quantity']=list[1]
            ing['measure'] = list[2]
            #print(ing)
            cook_book[dish].append(ing)           
print(cook_book)