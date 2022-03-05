# import copy
# lst12=[[1,2]
#       ,[3,4]]
# lst13=copy.deepcopy(lst12)# 深层复制
# # lst13=copy.copy(lst12) # 浅层复制
# # lst13=lst12.copy() # 浅层复制
# lst13[0][0]="傻了吧"
# print("lst12=",lst12)
# print("lst13=",lst13)
# print("id(lst12)=",id(lst12))
# print("id(lst13)=",id(lst13))
# print("id(lst12[0])=",id(lst12[0]))
# print("id(lst13[0])=",id(lst13[0]))

# print(range(1,10))
# for i in range(1,10):#Tab 对齐
#     print(i)
# print("哈哈")

# type(range(1,10))

# for  i in range(1,11,2): # 1,3,...,9
#     print(i)

# for  i in range(100,10,-10):
#     print(i)

# seq=list(range(1,10))
# seq.append("哈哈")
# for  i in seq:
#     print(i)
# print(len(seq))#显示长度
# print(seq[1])# 显示第一个元素
# print(seq[-1]) 

#0+1+2+...+n
# def my_sum(n):
#     n=n
#     i=0
#     sum=0
#     while i<=n:
#         sum+=i
#         i+=1
#     return sum

# print(my_sum(10))


# def factorial(n):
#     if n<=1:
#         return 1
#     else:
#         return n*factorial(n-1)

# text='''

# \\textbf{自然数}：$0,1,2\\cdots$

# \\textbf{整数}:$\\cdots,-2,-1,0,1,2\\cdots$

# 整数运算:$\\pm,\\times,\\div$. $\\longdiv{144}{12}$

# \\textbf{分数}:$\\displaystyle \\frac{1}{2},\\frac{2}{3}$正分数,负分数统称分数.

# '''
# print(text)

# with open ('test.tex', 'w', encoding='utf-8') as f: # 好处在于 with 内部语句结束以后自动关闭文件。
#     f.write(text)

# print(f.closed) # 可以看到返回值是 True, 说明文件是关闭了的

# text1="早点下课, 睡觉！"
# with open("test.tex",'a',encoding='utf-8')  as f:# a append
#     f.write(text1)
# print(f.closed)

## 思考：怎么遍历某个目录下的所有的文件（包含子目录）？如何遍历其中的某一种（JPG）文件？

# 4 迭代器 (iterator)

# lst7=[3,6,9,2,5,8,1,4,7]
# it=iter(lst7)
# print("it:",it)
# print(next(it))
# print(next(it))
# for iterm in it:
#     print(iterm)
# print("----")
# for iterm in it:
#     print(iterm)

# lst=["hello","world","china"]
# it=iter(lst)
# i=0
# while True:
#     try: #  ------ 运行try里面的代码模块
#         m=next(it)
#         print(m)
#         i+=1
#     # except StopIteration: # 如果出现 StopIteration 异常，则运行下面的代码块
#     except: # 一旦出现异常则运行下面的代码块
#         print("i=",i)
#         break
#     # -----

# # 5  字典(Dictionary)

# 字典是另一种可变容器模型，且可存储任意类型对象。

# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 ,格式如下所示：

# d = {key1 : value1, key2 : value2 }

# 注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。

# 参见 https://www.cnblogs.com/wind-wang/p/6090708.html

# 对字典 counter 进行排序
# ```python
# counter_sorted = sorted(counter.items(), key=lambda value:value[1], reverse=True)
# ```

# score={
#     "Tom":66
#     ,"Jerry":99
#     ,"Donald":100
#     ,"Mickey":60
# }
# counter_sorted = sorted(score.items(), key=lambda value:value[1], reverse=True)
# print(counter_sorted)
# print("score:",score)
# score["Minnie"]="beauty"
# print(score["Tom"])
# print("score:",score)
# print("score.items():",score.items())
# print("length:",len(score))
# for item in score:
#     print(f"{item}:",score[item])

# for i in score.keys():
#     print(f"{i}:",score[i])   
    
# print("score.values():",score.values())
# print("list(score.values()):",list(score.values()))

# for i in range(len(score)):
#     print(score.popitem(),"\t",end="") #popitem 返回并删除字典中最后一对键值
#     print(score)

