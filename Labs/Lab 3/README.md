# Lab 3: Supervised Learning I - Regression Models 📊

Welcome to Lab 3! In this lab, you'll learn about supervised learning through various regression models. You'll explore how to predict both continuous and binary outcomes, and discover how regularization techniques can help prevent overfitting.

## What's in This Lab?

- **Lab3.ipynb** - Jupyter notebook with step-by-step exercises
- Interactive examples with visualization and model evaluation

## What You'll Learn

1. **Linear Regression** - Predict continuous outcomes with a straight line
2. **Polynomial Regression** - Fit curved relationships with higher-degree polynomials
3. **Logistic Regression** - Predict binary outcomes (yes/no, positive/negative)
4. **Regularization Techniques** - Ridge, Lasso, and ElasticNet to prevent overfitting

## Getting Started

### Step 1: Open the Notebook
```bash
jupyter notebook Lab3.ipynb
```

### Step 2: Work Through the Sections
The notebook is organized into major sections:

#### Part 1: Linear Regression for Continuous Outcomes
Predict continuous values using a simple linear model.
- Learn how the model fits a line to the data
- Understand Mean Squared Error (MSE) and R² score
- Explore how `test_size` affects model performance

#### Part 2: Polynomial Regression for Continuous Outcomes
Extend linear regression to capture curved relationships.
- Use `PolynomialFeatures` to create polynomial terms
- Compare degree 1 (linear) vs. degree 3 polynomials
- Discover how polynomial degree affects model fit

#### Part 3: Logistic Regression for Binary Outcomes
Predict binary outcomes (e.g., disease presence, click vs. no-click).
- Learn about probability predictions with sigmoid function
- Evaluate with ROC curves and Precision-Recall curves
- Handle imbalanced datasets
- Understand the `C` parameter and its effect

#### Part 4: Regularization Techniques
Prevent overfitting using Ridge, Lasso, and ElasticNet.
- **Ridge Regression** - Penalizes large coefficients
- **Lasso Regression** - Can set coefficients to zero (feature selection)
- **ElasticNet** - Combines Ridge and Lasso penalties

## Key Concepts

### Continuous vs. Binary Outcomes
- **Continuous**: Temperature, price, age (any real number)
  - Use: Linear or Polynomial Regression
- **Binary**: Yes/No, True/False, 0/1
  - Use: Logistic Regression

### Evaluation Metrics

**For Continuous Outcomes:**
- **R² Score**: How well the model explains variance (0-1, higher is better)
- **Mean Squared Error (MSE)**: Average squared difference (lower is better)

**For Binary Outcomes:**
- **Accuracy**: Percentage of correct predictions
- **ROC-AUC**: How well the model distinguishes classes (0.5-1.0, higher is better)
- **Precision & Recall**: Trade-off between false positives and false negatives

### Regularization

Prevents overfitting by adding a penalty to large coefficients:

- **Ridge (L2)**: Shrinks coefficients, keeps all features
- **Lasso (L1)**: Shrinks coefficients, can eliminate features
- **ElasticNet**: Combination of Ridge and Lasso

**Alpha parameter:**
- Low alpha → Less regularization, model closer to original
- High alpha → More regularization, more coefficients reduced

### Polynomial Regression

Convert linear features to higher-degree terms:
```
Original: X = [1, 2, 3]
Degree 2: X = [1, 1, 2, 4, 3, 9]  (includes 1, X, X²)
```

This allows the model to fit curves instead of just lines.

## Common Issues & Solutions

**Problem**: Model performance seems worse with higher-degree polynomials
- **Solution**: This might be overfitting! Try regularization or cross-validation
- **Tip**: Visualize the fit to see if the model is capturing real patterns or noise

**Problem**: ROC curve is close to 0.5 (no better than random)
- **Solution**: Your features might not be predictive, or the dataset is too imbalanced
- **Tip**: Check class distribution and consider feature engineering

**Problem**: Lasso sets many coefficients to zero
- **Solution**: This is feature selection! It means those features aren't important
- **Tip**: Try reducing alpha to keep more features

## Exploration Questions

1. How does changing `test_size` affect model performance?
2. What's the difference between degree 1, 2, and 3 polynomials on your data?
3. How does the `C` parameter in LogisticRegression affect predictions?
4. What happens when you increase `alpha` in Ridge/Lasso? What's the ideal value?
5. When would Lasso be better than Ridge for your problem?

## Challenge Tasks

1. **Try ElasticNet** - It combines Ridge and Lasso. How does it compare?
2. **Feature Scaling** - Scale your features first. How does this affect linear/logistic regression?
3. **Hyperparameter Tuning** - Test multiple alpha values. Which gives the best R² or ROC-AUC?
4. **Custom Data** - Generate your own dataset with interactions. Can polynomial regression capture them?

## Additional Resources

- [Scikit-learn Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [Understanding ROC Curves](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)
- [Ridge vs. Lasso Regression](https://towardsdatascience.com/ridge-vs-lasso-regression-a-head-to-head-comparison-1ba63f7ae3d)
- [Polynomial Features](https://scikit-learn.org/stable/modules/preprocessing.html#polynomial-features)

## Next Steps

After completing this lab, you'll understand:
- When to use linear vs. polynomial vs. logistic regression
- How to evaluate regression models
- How regularization prevents overfitting
- The importance of hyperparameter tuning

Ready to build your first regression models? Let's go! 🚀
