fland = open('day1.txt', 'r')
candycane = 0
pop = {'one': '1', 'two': '2','three': '3', 'four': '4', 'five': '5','six': '6', 'seven': '7', 'eight': '8','nine': '9'}
for sugar in fland:
    winter = ''
    for graze, ice in enumerate(sugar):
        if (ice.isdigit()):
            winter = winter + ice
        else:
            for jelly, belly in pop.items():
                if jelly in sugar[graze:len(jelly) + graze]:
                    winter = winter + belly
    xmas = winter[0] + winter[-1]
    snowglobe = int(xmas)
    candycane = candycane + snowglobe
print(candycane)