### 思考：怎么利用词典统计词频！！

# 6 集合

# set1 = {"apple", "banana", "cherry"}
# print(type(set1))
# print("set1=", set1)
# set2={1,2,3,"apple"}
# print(type(set2))
# print("set2=", set2)
# set3=set1 | set2
# print(type(set3))
# print("set1 | set2=", set3)
# print("set1 & set2=", set1 & set2)
# set1.add("dog")
# print("set1.add(\"dog\")=", set1)
# set1.discard("apple")
# print("set1.discard(\"apple\")=", set1)
# for item in set3:
#     print(item)

# set3=set((list(set3).sort()))
# for item in set3:
#     print(item)

# set4={1,2,3,4}

# for item in set4:
#     print(item)

# lst10 = list(set4)
# print(lst10)
# print("-------")
# lst5=list(set4)
# print("lst5 previous:",lst5)
# print(list.sort(lst5, reverse=True))
# print("lst5 current:",lst5)
# set5=set(lst5)
# for item in set5:
#     print(item)

# set6={4,3,2,1}
# for item in set6:
#     print(item)

# s1=set(["apple", "banana", "cherry"])
# s2={1,2,3,"apple"}
# s3=s1 | s2
# print("random pop:",s3.pop()) # 怎么我在jupyter里总是弹出 1 ？ 抓狂吧^_^
# This in-built function of Python helps to pop out elements from a set just like the principle used in the concept while implementing Stack. This method removes a top element from the set but not the random element and returns the removed element. 
# 
# We can verify this by printing the set before using the pop() method.
# print(s3)
# s3 |=s2
# print(s3)
# print("s1=",s1)
# print("random pop:",s3.pop()) 
# print('s1.intersection(s2):',s1.intersection(s2))
# print('s1.difference(s2):',s1.difference(s2))
# print('s1.symmetric_difference(s2):',s1.symmetric_difference(s2))
# s3.clear()
# print("s3:",s3)
# s4=frozenset(["tom","laoyang"])

# # 9 类 class
# 关于类的使用，参考

# https://www.runoob.com/python/python-object.html


# 关于class的magic method 的使用，参考
#   - https://blog.csdn.net/kaever/article/details/105507217
#   - https://www.oschina.net/translate/python-magicmethods
#   - https://zhuanlan.zhihu.com/p/52014166
#   - https://docs.python.org/3/reference/datamodel.html




# class Employee: # 类名采用大驼峰命名（首字母全部大写）
#     pass

# emp_1=Employee()
# emp_2=Employee()
# # print(emp_1)
# # print(emp_2)

# emp_1.first="Donald"
# emp_1.last="Duck"
# emp_1.pay=50000

# emp_2.first="Mickey"
# emp_2.last="Mouse"
# emp_2.pay=60000

# print(emp_1.pay)
# print(emp_2.pay)

# 把工作用类来实现

# class Employee: # 类名采用大驼峰命名（首字母全部大写）

#     # raise_mount=1.04

#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay

#     def full_name(self): # 省略 self 要出错
#         return f"{self.first} {self.last}"

#     # def apply_raise(self):
#     #     self.pay=int(self.pay*1.04) # 有些时候不是非要涨 4%, 也许是其他的数目，所以可以设置一个变量，比如设置一个整个类共享的变量
#         # self.pay=int(self.pay*Employee.raise_mount) # 直接用 raise_mount 会报错 

# emp_1=Employee("Donald","Duck",50000) # emp_1.full_name()
# emp_2=Employee("Mickey","Mouse",60000)

# print(emp_1.pay)
# print(emp_2.pay)

# print("emp_2.full_name():",emp_2.full_name())
# print("Employee.full_name(emp_2):",Employee.full_name(emp_2))

# # lst=[1,2,3,4]
# # lst.sort(reverse=True)
# list.sort(lst,reverse=True)
# print(lst)

# 添加加薪的功能

# class Employee: # 类名采用大驼峰命名（首字母全部大写）

#     raise_mount=1.04

#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay

#     def full_name(self): # 省略 self 要出错
#         return f"{self.first} {self.last}"

#     def apply_raise(self):
#         self.pay=int(self.pay*self.raise_mount) # 直接用 raise_mount 会报错 ,用Employee.raise_mount 好？还是 self.raise_mount 好？

