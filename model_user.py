import random
import json

# It's what made NumPy obsolete
# Model in this place is supposed to be table of probabilities (aka model[choice][1]), num on the other hand is randomly generated number
# Index returned here is required for finding apropriate word choice list
def search(model, num):
    bottom = 0
    top = len(model) - 1
    closest = 0

    while bottom <= top:
        closest = int((bottom + top) / 2)
        if model[closest] < num:
            bottom = closest + 1
        elif model[closest] > num:
            top = closest - 1
        else:
            break
    
    return bottom


def generate(model, start = None):
    choice = random.choice(list(model.keys())) if start is None else start
    sentence = [choice]

    while True:
        choice = model[choice][0][search(model[choice][1], random.random())]
        if choice:
            sentence.append(choice)
        else:
            break

    return ' '.join(sentence)

if __name__ == "__main__":
    with open('model.json', 'r') as f:
        model = json.load(f)
    print(generate(model))