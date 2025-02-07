def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
    def client_inputs():
        client_one_principal = float(input("Principle (amount): "))
        client_one_time =      float(input("Time:               "))
        client_one_rate =      float(input("Rate:               "))
        return client_one_principal, client_one_time, client_one_rate

    client_one_principal, client_one_time, client_one_rate = client_inputs()
    amount = client_one_principal*(1+(client_one_rate/100))**client_one_time
    print("Compound Interest: "+str(round(amount - client_one_principal,2)))
    print("---")

    client_two_principal, client_two_time, client_two_rate = client_inputs()
    amount = client_two_principal*(1+(client_two_rate/100))**client_two_time
    print("Compound Interest: "+str(round(amount - client_two_principal,2)))
    print("---")

    client_three_principal, client_three_time, client_three_rate = client_inputs()
    amount = client_three_principal*(1+(client_three_rate/100))**client_three_time
    print("Compound Interest: "+str(round(amount - client_three_principal,2)))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":

    calculateCompoundInterest()