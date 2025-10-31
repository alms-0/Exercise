import matplotlib.pyplot as plt

fhand = open("StudentExercise.csv")

next(fhand)

def average(ls):
    total = 0
    for number in ls:
        total += float(number) # means (+=) total = total + float(numer)
    return total / len(ls)

ls = []

def prop_above(sl):
    count = 0
    avrg = average(ls)
    for elm in sl:
        if elm > avrg:
            count += 1
    proportion = count / len(sl)

    return proportion
def median(sl):
    sl.sort()
    n = len(sl)
    if n % 2 == 0:
        mid1 = sl[n //2 -1]
        mid2 = sl[n //2]
        return (mid1 + mid2) /2
    else:
        return sl[n //2]
def make_histogram(sl):
    plt.hist(sl ,bins = 6)
    plt.ylabel( "Frequency" )
    plt.xlabel( " Exercise hours")

    plt.show()
    
        
for line in fhand:
    
    hrs = line.split(',')
    hour = hrs[0]

    if hour == "":
        continue
    else:
        num = float(hour)
        ls.append(num)
print(ls)
print("Average is : ", round (average(ls),2))
print ("Prop Above: ",round (prop_above(ls),2))
print("Median is: ", median(ls))

make_histogram(ls)
