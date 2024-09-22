a= [1,2,3,4,5]
print(a)      #[1, 2, 3, 4, 5]
print(len(a)) #5
print(a[0])   #1
print(a[4])   #5
a[4]=99       
print(a)      #[1, 2, 3, 4, 99]
print(a[0:2]) #[1, 2]
print(a[1:])  #[2, 3, 4, 99]
print(a[:3])  #[1, 2, 3]
print(a[:-1]) #[1, 2, 3, 4]
print(a[:-2]) #[1, 2, 3]