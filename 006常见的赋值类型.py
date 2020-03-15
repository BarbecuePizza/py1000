# 变量赋值字符串 数字 列表 元组 字典

# 列表 特点 [] 中括号中可以写入不同类型的数据， 每个值直接用逗号分隔支持角标取值
alist = ["tom" , "jerry"]
print(alist[1])

# 元组 特点 ()
atuple = ("tom" , "jerry")
print(atuple[0])

# 字典 {} 字典没有索引值 键值对来取值  {"key":"value"}
username = input("username:")
password = input("password:")
adict = {"tom" : "123","jerry": "456"}
# print(adict["tom"],adict["jerry"])
if username in adict and password == adict[username]:
    print("weclome   " +username+ "   login!")
else:
    print("error!!")
