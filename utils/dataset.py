import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Cash:
    def __init__(self):
        pass


def set_cash(total=None):
    if total is None:
        total = ['lfw_allnames.csv', 'lfw_readme.csv', 'matchpairsDevTrain.csv', 'matchpairsDevTest.csv',
                 'mismatchpairsDevTest.csv', 'mismatchpairsDevTrain.csv',
                 'pairs.csv', 'people.csv', 'peopleDevTrain.csv', 'peopleDevTest.csv']
    for t in total:
        setattr(Cash, f'{t.replace(".csv", "")}', pd.read_csv(f'../data/data-i/{t}'))


def read_images(name: str, path: [str, os.PathLike] = '../data/data-i/lfw-deepfunneled/lfw-deepfunneled/'):
    pt = os.path.join(path, name)
    if not os.path.exists(pt): raise FileExistsError
    files = [os.path.join(pt, s) for s in os.listdir(pt) if os.path.exists(os.path.join(pt, s))]
    images = []
    for f in files:
        images.append(plt.imread(f))
    return np.array(images)


def load_images_from_path(path):
    all_images = {}
    for p in path:
        all_images[f'{p}'] = read_images(p)
    return all_images


