def even_odd_test(x):
    if (x % 2 == 0):
        print(f"{x} is even number")
    elif (x % 2 == 1):
        print(f"{x} is odd number")
    else:
        print(f"{x} is no integer")


even_odd_test(100)
even_odd_test(101)
even_odd_test(1.1)
# for
sum = 0
for x in range(1, 11):
    sum = sum + x**2
else:
    print(f"for] sum is {sum}")
# while
x = 1
sum = 0
while (x <= 10):
    sum = sum ** 2
    x = x + 1
else:
    print(f"while] sum is {sum}")
# continue
x = range(1, 6)
for j in x:
    if (j == 3):
        continue
    print(j, " continue")
# break
x = range(1, 6)
for j in x:
    if (j == 3):
        break
    print(j, " break")
# function


def my_sum(a=0, b=10):
    import numpy as np
    my_data = np.arange(a, b+1)
    sum1 = 0
    sum2 = 0
    for i in my_data:
        sum1 = sum1 + i
        sum2 = sum2 + i**2
    return sum1, sum2, len(my_data)


a = my_sum(1, 10)
print(a)
average = a[0]/a[2]
variation = (a[1] - a[2]*(average**2)) / (a[2] - 1)
print(f"aveage is {average} , variation is {variation}")
b = my_sum()
average = b[0]/b[2]
print(b)
variation = (b[1] - b[2]*(average**2)) / (b[2] - 1)
print(f"aveage is {average} , variation is {variation}")


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
