import taichi as ti

@ti.func
def triple(x):
    return x*3

@ti.kernel
def triple_array:
    for i in range(128):
        a[i] = triple(a[i])
