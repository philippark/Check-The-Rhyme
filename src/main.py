import pronouncing
import random
import nltk
nltk.download("punkt")

def find_rhymes(words):
    rhymes = dict()

    for word in words:
        matched = False
        for key in rhymes:
            if word in pronouncing.rhymes(key):
                rhymes[key].add(word)
                matched = True
                break
        
        if not matched:
            rhymes[word] = set()
            rhymes[word].add(word)
    
    color_mapping = dict()
    colors = []

    for key in rhymes:
        rand_color = random.choices(range(256), k=3)
        while rand_color in colors:
            rand_color = random.choices(range(256), k=3)

        for word in rhymes[key]:
            color_mapping[word] = rand_color
        
    return color_mapping


            

if __name__ == "__main__":
    words = ["anything", "bathing", "rover", "over", "crazy", "lazy", "yankees"]

    color_mapping = find_rhymes(words)

    print(color_mapping)