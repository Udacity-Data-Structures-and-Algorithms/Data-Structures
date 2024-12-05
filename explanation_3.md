## Problem 3: Huffman Coding

Overview - Data Compression

In general, a data compression algorithm reduces the amount of memory (bits) required to represent a message (data). The compressed data, in turn, helps to reduce the transmission time from a sender to receiver. The sender encodes the data, and the receiver decodes the encoded data. As part of this problem, you have to implement the logic for both encoding and decoding.

A data compression algorithm could be either lossy or lossless, meaning that when compressing the data, there is a loss (lossy) or no loss (lossless) of information. The Huffman Coding is a lossless data compression algorithm. Let us understand the two phases - encoding and decoding with the help of an example.

## Reasoning Behind Decisions:

### Encoding:

The encoding phase consists of the following steps:

1. Calculate the frequency of each character in the message using defaultdict.
2. Build the Huffman Tree using heapq and generate the Huffman codes for each character.
3. Encode the text into its compressed form.

### Decoding:

The decoding phase consists of the following steps:

1. Decode the encoded text.
2. Retrieve the encoded text from the Huffman Tree.


### Efficiency:

The efficiency of the code is determined by the time and space complexity of the code. The time complexity of the code is O(n log n), where n is the number of characters in the message. The space complexity of the code is O(n).


## Time Efficiency:

### Encoding:

1. Calculate the frequency of each character in the message: O(n)
2. Build and sort a list of tuples from lowest to highest frequencies: O(n log n)
3. Build the Huffman Tree by assigning a binary code to each letter: O(n log n)
4. Encode the text into its compressed form: O(n)

### Decoding:

1. Decode the encoded text: O(n)
2. Retrieve the encoded text from the Huffman Tree: O(n)


## Space Efficiency:

The space efficiency of the code is O(n), where n is the number of characters in the message.



