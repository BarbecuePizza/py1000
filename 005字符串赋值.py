"""
ans = input("您是否喜欢喝咖啡yes/no:")

if ans == "yes":
    print("制作咖啡")
elif ans == "no":
    print("随时恭候")
"""
# 字符串变量中所包含的索引值
astr = "python"
print(astr[0:2]) #变量[角标的起始位置 ：角标的结束位置]
print(astr[0:8])
print(astr[0:8:2]) #变量[角标的起始位置 ：角标的结束位置 : 步长值]
print(astr[-2])
print(astr[-1:-7:-1]) #反向取值
print(astr[:])
print(astr[::-1])


# if "p" in astr :
#     print("yes")
