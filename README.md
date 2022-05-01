# markov-chains-for-text-in-python-implementation

This code sucks, but it works I guess. It generates markov chain from text file you give it.
Code is big messy spaghetti, but it was put together in like an hour (and most of that time was messing around).

Changelog
------

From now on (23rd of April 2022) this thing doesn't relay on NumPy for number generation anymore. This means it also won't need as much RAM (Previous version hit 10 GB of RAM usage with 177 MB model yikes), and will be a lot faster.

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
            0.2,
            0.3,
            0.4,
            ...
        ]
    ],
    ...
}
```
Numbers 0.1, 0.2, 0.3, 0.4... represent probabilities of certain word happening after that word, those aren't absolute probabilities, each position is probability + sum of previous positions.

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
Model_user contains two functions 'generate' and 'search', 'search' takes as an argument list of possibilities, and randomly generated number, it's binary search, except it returns closest object, not equal one. 'generate' function takes as an argument model (usually loaded from file created by model_generator) and then generates random sentences based on that model, using our 'search' function, it choses words randomly based on probabilities until it hits None, program recognises None as end of sentence, which breaks loop, and returns our sentence as a string. This could theoretically cause endless loop, but it's very unlikely.

Limitations
------
Currently this code kinda sucks, so it has it's limitations, like for now it cannot be used for real time applications, I know it can be done, but for now it wasn't my priority. ~~Also if model is big then generating sentences can take couple of seconds.~~ (Fixed (I think)) This also currently works only on sentences, aka stuff that ends, so you can't use one big string of text cus generated sentences, you'll have to first create some markers that separate sentences and split it using those. Also model_generator splits given input using spaces, so word is something that has space before or after it (except single word sentences, those don't have spaces). Also current implementation sees words ended with . or , or other signs like that as different words (and I probably will leave it like that since I think it makes results more diverse). I will work on this thing in my free time if I will feel like it, but it's already satisfactory for me.

Third-party libraries used
------
This thing uses ~~[NumPy](https://numpy.org/) and~~ [tqdm](https://tqdm.github.io/)

~~Only really needed library is NumPy~~
(I'd like to still give credit for NumPy, as it made first version of this program possible)

Numpy is no longer required, so this program doesn't require any external library, but I used tqdm as I really love it for it's progress bars (it can be safely removed).

It also uses random and json libraries, but those aren't external.
