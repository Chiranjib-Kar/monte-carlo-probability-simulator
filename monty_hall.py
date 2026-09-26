"""Monte Carlo probability Simulator to simulate the Monty Hall Problem"""
import random
def monty_hall(trials:int=100000,switch:bool=True)->float:
    doors=[0,1,2]
    wins=0
    for i in range(trials):
        car_door = random.choice(doors)
        player_choose=random.choice(doors)
        remaining_door=[]
        for d in doors:
            if d!=car_door and d!=player_choose:
                remaining_door.append(d)
        host_open=random.choice(remaining_door)

        if switch:
            final=[]
            for x in doors:
                if x!=player_choose and x!=host_open:
                    final.append(x)
            final_choice=random.choice(final)
        else:
            final_choice=player_choose

        if final_choice==car_door:
            wins+=1
    return wins/trials

switch_prob=monty_hall(trials=100000,switch=True)
stay_prob=monty_hall(trials=100000,switch=False)
"""In case of switch decision we get the probability as 2/3 and in case of stay decision we get the probability 1/3 as evident from the result"""

print(f"Win probability while switching:{switch_prob}")
print(f"Win probability while staying:{stay_prob}")
        
