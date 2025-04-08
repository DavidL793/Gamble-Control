print("Lets go gambling!") #Gamble responsibly
print("It is said that you shouldn't spend more than 1% of your household income(Pre-tax) on gambling") #My source is google
income = int(input("Whats your household income in £:"))
budget = income/100

def pickGame():
    selection = input("""Where we going?
    1 - FGO""")

    if selection == "1":
        FGO(budget)
    else:
        print("Cmon man just pick 1")
def FGO(budget):
    summonCost = 3
    rateUpFiveServant = 0.8
    FiveServant = 1
    SpecificFiveServant = 0.11
    rateUpCraftEssence = 1.4
    rateUpFourServant = "n/a"
    def switchcase():
        decide = input("""What would you like to summon for (Respond with the number)
        1 - Rate up Five star servant
        2 - Five star servant in general
        3 - A specific off rate up 5 star servant
        4 - A specific Rate up 5 star craft essence
        """)
        if decide == "1":
            return rateUpFiveServant
        elif decide == "2":
            return FiveServant
        elif decide == "3":
            return SpecificFiveServant
        elif decide == "4":
            return rateUpCraftEssence
        else:
            print("Please try again")
            switchcase()
    choice = switchcase()

    hypoGuarantee = 100/choice
    sqCost = hypoGuarantee * 3
    print("The chances of getting what you want is: " + str(choice) + "%")
    print("In theory you would get what you want in " + str(hypoGuarantee) + " Pulls which would be " + str(sqCost) + " Saint Quartz")
    #On Average SQ cost: 1.575 per £
    cost = sqCost/1.575
    print("On average that would be: £" + str(round(cost, 2)))
    if cost >= budget:
        print ("This is above your budget I don't recommend you commit to this")
    else:
        print("Go for it, Remember this is not a guarantee and just a guide")
    
    
pickGame()
