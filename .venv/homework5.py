#Работа со списками
my_list = ['apple', 'banana', 'cherry', 'peach', 'strawberry', 'pear']
print(type(my_list))
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5])
my_list[3] = 'orange'
print(my_list)
#Работа со словарями
my_dict={'HI': 'Привет', 'How': 'Как', 'Processing': 'Обработка', 'Popularity':'Популярность'}
print(type(my_dict))
print(my_dict)
print(my_dict['HI'])
my_dict.setdefault('Hello', 'Здраствуйте')
print(my_dict)