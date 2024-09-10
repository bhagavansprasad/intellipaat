import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def r2_score_lenier_regression(data):
    df = pd.DataFrame(data)
    
    # Features and Target
    X = df[['X']]  # Feature
    Y = df['Y']    # Target

    # Splitting the dataset into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Predicting the target values
    Y_pred = model.predict(X_test)

    # Calculating the R2 score
    r2 = r2_score(Y_test, Y_pred)

    print(f"R2 Score: {r2}")


# Sample DataFrame
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 4, 5, 4, 5]
}

data = {
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Y': [2, 4, 5, 4, 5, 7, 8, 9, 10, 12]
}

def main():
    r2_score_lenier_regression(data)


if (__name__ == '__main__'):
    main()


