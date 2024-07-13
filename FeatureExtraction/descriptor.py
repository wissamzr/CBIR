from skimage.feature import graycomatrix, graycoprops
from BiT import bio_taxo
import cv2
import numpy as np

def glcm(image_path):
    data = cv2.imread(image_path, 0)
    co_matrix = graycomatrix(data, [1], [np.pi/4], None,symmetric=False, normed=False )
    dissimilarity = graycoprops(co_matrix, 'dissimilarity')[0, 0]
    cont = graycoprops(co_matrix, 'contrast')[0, 0]
    corr = graycoprops(co_matrix, 'correlation')[0, 0]
    ener = graycoprops(co_matrix, 'energy')[0, 0]
    asm = graycoprops(co_matrix, 'ASM')[0, 0]
    homo = graycoprops(co_matrix, 'homogeneity')[0, 0]
    return [dissimilarity, cont, corr, ener, asm, homo]

def bitdesc(image_path):
    data = cv2.imread(image_path, 0)
    return bio_taxo(data)