# Naive Bayes: Probability-Driven Classification

## Introduction to Naive Bayes Algorithm

*   **Naive Bayes Algorithm** is a **machine learning algorithm** used specifically for **classification problems**.
*   It can handle both **binary classification** (e.g., Yes/No) and **multi-class classification** (e.g., multiple categories).
*   To understand Naive Bayes, you need a **basic idea about probability**.
*   The entire Naive Bayes algorithm works based on **Bayes Theorem**.

## Key Probability Concepts for Naive Bayes

### Types of Events

There are two main types of events in probability:

*   **Independent Events**:
    *   **Definition**: One outcome **does not affect or change the probability of another outcome**.
    *   **Example**: Rolling a dice.
        *   The outcomes are 1, 2, 3, 4, 5, 6.
        *   **Probability of rolling a 1** is 1/6. Similarly, P(2) = 1/6, P(3) = 1/6, etc..
        *   Rolling a 1 doesn't change the probability of rolling a 2 in the next roll; values remain 1/6.

*   **Dependent Events**:
    *   **Definition**: One event **definitely changes the probability of the other event**.
    *   **Example**: Drawing marbles from a bag without replacement.
        *   **Scenario**: Bag has 3 orange marbles (O) and 2 yellow marbles (Y).
        *   **Question**: What is the probability of removing an orange marble, AND then a yellow marble?
        *   **Step 1: Probability of removing an orange marble first (P(O))**:
            *   Total orange marbles = 3. Total marbles = 5. So, P(O) = 3/5.
        *   **Step 2: Probability of removing a yellow marble AFTER an orange marble has been removed (P(Y given O))**:
            *   After removing one orange marble, there are now 4 marbles left in the bag (2 orange, 2 yellow).
            *   Probability of yellow marble is now 2/4 = 1/2.
            *   This is a **dependent event** because the first event (removing orange) changed the total number of marbles, thereby impacting the probability of the second event (removing yellow).
        *   **Combined Probability (P(O and Y)) for Dependent Events**:
            *   P(Orange and then Yellow) = P(Orange) \* P(Yellow **given** Orange has taken place).
            *   P(O and Y) = (3/5) \* (1/2) = 3/10.
            *   **Generic Formula for Dependent Events**: P(A and B) = P(A) \* P(B | A). This is **super important** for deriving Bayes Theorem.

### Conditional Probability

*   **Definition**: It's the **probability of an event (A) occurring given that another specific event (B) has already occurred**.
*   **Notation**: P(A | B) - "Probability of A given B".
*   **Example**: P(Yellow marble | Orange marble has already been taken out).

## Bayes Theorem

*   **Derivation**:
    *   Start with the general probability rule for two events A and B:
        *   P(A and B) = P(B and A).
    *   Expand using the dependent event formula:
        *   P(A) \* P(B | A) = P(B) \* P(A | B).
    *   Rearrange to solve for P(A | B):
        *   **P(A | B) = [P(A) \* P(B | A)] / P(B)**.
*   **Components of Bayes Theorem**:
    *   **P(A | B)**: This is what we want to calculate – **Probability of event A given B has occurred**. In machine learning, this is typically P(Class | Features).
    *   **P(A)**: **Probability of event A** (also known as Prior Probability of A). In ML, this is P(Class).
    *   **P(B | A)**: **Probability of event B given A has occurred** (also known as Likelihood). In ML, this is P(Features | Class).
    *   **P(B)**: **Probability of event B** (also known as Evidence or Marginal Probability). In ML, this is P(Features).

## Naive Bayes Algorithm in Machine Learning Problem Statement

*   **Goal**: In ML, we often have **independent features (X1, X2, X3)** and a **dependent feature (Y)**, which is our output (e.g., Yes/No).
*   **Application of Bayes Theorem**: We want to predict the class (Y) given the input features (X1, X2, X3).
    *   The equation we use is **P(Y | X1, X2, X3) = [P(Y) \* P(X1, X2, X3 | Y)] / P(X1, X2, X3)**.
*   **The "Naive" Assumption**: The Naive Bayes algorithm makes a "naive" assumption that **all input features (X1, X2, X3) are independent of each other given the class (Y)**. This simplifies the calculation significantly.
    *   Because of this assumption, **P(X1, X2, X3 | Y)** can be expanded as:
        **P(X1 | Y) \* P(X2 | Y) \* P(X3 | Y)**.
*   **Full Naive Bayes Formula (Simplified for ML)**:
    *   To predict a class (e.g., 'Yes' or 'No') given new features:
        **P(Yes | X1, X2, X3) = [P(Yes) \* P(X1 | Yes) \* P(X2 | Yes) \* P(X3 | Yes)] / P(X1) \* P(X2) \* P(X3)**.
        **P(No | X1, X2, X3) = [P(No) \* P(X1 | No) \* P(X2 | No) \* P(X3 | No)] / P(X1) \* P(X2) \* P(X3)**.
