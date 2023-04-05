import numpy as np
import open3d as o3d
import os

npy_path = os.path.dirname(__file__)+'/experiments/exp_wild/depth'

def main():
    def convert_npy(npy_path):
        for i in range(0, 99):
            print(i)
            np_image = np.array(o3d.io.read_image(npy_path+"step_"+str(i)+".npy"))
            print(np_image)
            print(type(np_image))
            o3d_image=o3d.geometry.Image(np_image)
            print(type(o3d_image))
            o3d.io.write_image(npy_path+"step"+str(i)+".png", o3d_image)
        return
    convert_npy(npy_path)
    return

if __name__=="__main__":
    main()