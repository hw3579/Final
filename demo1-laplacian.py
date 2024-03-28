import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

# Define the logistic growth function
def logistic_growth(t, r=1.0, K=100.0, P0=10.0):
    """Logistic growth function.
    P0: initial population
    r: growth rate
    K: carrying capacity
    t: time
    """
    return K * P0 * np.exp(r * t) / (K + P0 * (np.exp(r * t) - 1))

# First and second derivatives of the logistic growth function
def first_derivative(t, r=1.0, K=100.0, P0=10.0):
    return derivative(lambda t: logistic_growth(t, r, K, P0), t, dx=1e-6)

def second_derivative(t, r=1.0, K=100.0, P0=10.0):
    return derivative(lambda t: logistic_growth(t, r, K, P0), t, dx=1e-6, n=2)

# Time points to evaluate the functions
time = np.linspace(0, 6, 200)

# Calculate the population, first derivative, and second derivative
population = logistic_growth(time)
population_first_derivative = np.array([first_derivative(t) for t in time])
population_second_derivative = np.array([second_derivative(t) for t in time])


# Plot the original function

plt.plot(time, population, label='Original Function')
plt.title('Example Function')
plt.xlabel('x')
plt.ylabel('intensity')
plt.legend()
plt.grid(True)
plt.savefig('./fig/original_function.png')
plt.show()
# Plot the first derivative

plt.plot(time, population_first_derivative, label='First Derivative', color='orange')
plt.title('First Derivative')
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.legend()
plt.grid(True)
plt.savefig('./fig/first_derivative.png')
plt.show()
# Plot the second derivative

plt.plot(time, population_second_derivative, label='Second Derivative', color='green')
plt.title('Second Derivative')
plt.xlabel('x')
plt.ylabel('f\'\'(x)')
plt.legend()
plt.grid(True)
plt.savefig('./fig/second_derivative.png')
plt.show()
