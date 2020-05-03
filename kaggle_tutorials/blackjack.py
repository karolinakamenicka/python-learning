def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    k=0
    for i in range(len(hand_1)):
        print(hand_1[i])
        if hand_1[i] in "JQK":
            hand_1[i] = 10
        if hand_1[i] =='A':
            hand_1[i]=1
            k = k+1
        hand_1[i] =int(str(hand_1[i]))
    print(hand_1)
    sum_h1 = sum(hand_1)
    while k>0 and sum_h1 <11:
        k=k-1
        sum_h1 = sum_h1+10

    m=0
    for j in range(len(hand_2)):
        print(hand_2[j])
        if hand_2[j] in "JQK":
            hand_2[j] = 10
        elif hand_2[j] =='A':
            hand_2[j]=1
            m = m+1
        else:
            hand_2[j] =int(str(hand_2[j]))
    print(hand_2)
    sum_h2 = sum(hand_2)
    while m>0 and sum_h2 <11:
        m=m-1
        sum_h2 = sum_h2+10


    if (sum_h1<22 and sum_h1>sum_h2) or (sum_h1<22 and sum_h2>=21):
        return True
    return False

print(blackjack_hand_greater_than(['J', 'A','1'], ['6']))
