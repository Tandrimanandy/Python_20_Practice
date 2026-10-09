'''
Question 12: Cricket Match Statistics
A cricket application stores a player's name, runs scored, balls faced, and number of boundaries in a tuple. Write a function to calculate the strike rate and display whether the player scored a half-century.
Strike rate = (runs scored / balls faced) × 100.

'''


def cricket_stats(*player):
    name, runs, balls, boundaries = player

    strike_rate = (runs / balls) * 100 if balls else 0
    print(f"\n Player: {name}  \n Runs: {runs} \n Balls: {balls} \n Boundaries: {boundaries} \n Strike Rate: {strike_rate:.2f}")

    match runs:
        case r if r >= 100:
            print("Scored a century.")
        case r if r >= 50:
            print("Scored a half-century.")
        case _:
            print("Did not score a half-century.")

name = input("Enter player name: ")
runs = int(input("Enter runs scored: "))
balls = int(input("Enter balls faced: "))
boundaries = int(input("Enter number of boundaries: "))
cricket_stats(name, runs, balls, boundaries)
print()