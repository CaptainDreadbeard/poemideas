"""Random poetry line generator, by Robin Bolin
A random generator of sweet lines of cringey poetry

Tags: beginner, random, poem, word"""

import random

# set up constants

DESCRIPTION = ['presence', 'gait', 'smile']
POSSESSIVE_PRONOUNS = ['Her', 'Their']
PERSONAL_PRONOUNS = ['She', 'They']
FLOWERS = ['Roses', 'Tulips', 'Daisys', 'Indian Paintbrushes', 'Pussywillows', 'Carnations', 'Gardenias', 'Lillies', 'Hyacinths', 'Chrysanthemums', 'Daffodil', 'Sunflower']
OBJECTS = ['A fine set of pearls', 'like they were woven by Rumpelstiltskin', 'bars of gold', 'tears of platinum', 'fine cedar', 'precious metals', 'a four-leaf clover', 'ebony', 'ivory', 'emerald', 'the finest wine', 'a vintage omega', 'crystal clear water', 'honeycombs']
BODY_PARTS = ['eyes', 'hair', 'skin', 'hands', 'a chest', 'teeth', 'jaw', 'nose', 'cheeks', 'curves', 'belly']
ALLITERATION = ['pretty pristine', 'greatly glowing', 'lovingly luxurious', 'originally opalescent', 'energetically envigorating', 'succulently sweet', 'gorgeously glowing', 'heavenly hearth']

def main():
    print('Cringey Poem Generator!')
    print('By Robin Bolin')
    print()

    print('How to woo their feelings with poetic inspiration')
    while True:
        print("Enter the number of poetry lines to generate:")
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            numberOfLines = int(response)
            break # Exit once a valid number is entered

    for i in range(numberOfLines):
        PoetryLines = random.randint(1, 8)

        if PoetryLines == 1:
            PoemLine = LikeLine()
        elif PoetryLines == 2:
            PoemLine = ForLine()
        elif PoetryLines == 3:
            PoemLine = RemindLine()
        elif PoetryLines == 4:
            PoemLine = FeltLine()
        elif PoetryLines == 5:
            PoemLine = DescribeLine()
        elif PoetryLines == 6:
            PoemLine = MemoLine()
        elif PoetryLines == 7:
            PoemLine = LongingLine()
        elif PoetryLines == 8:
            PoemLine = GaveLine()

        print(PoemLine)
    print()



    print('Show this to your lover to make their heart warm!')


# Each of these functions returns a different type of linebreak:
def LikeLine():
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    body = random.choice(BODY_PARTS)
    randomitems = random.choice(OBJECTS)
    return '{} {} were like {}'.format(possessive,body, randomitems)


def ForLine():
    allit = random.choice(ALLITERATION)
    flower = random.choice(FLOWERS)
    body = random.choice(BODY_PARTS)
    return '{} {} for {}'.format(allit, flower, body)


def RemindLine():
    pronoun = random.choice(PERSONAL_PRONOUNS)
    body = random.choice(BODY_PARTS)
    randomitems = random.choice(OBJECTS)
    return '{} had {} reminding me of {}'.format(pronoun, body, randomitems)


def FeltLine():
    flower = random.choice(FLOWERS)
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    body = random.choice(BODY_PARTS)
    return '{} felt like {} {}'.format(flower, possessive, body)


def DescribeLine():
    randomitems = random.choice(OBJECTS) + 's'
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    body = random.choice(BODY_PARTS)
    return '{} couldn\'t describe {} {}'.format(randomitems, possessive, body)


def MemoLine():
    flower = random.choice(FLOWERS)
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    describe = random.choice(DESCRIPTION)
    return '{} recall memories of {} {}'.format(flower, possessive, describe)


def LongingLine():
    possessive = random.choice(POSSESSIVE_PRONOUNS)
    describe = random.choice(DESCRIPTION) + 's'
    randomitems = random.choice(OBJECTS)
    return '{} {} makes me long for {}'.format(possessive, describe, randomitems)


def GaveLine():
    pronoun = random.choice(PERSONAL_PRONOUNS)
    allit = random.choice(ALLITERATION)
    flower = random.choice(FLOWERS)
    return '{} gave me a feeling of {} {} on a Sunday morning.'.format(pronoun, allit, flower)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()