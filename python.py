import csv

initialList = []
with open('randomlist.txt') as bank:
    for row in csv.reader(bank):
        initialList.append(row[0])

print initialList

def isFriendsWith(word1, word2):
    if(len(word1) == len(word2)): # If the words are the same length, checks how many characters are different.
        similarity = 0
        i = 0
        for char in word1: # Runs through each character in word1 and checks if it is equal to the character in the same position in word2.
            if char == word2[i]:
                similarity += 1
            i += 1
        if(similarity + 1 == len(word1)):
            return True # Returns True only if exactly one character is different
        else:
            return False
    elif(len(word1) > len(word2)): # If word1 is longer, runs through each character in word 1, removing it and checking the new string against word2.
        charPosition = 0
        for char in word1:
            attempt = word1[:charPosition] + word1[charPosition+1:]
            if attempt == word2:
                return True
            charPosition += 1
        return False
    elif(len(word1) < len(word2)): # If word2 is longer, runs through each character in word 2, removing it and checking the new string against word1.
        charPosition = 0
        for char in word2:
            attempt = word2[:charPosition] + word2[charPosition+1:]
            if attempt == word1:
                return True
            charPosition += 1
        return False

firstFriends = {}

def createCloseFriendsDict(wordbank): # Takes a wordbank and creates a dictionary with each of the wordbank's words as keys and a list of that word's first degree friends as the respective values.
  for socialite in wordbank:
    if socialite not in firstFriends:
        firstFriends[socialite] = []
    for potentialFriend in wordbank:
      if isFriendsWith(socialite, potentialFriend): # If they're friends, add the new friend to the key's value list
        if potentialFriend != socialite and potentialFriend not in firstFriends[socialite]:
          firstFriends[socialite].append(potentialFriend)

createCloseFriendsDict(initialList)

def createSocialNetworks(friendbank): # Appends friends's friends ... 's friends to create social networks
  for word in friendbank.keys(): # Iterates through all words
    for friend in friendbank[word]: # Iterates through all friends for each word
      for friendsFriend in friendbank[friend]: # Iterates through all that friend's friends
        if friendsFriend not in friendbank[word] and friendsFriend != word:
          friendbank[word].append(friendsFriend) # Adds non-duplicates to list
  return friendbank

socialNetworks = createSocialNetworks(firstFriends)

print socialNetworks
