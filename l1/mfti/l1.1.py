print("как тебя зовут?")
name = input()
print("привет", name, "!", sep="")
age =  int(input("сколько тебе лет, " + name + "?"))
print('а я думал, тебе', age + 1 , end='')
x = age +1
if x >= 11 and x <= 19:
     print('лет')
else:
    if x % 10 == 1:
        print('год')
    else:
        if x % 10 >= 2 and x % 10 <= 4:
            print('года')
        else:
            print('лет')

print('!..')
