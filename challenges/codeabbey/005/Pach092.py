for a in """7 3 5
15 20 40
300 550 137""".split("\n"):
    print(min([int(x) for x in a.split(' ')]))
