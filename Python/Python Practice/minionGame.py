def minion_game(string):
    # your code goes here
    kevin_score=0
    stuart_score=0
    length= len(string)
    vowels='AEIOU'
    
    for i in range(length):
        substr_count= length - i
        if string[i] in vowels:
            kevin_score+=substr_count
        else:
            stuart_score+=substr_count
            
    if kevin_score>stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score>kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")  
    
    
    if __name__ == '__main__':
    s = input()
    minion_game(s)