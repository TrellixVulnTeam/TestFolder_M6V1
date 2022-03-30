import time

a='abcdefghijklmnopqrstuvwxyz'
print(a[2:8:3])
print(a[2:8:2])
print(2**5)
print(25**0.5)
print(5|9)
print(5&9)
a=-5
print(~a)
a=time.gmtime()
b=time.gmtime()

print(a)
print(a==b)
print(a is b)
print(id(a))
print(id(b))


s='crazyit.org'
print('it' in s)
print('s' in s)
print('s' not in s)
print('azy' in s)
print('ay' not in s)

my_list=['my',20,'list',5.2]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[-3:-1])
my_list=('my',20,'list',4.3)
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])

my_list=(1,2,3,4,5,6,7,8,9,0)
print(my_list[0:9:2])
print(my_list[0:10:2])
my_list=[1,2,3,4,5,6,7,8,9,0]
print(my_list[0:9:2])
print(my_list[0:10:2])


my_A=(1,2,3,4)
my_B=('my','B')
my_A_B=my_B+my_A
print(my_A_B)
print(my_A_B+('000','2222'))

order_ending=('st','nd','rd')*2+('th',)*31
print(order_ending)
print(len(order_ending))
print(max(order_ending))
print(min(order_ending))
#day=input("input day (1-31):")
#day_int=int(day)
#print(day+order_ending[day_int-1])

vals=10,20,30
print(vals)
print(type(vals))
print(vals[1])
a_tuple=tuple(range(1,30,2))
print(a_tuple)
print(len(a_tuple))
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o=a_tuple
print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
x,y,z=10,20,30
print(x,y,z)
print(x)
print(y)
print(z)
first,*second,rest=range(1,10,1)
print(first)
print(second)
print(rest)


