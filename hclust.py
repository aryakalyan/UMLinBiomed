import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram

# Step 1: Load the dataset
file_path = "PCA_Selected_Genes.csv"  # Ensure correct file path
df = pd.read_csv(file_path, index_col=0)  # Read CSV (comma-separated)

# Extract the subtype information (Group row)
subtypes = df.loc["Group"].copy()  # Extract subtype labels
df = df.drop(index="Group")  # Remove the Group row

# Convert gene expression values to numeric
df = df.apply(pd.to_numeric)

# Step 2: Perform hierarchical clustering using Ward's method
Z = linkage(df.T, method="ward", metric="euclidean")  # Ward's linkage with Euclidean distance

# Step 3: Plot the dendrogram
plt.figure(figsize=(14, 7))
dendrogram(Z, labels=df.columns, leaf_rotation=90, leaf_font_size=8)
plt.title("Cluster Dendrogram of Cell Lines")
plt.xlabel("Cell Lines")
plt.ylabel("Height (Euclidean Distance)")
plt.show()

# Step 4: Clustered heatmap with subtype annotations
# Create a color palette for subtypes
unique_subtypes = subtypes.unique()
subtype_colors = dict(zip(unique_subtypes, sns.color_palette("Set2", len(unique_subtypes))))
row_colors = subtypes.map(subtype_colors)  # Map colors to cell lines

# Ensure row_colors is a DataFrame for sns.clustermap
row_colors = pd.DataFrame(row_colors)

# Plot heatmap
sns.clustermap(df.T, row_cluster=True, col_cluster=False, cmap="viridis",
               row_colors=row_colors, figsize=(12, 8), method="ward")

plt.show()