*   **Denominator Optimization**:
    *   Notice that the denominator **P(X1) \* P(X2) \* P(X3)** is **constant for all classes** (Yes, No, or any other class).
    *   Since we are interested in **comparing probabilities** (e.g., which class has the highest probability), we can **ignore or "cut" the denominator**.
    *   **Simplified Calculation**: We only need to compute the numerator for each class.
        *   **P(Yes | X1, X2, X3) ≈ P(Yes) \* P(X1 | Yes) \* P(X2 | Yes) \* P(X3 | Yes)**.
        *   **P(No | X1, X2, X3) ≈ P(No) \* P(X1 | No) \* P(X2 | No) \* P(X3 | No)**.
    *   The class with the **highest calculated numerator** is the predicted output.

# 🌤️ Naive Bayes — Play Tennis Prediction Example

## 🎯 Goal:
Predict whether a person will **Play Tennis** (`Yes` or `No`) given:
- **Outlook = Sunny**
- **Temperature = Hot**

---

## 📊 Dataset

| ID | Outlook   | Temperature | Play |
|----|-----------|-------------|------|
| 1  | Sunny     | Hot         | No   |
| 2  | Sunny     | Hot         | No   |
| 3  | Overcast  | Hot         | Yes  |
| 4  | Rain      | Mild        | Yes  |
| 5  | Rain      | Cool        | Yes  |
| 6  | Rain      | Cool        | No   |
| 7  | Overcast  | Cool        | Yes  |
| 8  | Sunny     | Mild        | No   |
| 9  | Sunny     | Cool        | Yes  |
| 10 | Rain      | Mild        | Yes  |
| 11 | Sunny     | Mild        | Yes  |
| 12 | Overcast  | Mild        | Yes  |
| 13 | Overcast  | Hot         | Yes  |
| 14 | Rain      | Mild        | No   |

- Total records = 14
- `Play = Yes` → 9 instances
- `Play = No` → 5 instances

---

## 1. 🧮 Prior Probabilities

| Class | Count | Probability |
|--------|--------|-------------|
| Yes    | 9      | P(Yes) = 9/14 ≈ 0.643 |
| No     | 5      | P(No) = 5/14 ≈ 0.357 |

---

## 2. 📈 Likelihood Tables (Conditional Probabilities)

### ➤ P(Outlook | Class)

| Outlook   | Count in Yes | P(Outlook \| Yes) | Count in No | P(Outlook \| No) |
|-----------|--------------|------------------|--------------|-----------------|
| Sunny     | 2            | 2/9 ≈ 0.222       | 3            | 3/5 = 0.6       |
| Overcast  | 4            | 4/9 ≈ 0.444       | 0            | 0/5 = 0.0       |
| Rain      | 3            | 3/9 ≈ 0.333       | 2            | 2/5 = 0.4       |

### ➤ P(Temperature | Class)

| Temperature | Count in Yes | P(Temp \| Yes) | Count in No | P(Temp \| No) |
|-------------|--------------|----------------|--------------|----------------|
| Hot         | 2            | 2/9 ≈ 0.222     | 2            | 2/5 = 0.4      |
| Mild        | 4            | 4/9 ≈ 0.444     | 2            | 2/5 = 0.4      |
| Cool        | 3            | 3/9 ≈ 0.333     | 1            | 1/5 = 0.2      |

---

## 3. 🔢 Apply Naive Bayes Formula

### Formula:
```
P(Class | Features) = P(Class) × P(Feature_i | Class)
```

We calculate for both classes: **Yes** and **No**

---

### 🔹 P(Yes | Sunny, Hot)

```
P(Yes | Sunny, Hot)
= P(Yes) × P(Sunny | Yes) × P(Hot | Yes)
= (9/14) × (2/9) × (2/9)
= 0.643 × 0.222 × 0.222
≈ 0.0317
```

---

### 🔹 P(No | Sunny, Hot)

```
P(No | Sunny, Hot)
= P(No) × P(Sunny | No) × P(Hot | No)
= (5/14) × (3/5) × (2/5)
= 0.357 × 0.6 × 0.4
≈ 0.0857
```

---

## 4. ⚖️ Normalize the Probabilities (Optional)

To get actual probability values:

| Class | Unnormalized | Normalized |
|-------|--------------|------------|
| Yes   | 0.0317       | 0.0317 / (0.0317 + 0.0857) ≈ **0.27** |
| No    | 0.0857       | 0.0857 / (0.0317 + 0.0857) ≈ **0.73** |

---

## ✅ Final Prediction

Since:

- P(Yes | Sunny, Hot) ≈ 27%
- P(No | Sunny, Hot) ≈ 73%

**🔮 Prediction: "No" — The person is unlikely to play tennis.**