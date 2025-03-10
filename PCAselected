import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load dataset
url = "https://raw.githubusercontent.com/pine-bio-support/BioML2/main/CellLines_52samples_ExprData_Group.txt"
df = pd.read_csv(url, sep="\t", index_col=0)

# Extract Group labels
group_labels = df.loc["Group"].copy()
df_numeric = df.drop(index="Group").apply(pd.to_numeric)

# Transpose for PCA (samples as rows, genes as columns)
df_transposed = df_numeric.T

# Standardize data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_transposed)

# Perform PCA (retain top 3 components)
pca = PCA(n_components=3)
pca.fit(data_scaled)

# Get PCA loadings (contributions of genes to PCs)
loadings = pd.DataFrame(pca.components_.T, index=df_numeric.index, columns=['PC1', 'PC2', 'PC3'])

# Select top 50 genes contributing most to PC1, PC2, and PC3
top_genes_pc1 = loadings['PC1'].abs().nlargest(50).index
top_genes_pc2 = loadings['PC2'].abs().nlargest(50).index
top_genes_pc3 = loadings['PC3'].abs().nlargest(50).index

# Combine selected genes (remove duplicates)
selected_genes = list(set(top_genes_pc1) | set(top_genes_pc2) | set(top_genes_pc3))

# Create new dataset with selected genes
selected_gene_data = df_numeric.loc[selected_genes]

# Add group labels back
selected_gene_data.loc["Group"] = group_labels

# Save to CSV
selected_gene_data.to_csv("PCA_Selected_Genes.csv")

# Display the new dataset
print(f"New dataset with {len(selected_genes)} PCA-selected genes created!")
print(selected_gene_data.head())
