from sample_player.logger import logger


def determine_hand_group_pre_flop(hand_str):
    """
    Classifies hands into groups based on card ranks and suitedness.

    Args:
        hand (list): A list of two cards, each represented as a list [rank, suit].

    Returns:
        str: The hand group classification (Premium, Strong, Playable, Marginal, or Trash).
    """

    if "A" in hand_str:
        return "Premium"
    elif "K" in hand_str or "Q" in hand_str or "J" in hand_str:
        return "Strong"
    elif "10" in hand_str or "9" in hand_str or "8" in hand_str:
        return "Playable"
    elif "7" in hand_str or "6" in hand_str or "5" in hand_str:
        return "Marginal"
    else:
        return "Trash"


def estimate_win_probability_single_hand(hand) -> float:
    """
    Estimates win probability based on hand group and opponent count.

    Args:
        hand (list): A list of two cards, each represented as a list [rank, suit].

    Returns:
        float: The estimated probability of winning with the given hand.
    """

    hand_groups = {
        "Premium": 0.8,
        "Strong": 0.6,
        "Playable": 0.4,
        "Marginal": 0.2,
        "Trash": 0.1,
    }

    # Convert cards to a string for easy comparison
    hand_str = "".join(str(card) for card in hand)
    logger.info(hand_str)
    # Determine the hand group for the given hand
    hand_group = determine_hand_group_pre_flop(hand_str)

    # Get the corresponding probability for the hand group
    probability = hand_groups.get(hand_group, 0.0)

    return probability


def get_pre_flop_action(hole_card, min_amount, max_amount):
    """
    Determines pre-flop action based on hand strength and betting context.

    Args:
        hole_card (list): A list of two hole cards, each represented as a list [rank, suit].
        min_amount (int): The minimum bet amount required to stay in the hand.
        max_amount (int): The maximum bet amount allowed in the current round.
        opponent_count (int, optional): The number of opponents in the game. Defaults to 2.

    Returns:
        tuple[str, int]: A tuple containing the action ("call", "raise", or "fold") and the amount to bet or call.
    """

    hand_card = [s[-1] for s in hole_card]
    pre_flop_probability = estimate_win_probability_single_hand(hand_card)
    logger.info(
        f"Estimated Probability of Winning  teamACN {hole_card}: {pre_flop_probability}"
    )
    if max_amount == min_amount:
        return "call", min_amount
    elif max_amount < min_amount:
        return "fold", 0
    elif pre_flop_probability >= 0.8:
        raise_amount = max_amount * 0.3
        if min_amount > raise_amount:
            raise_amount = min_amount
        return "raise", raise_amount
    elif pre_flop_probability >= 0.7:
        raise_amount = max_amount * 0.2
        if min_amount > raise_amount:
            raise_amount = min_amount
        return "raise", raise_amount
    elif pre_flop_probability > 0.3 and pre_flop_probability < 0.7:
        return "call", min_amount
    else:
        return "fold", 0
