'''
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks,
and/or contains at least one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.
Input: Subject line as a string.
Output: Boolean.
Precondition: Subject can be up to 100 letters
'''


def is_stressful(subj):
    red_words = ["help", "asap", "urgent"]
    chunks = subj.split(' ')
    for word in chunks:
         if str.isupper():
             pass
    return False


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

