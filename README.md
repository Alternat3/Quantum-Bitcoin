## Quantum-Bitcoin
A blockchain using 3-qubit Grover's algorithm to mine blocks using quantum accuracies as proof-of-work difficulty.

> - On line 2 of grovers.py you need to supply your own IBM-Q API code which can be recieved by signing up *[here](https://quantum-computing.ibm.com/login)* and then uncomment lines 2 and 3 in order for the quantum program to work (or just remove them if you're only going to use simualtor).
> - If there is no API key in this field the real quantum computing **will not work**.

To run the blockchain use `python blockchain.py` and select either simulator or real quantum computer at the prompt.
- The blockchain will then initiate the genesis block and blocks can begin to be added.
Then follow the prompts in the terminal to use the blockchain. Number of iterations used is displayed along with the final accuracy when the block is finally added to the blockchain.
