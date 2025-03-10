import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load dataset
url = "https://raw.githubusercontent.com/pine-bio-support/BioML2/main/CellLines_52samples_ExprData_Group.txt"
df = pd.read_csv(url, sep="\t", index_col=0)

# Extract Group labels and ensure correct mapping
group_labels = df.loc["Group"].copy()
df_numeric = df.drop(index="Group").apply(pd.to_numeric)

# Transpose for PCA (samples as rows, genes as columns)
df_transposed = df_numeric.T

# Standardize data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_transposed)

# Perform PCA (retain top 3 components)
pca = PCA(n_components=3)
principal_components = pca.fit_transform(data_scaled)

# Convert PCA results into a DataFrame
pca_df = pd.DataFrame(principal_components, columns=['PC1', 'PC2', 'PC3'], index=df_transposed.index)
pca_df["Group"] = group_labels.values

# Explained variance ratio
explained_variance = pca.explained_variance_ratio_ * 100

# Define color mapping
color_map = {
    "Normal-like": "blue",
    "Basal": "red",
    "Luminal": "green",
    "Claudin-low": "purple"
}

# Define PC combinations for 2D plots
pc_combinations = [("PC1", "PC2"), ("PC1", "PC3"), ("PC2", "PC3")]

# Generate and show 2D PCA scatter plots
for x_pc, y_pc in pc_combinations:
    fig = px.scatter(
        pca_df, x=x_pc, y=y_pc, color="Group",
        color_discrete_map=color_map,
        labels={x_pc: f"{x_pc} ({explained_variance[int(x_pc[-1]) - 1]:.2f}%)",
                y_pc: f"{y_pc} ({explained_variance[int(y_pc[-1]) - 1]:.2f}%)"},
        title=f"PCA of Cell Line Expression Data ({x_pc} vs {y_pc})",
        width=900, height=600
    )
    fig.show()

# 3D PCA Scatter Plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Assign colors based on groups
unique_groups = pca_df["Group"].unique()
colors = sns.color_palette("husl", len(unique_groups))
group_color_map = {group: colors[i] for i, group in enumerate(unique_groups)}

# Plot each sample in 3D
for group in unique_groups:
    subset = pca_df[pca_df["Group"] == group]
    ax.scatter(subset["PC1"], subset["PC2"], subset["PC3"], label=group, color=group_color_map[group])

ax.set_xlabel(f"PC1 ({explained_variance[0]:.2f}%)")
ax.set_ylabel(f"PC2 ({explained_variance[1]:.2f}%)")
ax.set_zlabel(f"PC3 ({explained_variance[2]:.2f}%)")
ax.set_title("3D PCA Plot of Cell Line Expression Data")
ax.legend()

# Adjust viewing angle
ax.view_init(elev=20, azim=135)

plt.show()
