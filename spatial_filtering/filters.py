# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:29:54 2026

@author: rsalinas
"""

import numpy as np

from convolution import convolution_2D


def box_filter (
        image: np.ndarray,
        k_size : np.float32
        ) -> np.ndarray:
    kernel = np.ones((k_size, k_size))
    kernel = kernel / sum(kernel.ravel())
    
    filtered_image = convolution_2D(image, kernel)
    
    return filtered_image

def gaussian_filter (
        image: np.ndarray,
        k_size : np.float32,
        sigma : np.float32
        ) -> np.ndarray:

    k = k_size // 2
    x, y = np.meshgrid(np.arange(-k, k + 1), np.arange(-k, k + 1))

    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))  
    kernel = kernel / sum(kernel.ravel())
    
    filtered_image = convolution_2D(image, kernel)
    
    return filtered_image