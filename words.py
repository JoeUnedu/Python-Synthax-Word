#For a list of words, print out each word on a separate line, but in
# all uppercase. How can you change a word to uppercase? Ask Python
# for help on what you can do with strings!

#Turn that into a function, print_upper_words. 
# Test it out. (Don’t forget to add a docstring to your function!)

#Change that function so that it only
# prints words that start with the letter ‘e’ (either upper or lowercase).

#Make your function more general: you 
# should be able to pass in a set of letters, and 
# it only prints words that start with one of those letters.

def print_upper_words(words, must_start_with = {}):
  # len returns the number of items in an object
  #it also returns the number of character in the string if an object
  if (len(must_start_with) == 0):
    # let turn the words to upper case
    # we will need line 21 when we get to  line 32
    for word in words:
      print(word.upper())
      
  else:
         # At this time let set  an uper  sets 
         # that we need to add our characters or letters to it
      must_start_with_upper = set()
         # it is important we run a for loop cause we are about to add 
      for char in must_start_with:
        # we have succeded in adding  upper  char here for future ref.
        must_start_with_upper.add(char[0].upper())
        # let grab from line 21. if upper, print!
      for word in words:
          if (word[0].upper() in must_start_with_upper):
            print(word.upper())
        
 
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                  must_start_with={"h", "y"})