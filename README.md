# UMLinBiomed
# PCA and H-clust BioML Applications in Breast Cancer Cell Lines 

This repository provides a Python-based workflow for application of UML in Biomedicine to identify distinguishing molecular subtypes of breast cancer cell lines. The analysis includes:
✔ Extracting expression datasets from a publication by Daemen, Anneleen et al., “Modeling precision treatment of breast cancer” (Genome Biology, 2013).
✔ Performing Dimentionality Reduction by PCA.  
✔ Performing Hierarchical clustering (H-Clust) on PCA selected cell line 

## 🚀 Features

🔹 Reads NACCESS ASA output files for protein, RNA, and complex.  
🔹 Identifies interface atoms and residues based on ASA differences.  
🔹 Calculates total interface area in Å².  
🔹 Generates CSV output files for further analysis.  
🔹 Creates a PyMOL script to visualize interface residues.

## 📂 Repository Structure

📦 protein-rna-interface-analysis
 ┣ 📂 data
 ┃ ┣ 📄 CellLines_52samples.txt
 ┃ ┣ 📄 PCA_Selected_Genes.csv
 ┣ 📂 scripts
 ┃ ┣ 📄 pca.py
 ┃ ┗ 📄 hclust.py
 ┃ ┗ 📄 PCAselected.py
 ┣ 📄 README.md
 ┣ 📄 LICENSE
 ┗ 📄 .gitignore


## 🛠 Installation & Usage

1️⃣ **Install dependencies**:

```bash
pip install -r requirements.txt


📜 License
🔹 This project is privately licensed. Unauthorized use, copying, or distribution is strictly prohibited.
For inquiries regarding permissions, please contact arya.dhokte@gmail.com.

💡 Contributions Welcome! Fork the repo, submit pull requests, or report issues. 🚀
