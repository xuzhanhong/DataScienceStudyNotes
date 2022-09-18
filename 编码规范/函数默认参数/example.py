# 【反例】
def f(a, lst=[]):
    lst.append(a)
    return lst
