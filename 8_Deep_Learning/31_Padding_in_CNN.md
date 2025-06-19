# Padding in CNNs

## What is Padding?
*   Padding is a technique applied to prevent the loss of information in CNNs.
*   It involves adding one or more layers of "cushion" (extra pixels) around the border of the input image.
*   The number of layers added depends on the desired output size.

## How Padding Works (Example)
*   **Original:** A 6x6 image.
*   **With Padding:** If one layer of padding is added, the 6x6 image becomes an 8x8 image.
*   **After Convolution:** When this 8x8 padded image passes through a 3x3 filter, the output becomes 6x6.
*   This way, no information is lost, and the output image size matches the original input image size.

## Updated Formula for Output Size with Padding
*   The updated formula to calculate the output size after convolution with padding is: `n - f + 2p + 1`.
    *   `n` = original input size
    *   `f` = filter size
    *   `p` = number of padding layers

    *   **Example (6x6 image, 3x3 filter, desired output 6x6):**
        *   `6 = 6 - 3 + 2p + 1`
        *   `6 = 4 + 2p`
        *   `2 = 2p`
        *   `p = 1`
        *   This means one layer of padding is needed on all sides.

## Types of Padding Techniques
There are two common ways to fill the values in the added padding layers:
1.  **Zero Padding:** All the added cushion pixels are filled with zeros. This is the most common method.
2.  **Neighbor Padding:** The value of the closest neighboring pixel from the original image is assigned to the padding pixel. For example, if the border pixels are '1', the padding pixels next to them would also be '1'.

## Importance of Padding
*   The main goal of padding is to prevent the loss of information from the image during convolution operations.
*   It helps ensure that the output image after convolution has the same size as the initial input image.