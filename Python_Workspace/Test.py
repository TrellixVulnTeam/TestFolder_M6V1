
def Test_1(type):
    a = 123
    def A_1():
        nonlocal a
        print(a)
        if a==123:
            a=223
            print(a)
            return a*a
    def  B_1():
        print(a)
        if a==123:
            return a**a
    if type=="B_1":
        return B_1
    else:
        return A_1
mat_fun=Test_1("A_1")
data=mat_fun()
print(data)
mat_fun=Test_1("B_1")
data=mat_fun()
print(data)
mat_fun=Test_1("C_1")
data=mat_fun()
print(data)
def B_12(type):
    if type=="cc":
        return  lambda n:n+n+n
    if type=="bb":
        return  lambda n:n+n
B_0=B_12("cc")
print(B_0("cc"))
B_0=B_12("bb")
print(B_0("bb"))
