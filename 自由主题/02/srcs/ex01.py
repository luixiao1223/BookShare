import taichi as ti

ti.init()

a = ti.field(dtype=ti.f32, shape=(42, 63)) # A tensor of 42x63 scalars
b = ti.Vector.field(3, dtype=ti.f32, shape=4) # A tensor of 4x 3D vectors
c = ti.Matrix.field(2, 2, dtype=ti.f32, shape=(3, 5))
# A tensor of 3x5 2x2 matrices

loss = ti.field(dtype=ti.f32, shape=())
# A (0-D) tensor of a single scalar

a[3, 4] = 1
print('a[3, 4] = ', a[3, 4])
# "a[3, 4] = 1.000000"

b[2] = [6, 7, 8]

loss[None] = 3
print(loss[None])
