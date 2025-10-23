## Convergence Algorithm

### The Problem with Random `θ1` Changes

*   Previously, `θ1` values (like 1, 0.5, 0) were changed randomly to find the cost function.
*   This random approach is **not an efficient technique** for finding the best `θ1` value.

### The Solution: Convergence Algorithm

*   The **convergence algorithm** is a **super important optimized technique**.
*   Its main purpose is to **optimize the changes of `θ1`(slope or coefficient) and `θ0`(interception or bias) value**.
*   It helps to **automatically increase or decrease `θ1` and `θ0`** based on the gradient descent curve, starting from an initial value.

### How the Convergence Algorithm Works

*   The algorithm **repeats until convergence**.
*   **"Until convergence"** means until it reaches or gets very close to the **global minima** point.
*   The core equation for updating `θ_j` (which is `θ1` in this context) is:
	**`θ_j = θ_j - α * ∂J(θ_j)/∂θ_j`**.

### Key Components of the Algorithm

#### a. Derivative (Slope Calculation)

*   **Derivative** in this context means **calculating the slope** at a specific point on the gradient descent curve.
*   We initialize `θ_j` at some point and find its corresponding cost `J(θ_j)`.
*   The algorithm then calculates the slope at this point.
*   **To find the slope (derivative)**, we draw a **tangent line** at that point.

#### b. Understanding Positive and Negative Slopes

*   **Positive Slope**:
    *   If you look at the **right side of the tangent line and it points upwards**, it's a positive slope.
    *   When the derivative is positive, the equation `θ_j = θ_j - alpha * (positive value)` will **decrease `θ_j`**.
    *   This is necessary when `θ_j` is on the right side of the global minima, as we need to move it left (decrease its value) to reach the minima.
*   **Negative Slope**:
    *   If you look at the **right side of the tangent line and it faces downwards**, it's a negative slope.
    *   When the derivative is negative, the equation `θ_j = θ_j - alpha * (negative value)` results in `θ_j = θ_j + (positive value)`. This means it will **increase `θ_j`**.
    *   This is necessary when `θ_j` is on the left side of the global minima, as we need to move it right (increase its value) to reach the minima.

#### c. Alpha (Learning Rate)

*   **Alpha (α)** is called the **learning rate**.
*   It's typically initialized as a **small value**. For example, `0.001` is often a good practice and is used in `sklearn` library.
*   **Importance**: The learning rate **controls the speed at which convergence happens**.
    *   **Very small `alpha`**: The algorithm will take **more time to converge**.
    *   **Very big `alpha`**: The algorithm may **continuously jump around and never converge**.
*   It's crucial to select a value that is small but not too small.

### Continuous Process and Convergence

*   This process of calculating the slope and updating `θ_j` **iterates continuously**.
*   As `θ_j` is adjusted (increased for negative slopes, decreased for positive slopes), it **slowly moves towards the global minima**.
*   The process stops when `θ_j` converges near the global minima, leading to the **best fit line**.

## The Role of θ Values and Dimensions
*   **θ0** often represents the **intercept** (where the line crosses the y-axis), and **θ1** represents the **slope** in simple linear regression.
*   **2D Diagram (Simple Case):**
    *   If the intercept (θ0) is considered zero, the best fit line passes through the origin.
    *   In this simplified scenario, only **θ1 changes**, and Gradient Descent can be visualized in a **2D graph**.
*   **3D Diagram (More Realistic Case):**
    *   If θ0 is not zero (meaning the line doesn't pass through the origin), the visualization becomes a **3D diagram**.
    *   This 3D curve looks like an **inverted mountain**, and the aim is to find the lowest point (global minima).
    *   In this case, **both θ0 and θ1 are updated** iteratively to reach the global minima.

### Derivative with respect to θ0 (for j=0)
*   After applying derivative rules to the cost function with respect to `θ0`, the derivative simplifies to:
    *   **`(1 / m) * Σ [h_θ(x_i) - y_i]`**.
*   This is because the derivative of `h_θ(x_i) - y_i` with respect to `θ0` is `1` (since `θ1 * x` is treated as a constant).

### Derivative with respect to θ1 (for j=1)
*   Similarly, after finding the derivative of the cost function with respect to `θ1`, it simplifies to:
    *   **`(1 / m) * Σ [h_θ(x_i) - y_i] * x_i`**.
*   This `x_i` comes from the derivative of `h_θ(x_i) - y_i` with respect to `θ1`, which is `x_i` (since `θ0` is constant and `θ1 * x_i` derivative is `x_i`).

## Final Convergence Equations for Simple Linear Regression
In vectorized form:  
Let

**xᵢ** =  
[1  
xᵢ₁  
xᵢ₂  
xᵢ₃  
xᵢ₄],  

**θ** =  
[θ₀  
θ₁  
θ₂  
θ₃  
θ₄]

Hypothesis:

h_θ(**xᵢ**) = θᵀ **xᵢ**

*   **Repeat until convergence:**
    *   **θ0 Update:**
        *   `θ0 (new) = θ0 (old) - α * (1 / m) * Σ [h_θ(x_i) - y_i]`.
        *   For the intercept `(θ0)​, just use 𝑥𝑖0=1`
    *   **θ1 Update:**
        *   `θ1 (new) = θ1 (old) - α * (1 / m) * Σ [h_θ(x_i) - y_i] * x_i`.
*   These equations are repeatedly applied until the model finds the **best fit line** or **converges to the global minima** of the cost function.
