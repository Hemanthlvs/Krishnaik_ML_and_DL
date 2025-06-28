### Introducing LSTM: Overcoming RNN's Long-Term Memory Shortcomings

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