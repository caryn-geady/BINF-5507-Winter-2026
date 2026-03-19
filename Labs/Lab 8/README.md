# Lab 8: Radiomics and Machine Learning for Imaging 🧠🩻

Welcome to Lab 8! In this lab, you'll move from raw medical imaging data to machine learning-ready features, then use those features for both survival and classification tasks.

## What's in This Lab?

- **Lab8.ipynb** - Jupyter notebook with guided exercises
- **Imaging Data/** - Example CT/PET DICOM and NIfTI image/mask files
- **NSCLC Dataset/** - Clinical and pre-extracted radiomics feature tables
- **Graphics/** - Figures used in lab overview and discussion

## What You'll Learn

1. **DICOM Handling** - Load and inspect CT/PET DICOM metadata and image arrays
2. **NIfTI Handling** - Load 3D image volumes and segmentation masks
3. **Radiomics Feature Extraction** - Use PyRadiomics to quantify image characteristics
4. **Survival Modeling** - Build a Random Survival Forest from radiomics features
5. **Classification Modeling** - Build a logistic regression classifier for clinical targets

## Getting Started

### Step 1: Open the Notebook
```bash
jupyter notebook Lab8.ipynb
```

### Step 2: Work Through the Sections
The notebook is organized into two major parts:

#### Part 1: Going from Unstructured Data to Structured Data

**(1) DICOM Loading and Handling**
- Read CT and PET scans with `pydicom`
- Inspect metadata fields (modality, spacing, acquisition details)
- Visualize and compare image slices

**(2) NIfTI Loading and Handling**
- Read 3D image volumes and masks with `nibabel`
- Explore dimensions, voxel spacing, and data types
- Examine image/mask intensity patterns

**(3) Radiomics Feature Extraction**
- Use `RadiomicsFeatureExtractor` from `pyradiomics`
- Compare default extraction settings with parameterized workflows
- Inspect extracted shape, first-order, and texture features

#### Part 2: Using the Structured Data for ML

**(4) Building Survival and Classification Models**
- Align clinical and radiomics records across patients
- Build survival targets (`event`, `time`) for `sksurv`
- Train a `RandomSurvivalForest` and evaluate via concordance index
- Train a logistic regression classifier and evaluate with accuracy/AP

## Key Concepts

- **Unstructured vs Structured Data** - Converting imaging data into analyzable tabular features
- **Radiomics** - Quantitative descriptors of intensity, shape, and texture
- **Segmentation Masking** - Restricting feature extraction to biologically relevant regions
- **Survival vs Classification Tasks** - Different targets, metrics, and model families
- **Data Leakage** - Importance of preprocessing only within training folds/pipelines

## Key Libraries

| Library | Usage |
|---------|-------|
| `pydicom` | DICOM loading, metadata inspection |
| `nibabel` | NIfTI image/mask I/O |
| `pyradiomics` | Feature extraction from images and masks |
| `scikit-survival` (`sksurv`) | Survival target formatting and survival modeling |
| `scikit-learn` | Preprocessing pipelines, classification, evaluation |
| `pandas` / `numpy` | Data handling and numerical operations |

## Tips for Success

1. Verify image-mask alignment before feature extraction
2. Keep preprocessing steps inside a model pipeline to reduce leakage risk
3. Pay attention to class imbalance when interpreting classification metrics
4. Use concordance index for survival models rather than classification accuracy
5. Explore feature reduction (variance/correlation filtering, PCA, LASSO) to improve stability

Good luck! 🚀
