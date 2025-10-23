# 🧠 Using KMeans Clustering as a Feature in Machine Learning

Combining **unsupervised learning** (like clustering) with **supervised learning** can enhance a model's performance by capturing hidden patterns. This document explains how to use **KMeans clustering** to create a new feature and use it in a supervised ML pipeline.

---

## 🔍 Why Add Cluster Labels?

| Benefit | Description |
|--------|-------------|
| Reveal structure | Captures hidden patterns not obvious from raw features |
| Add information | Cluster label acts as an additional feature |
| Boost performance | Helps simpler models (like Logistic Regression) capture non-linear separations |
| May not always help | Needs testing — clustering must reflect useful structure |

---

## 🧪 Example: Iris Dataset with KMeans + Logistic Regression

```python
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load and scale data
data = load_iris()
X = StandardScaler().fit_transform(data.data)
y = data.target

# Step 1: Use KMeans to generate cluster labels
kmeans = KMeans(n_clusters=3, random_state=0)
cluster_labels = kmeans.fit_predict(X)

# Step 2: Add cluster labels as a new feature
X_with_cluster = np.hstack((X, cluster_labels.reshape(-1, 1)))

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_with_cluster, y, test_size=0.2, random_state=42)

# Step 4: Train a classifier
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 5: Evaluate performance
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
