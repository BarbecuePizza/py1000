# 整型
print("\033[1;33;40m整型的属性情况：\033[0m")
inta = 12
print(type(inta))
# dir 列出属性
# print(dir(inta))
# print(inta.__doc__)
print(inta.bit_length())
print("*" * 40)

# 字符串
print("\033[1;33;40m字符串的属性情况：\033[0m")
stra = "python"
print(type(stra))
# print(dir(stra))
print(stra.lower())
print(stra.upper())
print(stra.split("t"))
print("*" * 40)

# 元组  元组中的值不能变化，列表可以
print("\033[1;33;40m元组的属性情况：\033[0m")
tuplea = ("tom","jerry")
# print(dir(tuplea))
print(type(tuplea))
print(tuplea.index("tom"))
print("*" * 40)

# 列表
print("\033[1;33;40m列表的属性情况：\033[0m")
lista = ["tom","jerry"]
# print(dir(lista))
print(type(lista))
lista.append("bob")
print(lista)
print("*" * 40)

# 字典
print("\033[1;33;40m字典的属性情况：\033[0m")
dicta = {"tom":"123","jerry":"456"}
print(type(dicta))
# print(dir(dicta))
print(dicta.keys())
print(dicta.values())
dicta["tom"] = "789"
print(dicta)
