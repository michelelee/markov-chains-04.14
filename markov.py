import sys


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    # corpus is a string
    words_list = corpus.rstrip().split(" ") # put this on one line chained
    #words = words.strip("\n") this doesnt work because words is a list and you cant 
    # 'strip' a list... we may need a for loop! 
    words_list = [w.rstrip("\n.,").lower() for w in words_list]
    # we started with the for loop below and then condensed it into list_comprehension above.
    # for w in words:
    #     stripped_words.append(w.rstrip())
    
    # now create dictionary!!
    bigrams_dictionary = {}
    tuples_list = []
    for word in words_list:
        if word != words_list[-1]:
            tuples_list.append((word, words_list[words_list.index(word) + 1]))

    print tuples_list

    # for word in words_list:
    #     # first word = "some"
    #     bigram_key = (word, word + 1)
    #     index = words_list.index("Some")
    #     bigram_key = (words_list[index], words_list[index+1])
    #     bigrams_dictionary(bigram_key) = [words_list[index+2]]

    # for idx, word in enumerate(words_list): 
    #     next_word = words_list[idx+1]
    #     next_next_word = words_list[idx+2]
    #     if idx+2 < 7:    
    #         bigram_key = (word, next_word)
    #         bigrams_dictionary[bigram_key] = [next_next_word]

    #key- this will need to be a tuple for the first word in the bigram followed by the second word
    # pseudo code for how to get key 'key = (word in words_list, word+1 in words_list)'

    # bigrams_dictionary(key) = ""

    # # my_list = ['a', 'b', 'c']
    # # my_list[0] = "z"

    # #value- we're going to append this to the dictonary through a for loop 

    # print "This is words:", words_list
    
    # return {}
    # print tuples_list
    



# #def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text is here,\n Some text is there."
# Get a Markov chain

make_chains(input_text)
# print input_text
# chain_dict = make_chains(input_text)
# print "This is the dictionary:", chain_dict
# Produce random text
# random_text = make_text(chain_dict)

# print random_text
