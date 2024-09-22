
import numpy as np

print(1+3/2)
print(2^10)
print(2**10)
a=10
print(a)

a=[1,2,3,4,5]
# 에러
#print(a/3) 

a=np.arange(1,10)
print(a)
print(a/3) # OK
print(a//3) #몱
print(a%3) #나머지

#자료형
a=100
print(type(a))
b=100.1
print(type(b))
bool(23.7)
print(type(bool(23.7)))

#문자열 합치기
c="~"
d=str(a)+" "+c
print(d)

# 패키지
a =  np.arange(15)
print(a)
print(a[0])
print(a[1])
m = np.mean(a)
print(m)

#결측치
height=np.array([45,75,60,51,np.nan])
print(height)
#np.mean(height)
print(np.nanmean(height))
#무한대
# import numpy as np
x = np.array([1, -1, 0, np.infty, -np.inf])
print(x/np.Infinity)
#날짜 시간
import datetime as dt
now = dt.datetime.now()
print(now.strftime("%Y년%m월%d일 : %A"))
print(now.year)

dob = dt.datetime(2020, 9, 8)
print(dob.strftime("%Y-%m-%d: %A"))