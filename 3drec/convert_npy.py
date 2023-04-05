import numpy as np
import open3d as o3d

npy_path = '../3drec/experiments/exp_wild/depth'

def convert_npy(npy_path):
    for i in range(0, 99):
        np_image = np.array(open3d.io.read_image(npy_path+"step"+str(i)+".npy"))
        o3d_image=o3d.geometry.Image(np_image)
        o3d.io.write_image(npy_path+"step"+str(i)+".png", o3d_image)