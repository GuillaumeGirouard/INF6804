from pathlib import Path
import numpy as np 
import cv2 as cv
from skimage import io
from natsort import natsorted, ns


class dataloader:
    def __init__(self,path_frames = "./frames/",path_output_txt = "./"):
        self.path_frames = path_frames
        self.path_output_txt = path_output_txt
        self.input_data = [str(p) for p in Path( self.path_frames).glob('*.jpg')]
        self.input_data = natsorted(self.input_data, key=lambda y: y.lower())
        self.f = open(path_output_txt,'w')

    def load_input(self,i):
        return cv.imread(self.input_data[i])
    
    def load_result(self,index,results,benchmark_type = 'RESULT'):
        if(benchmark_type == 'RESULT'):
            for row in results:
                xmin = row[0]
                ymin = row[1]
                xmax = row[2]
                ymax = row[3]
                id = row[4]
                result = str(index) + " " + str(id) + " " + str(xmin) + " " + str(ymin) + " " + str(xmax-xmin) + " " + str(ymax-ymin)
                self.f.write(result+"\n")

        elif(benchmark_type == 'MOT'):
            for row in results:
                frame = index
                id = row[4]
                bb_left = row[0]
                bb_top = row[1]
                bb_width = row[2]-row[0]
                bb_height = row[3]-row[1]
                result = str(index) + ", " + str(id) + ", " + str(bb_left) + ", " + str(bb_top) + ", " + str(bb_width) + ", " + str(bb_height) + ", " + "1, -1, -1, -1"
                self.f.write(result+"\n")




# results = [[     1845.8,      448.91,      1919.9,      784.72,           7,          41,     0.25806],
#           [     1121.1,      216.52,        1492,       628.2,           6,          41,      0.4367]]

# data = dataloader("./frames/","./results.txt")
# image = data.load_input(0)
# data.load_result(1,results)
# print(image)

# MOT file format: <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <x>, <y>, <z>