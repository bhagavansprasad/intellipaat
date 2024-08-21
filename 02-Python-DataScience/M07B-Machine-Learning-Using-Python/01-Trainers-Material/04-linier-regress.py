import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Generate some sample data
np.random.seed(0)  # For reproducibility
x1 = np.random.randn(100)
x2 = np.random.randn(100)
y = 2 + 3 * x1 + 4 * x2 + np.random.randn(100)  # Linear relationship with noise

# Prepare the data for linear regression
X = np.column_stack((x1, x2))

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients
beta0 = model.intercept_
beta1, beta2 = model.coef_

# Create a grid for x1 and x2
x1_grid, x2_grid = np.meshgrid(np.linspace(min(x1), max(x1), 10),
                                 np.linspace(min(x2), max(x2), 10))

# Calculate the predicted y values based on the regression model
y_pred = beta0 + beta1 * x1_grid + beta2 * x2_grid

# Plot the data and regression plane
fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the original data points
ax.scatter(x1, x2, y, color='b', label='Data Points')

# Plot the regression plane
ax.plot_surface(x1_grid, x2_grid, y_pred, color='r', alpha=0.5, label='Regression Plane')

# Labels and title
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
ax.set_title('3D Linear Regression')
ax.legend()

# Show the plot
plt.show()
