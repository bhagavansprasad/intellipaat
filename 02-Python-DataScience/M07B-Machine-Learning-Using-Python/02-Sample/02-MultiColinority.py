import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
import numpy as np

def remove_multicollinearity(df, threshold=5.0):
    """
    Remove features from a DataFrame that have a Variance Inflation Factor (VIF)
    above a specified threshold, indicating multicollinearity.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the features.
    threshold (float): The VIF threshold above which features will be removed.

    Returns:
    pd.DataFrame: A DataFrame with multicollinear features removed.
    """
    
    # Create a copy of the DataFrame to avoid modifying the original
    df_cleaned = df.copy()
    
    # Calculate VIF for each feature
    vif_data = pd.DataFrame()
    vif_data["Feature"] = df_cleaned.columns
    vif_data["VIF"] = [variance_inflation_factor(df_cleaned.values, i) for i in range(df_cleaned.shape[1])]
    
    # Print initial VIF values
    print("Initial VIF values:")
    print(vif_data)
    
    # Remove features with VIF above the threshold
    while vif_data["VIF"].max() > threshold:
        # Identify the feature with the highest VIF
        feature_to_remove = vif_data.loc[vif_data["VIF"].idxmax(), "Feature"]
        print(f"Removing feature: {feature_to_remove} with VIF: {vif_data['VIF'].max()}")
        
        print(f"df :\n{df}")
        print(f"columns :{list(df_cleaned.columns)}")
        print(f"colname :{feature_to_remove}")
        
        # Remove the feature from the DataFrame
        df_cleaned = df_cleaned.drop(columns=feature_to_remove)

        print(f"Recalculate VIF, shape  :{df_cleaned.shape}")        
        print(f"Recalculate VIF, values :{df_cleaned.values}")        
        # Recalculate VIF
        # for i in range(df_cleaned.shape[1]):
        #     print(i)
        vif_data["VIF"] = [variance_inflation_factor(df_cleaned.values, i) for i in range(df_cleaned.shape[1])]
    
    # Print final VIF values
    print("Final VIF values:")
    print(vif_data)
    
    return df_cleaned

    r2_score_lenier_regression(data)

# Create a sample DataFrame
MAX_LEN = 10
data = {
    'A': np.random.rand(MAX_LEN),
    'B': np.random.rand(MAX_LEN),
    'C': np.random.rand(MAX_LEN),
    'D': np.random.rand(MAX_LEN) * 0.5 + np.random.rand(MAX_LEN) * 0.5  # Highly correlated with A
}

def main():
    # Remove multicollinearity
    print(f"data :{data}")
    
    df = pd.DataFrame(data)
    print(f"df :\n{df}")
    
    cleaned_df = remove_multicollinearity(df, threshold=5.0)

    # Display the cleaned DataFrame
    # print("Cleaned DataFrame:")
    # print(cleaned_df.head())

if (__name__ == '__main__'):
    main()
