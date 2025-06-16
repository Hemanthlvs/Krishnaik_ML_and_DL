## Introduction to ELU (Exponential Linear Units)

*   ELU is another activation function used to solve problems associated with ReLU.
*   It offers more advantages compared to Leaky ReLU and PReLU.

## ELU Formula (Forward Propagation)

*   The formula for ELU depends on the input value `x`:
    *   If `x > 0`, the output is `x`.
    *   If `x <= 0`, the output is given by:
    ```
    ELU(x) = α * (e^x - 1)
    ```
	where `α` is a hyperparameter that defines the value to which an ELU saturates for negative net inputs.
*   Unlike ReLU, ELU does not produce a straight line for negative inputs; instead, it has a specific curve.

## ELU Backward Propagation

*   For `x > 0`, the derivative (value in backward propagation) is `1`.
*   For `x <= 0`, the derivative is given by:
    ```
	dELU/dx = α * e^x
	```

## Advantages of ELU

1.  **No Dead ReLU Issues**: ELU solves the dead ReLU problem because it never outputs zeros for values greater than zero, and for negative values, it provides non-zero outputs.
2.  **Zero-Centric / Zero-Centered**: This is a major advantage over Leaky ReLU and PReLU.
    *   Being "zero-centered" means that the mean of the output values is almost zero.
    *   All the points are centered around zero, and it also handles different negative values.
    *   This property allows for more efficient weight updates.

## Disadvantages of ELU

1.  **Computationally Intensive**: The mathematical equation used for ELU is slightly more complex than that of previous techniques like Leaky ReLU, making it more computationally intensive.