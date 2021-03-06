import taichi as ti

@ti.kernel
def fill():
    for i in range(10): #parallelized
        x[i] += i

        s = 0
        for j in range(5):# Serialized
            s += j

        y[i] = s

@ti.kernel
def fill_3d():
    for i, j, k in ti.ndrange((3, 8), (1, 6), 9):
        x[i, j, k] = i + j+ k


#It is the loop at the outermost scope that gets parallelized, not the outermost loop.
@ti.kernel
def foo():
    for i in range(10): #parallelized
        pass

@ti.kernel
def bar(k: ti.i32):
    if k > 42:
        for i in range(10): #serial
            pass
