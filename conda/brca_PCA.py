#!/usr/bin/env/python3

import matplotlib
matplotlib.use('Agg')
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# load breast cancer diagnostics dataset and select cols of interest
brca_cols = ['mean radius', 'mean texture', 'mean perimeter', 'mean area',
       'mean smoothness', 'mean compactness', 'mean concavity',
       'mean concave points', 'mean symmetry', 'mean fractal dimension']

brca = datasets.load_breast_cancer(as_frame=True)
brca_data = brca.data[brca_cols]

print(f"considered features: {brca_cols}") 

# center and scale data
sc = StandardScaler()
brca_scaled = sc.fit_transform(brca_data)

# perform PCA with two PCs
pca = PCA(n_components=2)
pca.fit(brca_scaled)

# project data on PCs
pca_space = pca.transform(brca_scaled)

# plot
plt.scatter(pca_space[:, 0], pca_space[:, 1],
           c=brca.target, cmap=plt.cm.coolwarm)
plt.xlabel("PC 1")
plt.ylabel("PC 2")
plt.savefig('brca_pcs_py.png')


