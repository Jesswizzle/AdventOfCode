dataset = open('day2.txt','r')
r = 12
g = 13
b = 14
total = 0

#To iterate through strings:
for line in dataset:
    #print(line)
    largest_so_far_red = 0
    largest_so_far_green = 0
    largest_so_far_blue = 0

#Splitting string into LHS and RHS after colon:
    first, second = line.split(':')
    #print(first)
    #print(second)

    #Splitting RHS of colon based on ';':
    segments = second.split(';')
        #print(segments)
    #Splitting RHS of string by ',':
    for segment in segments:
            alone = segment.split(',')
            #print(alone)
    #Stripping whitespace on LHS:
            for part in alone:
                part = part.lstrip()
                #print(part)
    #Splitting number (third) and colour (fourth):
                third, fourth = part.split(' ')
                #print(third)
                #print(fourth)
                if 'red' in part:
                    red = int(third)
                    #print(red)
                    if red > largest_so_far_red:
                        largest_so_far_red = red
                        #print(largest_so_far_red, red)
                if 'green' in part:
                    green = int(third)
                    #print(green)
                    if green > largest_so_far_green:
                        largest_so_far_green = green
                        #print(largest_so_far_green, green)
                if 'blue' in part:
                    blue = int(third)
                    #print(blue)
                    if blue > largest_so_far_blue:
                        largest_so_far_blue = blue
                        #print(largest_so_far_blue, blue)
    total = total + (largest_so_far_red*largest_so_far_green*largest_so_far_blue)
print(total)
