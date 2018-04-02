#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 13:05:09 2018
This python file will detect an objet present in a video. 
@author: abhishek
"""
import torch
from torch.autograd import Variable
import cv2
from data import BaseTransform, VOC_CLASSES as labelmap
from ssd import build_ssd
import imageio

#defining the function that will do the detection.
def detect(frame, net, transform):
    height, width = frame.shape[:2]
    #apply the transform transformation
    frame_t = transform(frame)[0] # we are interested in the first element. 
    x = torch.from_numpy(frame_t).permute(2,0,1) # from RBG to GRB
    x = Variable(x.unsqueeze(0)) #first dimension that we are adding to the batch that we will feed to pytorch
    y = net(x) #give the tensor to 
    detections = y.data # a new tensor and give the data to 
    scale = torch.Tensor([width, height, width, height]) #scale will be a torch tensor
    #detections tensor containt 4 elements.
    # detections = [batch, number of classes, Number of occurance of the class, Touple of 5 elements. (score,x0,y0,x1,y1)]
    for i in range(detections.size(1)):
        j = 0
        while detections[0, i, j, 0] > 0.6: #score of occurance j of class i > 0.6
            pt = (detections[0, i, j, 1:] * scale)#the last element means from 1 to last element
            cv2.rectangle(frame, (int(pt[0]), int(pt[1])), (int([pt2]), int(pt[3])), (255,0,0), 2) #the 4 coordinates to draw a sqare.
            #print the lable to detect 
            cv2.putText(frame, labelmap[i - 1], (int(pt[0]), int(pt[1])), cv2.FONT_HERSHEY_COMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
            # we must increament the iterative variable
            j += 1
    return frame

#creating the SSD neural network
net = build_ssd('test')#just pass the face, trained or untrained, a ssd neural network is created
net.load_state_dict(torch.load('ssd300_mAP_77.43_v2.pth', map_location = lambda storage, loc: storage)) #torch.load 
    
#creating the transformation