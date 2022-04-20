# markov-chains-for-text-in-python-implementation

This code sucks, but it works I guess. It generates markov chain from text file you give it.
Code is big messy spaghetti, but it was put together in like an hour (and most of that time was messing around).


model_generator
------

"Model" generator creates from text json file with structure:
```
{
    "word": [
        [
            "next_word_1",
            "next_word_2",
            "next_word_3",
            "next_word_4",
            ...
        ],
        [
            0.1,
            0.1,
            0.1,
            0.1,
            ...
        ]
    ],
    ...
}
```

"next_word_*" represents any word that generator saw is possible after given piece of text, so for example if we give it sentence "This thing sucks" it will return:
```
{
    "This": [
        ["thing"], 
        [1.0]
    ],
    "sucks": [
        [None], 
        [1.0]
    ],
    "thing": [
        ["sucks"], 
        [1.0]
    ]
}
```
None (in json file it will be saved as null) means end of the sentence.

model_user
------
Model_user contains only one function 'generate' and it takes as an argument our model, it can be loaded from file created by model_generator, after that it just generated random sentences based on that model, using numpy.random.choice that takes arrays of words and probabilities as arguments (I am aware it also takes different arguments but it isn't necessary for this), and it randomly choses words until it hits None, which means it's end of sentence and then it returns it as a string. This could theoretically cause endless loop, but it's very unlikely.

Limitations
------
Currently this code kinda sucks, so it has it's limitations, like for now it cannot be used for real time applications, I know it can be done, but for now it wasn't my priority. Also if model is big then generating sentences can take couple of seconds. This also currently works only on sentences, aka stuff that ends, so you can't use one big string of text cus generated sentences, you'll have to first create some markers that separate sentences and split it using those. Also model_generator splits given input using spaces, so word is something that has space before or after it (except single word sentences, those don't have spaces). Also current implementation sees words ended with . or , or other signs like that as different words (and I probably will leave it like that since I think it makes results more diverse). I will work on this thing in my free time if I will feel like it, but it's already satisfactory for me.

Third-party libraries used
------
This thing uses [NumPy](https://numpy.org/) and [tqdm](https://tqdm.github.io/)

Only really needed library is NumPy, but I used tqdm as I really love it for it's progress bars.