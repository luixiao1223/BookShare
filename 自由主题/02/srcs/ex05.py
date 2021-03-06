import taichi as ti

ti.init(arch=ti.gpu)

n = 320
pixels = ti.field(dtype=ti.f32, shape=(n*2, n))

@ti.kernel
def paint(t: ti.f32):
    for i, j in pixels: # parallized over all pixels
        pixels[i, j] = i * 0.001 + j * 0.002 + t

paint(0.3)

