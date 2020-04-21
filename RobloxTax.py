import math

_DEBUG = False

def within(val, val2, margin, direction="pn"):
	if direction == "pn": return val - val2 <= margin and val - val2 >= (0-margin)
	elif direction == "p": return val - val2 >= margin
	if direction == "n": return val - val2 <= margin


def CalculateTax(target):
	current = target * 0.3

	while not within(current*0.7, target, 0.5, direction="p"):
		current = current + 1

		if _DEBUG:
			print(f"Current: {current} || Target: {target} || Tax: {current*0.7}")

	return int(math.ceil(current))
