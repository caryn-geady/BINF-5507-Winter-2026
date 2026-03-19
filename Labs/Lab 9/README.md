# Lab 9: Pharmacogenomic Analysis 💊🧬

Welcome to Lab 9! In this lab, you'll analyze pharmacogenomic screening data to study how experimental and biological factors relate to drug sensitivity in breast cancer cell lines.

## What's in This Lab?

- **Lab9.ipynb** - Jupyter notebook with guided workflow and model scaffolding
- **GDSC_DATASET.csv** - Semi-curated dataset from Genomics of Drug Sensitivity in Cancer (GDSC)
- **dose-response-curve.png** - Reference figure for interpreting IC50
- **PharmacoGxTutorial-optional.Rmd** - Optional R-based supplementary tutorial

## What You'll Learn

1. **Drug Response Fundamentals** - Interpret IC50 and dose-response relationships
2. **Data Processing & Exploration** - Filter, summarize, and visualize GDSC data
3. **Feature Engineering** - Encode categorical genomic/experimental variables
4. **Pairwise Reformulation** - Convert continuous IC50 comparisons into binary classification labels
5. **Modeling & Evaluation** - Compare baseline and more advanced classifiers

## Getting Started

### Step 1: Open the Notebook
```bash
jupyter notebook Lab9.ipynb
```

### Step 2: Work Through the Sections
The notebook is organized into three major sections:

#### Part 1: Data Processing / Exploration
- Load and clean the GDSC table
- Focus on BRCA (breast cancer) experiments
- Visualize IC50 distributions and inspect available metadata

#### Part 2: Framing the ML Question / Formatting Data
- Define feature matrix `X` and target `y` (`ln_ic50`)
- Encode binary/ternary categorical predictors
- One-hot encode drug target pathways
- Generate pairwise differences to build a binary learning task

#### Part 3: Implementing ML Models
- Use logistic regression as a baseline
- Compare with a stronger model (e.g., random forest)
- Evaluate performance and inspect influential features

## Key Concepts

- **IC50** - Concentration needed to inhibit 50% viability
- **Pharmacogenomics** - Linking molecular features to drug response
- **Pairwise Learning** - Predicting relative response between two experiments
- **Categorical Encoding** - Mapping non-numeric biological descriptors to model inputs
- **Model Comparison** - Balancing accuracy, interpretability, and robustness

## Key Libraries

| Library | Usage |
|---------|-------|
| `pandas` / `numpy` | Data wrangling and numeric operations |
| `matplotlib` / `seaborn` | Distribution plots and exploratory visualizations |
| `scikit-learn` | Train/test splits, classification models, evaluation |

## Tips for Success

1. Inspect class balance after pairwise label generation
2. Use fixed random seeds to support reproducible comparisons
3. Compare multiple metrics (accuracy, precision/recall, F1, PR-AUC) when classes are imbalanced
4. Examine feature importance/coefficient signs for biological plausibility
5. Test robustness by varying split seeds and hyperparameters

Good luck! 🚀
