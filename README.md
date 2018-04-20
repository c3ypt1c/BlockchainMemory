# BlockchainMemory
It's correct because it exists.

## Basic Concept:
A BitCoin inspired way to store data. It guarantees that your data is not changed at the start of the file. It uses a strong cryptographic hashing algorithm to check the data. Instead of using hashes, we use salts to generate hashes with a certain desired characteristics. These characteristics are the 0's at the start of hex digested hash.

## File Architecture:
The file is split into different parts:
"""<head>[order]<file>[filePath][length of data]</file></head>[DATA]<hash>sha512</hash><difficulty>[difficulty]</difficulty><"""
- Inside the "<head>" is the "[order]" which specifies in which order the file should be extracted. (TO BE IMPLEMENTED)
- The "[filePath]" inside the "<file>" tag specifies in order which file's data will be stored and "[length of data]" tells you how much of that data is there.
- The actual file data starts after the "</file></head>" tags. It continues until the sum of all file data specified in the head tags reaches length of the "[DATA]".
- Inside the "<hash>" tag lies the salt to make a certain amount of 0's in the file after the sha512 hex digest. 
- Difficulty is added to the end of the file to reduce ambiguity when it comes to the difficulty used for hashing.

## Milestones:
[x] - Finish Engine.py
[-] - Finish Chains.py (currently reworking)
	[ ] - Make Reports work
[ ] - Finish Verify.py
[ ] - Finish Extract.py
[x] - Finish ConfigChanger.py

## Current Goals:
[x] - Embed the difficulty into the file instead of guessing
[ ] - Rewrite Chains.py to block unwanted characters in a directory
[ ] - Finish Verify.py
[ ] - Try and optimize
