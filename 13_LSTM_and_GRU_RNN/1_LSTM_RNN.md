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

# LSTM: Input Gate and Candidate Memory

## Input Gate (I_t)

*   **Purpose**: The Input Gate is responsible for deciding **which new information should be added** to the memory cell, based on the current context.
*   **Calculation (I_t)**:
    *   It **combines the current input (`x_t`) and the previous hidden state (`h_t-1`)**. This is done by concatenating them.
    *   This combined input is then passed through a neural network layer.
    *   It is multiplied by specific weights, denoted as `w_I`.
    *   A bias (`B_I`) is added.
    *   Finally, a **sigmoid activation function** is applied to this result, which outputs `I_t`.
    *   The operation for `I_t` is very similar to how the Forget Gate (`f_t`) is calculated.

## Candidate Memory (C_t)

*   **Purpose**: The Candidate Memory's task is to **generate new candidate information** that might be added to the memory cell. It represents potential new information.
*   **Calculation (C_t)**:
    *   Similar to the Input Gate, it also **takes the previous hidden state (`h_t-1`) and the current input (`x_t`)** as its inputs.
    *   These inputs are combined and passed through a hidden layer with specific weights, denoted as `w_C` or `w_fc`.
    *   A bias is added.
    *   Crucially, a **tanh activation function** is applied to this result. This produces a new candidate vector, often denoted as `C_t`.
    *   The output `C_t` will be a vector, for example, a three-dimensional vector like `[0 2 0]`.

## Combining Input Gate and Candidate Memory

*   **Operation**: To decide which part of the new candidate information (`C_t`) actually gets added to the memory cell, a **point-wise multiplication operation** is performed between the Input Gate's output (`I_t`) and the Candidate Memory's output (`C_t`).
*   **Significance**: This multiplication allows for **selectively adding new information**. For instance, if `C_t` contains important context, and `I_t` has values like `[2 4 6]`, the multiplication will ensure that only the relevant parts (e.g., `8` in `[0 8 0]`) are considered for addition, effectively "gating" the new information.

## Forming the Final Cell State (C_t)

The final cell state at the current timestep (`C_t`) is derived from two main operations:

1.  **Forgetting**: The previous cell state (`C_t-1`) is multiplied point-wise by the **Forget Gate's output (`f_t`)**. This step **removes or "forgets" information** that is no longer relevant, especially if the context is switching.
2.  **Adding New Information**: The output of the **point-wise multiplication between the Input Gate (`I_t`) and the Candidate Memory (`C_t`)** is then **added** to the result from the forgetting step. This is where new, relevant information is incorporated into the memory cell.

*   **Equation**: The overall process to get the final cell state `C_t` is expressed as: `C_t = (f_t * C_t-1) + (I_t * C_t)`.
    *   Here, `f_t * C_t-1` represents the forgotten or retained information from the previous state.
    *   `I_t * C_t` represents the new information being added.

## Example Context for Understanding

Consider the sentence: "I stay in India. (lots of sentences in middle.......). I speak ------."

*   The LSTM's memory cell will **save the "India" context**.
*   When predicting the next word ("dash"), the neural network uses this saved context.
*   The **Input Gate and Candidate Memory** work together to potentially **add new information** (e.g., related to languages spoken in India) to the cell state.
*   Simultaneously, the **Forget Gate** might discard other irrelevant information.
*   This combined process allows the LSTM to predict "Hindi" or "English" based on the long-term context of "India". The prediction is strongly based on the country context.

# LSTM RNNs: Output Gate and Memory Cells

## Output Gate (O_t)
*   The output gate is responsible for determining what information from the memory cell will be outputted as the **hidden state (short-term memory)**.
*   **Operation:**
    *   It first performs a **sigmoid activation function**.
    *   The sigmoid takes `x_t` (current input) and `h_t-1` (previous hidden state) as inputs, along with a bias `b0`. This part acts like a hidden neural network.
    *   The result of this sigmoid operation is `O_t`.
    *   Then, a `tanh` operation is applied to the **memory cell state (C_t)**.
    *   A **point-wise multiplication operation** is performed between the `tanh(C_t)` output and the `O_t` (sigmoid output).
*   **Purpose:** This operation produces `h_t`, which is the **hidden state** or **short-term memory**.
*   **Role of h_t**: The `h_t` represents the context of the current or one previous timestamp. This `h_t` is then sent to the next timestamp.

## Memory Cells
*   **Long-Term Memory (C_t)**: This is represented by `C_t` (the memory cell).
    *   Information `C_t` is passed from the previous timestamp (`C_t-1`) and updated.
    *   The memory cell plays a **very important role** because it retains information for a longer context. It remembers information that needs to be remembered.
*   **Short-Term Memory (h_t)**: This is represented by `h_t` (the hidden state).
    *   `h_t` is derived from the memory cell (`C_t`) through the output gate.
    *   `h_t` is related to the current or just one previous context.
    *   Both `C_t` and `h_t` are passed to the next timestamp/layer.
	
## Overall LSTM Process
*   The LSTM operates in a **looping manner** across different timestamps (e.g., T=1, T=2, T=3).
*   Within each LSTM cell, information is both added (by the input gate and candidate memory) and removed (by the forget gate).
*   The entire process involves **forward and backward propagation**.
*   **Weights** (`w_I`, `w_C`, `w_O`) are updated through backpropagation to reduce the loss.
    *   `w_O` (weight assigned to output) is specifically related to getting back the hidden state.
*   The final output, `Y_hat`, can be obtained by passing the output to a sigmoid function, depending on the desired output type.

## Summary of Gate Functions
*   **Forget Gate**: Removes information from the memory cell.
*   **Input Gate & Candidate Memory**: Add information to the memory cell.
*   **Output Gate**: Distinguishes between the memory cell (`C_t`) and the hidden state (`h_t`), which represents the short-term memory.
