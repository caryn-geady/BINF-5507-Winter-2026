# Lab 7: Survival Modeling ⏳

Welcome to Lab 7! In this lab, you'll explore survival analysis techniques for modeling time-to-event data. These methods are widely used in clinical research to understand patient outcomes, disease progression, and risk factors.

## What's in This Lab?

- **Lab7.ipynb** - Jupyter notebook with step-by-step exercises
- **NSCLC Data** - Available via Lab 5's data folder (RNA-seq and clinical data)

## What You'll Learn

1. **Cox Regression** - Model hazard ratios using clinical covariates
2. **Regularized Cox Regression (LASSO)** - Handle high-dimensional data with L1/L2 penalties
3. **Random Survival Forest** - Non-parametric ensemble approach to survival modeling
4. **Kaplan-Meier Curve Analysis** - Visualize and compare survival probabilities over time
5. **Real-World Application** - Apply survival models to NSCLC Radiogenomics data

## Getting Started

### Step 1: Open the Notebook
```bash
jupyter notebook Lab7.ipynb
```

### Step 2: Work Through the Sections
The notebook is organized into three major sections:

#### Part 1: Survival Models

**1.1 Cox Regression**
Implement the Cox proportional hazards model using `lifelines`.
- Fit a semi-parametric model to estimate hazard ratios
- Interpret covariate effects on survival outcomes
- Explore baseline estimation methods and model assumptions

**1.2 Lasso for Censored Data**
Apply L1-regularized Cox regression using `scikit-survival`.
- Use `CoxnetSurvivalAnalysis` with L1/L2 penalties
- Evaluate model performance with the concordance index (C-index)
- Investigate how regularization affects feature selection

**1.3 Random Survival Forest**
Build a non-parametric ensemble survival model.
- Train a `RandomSurvivalForest` on the WHAS500 dataset
- Compute and visualize permutation-based feature importances
- Compare performance and interpretability with Cox models

#### Part 2: Kaplan-Meier Curve Analysis
Estimate and visualize survival probabilities using the Kaplan-Meier method.
- Fit a `KaplanMeierFitter` to time-to-event data
- Plot survival curves and interpret confidence intervals
- Stratify curves by covariates and apply the log-rank test

#### Part 3: Dataset Usage
Apply survival modeling to real-world NSCLC data.
- Clean and preprocess RNA-seq data using shared lab utilities
- Engineer a survival outcome from clinical date columns
- Fit survival models to NSCLC patient data

## Key Concepts

- **Censoring** - Handling incomplete observations where the event has not yet occurred
- **Hazard Ratio** - Relative risk of an event occurring between groups
- **Concordance Index (C-index)** - Discrimination metric for survival models (analogous to AUC)
- **Proportional Hazards Assumption** - Core assumption of the Cox model
- **Feature Importance** - Identifying which covariates drive survival outcomes

## Key Libraries

| Library | Usage |
|---------|-------|
| `lifelines` | Cox regression, Kaplan-Meier estimation |
| `scikit-survival` (`sksurv`) | Regularized Cox, Random Survival Forest |
| `sklearn` | Train/test splitting, permutation importance |
| `pandas` / `numpy` | Data manipulation and preprocessing |

## Tips for Success

1. Always check the proportional hazards assumption when using Cox regression
2. The C-index ranges from 0.5 (random) to 1.0 (perfect) — values above 0.6 are generally considered useful
3. LASSO regularization can shrink irrelevant coefficients to zero, effectively performing feature selection
4. Kaplan-Meier curves are non-parametric — no assumptions about the underlying distribution are needed
5. When working with the NSCLC dataset, survival time must be derived from the date columns

Good luck! 🚀
