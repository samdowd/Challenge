
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

test = ['hello', 'hellop', 'hallo', 'halpo', 'george']
firstFriends = {}

def createCloseFriendsDict(wordbank): # Takes a wordbank and creates a dictionary with each of the worbank's words as keys and a list of that word's first degree friends as the respective values.
  for socialite in wordbank:
    for potentialFriend in wordbank:
      if isFriendsWith(socialite, potentialFriend): # If they're friends, add the new friend to the key's value list
        if socialite in firstFriends:
          firstFriends[socialite].append(potentialFriend)
        else:
          firstFriends[socialite] = [potentialFriend]
      else: # If they're not friends, create an empty list for the key if it does not have one.
        if socialite not in firstFriends:
          firstFriends[socialite] = []

createCloseFriendsDict(test)

def createSocialNetworks(friendbank): #
  for word in friendbank.keys():
    for friend in friendbank[word]:
      for friendsFriend in friendbank[friend]:
        if friendsFriend not in friendbank[word]:
          friendbank[word].append(friendsFriend)
  return friendbank
      
      
socialNetworks = createSocialNetworks(firstFriends)

print socialNetworks
