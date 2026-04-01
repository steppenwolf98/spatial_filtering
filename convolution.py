# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:54:19 2026

@author: rsalinas
"""

import numpy as np

def convolution_2D (
        image: np.ndarray,
        kernel: np.ndarray
        )-> np.ndarray : 
    # Get sizes
    img_h, img_w = image.shape
    k_h, k_w = kernel.shape
    
    # Flip kernel for convolution
    kernel = kernel[::-1, ::-1]
    
    # Padding size
    pad_h = k_h // 2
    pad_w = k_w // 2
    
    # add padding
    padded_img = np.zeros((img_h + 2*pad_h, img_w + 2*pad_w))
    padded_img[pad_h : img_h + pad_h, pad_w: img_w + pad_w] = image


    # Output image with same size
    output = np.zeros((img_h, img_w))
    
    # Convolution
    for i in range(img_h):
        for j in range(img_w):
            region = padded_img[i:i + k_h, j:j + k_w]
            output[i, j] = np.sum(region * kernel)
            
    return output




    