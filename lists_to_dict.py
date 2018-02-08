name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "extra"]

# def makeDict(key, value):
#     print zip(key, value)
# makeDict(name, favorite_animal)

# hacker challenge:
def makeDict(key, value):
    if len(key) > len(value):
        value.extend(['none'])
        print zip(key, value)
    elif len(key) < len(value):
        key.extend(['none'])
        print zip(value, key)
    else:
        print zip(key, value)
makeDict(name, favorite_animal)