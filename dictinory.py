#dictinory: dictinory is a collection of keys and values pairs. It is used in {}.
Menu={1:'Tiffins',2:'Veg Starter',3:'Chicken Starter',4:'Dessert',5:'pastry'}
Menu[1];
Menu[3];
Menu[5];
Menu.get(3);
Menu.get(4);
Menu.get(7);
Menu.pop(1);
print(Menu);
print(Menu.get(3));
print(Menu.get(4));
print(Menu.get(7));
print(Menu.get(0,'welcome'));
print(Menu.get(6,'visit again'));
Tiffins=[1,2,3,4,5];
names=['Idly','Dosa','bonda','punugulu','bajji'];
print(names[2]);
rest=dict(zip(Tiffins,names));      #Zip is used to merge the keys and values into dictinory
print(rest);
clients={'vinni':'dosa','vinesh':'idly','srikanth':['dosa','biryani','coke'],'rohit':{'tiffins':'sambar Idly','veggies':'paneer','chipotle':'burrito bowl'}}
print(clients['vinni']);
print(clients['srikanth'][2]);
print(clients['rohit']);
print(clients['rohit']['tiffins']);




