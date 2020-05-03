def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    money = 0
    for i in range(n_runs):
        money = money + play_slot_machine()-1
    return money/n_runs

print(estimate_average_slot_payout(1000))
