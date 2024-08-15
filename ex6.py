def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, data in sorted_items:
        if budget >= data['cost']:
            selected_items.append(item)
            budget -= data['cost']
            total_calories += data['calories']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name, data = item_list[i - 1]
        cost = data['cost']
        calories = data['calories']
        
        for j in range(1, budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]
    
    total_calories = dp[n][budget]
    
    j = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, _ = item_list[i - 1]
            selected_items.append(item_name)
            j -= items[item_name]['cost']
    
    return selected_items, total_calories

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_selection, greedy_calories = greedy_algorithm(items, budget)
print("Greedy selection:", greedy_selection)
print("Total calories (greedy):", greedy_calories)

dp_selection, dp_calories = dynamic_programming(items, budget)
print("Dynamic programming selection:", dp_selection)
print("Total calories (DP):", dp_calories)
