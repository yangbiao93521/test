# -*- coding: utf-8 -*-
# 定义一个类
class Student(object):
    def name(self):
        print(f"面向对象里的方法")
# 类的使用
S1=Student()   #被称为对象/类的示例
#类的示例使用方法
S1.name()

# python面向对象编程
# 类是对客观世界中事物的抽象，而对象是类实例化后的实体
# 类的特点？
# 1.封装
# 2.继承
# 3.多态
# 类的组成？
# 1.属性
# 2.方法
# 类的书写格式？
# 1.class  关键字，定义一个类
# 2.类名：每个单词的的首字母大写
# 3.object:代表所有类的基类
# 4.面向过程、函数式代码的语句块
# 例如：
# class   类名(object):
#     语句块【面向过程、函数式】
# 类的属性

# 类
class Student(object):
    height = 170
    weight = 79
    def name(self,x):
        k="sda"   #局部变量（示例属性）
        print(f"有个人叫{x},他的身高是{self.height}cm,体重是{self.weight}")
S1=Student()
S1.name("哈哈哈")



class   Gilefriend(object):
    a="善解人意"
    b="孝敬老人"
    e="喜怒无常"
    f="可恶魔可天使"
    g="上得了厅堂下得了厨房"
    def   name(self,x):
        print(f"理想女朋友{x},必须有{self.a}和{self.b}的基本素质")
    def  tedian(self,y):
        print(f"附带{y},{self.e}和{self.f}的特点，最好还能{self.g}")

i=Gilefriend()
j=Gilefriend()
i.name("candy")
j.tedian("特点")

class  A(object):
    banji=1
    def __init__ (self,name,age):  #类的构造方法
        self.name=name
        self.age=age
        #如果定义了init方法，在创造对象的时候，必须传入参数
    def show(self):
        print(f"有个人叫{self.name},年龄是{self.age},班级是{self.banji}")
# 类的使用
a=A("张三",12)   #创造对象的过程
a.show()      #对象使用类的方法
class  A(object):
    #  类的属性
    banji = 1
    __sex="男"   #类的私有属性
    def __init__(self,name,age):    #类的构造方法
        #对象的属性
        self.name = name
        self.age = age
        self.__g="abc"    #对象的私有属性
    def  show(self):
        print(f"有个人的名字叫{self.name},年龄是{self.age},班级是{self.banji}")
#类的使用
a = A("张三",12)       #   创造对象的过程
a.show()                          #  对象使用类的方法   类的方法只有类的对象能使用

# 类的属性可以别哪些使用？
# 1.类的公有属性可以直接使用类名。属性名
# 2.类的私有属性在类的外部不能通过类名。属性名的方式使用
# 对象使用类的属性
# 1.对象公有属性，通过对象名。属性名的方式使用
# 2.对象私有属性,不能在类的外部通过对象名.属性名的方式使用
# 3.类名.对象的属性是不可以的
# 4.私有属性被定义之后，不希望被修改，可以通过：self.__变量名/self._类名__变量名的方式使用它





# 属性？
# 1.类的属性
#     私有
#     公有
# 2.实例属性
#     私有
#     公有
#
# 区分类的属性和对象属性
# 1.类的属性：定义在类的内部，方法的外部
# 2.对象的属性：定义在init方法的内部
#
# 公有和私有？
# 私有的是以双下划綫开头的：————sex="男"
# 公有的


class  A(object):
    banji = 1
    __sex="男"
    def __init__(self,name,age):

        self.name = name
        self.age = age
        self.__g="abc"
    def  show(self):
        k="asd"
        print(f"有个人的名字叫{self.name},年龄是{self.age},班级是{self.banji}")
        print(f"在类的方法内部使用类的公有属性{self.banji}"
              f"在类的方法内部使用类的私有属性{self.__sex},私有对象属性{self.__g},公有对象属性{self.name}")
