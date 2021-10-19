
# The Lead Game  |    Problem Code: TLG
# Problem Statement :  https://www.codechef.com/problems/TLG


cummScore1, cummScore2 = [], []
for _ in range(int(input())):
    
    player1Score, player2Score = map(int, input().split())
    
    if cummScore1 and cummScore2:
        cummScore1.append(cummScore1[-1] + player1Score)
        cummScore2.append(cummScore2[-1] + player2Score)
    else:
        cummScore1.append(player1Score)
        cummScore2.append(player2Score)

leadPlayer = 0
winLead = -1

for score1, score2 in zip(cummScore1, cummScore2):
    
    lead = abs(score2 - score1)
    
    if score1 > score2 and lead > winLead:
        leadPlayer = 1
    
    elif score2 > score1 and lead > winLead:
        leadPlayer = 2 
        
    winLead = max(winLead, lead)
    
print(leadPlayer, winLead)
    
    
# Input -               

# 5
#                              Cummulative Scores
# Player1    Player2        Player1         Player2     Lead Player       Lead

# 140       82              140             82          Player1           58
# 89        134             229             216         Player1           13
# 90        110             319             326         Player2           7
# 112       106             431             432         Player2           1
# 88        90              519             522         Player2           3