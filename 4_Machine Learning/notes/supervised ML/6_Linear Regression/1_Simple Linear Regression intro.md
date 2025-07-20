# Simple Linear Regression

## 1. Introduction to Simple Linear Regression
*   Simple Linear Regression is your **first machine learning algorithm**.
*   It's a **very important algorithm** because the techniques learned here are also applicable to deep learning, especially when learning the first neural network (Artificial Neural Network).
*   It's crucial to understand and remember this algorithm.

## 2. What Problems Simple Linear Regression Solves
*   It solves **regression problem statements** within **supervised machine learning** techniques.
*   This means it's used when you want to predict a continuous numerical output.

## 3. Example Dataset
*   Consider a dataset with two features: **weight and height**.
*   **Example Data Points**:
    *   Weight: 74kg, Height: 170cm
    *   Weight: 80kg, Height: 180cm
    *   Weight: 75kg, Height: 175.5cm

## 4. Goal of Simple Linear Regression
*   The main aim is to **train a model**.
*   This model should be able to **predict the height whenever new weight is provided**.
*   In the example, **weight is the independent feature (input)**, and **height is the output or dependent feature**.

## 5. Why "Simple" Linear Regression?
*   It's called "simple" because it involves **only one input feature and one output feature**.
*   If there were multiple input features, it would be called **Multiple Linear Regression**.
*   Understanding Simple Linear Regression is important because its terminologies and mathematics apply to Multiple Linear Regression as well.

## 6. How the Model Works (Geometric View)
*   Imagine plotting the data points with weight on one axis and height on the other.
*   The goal is to **create a "best fit line"** through these plotted points.
*   This best fit line will help in making predictions for new weights.

## 7. How Prediction Happens
*   Once the best fit line is created:
    1.  For a **new weight**, locate it on the weight axis.
    2.  Move vertically from that weight point until you **meet the best fit line**.
    3.  Then, move horizontally from that point on the line to the height axis.
    4.  The value on the height axis where it meets is the **predicted height** for that specific new weight.

## 8. Selecting the "Best Fit Line"
*   The best fit line is created in a way that **minimizes the "error"**.
*   **Error** is the **distance between the true (actual) data points and the points predicted by the line**.
*   The "true points" are the actual output values in the dataset (e.g., 170cm, 180cm, 175.5cm heights).
*   The sum of these distances (or errors) should be **minimal** to select the best fit line.