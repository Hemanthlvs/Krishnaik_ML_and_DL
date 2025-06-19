# RGB and Grayscale Images Explained

## Image Basics

*   **Pixels**: Images are divided into small units called pixels.
*   **Pixel Values**: The value of each pixel typically ranges from 0 to 255.
*   **Image Dimensions**: Image dimensions are usually described as `Width x Height x Channels`.
    *   The first two numbers (`Width x Height`) represent the number of pixels horizontally and vertically.
    *   The last number represents the number of channels.

## Grayscale Images

*   **Appearance**: Grayscale images are also known as black and white images.
*   **Channels**: They have only **one** channel.
*   **Representation/Dimensions**: An image with 6 pixels horizontally and 6 pixels vertically would be represented as `6 x 6 x 1`.
*   **Pixel Values**: Every pixel in a grayscale image has a value ranging from 0 to 255 within its single channel.

## RGB (Colored) Images

*   **Appearance**: These are colored images.
*   **Channels**: They are divided into **three** channels:
    *   Red channel
    *   Green channel
    *   Blue channel
*   **Combination**: When these three channels are combined, they form any colored image. The final color depends on the values in each Red, Green, and Blue channel.
*   **Representation/Dimensions**: An image with 4 pixels horizontally and 4 pixels vertically would be represented as `4 x 4 x 3`.
*   **Pixel Values**: Each pixel within **each** of the Red, Green, and Blue channels has a value ranging from 0 to 255.