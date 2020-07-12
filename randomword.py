import random
random.seed()

def randomnoun():

    with open('nouns.txt', 'r') as file:
        nouns = [noun.replace('\n', '') for noun in file.readlines()]

        randomnoun = random.choice(nouns)

        return randomnoun

def randomnounoutof(x):
    with open('nouns.txt','r') as file:
        nouns = []
        for i in range(x):
            nouns.append(file.readline(i))
        nouns = [noun.replace('\n', '') for noun in nouns]

        randomnoun = random.choice(nouns)
        
        return randomnoun

if __name__ == '__main__':
    print(randomnoun())
