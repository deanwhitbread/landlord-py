
from misc import constants as const

''' Valid Card Hands Methods '''
def is_solo(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a solo hand, False otherwise. 

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return len(number_freq.keys())==1 and sum(number_freq.values())==1

def is_solo_chain(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a solo chain hand, False otherwise.

    Args:  
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    if contains_invalid_sequences(number_freq):
        return False

    # check chain length not exceeded
    max_chain_length = 12
    cards_in_hand = sum(number_freq.values())
    if cards_in_hand<5 or cards_in_hand>max_chain_length:
        return False

    freq = convert_ace_card_to_highest_number(number_freq)

    return is_chain_in_sequence(freq, cards_in_hand, 1)

def is_pair(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a pair hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return sum(number_freq.values())==2 and (is_rocket(number_freq) or len(number_freq.keys())==1)

def is_pair_chain(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a pair chain hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    if contains_invalid_sequences(number_freq):
        return False

    # check chain length.
    max_chain_length = 20
    cards_in_hand = sum(number_freq.values())
    if cards_in_hand<6 or cards_in_hand>max_chain_length or cards_in_hand%2==1:
        return False

    freq = convert_ace_card_to_highest_number(number_freq)

    return is_chain_in_sequence(freq, cards_in_hand, 2)

def is_trio(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a trio hand, False otherwise.

    Args:  
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return len(number_freq.keys())==1 and sum(number_freq.values())==3

def is_trio_chain(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a trio chain hand, False otherwise. 
    Note: A trio chain is also known as an airplane hand. 

    Args:  
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    if contains_invalid_sequences(number_freq):
        return False

    # check chain length.
    max_chain_length = 18
    cards_in_hand = sum(number_freq.values())
    if cards_in_hand<6 or cards_in_hand>max_chain_length or cards_in_hand%3!=0:
        return False

    freq = convert_ace_card_to_highest_number(number_freq)

    return is_chain_in_sequence(freq, cards_in_hand, 3)

def is_trio_with_solo(number_freq):
    pass 

def is_trio_with_pair(number_freq):
    pass 

def is_airplane_with_solo(number_freq):
    pass 

def is_airplane_with_pair(number_freq):
    pass

def is_bomb(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a bomb hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return len(number_freq.keys())==1 and sum(number_freq.values())==4

def is_rocket(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a rocket hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return len(number_freq.keys())==2 and 14 in number_freq.keys() and 15 in number_freq.keys()

def contains_solo_hand(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played contains a solo hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return (each_trio_has_matching_non_trio_hand(number_freq, is_solo=True) and 
        not does_two_preceed_three_in_trio_chain(number_freq))

def contains_pair_hand(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played contains a pair hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return (each_trio_has_matching_non_trio_hand(number_freq, is_solo=False) and 
        not does_two_preceed_three_in_trio_chain(number_freq))

def contains_trio_hand(number_freq):
    pass

def contains_trio_chain_hand(number_freq):
    pass

def is_chain(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a chain hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return (is_solo_chain(number_freq) or is_pair_chain(number_freq) or
        is_trio_chain(number_freq))

def is_combination(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand being played is a combination hand, False otherwise.

    Args: 
        number_freq - A hash map that maps the card number to the number of 
                    times it appears in the hand.
    '''
    return contains_solo_hand(number_freq) or contains_pair_hand(number_freq)

def convert_ace_card_to_highest_number(number_freq: dict[int:int]) -> bool:
    '''Return a hash map with the ace card number converted to a new number
    using an offset value. 

    Args:
        number_freq - A hash map that maps the card number to the number of 
                times it appears in the hand.
    '''
    offset = 13
    freq_map = number_freq.copy()
    if 1 in freq_map.keys():
        freq_map[1+offset] = freq_map[1]
        del freq_map[1]

    return freq_map

def is_chain_in_sequence(number_freq: dict[int:int], cards_in_hand: int, card_freq: int) -> bool:
    '''Return True if the card chain is in sequence, False otherwise.
    
    Args:
        number_freq - A hash map that maps the card number to the number of 
                times it appears in the hand.
        cards_in_hand - An integer representing the number of cards in the 
                        players' hand.
        card_freq - An integer representing the expected number of times a
                    card appears in the hand. For instance, it is expected to
                    have 2 cards with the same card number when it is a pair.
    '''
    max_card_number = max(number_freq.keys())
    min_card_number = max_card_number-int(cards_in_hand/card_freq)+1
    for i in range(min_card_number, max_card_number+1):
        if i not in number_freq.keys() or number_freq[i]!=card_freq:
            return False

    return True

def contains_invalid_sequences(number_freq: dict[int:int]) -> bool:
    '''Return True if the hand contains an invalid chain sequence, False otherwise.
    
    Args:
        freq_map - A hash map that maps the card number to the number of 
                times it appears in the hand.
    '''
    return (14 in number_freq.keys() or 15 in number_freq.keys() or 2 in number_freq.keys() or 
        (1 in number_freq.keys() and not 13 in number_freq.keys()))

def each_trio_has_matching_non_trio_hand(number_freq: dict[int:int], is_solo) -> bool:
    '''Return True if each trio in the sequence has a non-trio hand for each
    trio, False otherwise.
    
    Args:
        freq_map - A hash map that maps the card number to the number of 
                times it appears in the hand.
        non_trio_cards - An integer representing the number of cards in the non-trio hand.
    '''
    cards_needed = 0
    joker_found = False 
    for key, val in number_freq.items():
        if val==4:
            cards_needed += 2
        elif val==3:
            cards_needed += 1
        elif is_solo:
            if (key==14 or key==15) and not joker_found:
                joker_found = True 
            elif (key==14 or key==15) and joker_found:
                return False 

            cards_needed -= 1 
        else:
            if (key==14 or key==15) and not joker_found:
                joker_found = True 
            elif (key==14 or key==15) and joker_found:
                joker_found = False 
                cards_needed -= 1
            elif val==2:
                cards_needed -= 1
            else:
                return False

    if not is_solo and joker_found:
        return False
    
    return cards_needed==0

def does_two_preceed_three_in_trio_chain(number_freq):
    '''Return True if 2 preceeds 3 in the trio chain, False otherwise.
    
    Args:
        number_freq - A hash map that maps the card number to the number of 
                times it appears in the hand.
    ''' 
    trio_hands = set()
    for key, val in number_freq.items():
        if val==3 and (key==2 or key==3):
            trio_hands.add(key)

    return 2 in trio_hands and 3 in trio_hands

def get_hand_category(number_freq):
    if is_solo(number_freq):
        return const.CARD_CATEGORY.SOLO
    elif is_solo_chain(number_freq):
        return const.CARD_CATEGORY.SOLO_CHAIN
    elif is_pair(number_freq):
        return const.CARD_CATEGORY.PAIR
    elif is_pair_chain(number_freq):
        return const.CARD_CATEGORY.PAIR_CHAIN
    elif is_trio(number_freq):
        return const.CARD_CATEGORY.TRIO
    elif is_trio_chain(number_freq):
        return const.CARD_CATEGORY.TRIO_CHAIN
    elif is_bomb(number_freq):
        return const.CARD_CATEGORY.BOMB
    elif is_rocket(number_freq):
        return const.CARD_CATEGORY.ROCKET
    elif is_trio_with_solo(number_freq):
        return const.CARD_CATEGORY.TRIO_WITH_SOLO
    elif is_trio_with_pair(number_freq):
        return const.CARD_CATEGORY.TRIO_WITH_PAIR
    elif is_airplane_with_solo(number_freq):
        return const.CARD_CATEGORY.AIRPLANE_WITH_SOLO
    elif is_airplane_with_pair(number_freq):
        return const.CARD_CATEGORY.AIRPLANE_WITH_PAIR
    else:
        msg = f"The card sequence {[key for key, val in number_freq.items() for _ in range(val) ]} is not a recognised category."
        raise RuntimeError(msg)      
