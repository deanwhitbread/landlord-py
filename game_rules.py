
''' Valid Card Hands Methods '''
def is_solo(number_freq):
    '''Return if the hand being played is a solo hand. 

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.

    Returns: True if the hand is a solo hand, False otherwise. 
    '''
    return len(number_freq.keys())==1 and sum(number_freq.values())==1

def is_solo_chain(number_freq):
    '''Check whether the hand being played is a solo chain hand.

    Args: 
        hand - A collection of Card objects containing at least one object. 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.

    Returns: True if the hand is a solo chain hand, False otherwise. 
    '''
    # check for invalid card numbers in sequence
    if (14 in number_freq.keys() or 15 in number_freq.keys() or 
        2 in number_freq.keys()):
        return False

    # check chain length not exceeded
    max_chain_length = 12
    cards_in_hand = sum(number_freq.values())
    if cards_in_hand<5 or cards_in_hand>max_chain_length:
        return False

    # convert the ace card to the highest card using an offset value.  
    offset = 13
    freq = number_freq.copy()
    if 1 in freq.keys():
        freq[1+offset] = freq[1]
        del freq[1]

    # check chain is a sequence.
    max_card_number = max(freq.keys())
    min_card_number = max_card_number-cards_in_hand+1
    for i in range(min_card_number+1, max_card_number+1):
        if i not in freq.keys() or freq[i]!=1:
            return False

    return True

def is_pair(number_freq):
    '''Check whether the hand being played is a pair hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    
    Returns: True if the hand is a pair hand, False otherwise. 
    '''
    return sum(number_freq.values())==2 and (is_rocket(number_freq) or len(number_freq.keys())==1)

def is_pair_chain(number_freq):
    '''Check whether the hand being played is a pair chain hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.

    Returns: True if the hand is a pair chain hand, False otherwise. 
    '''
    # check for invalid card numbers in sequence.
    if (14 in number_freq.keys() or 15 in number_freq.keys() or 
        2 in number_freq.keys()):
        return False 

    # check chain length.
    max_chain_length = 20
    cards_in_hand = sum(number_freq.values())
    # if len(hand)<6 or len(hand)>max_chain_length or len(hand)%2==1:
    if cards_in_hand<6 or cards_in_hand>max_chain_length or cards_in_hand%2==1:
        return False

    # convert ace card number to the highest card number using an offset value.
    offset = 13
    freq = number_freq.copy()
    if 1 in freq.keys():
        freq[1+offset] = freq[1]
        del freq[1]

    # check the sequence of the chain. 
    max_card_number = max(freq.keys())
    # min_card_number = max_card_number-int(len(hand)/2)+1
    min_card_number = max_card_number-int(cards_in_hand/2)+1
    for i in range(min_card_number+1, max_card_number+1):
        if i not in freq.keys() or freq[i]!=2:
            return False 

    return True

def is_trio(number_freq):
    '''Check whether the hand being played is a trio hand.

    Args:  
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    
    Returns: True if the hand is a trio hand, False otherwise. 
    '''
    return len(number_freq.keys())==1 and sum(number_freq.values())==3

def is_trio_chain(number_freq):
    '''Check whether the hand being played is a trio chain hand. Note: A trio chain 
    is also known as an airplane hand. 

    Args:  
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.

    Returns: True if the hand is a trio chain or airplane hand, False otherwise. 
    '''
    # check for invalid card numbers in sequence.
    if (14 in number_freq.keys() or 15 in number_freq.keys() or 
        2 in number_freq.keys()):
        return False 

    # check chain length.
    max_chain_length = 18
    cards_in_hand = sum(number_freq.values())
    if cards_in_hand<6 or cards_in_hand>max_chain_length or cards_in_hand%3!=0:
        return False

    # convert ace card number to the highest card number using an offset value.
    offset = 1
    freq = number_freq.copy()
    if 1 in freq.keys():
        freq[1+offset] = freq[1]
        del freq[1]

    # check the sequence of the chain. 
    max_card_number = max(freq.keys())
    # min_card_number = max_card_number-int(len(hand)//3)+1
    min_card_number = max_card_number-int(cards_in_hand//3)+1
    for i in range(min_card_number+1, max_card_number+1):
        if i not in freq.keys() or freq[i]!=3:
            return False

    return True

def is_bomb(number_freq):
    '''Check whether the hand being played is a bomb hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    
    Returns: True if the hand is a bomb hand, False otherwise. 
    '''
    return len(number_freq.keys())==1 and sum(number_freq.values())==4

def is_rocket(number_freq):
    '''Check whether the hand being played is a rocket hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.

    Returns: True if the hand is a rocket hand, False otherwise. 
    '''
    return len(number_freq.keys())==2 and 14 in number_freq.keys() and 15 in number_freq.keys()

def contains_solo_hand(number_freq):
    '''Check whether the hand being played contains a solo hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.

    Returns: True if the hand contains a solo hand, False otherwise. 
    '''
    is_bomb, is_trio_combination = False, False 
    trio_cards, number_of_solo_cards_needed = 0, 0
    for k,v in number_freq.items():
        if v==4:
            is_bomb = True 
            number_of_solo_cards_needed += 2
        elif v==3:
            is_trio_combination = True 
            number_of_solo_cards_needed += 1
        else:
            number_of_solo_cards_needed -= 1

    contains_rocket = 14 in number_freq.keys() and 15 in number_freq.keys()
    if (not is_bomb and not is_trio) or contains_rocket:
        return False

    # check if 2 preceeds 3 in airplane sequence. 
    trios = set()
    for k,v in number_freq.items():
        if v==3 and (k==2 or k==3):
            trios.add(k)

    if 2 in trios and 3 in trios:
        return False

    return number_of_solo_cards_needed==0

def contains_pair_hand(number_freq):
    '''Check whether the hand being played contains a pair hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    
    Returns: True if the hand contains a pair hand, False otherwise. 
    '''
    is_bomb, is_trio_combination, joker_seen = False, False, False
    trio_cards, number_of_pair_cards_needed = 0, 0
    for k,v in number_freq.items():
        if v==4:
            is_bomb = True 
            number_of_pair_cards_needed += 2
        elif v==3:
            is_trio_combination = True 
            number_of_pair_cards_needed += 1
        elif v==2:
            number_of_pair_cards_needed -= 1
        elif v==1 and (k==14 or k==15):
            if not joker_seen:
                joker_seen = True 
            else: 
                joker_seen = False
                number_of_pair_cards_needed -= 1
        else:
            return False

    
    if (not is_bomb and not is_trio) or joker_seen:
        return False

    # check if 2 preceeds 3 in airplane sequence. 
    trios = set()
    for k,v in number_freq.items():
        if v==3 and (k==2 or k==3):
            trios.add(k)

    if 2 in trios and 3 in trios:
        return False

    return number_of_pair_cards_needed==0

def is_chain(number_freq):
    '''Check whether the hand being played is a chain hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    
    Returns: True if the hand is chain type hand, False otherwise. 
    '''
    return (is_solo_chain(number_freq) or is_pair_chain(number_freq) or
        is_trio_chain(number_freq))

def is_combination(number_freq):
    '''Check whether the hand being played is a combination hand.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    
    Returns: True if the hand is a combination hand, False otherwise. 
    '''
    return contains_solo_hand(number_freq) or contains_pair_hand(number_freq)


    

    
