исходная_строка = "xxx uefdjaeyx ixas xoiek"
новая_строка = ""
for x in исходная_строка:
    if x == "x":
        новая_строка += "y"
    else:
        новая_строка += x
print(исходная_строка)
print(новая_строка)