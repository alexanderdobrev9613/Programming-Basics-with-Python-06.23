detergent_bottles = 750 * int(input())
tobewashed = input()

# logic
total_clean_dishes = 0
total_clean_pots = 0
leftover_detergent = 0
detergent_per_dish = 5
detergent_per_pot = 15
wash_count = 0
detergent_used = 0

while True:
    if tobewashed != 'End':
        tobewashed = int(tobewashed)
        wash_count += 1
        if wash_count % 3 == 0:
            detergent_used += detergent_per_pot * tobewashed
            total_clean_pots += tobewashed
        else:
            detergent_used += detergent_per_dish * tobewashed
            total_clean_dishes += tobewashed
    else:
        diff = abs(detergent_bottles - detergent_used)
        print("Detergent was enough!")
        print(f"{total_clean_dishes} dishes and {total_clean_pots} pots were washed.")
        print(f"Leftover detergent {diff} ml.")
        break
    if detergent_bottles < detergent_used:
        diff = abs(detergent_bottles - detergent_used)
        print(f"Not enough detergent, {diff} ml. more necessary!")
    tobewashed = input()