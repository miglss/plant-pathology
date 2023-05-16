import os
import pandas
import numpy
import cv2

def get_images_shape(dir_path):
    """
    function to get all images height/width for future EDA 
    """
    height = []
    width = []
    for filename in os.listdir(dir_path):
        img_path = os.path.join(dir_path, filename) # get img path

        img = cv2.imread(img_path) # read img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        #img shape is (H,W,C)
        height.append(img.shape[0]) # append image height
        width.append(img.shape[1]) # append image width
    return height, width

def preprocess_csv(csv):
    labels = []
    for i in range(len(csv)):
        if csv.iloc[i, :]["healthy"] == 1:
            labels.append(0)
        elif csv.iloc[i, :]["multiple_diseases"] == 1:
            labels.append(1)
        elif csv.iloc[i, :]["rust"] == 1:
            labels.append(2)
        elif csv.iloc[i, :]["scab"] == 1:
            labels.append(3)
    csv.drop(["healthy", "multiple_diseases", "rust", "scab"], axis = 1, inplace = True)
    csv["label"] = labels
    return csv