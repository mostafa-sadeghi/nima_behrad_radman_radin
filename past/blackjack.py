import random
HEARTS = chr(9829)  # '♥'
DIAMONDS = chr(9830)  # '♦'
SPADES = chr(9824)  # '♠'
CLUBS = chr(9827)  # '♣'

BACKSIDE = 'backside'


def getBet(maxBet):
    print(f'How much money do you bet? (1-{maxBet}):')
    bet = int(input('> '))
    if 1 <= bet <= maxBet:
        return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))

    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    if showDealerHand:
        print('DEALER:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ???')
        displayCards([BACKSIDE]+dealerHand[1:])

    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    rows = ['']*4
    for card in cards:
        rows[0] += '  ___  '
        if card == BACKSIDE:
            rows[1] += ' |## | '
            rows[2] += ' |###| '
            rows[3] += ' |_##| '
        else:
            rank, suit = card
            rows[1] += f' |{rank}  | '
            rows[2] += f' | {suit} | '
            rows[3] += f' |_{rank} | '
    for row in rows:
        print(row)


def getMove(playerHand, money):
    moves = ['H', 'S']
    if len(playerHand) == 2 and money > 0:
        moves.append('D')

    move = input(', '.join(moves) + '> ').upper()
    if move in ('H', 'S'):  # if move == 'H' or move =='S'
        return move
    if move == 'D' and 'D' in moves:
        return move


print('''BlackJack Game.
Rules: We must get close to 21.
Ace -> 1 or 11
King, Queen, Jack -> 10
others cards their own number
(H) => take another card
(S) stop
(D) double
''')

money = 5000
while True:
    if money <= 0:
        print("Youre broke.")
        print("Thanks for playing!")
        exit()
    print("Money:", money)
    bet = getBet(money)

    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]
    print('Bet:', bet)

    while True:
        displayHands(playerHand, dealerHand, False)
        print()

        if getHandValue(playerHand) > 21:
            break
        move = getMove(playerHand, money-bet)
        if move == 'D':
            additionalBet = getBet(min(bet, (money-bet)))
            bet += additionalBet
            print(f'Bet increased to {bet}')

        if move == 'H':
            newCard = deck.pop()
            rank, suit = newCard
            print(f'new card is: {rank} {suit}')
            playerHand.append(newCard)
            if getHandValue(playerHand) > 21:
                continue

        if move == 'S':
            break

    if getHandValue(playerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            print("player takes another card...")
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand, False)
            if getHandValue(dealerHand) > 21:
                break

        input('press enter to continue...')

    displayHands(playerHand, dealerHand, True)
    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)

    if dealerValue > 21:
        print('Dealer loses...')
        money += bet
    elif playerValue > 21 or dealerValue > playerValue:
        print("You Lost!")
        money -= bet

    elif playerValue > dealerValue:
        print("You Lost!")
        money -= bet

    elif playerValue == dealerValue:
        print("EQUAL")

    input('Press Enter To continue...')
