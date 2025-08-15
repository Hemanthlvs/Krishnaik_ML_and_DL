# Hyperparameter Tuning: GridSearchCV vs RandomizedSearchCV

## 🔍 Why Hyperparameter Tuning?
To find the best values of model parameters (like C, alpha, max_depth, etc.) that improve model accuracy and reduce error.

## ✅ GridSearchCV

- Tries all possible combinations from the parameter grid.
- Very accurate because it checks every option.
- Uses cross-validation to evaluate each combination.
- Slower when parameter grid is large.
- Best for small search space or when we have time.

## ⚡ RandomizedSearchCV

- Selects random combinations from the parameter space.
- Faster than GridSearchCV.
- Does not guarantee best result, but gives good enough.
- Useful when there are many parameters or less time.

## 🆚 Difference Between GridSearchCV and RandomizedSearchCV

| Feature                | GridSearchCV            | RandomizedSearchCV       |
|------------------------|-------------------------|---------------------------|
| Checks all combinations| ✅ Yes                  | ❌ No (random selection)  |
| Speed                  | 🐢 Slow for large grid   | ⚡ Fast                   |
| Accuracy               | ✅ More accurate         | ⚠️ Approximate            |
| Best for               | Small parameter space   | Large parameter space     |

## 📌 When to Use What?

- Use **GridSearchCV** when:
  - You have fewer hyperparameters.
  - You want the exact best settings.
  - Time is not a big issue.

- Use **RandomizedSearchCV** when:
  - You have many parameters to test.
  - You want faster results.
  - You are okay with near-best performance.
