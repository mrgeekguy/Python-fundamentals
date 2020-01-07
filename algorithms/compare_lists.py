list_1 = [2, 5, 7, 19]
list_2 = [3, 5, 19, 28]

def compare(a, b):
    ascore = 0
    bscore = 0
    for n1, n2 in zip(a, b):
        if n1 > n2:
            ascore += 1
        elif n2 > n1:
            bscore += 1
    else:
        False
    return ascore, bscore

my_stuff = compare(list_1, list_2)