# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as file:
        file_content = file.read()
    return file_content
# return "Hello World"


def count_words(str):
    # [assignment] Add your code here
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


file = open("story.txt", "r")
data = file.read()
print(count_words(data))

# return {"as": 10, "would": 20}
