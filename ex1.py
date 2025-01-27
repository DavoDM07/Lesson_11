#Write a function that checks if a sentence is a pangram.


def pangram_question(question):
    key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    result = True
    for i in question:
        if i not in question:
            result = False
    return result

print(pangram_question('the quick brown fox jumps over the lazy dog'))
