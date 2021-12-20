def computepay(h, r):
	h = float(h)
	r = float(r)
	if h > 40:
		total = ((40 * r) + r * 1.5 * (h - 40))
	else:
		total = h * r
	return total

print(computepay(45, 10.5))
