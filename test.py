# python 笔记
# list 有序集合 类似list
list = ['1', 'a']

# tuple  元组 类似数组
tuple = {1, 'a'}

#  dic  字典  类似map
dic = {'a': 1, 'b': 2}

#  set  无序不重复集合，过滤重复
set = ([1, 1, 2, 2, 3, 3])


# 函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


a = my_abs(2018 - 1966)
print(a)


# 可变参数用*表示，参数长度不一定
def my_test_more(*x):
    size = len(x)
    if size > 0:
        n = 0
        _sum = 0

        while n < size:
            _sum = _sum + int(x[n])
            n = n + 1

        return _sum
    else:
        return x


c = my_test_more(10, 35)
print(c)


# 关键字参数用**kw表示,该参数可选,kw 是dict  字典（类似map）
def my_test_muti(a, b, **kw):
    print('a', a, 'b', b, 'other{', kw, '}')
    return 0


city = my_test_muti(1, 2, c='Beijing', d='nanjing')

# 另一种写法
extra = {'city': 'Beijing', 'job': 'Engineer'}

city3 = my_test_muti(2, 3, **extra)


# 命名关键字参数 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

def my_test_muti2(a, b, *, job, adress):
    print('a', a, 'b', b, 'other{job', job, 'adress:', adress, '}')
    return 0


# 只接收city和job作为关键字参数。这种方式定义的函数如下：

city2 = my_test_muti2(1, 2, job='工人', adress='工厂')


#  参数组合在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数或关键字参数。数量不确定的参数只可存在一个
#  比如可变参数和关键字参数
#   必选参数、默认参数、可变参数、关键字参数
def f1(a, b, c=0, *d, **e):
    pass


#   必选参数、默认参数、命名关键字参数、关键字参数
def f2(a, b, c=0, *, d, **kw):
    pass

#   递归的尾递归写法：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

def fact_iter(num, product):
    if num == 1:
        return product
    else:
        # return n * fact(n - 1)  使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的
        # 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
        return fact_iter(num - 1, num * product)

