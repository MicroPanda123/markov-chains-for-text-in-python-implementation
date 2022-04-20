import numpy as np

def generate(model):
    choice = np.random.choice(list(model.keys()))
    sentence = [choice]

    while True:
        choice = np.random.choice(model[choice][0], replace=True, p=model[choice][1])
        if choice:
            sentence.append(choice)
        else:
            break

    return ' '.join(sentence)