# emp_1=Employee("Donald","Duck",50000)
# emp_2=Employee("Mickey","Mouse",60000)

# emp_1.raise_mount=1.05

# print("emp_1.__dict__:\n",emp_1.__dict__)

# print("Employee.raise_mount:",Employee.raise_mount)
# print("emp_1.raise_mount:",emp_1.raise_mount)
# print("emp_2.raise_mount:",emp_2.raise_mount)
# emp_1.apply_raise()
# print(emp_1.pay)

# class method
# 
# class Employee: # 类名采用大驼峰命名（首字母全部大写）

#     raise_mount=1.04

#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay

#     def full_name(self): # 省略 self 要出错
#         return f"{self.first} {self.last}"

#     def apply_raise(self):
#         self.pay=int(self.pay*self.raise_mount) # 直接用 raise_mount 会报错 ,用Employee.raise_mount 好？还是 self.raise_mount 好？
   
#     @classmethod
#     def set_raise_amt(cls,amount):
#        cls.raise_mount=amount

# emp_1=Employee("Donald","Duck",50000)
# emp_2=Employee("Mickey","Mouse",60000)

# # emp_1.raise_mount=1.06

# # Employee.set_raise_amt(1.05)

# # emp_1.set_raise_amt(1.05)

# # print("emp_1.__dict__:\n",emp_1.__dict__)

# print("Employee.raise_mount:",Employee.raise_mount)
# print("emp_1.raise_mount:",emp_1.raise_mount)
# print("emp_2.raise_mount:",emp_2.raise_mount)

# class method
# 
# class Employee: # 类名采用大驼峰命名（首字母全部大写）
#     num_of_emps=0
#     raise_mount=1.04

#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         # self.pay=int(pay) # 万一收到的是字符串格式的数字，好转化成整数
#         self.pay=pay
#         Employee.num_of_emps +=1

#     def full_name(self): # 省略 self 要出错
#         return f"{self.first} {self.last}"

#     def apply_raise(self):
#         self.pay=int(self.pay*Employee.raise_mount) # 直接用 raise_mount 会报错 ,用Employee.raise_mount 好？还是 self.raise_mount 好？
   
#     @classmethod
#     def set_raise_amt(cls,amount):
#        cls.raise_mount=amount

#     @classmethod
#     def from_string(cls,emp_str):
#         first,last,pay =emp_str.split("-") # 遇到 - 就拆开
#         return Employee(first,last,pay)

# emp_1=Employee.from_string("Donald-Duck-50000")
# emp_2=Employee.from_string("Mickey-Mouse-60000")

# # emp_1.raise_mount=1.06

# # Employee.set_raise_amt(1.05)

# # emp_1.set_raise_amt(1.05)

# # print("emp_1.__dict__:\n",emp_1.__dict__)

# print("Employee.raise_mount:",Employee.raise_mount)
# print("emp_1.raise_mount:",emp_1.raise_mount)
# print("emp_2.raise_mount:",emp_2.raise_mount)
# print(emp_1.pay)
# print(type(emp_1.pay))

# static mathod

class Employee: # 类名采用大驼峰命名（首字母全部大写）
    num_of_emps=0
    raise_mount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        # self.pay=int(pay) # 万一收到的是字符串格式的数字，好转化成整数
        self.pay=pay
        Employee.num_of_emps +=1

    def full_name(self): # 省略 self 要出错
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay=int(self.pay*Employee.raise_mount) # 直接用 raise_mount 会报错 ,用Employee.raise_mount 好？还是 self.raise_mount 好？
   
    @classmethod
    def set_raise_amt(cls,amount):
       cls.raise_mount=amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay =emp_str.split("-") # 遇到 - 就拆开
        return Employee(first,last,pay)
    
    @staticmethod # 不会对 class 里面的数据做任何操作
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

import datetime
# 关于datetime 的参考资料
# https://www.runoob.com/python/python-date-time.html
# https://blog.csdn.net/gty931008/article/details/80254806
# https://zhuanlan.zhihu.com/p/40013414


my_date=datetime.date(2022,2,27)
print(Employee.is_workday(my_date))
