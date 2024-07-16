import numpy as np
import random


def main():
    score = 0
    ov = -1
    cards = list(np.random.randint(1, 30, size=8))
    
    print(f"cards :{cards}")
    for i, v in enumerate(cards):
        if (i == 0):
            ov = v
            print(f"ov :{ov}")
            continue
        
        guess = random.randint(False, True)
        if (guess == True):
            if (v > ov):
                score += 20
            else:
                score -= 15
        else:
            if (v < ov):
                score += 20
            else:
                score -= 15
            
        print(f"ov :{ov}, v :{v}, guess :{guess}, score :{score}")
        ov = v
        
    return score
    
    

if __name__ == "__main__":
    retval = main()
    print (f"score :{retval}")
