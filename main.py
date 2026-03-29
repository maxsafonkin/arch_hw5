import requests
from collections import Counter


def get_text(url):
    response = requests.get(url)
    return response.text


def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    text = get_text(url)
    page_counts = Counter(text.split())

    words_to_count = []
    with open(words_file, "r") as file:
        for line in file:
            word = line.strip()
            if word:
                words_to_count.append(word)

    frequencies = {word: page_counts[word] for word in words_to_count}

    print(frequencies)


if __name__ == "__main__":
    main()
