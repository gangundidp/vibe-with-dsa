from typing import List

class LemonadeStand:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0  
        ten = 0   
        
        # Process each customer's bill
        for bill in bills:
            if bill == 5:
                # Customer pays with $5 -> no change needed
                five += 1
                
            elif bill == 10:
                # Customer pays with $10 -> needs $5 as change
                if five > 0:
                    five -= 1  # Give one $5 as change
                    ten += 1   # Accept the $10 bill
                else:
                    return False  # Cannot provide change
                
            else:  # bill == 20
                # Customer pays with $20 -> needs $15 as change
                if five > 0 and ten > 0:
                    five -= 1  # Use one $5
                    ten -= 1   # Use one $10
                elif five >= 3:
                    five -= 3  # Use three $5 bills
                else:
                    return False  # Cannot provide change

        return True  # Successfully gave change to all customers



if __name__ == "__main__":
    stand = LemonadeStand()
    bills = [5, 5, 5, 10, 20]
    print("Queue of customers:", *bills)


    ans = stand.lemonadeChange(bills)
    if ans:
        print("It is possible to provide change for all customers.")
    else:
        print("It is not possible to provide change for all customers.")