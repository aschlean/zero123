import numpy as np
import open3d as o3d
import os
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--steps", action="store", type=int, help="number of depth images to convert")
parser.add_argument("-p", "--path", action="store", type=str, help="path to depth images")
parser.add_argument("-o", "--onebyone", action="store_true", help="convert one depth image at a time")
parser.add_argument("-n", "--number", action="store", type=int, help="number of depth image to convert")
args = parser.parse_args()

def main():
    if args.path is None:
        npy_path = os.path.dirname(__file__)+'/experiments/exp_wild/depth/'
    else:
        npy_path = os.path.dirname(__file__)+args.path
    def convert_npy(npy_path, steps):
        np.set_printoptions(threshold=sys.maxsize)
        if not args.onebyone:
            for i in range(0, steps):
                print(i)
                np_image = np.load(npy_path+"step_"+str(i)+".npy")
                print(np_image.shape, np_image.dtype)
                print(np_image)
                o3d_image=o3d.geometry.Image(np_image)
                print(type(o3d_image))
                o3d.io.write_image(npy_path+"step_"+str(i)+".png", o3d_image)
        else:
            print(args.number)
            np_image = np.load(npy_path+"step_"+str(args.number)+".npy")
            print(np_image.shape, np_image.dtype)
            print(np_image)
            o3d_image=o3d.geometry.Image(np_image)
            print(type(o3d_image))
            o3d.io.write_image(npy_path+"step_"+str(args.number)+".png", o3d_image)
        return
    convert_npy(npy_path, args.steps)
    return

if __name__=="__main__":
    main()