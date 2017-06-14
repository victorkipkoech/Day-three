import re

def word_to_count(statement):
    words= statement.split()
    dic ={}


    for word in words:
        if word in dic:
            dic[word_to_count]+=1

        else:
            dic[word_to_count] =1
    return dic