# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:04:34 2026

@author: rsalinas
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("spatial_filtering")
except PackageNotFoundError:
    __version__ = "unknown"

from spatial_filtrering.filters import (
    box_filter,
    gaussian_filter
)