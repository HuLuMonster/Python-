str1  = "HelloWorld!"
print(str1)
#定义字典
my_dict1 = {"邓翔戈": 389,"王品越": 390}
#定义空字典的两种方法
my_dict2 = {}
my_dict3 = dict()
print(my_dict1)
print(my_dict2)
print(my_dict3)
#字典不能存放重复的关键字key 不可以使用下标索引 只能使用key值来找value值
my_dict1 = {"邓翔戈": 389,"王品越": 390,"邓翔戈": 391,"王品越": 392}
print(my_dict1)
score = my_dict1["邓翔戈"]
print(score)
#字典可以嵌套
my_dict4 = {"考研初试":{
    "英语": 65,
    "数学": 125,
    "政治": 62,
    "专业课": 137
    }, "考研复试":{
    "英语": 85,
    "机试": 90,
    "面试": 90
    }
}
print(my_dict4)
print(my_dict4["考研复试"])
print(my_dict4["考研初试"]["数学"])
