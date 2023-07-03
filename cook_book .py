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
print()

# Задача 2
def get_shop_list_by_dishes(dishes, person_count):
    dishes=dishes
    person_count=person_count
    list ={}
    for i in dishes:
        for j in cook_book.keys():
            if j==i:
                products=(cook_book[j])
                for k in products:
                    ingredient=k.get('ingredient_name')
                    # print(ingredient)
                    if ingredient in list.keys(): 
                        x=int(k.get('quantity'))*person_count
                        #print(x)
                        y=list.get(ingredient)
                        #print(y)
                        for i in y:
                            for key, value in i.items():
                                if key=='quantity':
                                    z=value+x
                                    #print(z)
                        list[ingredient]=[]
                        df={}
                        quant=k.get('quantity')
                        meas=k.get('measure')
                        df['measure']=meas
                        df['quantity']=z
                        list[ingredient].append(df)        

                        
                    else:
                        list[ingredient]=[]
                        df={}
                        quant=k.get('quantity')
                        meas=k.get('measure')
                        df['measure']=meas
                        df['quantity']=int(quant)*person_count
                        list[ingredient].append(df)
    
    return list
    
    
#get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)       
print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 3))


