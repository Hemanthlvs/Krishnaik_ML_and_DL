# Dimensionality Reduction: Feature Selection vs. Feature Extraction

## 1. What is Dimensionality Reduction?
*   It's a technique used to **reduce the number of features** or **extract important features** from existing ones.

## 2. Why Perform Dimensionality Reduction?
There are three main reasons:

### a. To Prevent the Curse of Dimensionality
*   When you have too many features (dimensions), the data becomes very sparse, making it difficult for models to find meaningful patterns and generalise well.

### b. To Improve the Performance of the Model
*   Imagine a dataset with 100 features (dimensions).
*   Every model trains by applying mathematical equations to all these dimensions.
*   More dimensions mean these equations take **more time for training**.
*   Reducing dimensions can significantly **speed up model training** and improve overall performance.

### c. To Visualize and Understand the Data
*   Humans can primarily visualize data in **2D or 3D**. We cannot easily visualize 4D or higher dimensions.
*   If your dataset has 100 dimensions, you cannot visualize it directly.
*   By reducing the number of dimensions to 2D or 3D, you can **clearly see and understand the data**.
*   The major aim here is to **understand the data**.

## 3. Feature Selection

### a. What is Feature Selection?
*   It's a process where we **select the most important features** that help in predicting the output.
*   Basically, you **choose a subset of original features**.

### b. How Do We Determine "Important" Features?
We look for relationships between input features (X) and the output feature (Y). Strong relationships indicate important features.

#### i. Covariance
*   **Definition**: A statistical measure to quantify the **relationship between two variables** (X and Y).
*   **Formula**: `Cov(X, Y) = Σ [(Xi - X̄)(Yi - ȳ)] / (n - 1)` (for sample data).
*   **Interpretation**:
    *   **Positive Covariance**: Indicates a **positive linear relationship**. As X increases, Y increases; as X decreases, Y decreases.
    *   **Negative Covariance**: Indicates an **inverse linear relationship**. As X decreases, Y increases; as X increases, Y decreases.
    *   **Covariance ≈ Zero**: Indicates **no linear relationship** between X and Y. Data points might appear scattered circularly.
*   **Significance**: Features with **highly positive or negative covariance** with the output are considered **super important**. If covariance is near zero, the feature can often be removed.

#### ii. Pearson Correlation (Coefficient)
*   **Definition**: A **standardized version of covariance**. It also quantifies the linear relationship.
*   **Formula**: `Pearson Correlation = Cov(X, Y) / (σx * σy)` (where σ is standard deviation).
*   **Range**: Unlike covariance, Pearson correlation always ranges between **-1 to +1**.
*   **Interpretation**:
    *   **Closer to +1**: **Strong positive correlation**. X and Y are highly positively correlated.
    *   **Closer to -1**: **Strong negative correlation**. X and Y are highly negatively correlated.
    *   **Near to 0**: **No relationship**.
*   **Usage in Feature Selection**: We use correlation and covariance to **determine the relationship** between features and the output, helping us decide which features to keep or drop.

### c. Example: Housing Dataset for Feature Selection
*   **Independent Features**: House Size, Fountain Size.
*   **Dependent Feature (Output)**: Price of the House.

*   **House Size vs. Price**:
    *   Common sense suggests House Size is important.
    *   Plotting usually shows a **linear relationship** (e.g., as house size increases, price increases).
    *   Calculating **covariance** will likely yield a **high positive value**, or **correlation** will be close to **+1**.
    *   **Conclusion**: House Size is an **important feature** and should be kept.

*   **Fountain Size vs. Price**:
    *   Common sense suggests Fountain Size may **not be a very important feature** for apartment prices.
    *   Plotting may show **no clear relationship** (e.g., price is stagnant even if fountain size increases).
    *   Calculating **covariance** will likely be **very low or near zero**, or **correlation** will be close to **0** (e.g., 0 to 0.25).
    *   **Conclusion**: Fountain Size is **not that important** and can be **dropped**.
*   This process of dropping less important features is what we usually do in **feature selection**.

## 4. Feature Extraction

### a. What is Feature Extraction?
*   In feature extraction, we **transform existing independent features to create new features**.
*   The goal is to **reduce the number of features** (dimensions) while retaining as much information as possible.

### b. When to Use Feature Extraction?
*   You use feature extraction when **all your independent features are super important** for predicting the output.
*   If you find that all your input features have a **high correlation or covariance** with the dependent feature, you **cannot simply drop** any of them using feature selection.

### c. Example: Housing Dataset for Feature Extraction
*   **Independent Features**: Room Size, Number of Rooms.
*   **Dependent Feature (Output)**: Price of the House.
*   In this scenario, both Room Size and Number of Rooms are **super important** for predicting house price. You cannot drop either of them.
*   **Process**: We take these two independent features and **apply some transformation** to them.
*   **Result**: This transformation extracts a **new feature**, say "House Size," from "Room Size" and "Number of Rooms".
*   Now, instead of two features (Room Size, Number of Rooms), you use one new feature (House Size) to predict the Price.
*   **Core Idea**: You're **deriving a new feature** from the features that are already present.
*   **Information Loss**: Some amount of information might be lost, but the domain expert can still predict the price with the new, reduced feature set.
*   **Real-world**: Typically, you might reduce 10-15 features down to 2-3 features using extraction.
*   This also helps in **visualizing and understanding the data** better, just like with feature selection.