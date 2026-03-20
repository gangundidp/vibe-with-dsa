# Class to represent an item with value and weight
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate the maximum value we can get with fractional knapsack
def fractionalKnapsack(W, arr, n):

    # Sort items based on the value/weight ratio in descending order
    arr.sort(key=lambda x: (x.value / x.weight), reverse=True)

    currWeight = 0
    finalValue = 0.0

    for i in range(n):

        if currWeight + arr[i].weight <= W:
            currWeight += arr[i].weight
            finalValue += arr[i].value  # Add the full value of the item
        else:
            remain = W - currWeight
            finalValue += (arr[i].value / arr[i].weight) * remain
            break  
        
    return finalValue  


if __name__ == "__main__":
    n = 3
    weight = 50  # Capacity of knapsack
    arr = [Item(100, 20), Item(60, 10), Item(120, 30)]
    
    ans = fractionalKnapsack(weight, arr, n)
    print(f"The maximum value is: {ans:.2f}")
    