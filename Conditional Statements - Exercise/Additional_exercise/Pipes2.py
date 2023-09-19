# user input

v = int(input())
p_1_litters_per_h = int(input())
p_2_litters_per_h = int(input())
hours_missing = float(input())

# logic

p_1_overall = p_1_litters_per_h * hours_missing
p_2_overall = p_2_litters_per_h * hours_missing

space = p_1_overall + p_2_overall

percentage_v = (space / v * 100)

percentage_p_1 = (p_1_overall / space) * 100
percentage_p_2 = (p_2_overall / space) * 100

litters_above = abs(v - space)

# output

if v > space:
    print(f'The pool is{percentage_v: .2f}% full. Pipe 1:{percentage_p_1: .2f}%. Pipe 2:{percentage_p_2: .2f}%.')
else:
    print(f'For{hours_missing: .2f} hours the pool overflows with{litters_above: .2f} liters.')