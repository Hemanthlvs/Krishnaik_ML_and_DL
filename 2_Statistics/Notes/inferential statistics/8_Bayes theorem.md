# Bayes Theorem:

## Introduction to Bayes Statistics and Bayes Theorem

*   **Bayes Theorem** is a very important concept, especially for machine learning algorithms like Naive Bayes, because it is entirely based on probabilities.
*   **Bayesian statistics** is an approach to data analysis and parameter estimation that uses Bayes Theorem. It helps in performing data analysis and estimating population parameters.

## Key Probability Concepts

Before understanding Bayes Theorem, it's crucial to understand two types of events:

### A. Independent Events

*   **Definition:** Events where the outcome of one event does not affect the outcome of another event.
*   **Examples:**
    *   **Rolling a dice:** The probability of rolling any number (e.g., 1) is 1/6, and this doesn't change for subsequent rolls. Each roll is independent of the previous one.
    *   **Tossing a coin:** The probability of getting a head or a tail is 0.5. If a head comes now, the next toss's outcome is not impacted; all events are independent.

### B. Dependent Events

*   **Definition:** Events where the outcome of one event impacts the outcome of a subsequent event.
*   **Example (Marbles in a bag):**
    *   Imagine a bag with 3 yellow marbles and 2 red marbles (total 5 marbles).
    *   **Event 1: Taking out a red marble.** The probability of drawing a red marble is 2/5 (2 red marbles out of 5 total).
    *   **Event 2: Taking out a yellow marble AFTER taking out a red marble.**
        *   After the first red marble is taken out, there are only 4 marbles left in the bag.
        *   The probability of drawing a yellow marble now becomes 3/4 (3 yellow marbles out of 4 total).
    *   This is a dependent event because taking out the first marble **reduced the total number of marbles from 5 to 4**, impacting the probability of the second event.

## Conditional Probability

*   **Concept:** Used to calculate probabilities for dependent events.
*   **Formula for Dependent Events (e.g., red AND yellow):**
    *   `P(Red AND Yellow) = P(Red) * P(Yellow given Red event has occurred)`.
    *   **Conditional Probability:** `P(Yellow given Red)` means the probability of yellow occurring when the red event has already happened.
    *   In the marble example, `P(Red AND Yellow) = (2/5) * (3/4) = 6/20`.

## Derivation of Bayes Theorem

Bayes Theorem is derived from the commutative property of dependent events:

*   We know `P(A AND B) = P(A) * P(B | A)`.
*   Also, `P(B AND A) = P(B) * P(A | B)`.
*   Since `P(A AND B)` is the same as `P(B AND A)`:
    `P(A) * P(B | A) = P(B) * P(A | B)`.
*   Rearranging this equation to solve for `P(A | B)` gives us **Bayes Theorem**:
    **`P(A | B) = [P(A) * P(B | A)] / P(B)`**.
*   **Alternative form:** You might also see `P(B | A) = [P(B) * P(A | B)] / P(A)`. Both are Bayes Theorem, just for different events.

## Understanding Bayes Theorem Parameters

In the Bayes Theorem formula (`P(A | B) = [P(A) * P(B | A)] / P(B)`):

*   **A, B:** These represent **events**.
*   **P(A | B):** This is the **probability of event A given that event B is true** (i.e., event B has already occurred).
*   **P(B | A):** This is the **probability of event B given that event A is true** (i.e., event A has already occurred).
*   **P(A):** This is the **independent probability of event A**.
*   **P(B):** This is the **independent probability of event B**.

## Application in Machine Learning (Naive Bayes)

Bayes Theorem is very useful in machine learning, particularly for the Naive Bayes algorithm.

*   **Scenario:** Consider a dataset with features like `size of house (X1)`, `number of rooms (X2)`, `location (X3)`, and an output feature like `price (Y)`.
    *   `X1, X2, X3` are **independent/input features**.
    *   `Y` is the **output/dependent feature**.
*   **Goal:** Use the input features to **predict the price** (output feature).
*   **Applying Bayes Theorem:** In machine learning, we often want to find the **probability of an output `Y` given the input features `X1, X2, X3`**.
*   The Bayes Theorem equation for this scenario is:
    **`P(Y | X1, X2, X3) = [P(Y) * P(X1, X2, X3 | Y)] / P(X1, X2, X3)`**.
*   This equation is a core part of the **Naive Bayes algorithm** and is used to calculate the probabilities of the output feature `Y`. Knowing this formula is key to understanding Naive Bayes.