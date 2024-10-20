my_list = ['uhhhh','😐', 7, 19, 'hello','🤷' ]
my_list.append("hi")
my_list.insert(2, '👋 👋')

count = 0
while count < len(my_list):
    print(count, my_list[count])
    count = count +1
    
    
for example in my_list:
    if str(example).lower()[0] == 'h':
        print(example, "starts with h")