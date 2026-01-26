# Lab 2: Data Cleaning for Machine Learning 🧹

Welcome to Lab 2! In this lab, you'll learn how to clean and prepare messy data for machine learning. Real-world data is rarely perfect, so knowing how to handle missing values, encode categorical features, and scale data is essential.

## What's in This Lab?

- **Lab2.ipynb** - Jupyter notebook with step-by-step exercises
- **functionals.py** - Python functions for building a simple ML model
- **messy_data.csv** - Dataset with intentional issues for you to clean

## What You'll Learn

1. **Handling Missing Data** - Identify and deal with missing values
2. **Encoding Categorical Features** - Convert text categories to numbers
3. **Feature Scaling** - Standardize numeric features for better model performance
4. **Train/Test Splitting** - Split data properly to evaluate models
5. **Building a Simple Model** - Use logistic regression to make predictions

## Getting Started

### Step 1: Open the Notebook
```bash
jupyter notebook Lab2.ipynb
```

### Step 2: Work Through the Exercises
Follow along in the notebook. You'll:
- Load and explore the messy data
- Clean the data step by step
- Use the `simple_model()` function from `functionals.py`
- Experiment with different preprocessing options

### Step 3: Understand the `simple_model()` Function

The `simple_model()` function in `functionals.py` demonstrates a complete ML pipeline:

```python
simple_model(
    input_data,           # Your DataFrame
    split_data=True,      # Split into train/test sets?
    scale_data=False,     # Apply feature scaling?
    print_report=False    # Print detailed classification metrics?
)
```

**What it does:**
1. Removes columns with missing data
2. Separates features from target variable
3. One-hot encodes categorical features
4. Splits data into train/test sets (80/20)
5. Optionally scales features using StandardScaler
6. Trains a logistic regression model
7. Evaluates model performance

### Step 4: Experiment!

Try different combinations:
```python
# Basic model, no scaling
simple_model(df, split_data=True, scale_data=False)

# With feature scaling
simple_model(df, split_data=True, scale_data=True)

# With detailed report
simple_model(df, split_data=True, scale_data=True, print_report=True)
```

## Key Concepts

### Missing Data
- **Removing columns**: Simple but loses information
- **Imputation**: Fill missing values with mean, median, or mode
- **Impact**: Missing data can break ML models

### Categorical Encoding
- **One-hot encoding**: Convert categories like "red", "blue" to binary columns
- **Example**: `color_red=1, color_blue=0` for a red item
- **Why**: Most ML algorithms need numeric input

### Feature Scaling
- **StandardScaler**: Transform features to have mean=0 and std=1
- **Why**: Prevents features with large ranges from dominating the model
- **Example**: Age (0-100) vs. Income ($0-$1M) should be comparable

### Train/Test Split
- **Train set**: Used to fit the model (80% of data)
- **Test set**: Used to evaluate the model (20% of data)
- **Stratified split**: Maintains class balance in both sets

## Common Issues & Solutions

**Problem**: `KeyError` or missing columns
- **Solution**: Check that your data has the expected columns
- **Tip**: Use `df.columns` to see what's actually in your data

**Problem**: Model accuracy seems too good/bad
- **Solution**: Try with and without feature scaling
- **Tip**: Print the classification report to see detailed metrics

**Problem**: Warning about convergence
- **Solution**: The model might need more iterations or scaled features
- **Tip**: Try `scale_data=True`

## Challenge Questions

1. What happens to model accuracy when you scale the data?
2. Why do we use stratified splitting?
3. What would happen if we scaled the data BEFORE splitting?
4. How does one-hot encoding change the number of features?

## Additional Resources

- [Pandas documentation on missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Scikit-learn preprocessing guide](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Understanding classification reports](https://www.nb-data.com/p/breaking-down-the-classification)

## Next Steps

After completing this lab, you'll be ready to:
- Handle messy real-world datasets
- Prepare data for machine learning models
- Understand the importance of proper preprocessing
- Apply these techniques to your own projects

Happy coding! 🚀
