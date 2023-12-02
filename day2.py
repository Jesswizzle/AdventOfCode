floppy = open('day2.txt','r')
r = 12
g = 13
b = 14
total = 0
for boringline in floppy:
    #print(boringline)
    flag = True
    first, second = boringline.split(':')
    #print(first)
    #print(second)
    berry, gamenum = first.split(' ')
    gamenum = int(gamenum)
    #print(gamenum)

    segments = second.split(';')
    #print(segments)
    for segment in segments:
        alone = segment.split(',')
        #print(alone)
        for part in alone:
            part = part.lstrip()
            #print(part)
            third, fourth = part.split(' ')
            #print(third)
            #print(fourth)
            if 'red' in part:
                red = int(third)
                #print(red)
                if red > r:
                    flag = False
            if 'green' in part:
                green = int(third)
                #print(green)
                if green > g:
                    flag = False
            if 'blue' in part:
                blue = int(third)
                #print(blue)
                if blue > b:
                    flag = False
    if flag:
        total = total + gamenum
print(total)
