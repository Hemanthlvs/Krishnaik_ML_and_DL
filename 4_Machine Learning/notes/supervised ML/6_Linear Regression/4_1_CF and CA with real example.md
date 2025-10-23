# Cost Function Example with 4 Input Features (Linear Regression)

In multiple linear regression, we use the cost function to measure how well our hypothesis fits the data. We typically use **Mean Squared Error (MSE)** as the cost function.

---

## Hypothesis Function

Given 4 features:

**h(𝑥ᵢ) = θ₀ + θ₁·xᵢ₁ + θ₂·xᵢ₂ + θ₃·xᵢ₃ + θ₄·xᵢ₄**

---

## Sample Training Data (3 Examples)

| i | xᵢ₁ | xᵢ₂ | xᵢ₃ | xᵢ₄ | yᵢ |
|---|------|------|------|------|-----|
| 1 | 1    | 2    | 3    | 4    | 10  |
| 2 | 2    | 0    | 1    | 3    | 12  |
| 3 | 3    | 1    | 0    | 2    | 13  |

Initial parameter values:

- θ₀ = 0.5  
- θ₁ = 0.1  
- θ₂ = 0.2  
- θ₃ = 0.3  
- θ₄ = 0.4

---

## Step 1: Compute Predictions h(𝑥ᵢ)

Using the hypothesis formula:

- h(x₁) = 0.5 + 0.1·1 + 0.2·2 + 0.3·3 + 0.4·4 = 3.5  
- h(x₂) = 0.5 + 0.1·2 + 0.2·0 + 0.3·1 + 0.4·3 = 2.2  
- h(x₃) = 0.5 + 0.1·3 + 0.2·1 + 0.3·0 + 0.4·2 = 1.8

---

## Step 2: Compute Squared Errors

| i | yᵢ  | h(𝑥ᵢ) | Error (h(𝑥ᵢ) - yᵢ) | Squared Error |
|---|------|--------|---------------------|----------------|
| 1 | 10   | 3.5    | -6.5                | 42.25          |
| 2 | 12   | 2.2    | -9.8                | 96.04          |
| 3 | 13   | 1.8    | -11.2               | 125.44         |

---

## Step 3: Compute Cost Function (MSE)

Cost Function:

**J(θ) = (1 / 2m) · Σ (h(𝑥ᵢ) - yᵢ)²**  
Where **m = 3** (number of examples)

**J(θ) = (1 / 6) · (42.25 + 96.04 + 125.44)**  
**J(θ) = (1 / 6) · 263.73 = 43.955**

---

## Interpretation

A cost of **43.955** means the model's current parameter values produce a moderate amount of error. The training process (gradient descent) will iteratively update the θ parameters to minimize this cost and get closer to the best-fit line in 4D space.

Repeat this process during training until **convergence**.



# Gradient Descent and convergence algorithm Example with Actual Data

Suppose you have 3 training examples:

| i | x\_{i1} | x\_{i2} | x\_{i3} | x\_{i4} | y\_i |
| - | ------- | ------- | ------- | ------- | ---- |
| 1 | 1       | 2       | 3       | 4       | 10   |
| 2 | 2       | 0       | 1       | 3       | 12   |
| 3 | 3       | 1       | 0       | 2       | 13   |

Initial parameters (random guess):

θ = \[θ₀, θ₁, θ₂, θ₃, θ₄] = \[0.5, 0.1, 0.2, 0.3, 0.4]

Learning rate:

α = 0.01

Number of examples:

m = 3

---

**Step 1: Compute hypothesis (h\_θ(x\_i)) for each training example**

Recall hypothesis formula:

h\_θ(x\_i) = θ₀ \* 1 + θ₁ \* x\_{i1} + θ₂ \* x\_{i2} + θ₃ \* x\_{i3} + θ₄ \* x\_{i4}

Calculate for each example:

* h\_θ(x₁) = 0.5 + 0.1 \* 1 + 0.2 \* 2 + 0.3 \* 3 + 0.4 \* 4 = 3.5
* h\_θ(x₂) = 0.5 + 0.1 \* 2 + 0.2 \* 0 + 0.3 \* 1 + 0.4 \* 3 = 2.2
* h\_θ(x₃) = 0.5 + 0.1 \* 3 + 0.2 \* 1 + 0.3 \* 0 + 0.4 \* 2 = 1.8

---

**Step 2: Compute errors (h\_θ(x\_i) - y\_i)**

| i | h\_θ(x\_i) | y\_i | Error (h\_θ(x\_i) - y\_i) |
| - | ---------- | ---- | ------------------------- |
| 1 | 3.5        | 10   | -6.5                      |
| 2 | 2.2        | 12   | -9.8                      |
| 3 | 1.8        | 13   | -11.2                     |

