import random
CARD = ['Diamond','Spades','Hearts','clubs']

ranks = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

def pick_a_card():
        card = random.choices(CARD )
        rank = random.choices(ranks)
        return(f'The {rank} of {card}')

print (pick_a_card())