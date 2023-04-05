import numpy as np
import open3d as o3d
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--steps", default=100, type=int, help="number of depth images to convert",
                    action="store_const")
args = parser.parse_args()
npy_path = os.path.dirname(__file__)+'/experiments/exp_wild/depth/'


def main():
    def convert_npy(npy_path, steps):
        np.set_printoptions(threshold=sys.maxsize)
        for i in range(0, steps):
            print(i)
            np_image = np.load(npy_path+"step_"+str(i)+".npy")
            print(np_image.shape, np_image.dtype)
            print(np_image)
            o3d_image=o3d.geometry.Image(np_image)
            print(type(o3d_image))
            o3d.io.write_image(npy_path+"step_"+str(i)+".png", o3d_image)
        return
    convert_npy(npy_path, args.steps)
    return

if __name__=="__main__":
    main()