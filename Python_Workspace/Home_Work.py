alist=input("Enter: ")
blist=alist.split()
blist = list(dict.fromkeys(blist))
blist.sort()
strlist=""
for list in blist:
    strlist+=list
    strlist+=" "
print(strlist)