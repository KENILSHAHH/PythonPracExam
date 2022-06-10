my_list = ['p', 'q']
n=int(input("Input a number "))

new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)