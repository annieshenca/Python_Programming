class Palindrome:
  @staticmethod
  def is_palindrome(word):
    # Please write your code here.
    
    # Step1: turn all characters lower case
    word = word.lower()
    l = len(word)
    mid = int(l/2)
    
    # Step2: Loop through from index 0 to the middle point on the word.
    # Closing towards the center and check if the character in the front is
    # the same as the back.
    for idx in range(0,mid):
        if word[idx] != word[l-1-idx]:
            return False
    return True


# Driver code.
word = input()
print(Palindrome.is_palindrome(word))
