#user input
kozunaci = int(input())
egg_trays = int(input())
cookies = int(input())

#logic
kozunaci_price = kozunaci * 3.2
eggs = 4.35 * egg_trays
cookies_price = 5.4 * cookies
paint = 0.15 * (egg_trays * 12)

total = kozunaci_price + eggs + cookies_price + paint

#print output
print(f'{total:.2f}')