---

**Step 3: Calculate each update term for each θ\_j**

Update formula:

θ\_j := θ\_j - α \* (1/m) \* Σ\_{i=1 to m} (h\_θ(x\_i) - y\_i) \* x\_{ij}

where x\_{i0} = 1 for the intercept θ₀.

Calculate sums:

| Parameter (θ\_j) | x\_{ij} for i=1,2,3 | Sum Σ (h\_θ(x\_i) - y\_i) \* x\_{ij}     |
| ---------------- | ------------------- | ---------------------------------------- |
| θ₀               | \[1, 1, 1]          | -6.5 + (-9.8) + (-11.2) = -27.5          |
| θ₁               | \[1, 2, 3]          | -6.5\*1 + (-9.8)\*2 + (-11.2)\*3 = -59.7 |
| θ₂               | \[2, 0, 1]          | -6.5\*2 + (-9.8)\*0 + (-11.2)\*1 = -24.2 |
| θ₃               | \[3, 1, 0]          | -6.5\*3 + (-9.8)\*1 + (-11.2)\*0 = -29.3 |
| θ₄               | \[4, 3, 2]          | -6.5\*4 + (-9.8)\*3 + (-11.2)\*2 = -77.8 |

---

**Step 4: Calculate update amounts**

Divide sums by m=3 and multiply by learning rate α=0.01:

| Parameter | Update amount = α \* (1/m) \* Sum |
| --------- | --------------------------------- |
| θ₀        | 0.01 \* (-27.5 / 3) = -0.0917     |
| θ₁        | 0.01 \* (-59.7 / 3) = -0.199      |
| θ₂        | 0.01 \* (-24.2 / 3) = -0.0807     |
| θ₃        | 0.01 \* (-29.3 / 3) = -0.0977     |
| θ₄        | 0.01 \* (-77.8 / 3) = -0.2593     |

---

**Step 5: Update parameters**

θ\_j := θ\_j - update amount

| Parameter | Before Update | After Update             |
| --------- | ------------- | ------------------------ |
| θ₀        | 0.5           | 0.5 - (-0.0917) = 0.5917 |
| θ₁        | 0.1           | 0.1 - (-0.199) = 0.299   |
| θ₂        | 0.2           | 0.2 - (-0.0807) = 0.2807 |
| θ₃        | 0.3           | 0.3 - (-0.0977) = 0.3977 |
| θ₄        | 0.4           | 0.4 - (-0.2593) = 0.6593 |

---

### Summary

| Parameter | Before Update | After Update |
| --------- | ------------- | ------------ |
| θ₀        | 0.5           | 0.5917       |
| θ₁        | 0.1           | 0.299        |
| θ₂        | 0.2           | 0.2807       |
| θ₃        | 0.3           | 0.3977       |
| θ₄        | 0.4           | 0.6593       |

This completes **one step of gradient descent**! Repeat this process until θ values converge.

---

-----------------------------------------------------------------

# ✅ What Happens After One Step of Gradient Descent?

Now that you’ve completed one full update using gradient descent, here’s what comes next in the training process:

---

## 🔁 1. Repeat the Gradient Descent Steps

Use the updated θ values from the previous step:

θ₀ = 0.5917  
θ₁ = 0.299  
θ₂ = 0.2807  
θ₃ = 0.3977  
θ₄ = 0.6593  

With these new θ values:

- Recompute the hypothesis h(xᵢ) for each training example  
- Calculate the new errors (h(xᵢ) - yᵢ)  
- Compute gradients  
- Update θ again using the same formula  
- Repeat this process in a loop

---

## 📉 2. Track Cost Function After Each Iteration

After every update:

- Recalculate the **cost function J(θ)**, typically using **Mean Squared Error (MSE)**
- It should **decrease** after each step if learning is progressing correctly

Example:

After iteration 1:  
Cost J(θ) = 43.955

After iteration 2:  
Cost J(θ) = 32.1 ✅ (Improved)

---

## 🛑 3. Stopping Criteria

Repeat the above process **until one of the following is true**:

- The change in cost is very small (e.g., < 0.0001)
- You reach the **maximum number of iterations**
- The gradient values become near zero (i.e., convergence)

This is when **training stops**, and you’ve likely found the optimal parameters!

---

## 🧩 Optional Enhancements

- 🔄 Use **feature scaling / normalization** to improve speed
- 🚀 Try different **learning rates (α)** to avoid overshooting or slow learning
- 📈 Plot **cost vs iterations** to visualize convergence

---

## 🎯 Final Goal

> The goal of training is to **minimize the cost function J(θ)**  
> so that your model generalizes well to unseen data and predictions are as accurate as possible.

Once converged, your trained model is ready to **make predictions** on new inputs.

