# Convolutional Neural Networks (CNNs): The Intuition of Filters

## Introduction to Convolution Operation
*   The first operation in a Convolutional Neural Network (CNN) is called the **convolution operation**.
*   It helps CNNs understand how they work by processing images and finding information within them, similar to how the visual cortex processes information.

## Image Representation
*   Images are made up of pixels.
*   A grayscale image can be represented as `height x width x 1` (e.g., 6x6x1 for a 6x6 pixel image).
*   Pixel values usually range from 0 to 255.
    *   0 typically represents black color.
    *   255 typically represents white color.

## Normalization (Pre-processing Step)
*   **Step 1:** Before starting the convolution operation, you need to **normalize** the pixel values.
*   Normalization means converting all pixel values to a range between 0 and 1.
*   This is a mandatory step in any CNN and helps with further processing.
*   To normalize, divide all pixel values by 255 (the maximum pixel value).
    *   0 becomes 0 (0/255).
    *   255 becomes 1 (255/255).

## Filters (Kernels)
*   In CNNs, **filters** (also called kernels) perform the work of processing information, similar to layers like V1, V2 in the visual cortex.
*   A filter is a small matrix (e.g., 3x3 matrix).
*   **Purpose of filters:** To extract information from images, such as vertical edges, horizontal edges, round edges, or other patterns.
*   Filters can have different sizes (e.g., 3x3, 5x5, 7x7).

## How Convolution Operation Works
1.  **Placement:** The filter (e.g., 3x3) is placed on top of a section of the image (e.g., the first 3x3 pixels).
2.  **Multiplication and Summation:** Each value in the filter is multiplied by the corresponding pixel value directly underneath it.
3.  **Summation:** All these multiplied results are then added together (summed up) to produce a single output value.
## Stride
*   **Stride** is the "jump" or movement of the filter across the image.
*   If `stride = 1`, the filter moves one position (pixel) to the right.
*   Once the filter reaches the rightmost edge, it moves down to the next row and continues moving to the right.
*   This process continues until the filter has covered the entire image.

## Output and Edge Detection
*   The convolution operation produces a new, smaller output matrix (e.g., a 6x6 image with a 3x3 filter results in a 4x4 output).
*   **De-normalization (for understanding):** The output values can be de-normalized (e.g., converting back to 0-255 scale) to visualize the result.
    *   For example, if the output contains 0s and -4s, after de-normalization, 0s might become 255 (white) and -4s might become 0 (black).
*   **Information Extraction:** Certain filter values are designed to detect specific features. For instance, a "vertical edge filter" will highlight vertical edges in the image.
    *   This is similar to how the V1 layer in the visual cortex is responsible for finding edges and orientations.
*   Different filters can find different features (e.g., vertical edges, horizontal edges, round edges).

## Filter Values (Predefined vs. Learned)
*   While some filters have predefined values (like the vertical edge filter example), in real CNNs, the filter values are **not fixed**.
*   Instead, they are **randomly initialized** and then updated or "learned" during the training process through forward and back propagation.
*   A CNN can have many different filters, each identifying different features, leading to multiple output matrices.

## Output Size Calculation and Information Loss
*   The output size of the convolved image can be calculated using the formula: `(n - f + 1)`.
    *   `n` = size of the input image (e.g., 6 for 6x6).
    *   `f` = size of the filter (e.g., 3 for 3x3).
    *   Example: `(6 - 3 + 1) = 4`, resulting in a 4x4 output.
*   A consequence of this operation is that the output image is smaller than the input, meaning some **information is lost**.