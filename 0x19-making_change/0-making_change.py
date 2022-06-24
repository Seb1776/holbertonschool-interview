#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to
meet a given amount total.
"""


def makeChange(coins, total):
	"""
	Return: fewest number of coins needed to meet total.
	-If total is 0 or less, return 0.
	-If total cannot be met by any number
	"""
	if total <= 0:
		return 0

	coins.sort(reverse=True)

	i, ncoins = (0, 0)
	cpy_total = total
	len_coins = len(coins)

	while(i < len_coins and cpy_total > 0):
		if (cpy_total - coins[i]) >= 0:
			cpy_total -= coins[i]
			ncoins += 1
		else:
			i += 1

	check = cpy_total > 0 and ncoins > 0
	return -1 if check or ncoins == 0 else ncoins
