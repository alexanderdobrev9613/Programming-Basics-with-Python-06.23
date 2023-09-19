start_range = int(input())
end_range = int(input())

barcodes = ""

for a in range(start_range // 1000, (end_range // 1000) + 1):
    for b in range((start_range // 100) % 10, ((end_range // 100) % 10) + 1):
        for c in range((start_range // 10) % 10, ((end_range // 10) % 10) + 1):
            for d in range(start_range % 10, (end_range % 10) + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    barcode = a * 1000 + b * 100 + c * 10 + d
                    barcodes += f"{barcode} "

print(barcodes)