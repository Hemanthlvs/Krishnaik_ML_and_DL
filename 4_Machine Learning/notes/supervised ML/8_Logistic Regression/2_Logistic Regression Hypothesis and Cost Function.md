# Logistic Regression: Hypothesis and Cost Function

## Sigmoid Activation Function

*   To "squash" those results, we introduce a new concept called the **Sigmoid Activation Function**.
*   **Sigmoid Equation:** It's given by `sigmoid(z) = 1 / (1 + e⁻ᶻ)`.
*   **Important Thing about Sigmoid:**
    *   No matter what value `z` has (it can be anything, negative or positive), the `sigmoid(z)` output will **always be between 0 and 1**. This solves our output range problem!
    *   The graph of the sigmoid function looks like an 'S' shape.
    *   The middle point of the output is **0.5**.
    *   If your `z` value is **greater than zero (z > 0)**, then `sigmoid(z)` will be **greater than 0.5**.
*   By applying this sigmoid function to our best fit line, both the outlier issue and the output range issue get sorted.

## The Logistic Regression Hypothesis

*   Okay, so what do we do in Logistic Regression? First, we create that "best fit line" (the linear part), and then, **on top of it, we apply the sigmoid activation function**.
*   **Our New Hypothesis Notation:** We call it `hθ(x)`.
*   **What is `z`?** The `z` value inside the sigmoid function is basically the linear equation itself:
    *   For one independent feature: `z = θ₀ + θ₁x₁`.
    *   If you have multiple features: `z = θ₀ + θ₁x₁ + θ₂x₂ + θ₃x₃ + ...`.
*   **The Final Logistic Regression Hypothesis Equation:**
    `hθ(x) = 1 / (1 + e⁻ᶻ)` where `z = θ₀ + θ₁x₁` (or with more features).
*   This hypothesis is awesome because it always gives us an output between **0 and 1**, which we can then interpret as probabilities for classification.

## Why Linear Regression's Cost Function is a No-Go!

*   Let's quickly recall the Linear Regression Cost Function (Mean Squared Error): `J(θ₀, θ₁) = (1/2m) Σ (hθ(xᵢ) - yᵢ)²`.
*   Now, if we just swap `hθ(x)` with our new sigmoid-based `hθ(x)` in this cost function for Logistic Regression, we hit a roadblock:
    *   When you plot this new cost function against your `theta` values, it gives you a **non-convex function**.
*   **What are Convex and Non-Convex Functions?**
    *   **Convex Function:** Imagine a nice, smooth bowl. It has only **one "lowest point" (Global Minima)**. Gradient Descent (our optimization algorithm) loves this because it will always find that single best solution.
    *   **Non-Convex Function:** This one is like a bumpy road with many "dips" (Local Minima) in addition to the actual lowest point (Global Minima).
*   **The Problem with Local Minima:** If our Gradient Descent starts and lands on a "local minima" (one of those small dips), it can get **stuck there**. Why? Because the slope at that point becomes zero, and the algorithm thinks it has found the best solution, even if it's not the actual "Global Minima".
*   So, that's why the standard Mean Squared Error cost function is **not suitable** for Logistic Regression.

## The Real Hero: Logistic Regression Cost Function (Log Loss)

*   To get a beautiful **convex function** (which is a must for Gradient Descent to work properly), we use a different cost function called **Log Loss** (or sometimes Binary Cross-Entropy Loss).
*   This Log Loss works like this, based on the actual output `y`:
    *   **If the actual `y` value is 1:** The cost for that example is `-log(hθ(x))`.
    *   **If the actual `y` value is 0:** The cost for that example is `-log(1 - hθ(x))`.
*   When we use these log conditions, it mathematically makes our cost function **convex**.
*   **The Combined Log Loss Equation (for one data point `i`):**
    `Cost(hθ(xᵢ), yᵢ) = -yᵢ log(hθ(xᵢ)) - (1 - yᵢ) log(1 - hθ(xᵢ))`.
    *   **Cool trick:** If `yᵢ` is 1, the second part `(1 - yᵢ) log(...)` becomes zero. If `yᵢ` is 0, the first part `-yᵢ log(...)` becomes zero. So, only the relevant term contributes to the cost.
*   **The Full Logistic Regression Cost Function (J(θ)):**
    `J(θ₀, θ₁) = -(1/2m) Σ [yᵢ log(hθ(xᵢ)) + (1 - yᵢ) log(1 - hθ(xᵢ))]`.
    (He mentioned `1/2m` here, though usually, it's `1/m` for log loss. We'll stick to what was taught in the source for these notes.)
*   This `J(θ₀, θ₁)` is the final cost function, and it **will always give a convex function**.

## Minimizing the Cost Function (Gradient Descent)

*   Our ultimate goal is to **minimize this `J(θ₀, θ₁)` cost function**.
*   We do this by continuously tweaking the values of `theta (θ₀, θ₁, etc.)`.
*   The method we use is the **Gradient Descent convergence algorithm**.
*   **The Update Rule for Theta:**
    `θⱼ = θⱼ - α * (∂/∂θⱼ)J(θ₀, θ₁)`.
    *   `θⱼ` is the specific theta parameter we are updating (like `θ₀` or `θ₁`).
    *   `α` (alpha) is the **learning rate**. It controls how big a step we take each time we update theta.
    *   `(∂/∂θⱼ)J` is the **derivative** of the cost function with respect to `θⱼ`. This tells us the slope, which guides us in the right direction to minimize the cost.
*   By repeating this process, we keep updating `theta` values until we reach the minimum point of the cost function, finding the best parameters for our Logistic Regression model.
