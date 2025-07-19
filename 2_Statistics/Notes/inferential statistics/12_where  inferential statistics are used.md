# 📊 When Do We Use Statistical Tests in Machine Learning & Deep Learning?

Machine Learning (ML) and Deep Learning (DL) mainly work by learning patterns from data.  
They do **not use statistical tests** (like **t-test**, **z-test**, **chi-square**, or **ANOVA**) **inside the model**.  

But we can use these tests **before** or **after** training to better understand our data and to make better decisions.

---

## ✅ 1. During EDA (Exploratory Data Analysis)

We use statistical tests to check if there is any **relationship between columns (features)**.

### 🧪 Example:
We want to know if **ticket price** is different for **economy class** and **business class**.

Use a **t-test**:

```python
from scipy.stats import ttest_ind

eco = df[df['class'] == 'Economy']['price']
bus = df[df['class'] == 'Business']['price']

t_stat, p_val = ttest_ind(eco, bus)
print("P-value:", p_val)
```

📌 If `p-value < 0.05`, then the prices are **significantly different** → good feature for the model.

---

## ✅ 2. Before Modeling (Check If Data Is Good)

We can use tests to check if our **train and test data** are similar.  
This helps detect **data drift** or **sampling bias**.

| Concept           | Definition                                     | Example                                                   |
| ----------------- | ---------------------------------------------- | --------------------------------------------------------- |
| **Data Drift**    | Real-world data changes after model is trained | Flight price patterns change post-COVID                   |
| **Sampling Bias** | Training data doesn’t reflect full population  | Model trained on only metro cities, used for all of India |


### 🧪 Example:
Check if age distribution is the same in train and test:

```python
from scipy.stats import ks_2samp

ks_stat, p_val = ks_2samp(train['age'], test['age'])
```

📌 If `p-value < 0.05`, then the **distributions are different** → model may not perform well on test data.

---

## ✅ 3. Comparing Two Models

After training two models (Model A and Model B), we want to know:  
**Is Model B really better than Model A, or just lucky?**

We use a **paired t-test** on their cross-validation scores:

```python
from scipy.stats import ttest_rel

t_stat, p_val = ttest_rel(model_a_scores, model_b_scores)
```

📌 If `p-value < 0.05`, then Model B is **statistically better**.

---

## ✅ 4. A/B Testing (In Real-world Deployment)

Suppose you show **two versions of your website or app** (Version A and Version B) to users.  
You want to check which version gives more clicks or sales.

You can use:
- **Chi-square test** for categorical outcomes (e.g., clicked or not)
- **Z-test for proportions** to compare conversion rates

These tests help you take **data-backed decisions**.

---

## ❌ Where Statistical Tests Are NOT Used

- Inside ML/DL models like **Random Forest**, **XGBoost**, **CNN**, etc.
- These models use **loss functions and optimization**, not statistical hypothesis testing.
- They do not calculate **p-values** or **confidence intervals** by default.

---

## 🧠 Summary Table

| When Used                     | Why We Use Test                        |
|------------------------------|----------------------------------------|
| ✅ During EDA                | To check relation between features     |
| ✅ Before Modeling           | To validate training/test data quality |
| ✅ After Modeling            | To compare models statistically        |
| ✅ In A/B Testing            | To check if changes give real results  |
| ❌ Inside ML/DL Models       | Models use loss/gradients, not p-values|

📌 Statistical tests are **helpers to guide ML**, not part of model training itself.

---
