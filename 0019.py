best = 1000000000
sour = []
bitter = []

def find_best(i, sour_level, bitter_level, n):
    global best
    if((i==n) and (bitter_level>0) and (abs(sour_level-bitter_level)<best)):
        best = abs(sour_level-bitter_level)
    elif (i!=n):
        find_best(i+1, sour_level, bitter_level, n) # dont choose i ingredient
        find_best(i+1, sour_level*sour[i], bitter_level+bitter[i], n) # choose i ingredient

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        ingredient = str(input()).split(' ')
        sour.append(int(ingredient[0]))
        bitter.append(int(ingredient[1]))

    find_best(0, 1, 0, n)

    print(best)

