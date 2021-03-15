import json

def preprocess(strings):
    return [" ".join(string.split()).replace(",", "").replace(".", "").replace("?", "") for string in strings]

def find_n_grams(string, n):
    words = string.split(" ")
    n_grams = []

    for i in range(len(words) - n + 1):
        n_grams.append(" ".join([words[i + idx] for idx in range(n)]))

    return n_grams

def find_modal_substring(strings, num_words, place):
    n_grams_per_string = [find_n_grams(string, num_words) for string in strings]
    max_num_occurences = 0
    modal_substring = None
    counter = 0

    for i in range(len(strings)):
        counter += 1
        if counter == place:
          n_grams = n_grams_per_string[i]

          for n_gram in n_grams:
              num_occurences = 1

              for j in range(i + 1, len(strings)):
                  if n_gram in n_grams_per_string[j]:
                      num_occurences += 1

              if num_occurences > max_num_occurences:
                  max_num_occurences = num_occurences
                  modal_substring = [n_gram, num_occurences]
              elif num_occurences == max_num_occurences and len(modal_substring) < len(n_gram):
                  max_num_occurences = num_occurences
                  modal_substring = [n_gram, num_occurences]
        else:
          continue

    return modal_substring

def processData(strings):
  return find_modal_substring(preprocess(strings), 2, 1)

strings = ["hello channing", "hello channing", "hello taylor", "hello david", "hello channing babb", "helloo channing babb", "wow channing babb", "channing is here"]

print(json.dumps(processData(strings)))
