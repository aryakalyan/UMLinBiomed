import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram

# Step 1: Load the dataset
url = "https://raw.githubusercontent.com/aryakalyan/UMLinBiomed/8b2adaec1676d475ed3f1563a116aac4d9124aca/CellLines_52samples.txt"

# Read the dataset while skipping the 'Group' row but keeping column headers
df = pd.read_csv(url, sep="\t", index_col=0)

# Extract the subtype information (row 2)
subtypes = df.iloc[0, :]  # First row contains subtype info
df = df.iloc[1:, :]  # Remove the 'Group' row

# Convert gene expression values to numeric
df = df.apply(pd.to_numeric)

# Step 2: Perform hierarchical clustering using Ward's method
Z = linkage(df.T, method="ward", metric="euclidean")  # Ward's linkage with Euclidean distance

# Step 3: Plot the dendrogram
plt.figure(figsize=(14, 7))
dendrogram(Z, labels=df.columns, leaf_rotation=90, leaf_font_size=8)
plt.title("Cluster Dendrogram")
plt.xlabel("Cell Lines")
plt.ylabel("Height (Euclidean Distance)")
plt.show()

# Step 4: Plot a clustered heatmap with subtype annotations
# Create a color palette for subtypes
unique_subtypes = subtypes.unique()
subtype_colors = dict(zip(unique_subtypes, sns.color_palette("Set2", len(unique_subtypes))))
row_colors = subtypes.map(subtype_colors)  # Map colors to cell lines

# Plot heatmap
sns.clustermap(df.T, row_cluster=True, col_cluster=False, cmap="viridis",
               row_colors=row_colors, figsize=(12, 8), method="ward")

plt.show()
