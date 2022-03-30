
a='our domain is crazyit .org'
table ={97:945,98:946,116:964}
print(a.translate(table))
print(a.title())
print(a.lower())
print(a.upper())
b = a.title()
print(b)
Bignum=123
Bignum1=123
a_1=a.split(None,4)
print(a_1)
a_2='//'.join(a_1)
print(a_2)
print("Test: %s and %s " %(Bignum,Bignum1))
print("Test: %d and %o " %(Bignum,Bignum1))
print("Test: %e and %E " %(Bignum,Bignum1))
print("Test: %-09.3f and %F " %(Bignum,Bignum1))
print("Test: %G and %c " %(Bignum,Bignum1))
print("Test: %r and %X " %(Bignum,Bignum1))


print(4//1)

table=str.maketrans('abc','erw')

print (table)