a = A("张三",12)
a.show()

#
# 方法
# 1.静态方法
# 2.类方法
# 3.普通方法
# 4.私有方法
#
# 类的方法可以被哪些使用
# 1.类中的普通方法不能被类名。方法名的方式使用
# 2.对象名。普通方法名使用——>使用普通方法
# 3.对象名。类方法名使用——>使用类方法
# 4.对象名。静态方法名——>使用静态方法
# 5.私有方法不可以在类的外部使用
# 6.静态方法，类方法可以使用  类名.类方法名/静态方法名
class  A(object):
    banji = 1
    __sex="男"
    def __init__(self,name,age):

        self.name = name
        self.age = age
        self.__g="abc"
    def  show(self):   #普通方法
        k="asd"
        print(f"有个人的名字叫{self.name},年龄是{self.age},班级是{self.banji}")
        print(f"在类的方法内部使用类的公有属性{self.banji}"
              f"在类的方法内部使用类的私有属性{self.__sex},私有对象属性{self.__g},公有对象属性{self.name}")
    @staticmethod  #将普通方法转变成静态方法
    def  foo():    #静态方法———>类似于函数
        print("类的静态方法")
    @classmethod   #将普通方法转变成类方法
    def koo(cls):   #类方法  cls和self  的作用一致，只不过换了个名字而已
        print("类的类方法")
    def __siyou(self):
        print("私有方法")
    def yu(self):
        #在类的方法中使用其他方法的方式
        #self.方法名(虽有的方法名）
        self.__siyou()
        self.koo()
        self.foo()
a = A("张三",12)
a.show()
a.foo()
A.koo()
a.yu()
a.__siyou()  #不可以使用


# 继承
class   B(object):
    def  __init__(self,name,age):
        self.name=name
        self.age=age
    def  say(self):
        print(f"B类中的普通方法")
        return self.name,self.age
#（类名）——>继承于"类名"类，只要被继承类有的，继承类都可以直接使用
class   C(B):
    def  talk(self):
        res=super().say()  #super只会往上找
        print(res)
#多态——>重写方法
        def say(self):
            print("C类里的方法")
c1=C("张三",99)
c1.talk()
c1.say()

# 多态：继承类对被继承类的方法的重写（方法名一样，语句块不一样）
# 如何在多态之后使用被继承类的方法？
# 使用supper().被继承类的方法








class Ren(object):
    role = "ren"
    def __init__(self,name,gjl,sm,money):  # 名字  攻击力  生命  钱
        self.name = name
        self.gjl = gjl
        self.sm = sm
        self.money = money

    def gj(self,dog):
        dog.sm -= self.gjl

class Dog(object):
    role = "dog"
    def __init__(self,name,dx,gjl,sm):  # 名字 大小  攻击力  生命
        self.name = name
        self.dx = dx
        self.gjl = gjl
        self.sm = sm

    def yr(self,ren):
        ren.sm -= self.gjl

class Bq(object):
    def __init__(self,name,dao,gj,sml):  # 名字  刀  攻击  生命力
        self.name = name
        self.dao = dao
        self.gj = gj
        self.sml = sml
    def update(self,obj):        #  obj人
        obj.money -= self.dao    #  人的钱 -  武器价钱
        obj.gjl += self.gj       #  人的攻击加武器攻击
        obj.sm += self.sml       #  人的生命加武器生命
    def kan(self,obj):
        obj.sm -= 500

wuqi = Bq("长矛",200,6,1000)
r = Ren("孙岗祥",10,1000,600)
gou = Dog("里紧迫","大",10,1000)

if r.money > wuqi.dao:
    wuqi.update(r)
    r.bq = wuqi
print(r.money,gou.sm,r.gjl)

print(gou.sm)
print(r.sm)
r.gj(gou)
print(gou.sm)
gou.yr(r)
print(r.sm)
r.bq.kan(gou)
print(gou.sm)
