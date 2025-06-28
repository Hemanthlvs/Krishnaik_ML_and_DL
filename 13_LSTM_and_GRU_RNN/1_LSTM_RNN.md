# Introducing LSTM: Overcoming RNN's Long-Term Memory Shortcomings

#### Problems with RNNs
*   RNNs are **not able to solve long-term dependencies**.
*   This inability is due to the **vanishing gradient problem**.

#### Introduction to LSTM
*   LSTM stands for **Long Short-Term Memory** RNN.
*   It is a new variant of Recurrent Neural Networks (RNNs).
*   LSTM RNN is designed to **solve the long-term dependency problem** that RNNs face.
*   **LSTM RNN adds a long-term memory component** to the existing short-term memory.

#### Long-Term Memory (Memory Cell) in LSTM
*   The long-term memory is represented as a **continuous moving line** (analogous to an airport conveyor belt).
*   The main purpose of this memory is to **add context when required and remove context when not required**.
*   This memory cell acts like a **library book** or **brain cells**, remembering important information for longer periods when needed (e.g., for an "exam day") and discarding it when not.

# LSTM RNN: Architecture and Core Operations

*   **Unlike simple RNNs**, which have one feedback loop, LSTM RNNs have an additional feedback loop that acts as a **long-term memory**.

### Key Components (Gates)

A single hidden neuron in an LSTM RNN has three important gates:

*   **Forget Gate**: This is the first part of the LSTM neuron. It decides what information to remove from the memory cell.
*   **Input Gate & Candidate Memory**: This is the second part. It is responsible for adding new information to the memory cell.
*   **Output Gate**: This is the third part. It determines what information will be output from the LSTM.

### Inputs and States

*   **`x(T)`**: This represents the **inputs** passed with respect to a specific **timestamp** (e.g., current time).
*   **`h(T-1)`**: This is the **hidden state** of the **previous timestamp's hidden neuron**. It acts as a **short-term memory**.
*   **`C(T-1)`**: This is the **memory cell of the previous timestamp**. It represents the **long-term memory**.
*   **`C(T)`**: This is the **memory cell's state for the current timestamp** after information has been removed and added.

### Notations and Operations

Several notations and operations are used within the LSTM architecture diagrams:

*   **Neural Network Operator Layer** (represented by shapes containing "sigmoid" or "tanh"):
    *   This indicates a **hidden neuron or hidden layer neuron** where an **activation function** (like sigmoid or tanh) has been applied to the neurons.
    *   Inputs `x(t)` and `h(t-1)` are combined and then sent to this layer.
*   **Point-wise Operations** (pink color operations):
    *   **Point-wise Multiplication** (circle with `x` inside): Multiplies each corresponding element of two vectors.
    *   **Point-wise Addition** (circle with `+` inside): Adds each corresponding element of two vectors.
    *   **Point-wise TanH Operation** (circle with `tan H` inside): Applies the `tanh` activation function to each element of a single vector (e.g., `tanh(1)`, `tanh(2)`, `tanh(3)`).
*   **Vector Transfer** (arrows):
    *   Indicates that a vector is being transferred from one state or part of the network to another.
*   **Concatenate** (represented by combining lines/vectors):
    *   Means **combining two vectors** into a single, larger vector, rather than adding them.
    *   This combined vector is then sent as input to other neurons or hidden layers.
*   **Copy**:
    *   Allows for creating a **duplicate copy** of a vector.

### Memory Cell

*   The top line in the LSTM diagram is called the **memory cell**.
*   It is specifically designed for **long-term memory**.
*   It's main function is to **save information** that is needed and **remove information** that is not.

# LSTM RNN: Understanding the Forget Gate

## Purpose of the Forget Gate
*   The forget gate's primary role is to **decide what information to "forget" or "let go" from the memory cell, and what to keep**, based on the current context.
*   It can completely remove previous context, retain all of it, or partially remove specific parts.

## Inputs to the Forget Gate
*   The forget gate takes two main inputs:
    *   `x_t`: The **current input word vector** at time `t`. Words are converted into vectors (e.g., 3 or 4 dimensions).
    *   `h_{t-1}`: The **hidden state from the previous neuron** (previous timestamp). Its dimension matches that of the current word vector (e.g., 3 dimensions if `x_t` is 3 dimensions, or if `c_{t-1}` is 3D).
*   These two inputs (`x_t` and `h_{t-1}`) are **concatenated** (combined).
    *   Example: If `h_{t-1}` is 3D and `x_t` is 4D, the concatenated input will be 7 dimensions (3+4). This combined input becomes the input to the neural network for the forget gate.

## Neural Network Structure for the Forget Gate
*   The concatenated input (`h_{t-1}` and `x_t`) is fed into a **neural network**.
*   This network typically has a **hidden layer** with neurons (e.g., three hidden neurons were used in the example).
*   An **activation function** (e.g., Sigmoid, which outputs values between 0 and 1) is applied to each hidden neuron.
*   Neurons also have biases.
*   The output of this neural network is a vector called `f_t` (forget gate output).
*   The dimensions of `f_t` will match the dimensions of `c_{t-1}` (the previous memory cell state) and `h_{t-1}`.
    *   Example: If the concatenated input is 1x7 and there are 3 hidden neurons, the weights connecting them would be 7x3. The dot product of a 1x7 input with 7x3 weights results in a 1x3 output (`f_t`). This explains why `h_{t-1}` and `c_{t-1}` would also be 3-dimensional in this example.

## The Point-wise Operation (Core of Forgetting)
*   The calculated `f_t` vector then performs a **point-wise multiplication operation** with `c_{t-1}` (the previous memory cell state).
*   **How `f_t` affects `c_{t-1}` (Memory Cell):**
    *   **If `f_t` is `[0 0 0]`**: This indicates that the complete sentence context has changed. When multiplied point-wise with `c_{t-1}`, it **makes all previous context in the memory cell entirely zero**, effectively removing it.
    *   **If `f_t` is `[1 1 1]`**: This means **nothing is removed** from the `c_{t-1}` memory cell. The previous context is considered important and is fully retained.
    *   **If `f_t` contains values between 0 and 1 (e.g., `[0.5, 1, 0.5]`)**: This signifies that **some context is partially removed** or scaled down, while other parts are retained. For example, `` multiplied by `[0.5, 1, 0.5]` becomes `[3, 8, 4.5]`, showing selective removal.

## Conclusion
*   The forget gate intelligently decides **which information to "let go" or "not let go"** from the memory cell based on the current input context.
*   This operation allows the LSTM to **selectively remove or retain information** over long sequences, preventing vanishing or exploding gradients and managing long-term dependencies effectively.
