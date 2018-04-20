# Blockchain Memory
It's correct because it exists.

## Basic Concept:
A BitCoin inspired way to store data. It guarantees that your data is not changed at the start of the file. It uses a strong cryptographic hashing algorithm to check the data. Instead of using hashes, we use salts to generate hashes with a certain desired characteristics. These characteristics are the 0's at the start of hex digested hash.

## File Architecture:
The file is split into different parts:
`<head>[order]<file>[filePath][length of data]</file></head>[DATA]<hash>sha512</hash><difficulty>[difficulty]</difficulty>`
- Inside the `<head>` is the `[order]` which specifies in which order the file should be extracted. (TO BE IMPLEMENTED)
- The `[filePath]` inside the `<file>` tag specifies in order which file's data will be stored and `[length of data]` tells you how much of that data is there.
- The actual file data starts after the `</file></head>` tags. It continues until the sum of all file data specified in the head tags reaches length of the `[DATA]`.
- Inside the `<hash>` tag lies the salt to make a certain amount of 0's in the file after the sha512 hex digest. 
- Difficulty is added to the end of the file to reduce ambiguity when it comes to the difficulty used for hashing.

## Helping and Contributing:
You may want to help this project grow with your own code and documentation. [Here](CONTRIBUTING.md) are the rules for contribution. If you want to post issues, bugs, program breaking things, please refere to our [Code of Conduct](CODE_OF_CONDUCT.md). If you want to use this program for your own work, [feel free to do so](LICENSE)!

## Milestones:
- __Finish Chains.py (currently reworking)__
- Make Reports inside Chains.py work
- Finish Verify.py
- Finish Extract.py

## Current Goals:
- Rewrite Chains.py to block unwanted characters in a directory
- Finish Verify.py
- Try and optimize
- Allow for translations
