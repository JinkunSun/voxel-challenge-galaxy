from numpy import vectorize
from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=2)
scene.set_floor(-63, (1.0, 1.0, 1.0))
scene.set_background_color((0.5, 0.5, 0.4))

@ti.func
def create_cube(length:int):
    for i,j,k in ti.ndrange(length,length,length):
        for x,y,z in ti.ndrange(2,2,2):
            scene.set_voxel(vec3((1-2*x)*i,length,(1-2*z)*k),2,vec3(1,1,1))
@ti.func
def create_cricle(radius:int, centre_x,centre_y,centre_z:int,r,g,b:float):
    for i,j,k in ti.ndrange((-radius,radius),(-radius,radius),(-radius,radius)):
        if i*i+j*j+k*k <= radius*radius:
            scene.set_voxel(vec3(i+centre_x,j+centre_y,k+centre_z),1,vec3(r,g,b))                  
@ti.func
def create_ring(radius_max,radius_min:int, centre_x,centre_z:int,r=1.0,g=1.0,b=1.0):
    for i,j in ti.ndrange((-radius_max,radius_max),(-radius_max,radius_max)):
        if i*i+j*j <= radius_max*radius_max and i*i+j*j >=radius_min*radius_min:
            scene.set_voxel(vec3(i+centre_x,0,j+centre_z),1,vec3(r,g,b))
@ti.kernel
def initialize_voxels():
    create_cube(63)
    create_cricle(13,0,0,0, 1,0.647,0)
    create_cricle(8,48,0,-25, 0.71,0.71,0.71)
    create_cricle(4,0,0,35, 0.3,0.25,0.25)
    create_cricle(5,20,0,0, 0,0.75,1)
    create_ring(20,19,0,0)
    create_ring(35,34,0,0)
    create_ring(55,54,0,0)
    create_ring(13,11,48,-25 ,0.804,0.586,0.484)
initialize_voxels()
scene.finish()