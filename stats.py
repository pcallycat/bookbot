
def count_words(text):
    return len(text.split())

def count_character_occurances(text):
    characters = set(text.lower())
    counts = {}
    for character in characters:
        count = 0
        for letter in text:
            if letter.lower() == character:
                count += 1
        counts.update({character:count})
    return counts

def sort_on(dict):
    return dict["count"]

def sorted_character_occurances(occurances):
    sorted = []
    for key, value in occurances.items():
        if key.isalpha():
            sorted.append({"letter": key, "count": value})
    sorted.sort(reverse=True, key=sort_on)
    return sorted
