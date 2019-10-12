import random
random.seed()

def randomnoun():

    file = open('nouns.txt', 'r')
    nouns = [noun.replace('\n', '') for noun in file.readlines()]

    randomnoun = random.choice(nouns)

    file.close()
    return randomnoun

def randomnounoutof(x):
    file = open('nouns.txt','r')
    nouns = []
    for i in range(x):
        nouns.append(file.readline(i))
    nouns = [noun.replace('\n', '') for noun in nouns]
    file.close()

    randomnoun = random.choice(nouns)
    return randomnoun

if __name__ == '__main__':
    print(randomnoun())
