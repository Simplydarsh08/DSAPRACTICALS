7 -
# Merge Sort to sort online orders by delivery time 
 
def merge_sort(orders): 
    if len(orders) <= 1: 
        return orders 
 
    # Divide 
    mid = len(orders) // 2 
    left_half = merge_sort(orders[:mid]) 
    right_half = merge_sort(orders[mid:]) 
 
    # Conquer (Merge) 
    return merge(left_half, right_half) 
 
def merge(left, right): 
    sorted_orders = [] 
    i = j = 0 
 
    # Compare and merge 
    while i < len(left) and j < len(right): 
        if left[i]['delivery_time'] <= right[j]['delivery_time']: 
            sorted_orders.append(left[i]) 
            i += 1 
        else: 
            sorted_orders.append(right[j]) 
            j += 1 
 
 
    # Append remaining elements 
    sorted_orders.extend(left[i:]) 
    sorted_orders.extend(right[j:]) 
    return sorted_orders 
 
# ---------------------------- 
# Example Usage 
# ---------------------------- 
if __name__ == "__main__": 
    orders = [ 
        {'order_id': 'O101', 'delivery_time': 45}, 
        {'order_id': 'O102', 'delivery_time': 20}, 
        {'order_id': 'O103', 'delivery_time': 30}, 
        {'order_id': 'O104', 'delivery_time': 10}, 
        {'order_id': 'O105', 'delivery_time': 25} 
    ] 
 
    print("Original Orders:") 
    for order in orders: 
        print(order) 
 
    sorted_orders = merge_sort(orders) 
 
    print("\nSorted Orders by Delivery Time (Ascending):") 
    for order in sorted_orders: 
        print(order)

