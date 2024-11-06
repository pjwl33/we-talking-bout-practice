from collections import deque

# Explanation:
# Case Insensitivity: Converts the words to lowercase to ensure that the algorithm is case-insensitive.
# Breadth-First Search (BFS): This algorithm uses BFS to explore all words reachable by changing one letter at a time. BFS is suitable for finding the shortest path.
# Word Generation: It generates new words by replacing each character in the current word with every letter from 'a' to 'z' and checks if this new word is in the dictionary.
# Termination: If the end_word is reached, it returns the sequence of words as the path. If no valid path is found, it returns False.

def wordLadder(startWord, endWord, wordDict):
    # convert to lowercase
    startWord = startWord.lower()
    endWord = endWord.lower()
    wordDict = set(word.lower() for word in wordDict)

    # ensure word is in the dict for end
    if endWord not in wordDict:
        return False

    # Init the queue with starting word and empty path
    q = deque([(startWord, [startWord])])

    while q:
        currWord, path = q.popleft()        
             
        # If we've reached the end word, return the path including endWord
        if currWord == endWord:
            return path
        
        # Generate all possible words by changing one letter at a time
        for i in range(len(currWord)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = currWord[:i] + c + currWord[i + 1:]
                
                # Only consider the word if it's in the dictionary and not visited
                if nextWord in wordDict:
                    q.append((nextWord, path + [nextWord]))
                    wordDict.remove(nextWord)  # Mark this word as visited by removing it

    # If no valid transformation is found, return False
    return False