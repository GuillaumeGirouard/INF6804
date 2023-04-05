from pathlib import Path
import numpy as np 
import cv2 as cv
from skimage import io
from natsort import natsorted, ns


class dataloader:
    def __init__(self,path_frames = "./frames/",path_output_txt = "./"):
        self.path_frames = path_frames
        self.input_data = [str(p) for p in Path( self.path_frames).glob('*.jpg')]
        self.input_data = natsorted(self.input_data, key=lambda y: y.lower())
        self.f = open(path_output_txt,'w')

    def load_input(self,i):
        return cv.imread(self.input_data[i])
    
    def load_result(self,index,results):
        for row in results:
            #if(row[5] == 41):
                xmin = round(row[0])
                ymin = round(row[1])
                xmax = round(row[2])
                ymax = round(row[3])
                id = row[4]
                result = str(index) + " " + str(id) + " " + str(xmin) + " " + str(ymin) + " " + str(xmax-xmin) + " " + str(ymax-ymin)
                self.f.write(result+"\n")
            else:
                pass
        self.f.close()



# results = [[     1845.8,      448.91,      1919.9,      784.72,           7,          41,     0.25806],
#           [     1121.1,      216.52,        1492,       628.2,           6,          41,      0.4367]]

# data = dataloader("./frames/","./results.txt")
# image = data.load_input(0)
# data.load_result(1,results)
# print(image)
