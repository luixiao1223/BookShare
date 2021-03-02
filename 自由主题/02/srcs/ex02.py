import taichi as ti

@ti.kernel
def hello(i: ti.i32):
    a = 40
    print("hello world!", a+i)

hello(2)

@ti.kernel
def calc()-> ti.32:
    s = 0
    for i in range(10):
        s += i
    return s
