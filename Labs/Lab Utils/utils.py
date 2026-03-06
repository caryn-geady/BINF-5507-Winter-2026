# IMPORTS THAT WOULD BE USED BY THE FUNCTIONS
from sklearn.impute import KNNImputer


# LIST OF FUNCTIONS BELOW HERE
def testing():
    print("This is a test function. Let's see if the updates stick!")
    

"""
Notes/scrap for the clean_nsclc_rna function

Possible name-pair args for my function:
- threshold to remove columns with missing data
- number of neightbours for the KNN Imputer method
Mandatory args:
- rna  

"""    
  
def clean_nsclc_rna(data, threshold_to_remove_column=0.5, n_neighbors=5):
    
    """
    This function will take in the RNA sequencing data from the TCIA NSCLC dataset and return a cleaned dataset. First, we remove columns that are missing beyond the provded threshold of data. Second, we impute missing data using the KNNImputer functionality.
    
    Args:
    - data (pd.DataFrame): The RNA sequencing data to be cleaned (the expected data is specified). 
    - threshold_to_remove_column (float): The threshold for removing columns with missing data. Columns with a proportion of missing data greater than this threshold will be removed. Default is 0.5 (i.e., 50%).
    - n_neighbors (int): The number of neighbors to use for KNN imputation. Default is 5. This means that the imputation will be based on the 5 nearest neighbors in the feature space.   
    
    Returns:
    pd.DataFrame: The cleaned version of the input RNA sequencing data.
    pd.Series: The 'Unnamed: 0' column from the original RNA sequencing data, which contains the unique identifiers for each sample (usubjid).
    """
    
    # 1. Remove columns that are missing TOO MUCH data
    cols_to_drop = data.columns[data.isnull().mean() > threshold_to_remove_column]
    data.drop(columns=cols_to_drop, inplace=True)
    
    # 2. Impute missing values using KNN imputation (why is this a good choice for imputation?)
    usubjid_data = data.copy()['Unnamed: 0']
    sequencing_no_usubjid = data.drop(columns=['Unnamed: 0'], axis=1)

    imputer = KNNImputer(n_neighbors=n_neighbors)
    cleaned_data = imputer.fit_transform(sequencing_no_usubjid)
    
    return cleaned_data, usubjid_data