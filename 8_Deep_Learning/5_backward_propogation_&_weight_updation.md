# Backpropagation and Weight Updates

## 1. Neural Network Architecture Overview

- **Input Layer**: This layer takes independent features from the dataset (e.g., X1, X2, X3).
  - **Example Inputs**: IQ, study hours, play hours.
  
- **Hidden Layer**: In this example, it contains two neurons.
  - A **bias** is also added to the hidden layer.
  - **All inputs are connected to all hidden neurons**.
  - **Weights (w1-w6)** are initialized for these connections.
  
- **Output Layer**:
  - This layer has **one output neuron** because it is solving a **binary classification problem** (output is either 0 or 1).
  - For **multi-class classification**, the number of output neurons corresponds to the number of classes (e.g., two neurons for three outputs like 0, 1, 2).
  - Connections from the hidden layer to the output layer also have **weights (w7, w8)**.

## 2. Forward Propagation (Recap)

- **Process**: Inputs are taken, multiplied by weights, a bias is added, and then an activation function is applied.
  
- **Matrix Multiplication Example**:
  - If there are three input neurons and two hidden neurons, the matrix multiplication shape will be **3 x 2**.
  - Example calculation: `X1*W1 + X1*W2 + X2*W3 + X2*W4 + X3*W5 + X3*W6`.

## 3. Loss Function

- **Purpose**: To calculate the **difference between the predicted output and the actual output**.
  
- **Main Aim**: To **minimize the loss function**.

- **Types of Loss Functions**:
  - **For Regression Problems**:
    - Mean Squared Error (MSE)
    - Mean Absolute Error (MAE)
    - Huber Loss
  - **For Classification Problems**:
    - Binary Cross Entropy
    - Cross Entropy
    - Categorical Cross Entropy
  
- **Simple Loss Function Concept**: The loss can be represented as `(y - y_hat)^2`, where `y_hat` is the predicted output.

## 4. Backward Propagation and Weight Updates

- **When it Happens**: Weight updates occur during **backward propagation** after calculating the loss function.
  
- **Direction**: Backward propagation starts from the loss and updates weights back through the network (e.g., w7 and w8 first).

### 4.1. Weight Update Formula

- The formula for updating weights is:
  **`w_new = w_old - (learning_rate * derivative_of_loss_with_respect_to_w_old)`**
  - **`w_new`**: The updated weight.
  - **`w_old`**: The current weight.
  - **`learning_rate`**: A parameter that controls the step size.
  - **`derivative_of_loss_with_respect_to_w_old`**: Represents the **slope** of the graph plotted with respect to the weights and the loss function, known as **gradient descent**.

### 4.2. Understanding Gradient Descent and Slope

- The relationship between weights and loss often forms a **gradient descent curve**.
  
- The **goal** is to reach the **global minimum** of this curve, where the loss is minimized.
  
- At the global minimum, the **slope is zero**, indicating no further weight updates are needed.

### 4.3. How the Weight Update Formula Works

- **Scenario 1: Negative Slope (Left of the global minimum)**
  - The current weight is to the left of the global minimum.
  - The derivative will be a **negative value**.
  - Formula: `w_new = w_old - (learning_rate * negative_value) = w_old + (positive_value)`.
  - Result: **`w_new` will be greater than `w_old`**, increasing the weight towards the global minimum.

- **Scenario 2: Positive Slope (Right of the global minimum)**
  - The current weight is to the right of the global minimum.
  - The derivative will be a **positive value**.
  - Formula: `w_new = w_old - (learning_rate * positive_value)`.
  - Result: **`w_new` will be less than `w_old`**, decreasing the weight towards the global minimum.

- This confirms that the weight update formula consistently guides the weights towards the global minimum.

## 5. The Importance of Learning Rate

- The **learning rate** is a crucial parameter in the weight update formula.
  
- It dictates the **step size** taken towards the global minimum in each iteration.

### 5.1. Small Learning Rate (e.g., 0.001)

- Results in **smaller step sizes**.
- Weights update gradually, leading to **slower but more precise convergence** towards the global minimum.
- It is generally a **good practice to use a small learning rate**.

### 5.2. Large Learning Rate

- Results in **larger step sizes**.
- The model might **oscillate** around the global minimum or even **diverge** entirely.
- This can lead to the model **never converging**.

## 6. Convergence to Global Minimum

- When the weight `w` reaches the **global minimum**:
  - The **slope (derivative of loss with respect to w)** becomes **zero**.
  - Substituting this into the weight update formula: `w_new = w_old - (learning_rate * 0) = w_old`.
  - This means **`w_new = w_old`**, indicating that the weights no longer need to be updated, and the loss function is minimized (close to zero).

## 7. Optimizers

- **Role**: Optimizers are used to **reduce the loss value** by updating the weights.
  
- **Gradient Descent Optimizer**: A simple example of an optimizer that achieves this.

