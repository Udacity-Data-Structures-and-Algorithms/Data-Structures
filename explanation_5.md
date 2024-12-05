
## Problem 5: Blockchain

### Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

## Reasoning Behind Decisions:

The blockchain is implemented as a linked list. The `Block` class is used to create a block object that contains the data, the hash of the previous block, and the timestamp. The `Blockchain` class is used to create a blockchain object that contains the head of the blockchain. The `add_block` method is used to add a new block to the blockchain. 


## Time Efficiency:

    Time Complexity:
    ----------------
    - Initializing the blockchain: O(1)
    - Adding a block to the blockchain: O(n) where n is size of the block data
    - Accessing the last block: O(1)


## Space Efficiency:

    Space Complexity:
    -----------------
    O(b * d) where b is the number of blocks and d is the average size of the block data