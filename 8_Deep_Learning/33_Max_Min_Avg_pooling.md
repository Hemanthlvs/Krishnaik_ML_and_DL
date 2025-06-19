# CNN: Pooling Layers and Location Invariance

### A. Max Pooling
*   **Definition**: Max pooling is applied on the output of a convolution layer (after the ReLU operation).
*   **Purpose**: The main concept behind max pooling is **location invariance**.
    *   **Location Invariance**: Means that wherever specific images or shapes are present (e.g., cat faces, car wheels), max pooling should be able to extract that specific part.
    *   It helps in extracting important information and focusing on key features (like round edges of a cat face or car wheels), regardless of their exact position. It concentrates on the highest intensity pixels.
*   **How it Works**:
    *   A filter (e.g., 2x2) is applied over the output of the convolution layer.
    *   Within the filter's window, the **maximum value** is selected.
    *   After selecting the maximum value, the filter moves with a **stride of two** (not one), taking large jumps to pick out maximum intensity pixels. This means it does not repeat previous areas.
    *   Max pooling can be applied to outputs from multiple filters (F2, F3, F4, etc.).

### B. Min Pooling
*   **Definition**: Instead of taking the maximum element, min pooling takes the **minimum element** from the filter's window.
*   **Purpose**: To focus on the minimum intensity pixels available in the image. The choice between pooling methods depends on the specific use case.

### C. Average Pooling (Mean Pooling)
*   **Definition**: Average pooling (also called mean pooling) calculates the **average of all values** within the filter's window.

## CNN Architecture Structure
*   A typical CNN architecture involves horizontally stacking convolution layers and pooling layers multiple times.
*   The general flow is: Input -> Convolution Layer (multiple filters + ReLU) -> Max Pooling -> Output.
*   This sequence (Convolution Layer + Max Pooling) can be repeated any number of times to find more information from the image.
*   Finally, a **fully connected layer** is applied at the end.