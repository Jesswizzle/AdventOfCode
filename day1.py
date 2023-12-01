fhand = open('day1.txt','r')
candycane = 0
for snow in fhand:
    #print(snow)
    winter = ""
    for ice in snow:
        if (ice.isdigit()):
            winter = winter + ice
    #print(winter)
    xmas = winter[0] + winter[-1]
    #print(xmas)
    snowglobe = int(xmas)
    #print(type(snowglobe))
    candycane = candycane + snowglobe
print(candycane)
