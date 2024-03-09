def process_name(name):
    return name.lower().capitalize()

def calculate_diversity_rarity(names):
    freq = {}
    total_names = len(names)
    
    for name in names:
        full_name = process_name(name.split())
        if (len(full_name) > 4 or len(full_name) < 2):
            continue
        elif re.search(r'[^a-zA-Z-]', name):
            continue
        family_name = full_name[-1]
        if family_name in freq:
            freq[family_name] += 1
        else:
            freq[family_name] = 1
    
    unique_names = sum(1 for value in freq.values() if value == 1)
    diversity_percentage = len(freq) / total_names * 100
    rarity_percentage = unique_names / total_names * 100
    
    return diversity_percentage, rarity_percentage

# Read input
try:
    n = int(input())
    names = [input().strip() for _ in range(n)]

    diversity, rarity = calculate_diversity_rarity(names)
    print(int(diversity))
    print(int(rarity))

except Exception as e:
    print(-1)
