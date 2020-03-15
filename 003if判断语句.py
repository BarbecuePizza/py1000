# # 要求用户名为tom 密码为123
# name = input("请输入你的名字：")
# password = input("请输入你的密码：")
# # and or not
# if (name == "tom") and (password == "123"):
#     print("欢迎"+name+"用户登录")
# else:
#     print("用户名密码错误请重新登陆！")


# =============================================

# 多分支判断
num = int(input("请输入成绩："))
if num >= 0 and num <=59:
    print("不及格")
elif num >= 60 and num <=69:
    print("及格")
elif num >= 70 and num <=79:
    print("良好")
elif num >= 80 and num <=100:
    print("优秀")
else:
    print("请输入1到100以内的成绩")
