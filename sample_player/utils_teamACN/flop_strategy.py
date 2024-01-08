def get_card_action(best_hand, highest_hand, min_amount, max_amount):
    """
    Determines the appropriate poker action (call, raise, or fold) based on the player's hand strength
    and current betting context.

    Args:
        best_hand (int): The numerical category of the player's best possible hand (1-9, with 9 being the best).
        highest_hand (int): The numerical category of the highest possible hand on the table.
        min_amount (int): The minimum bet amount required to stay in the hand.
        max_amount (int): The maximum bet amount allowed in the current round.

    Returns:
        tuple[str, int]: A tuple containing the recommended action ("call", "raise", or "fold") and the
            amount to bet or call.
    """
    if max_amount == min_amount:
        return "call", min_amount
    elif max_amount < min_amount:
        return "fold", 0
    elif best_hand == 9:
        raise_amount = max_amount * 0.4
        if min_amount > raise_amount:
            raise_amount = min_amount
        return "raise", raise_amount
    elif best_hand >= 8 and highest_hand > 8:
        raise_amount = max_amount * 0.3
        if min_amount > raise_amount:
            raise_amount = min_amount
        return "raise", raise_amount
    elif best_hand >= 7 and highest_hand > 7:
        raise_amount = max_amount * 0.2
        if min_amount > raise_amount:
            raise_amount = min_amount
        return "raise", raise_amount
    elif best_hand >= 5 and highest_hand > 7:
        raise_amount = max_amount * 0.15
        if min_amount > raise_amount:
            raise_amount = min_amount
        return "raise", raise_amount
    elif best_hand >= 2 and best_hand < 5:
        raise_amount = max_amount * 0.10
        if min_amount > raise_amount:
            raise_amount = min_amount
        return "raise", raise_amount
    elif best_hand >= 1 and best_hand < 2:
        return "call", min_amount
    else:
        return "fold", 0
