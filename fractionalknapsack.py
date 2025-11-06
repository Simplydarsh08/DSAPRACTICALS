# Fractional Knapsack Problem (Greedy Algorithm)

def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    
    # Calculate profit/weight ratio
    ratio = []
    for i in range(n):
        ratio.append(profits[i] / weights[i])
    
    # Combine all data and sort by ratio (descending)
    items = list(zip(weights, profits, ratio))
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_profit = 0
    for w, p, r in items:
        if capacity >= w:
            # Take the whole item
            capacity -= w
            total_profit += p
        else:
            # Take the fractional part
            total_profit += p * (capacity / w)
            break  # Knapsack is full
    
    return total_profit


# Example
weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

max_profit = fractional_knapsack(weights, profits, capacity)
print("Maximum profit:", max_profit)
