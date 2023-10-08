def playing_domino(cards, deck):
    max_sum = 0
    result = None
    
    for i in cards:
        if deck[0] in i or deck[1] in i:  
            card_sum = sum(i)
            if card_sum > max_sum:
                max_sum = card_sum
                result = i
                
    if result:
        return result
    else:
        return []
if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []