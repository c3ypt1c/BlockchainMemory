# BlockchainMemory
Self verifying memory chain.

## Basic Concept:
It's basically a BitCoin inspired way to store data. It guarantees that your data is not changed at the start of the file. It uses a strong cryptographic hashing algorithm to check the data. Instead of using hashes, we use salts. 

## File Architecture:
The file is split into different parts:
"""<head>[order]<file>[filePath][length of data]</file></head>[DATA]<hash>sha512</hash>"""
- Inside the "<head>" is the "[order]" which specifies in which order the file should be extracted. (TO BE IMPLEMENTED)
- The "[filePath]" inside the "<file>" tag specifies in order which file's data will be stored and "[length of data]" tells you how much of that data is there.
- The actual file data starts after the "</file></head>" tags. It continues until the sum of all file data specified in the head tags reaches length of the "[DATA]".
- Inside the "<hash>" tag lies the salt to make a certain amount of 0's in the file after the sha512 hex digest. 
