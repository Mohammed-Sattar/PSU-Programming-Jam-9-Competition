# N, K = map(int, input().split())

# if (N < 1 or N > 105 or K < 1 or K > 103):
#     print(-1)
#     SystemExit()
# requirements = list(map(int, input().split()))
# diffs = []
# valid = True
# for i in range(len(requirements)-1):
#     diffs.append(abs(requirements[i] - requirements[i+1]))

# for diff in diffs:
#     if diff > K:
#         print(-1)
#         valid = False
#         break

# if (valid):
    # print(*requirements, end=' ')


def is_valid_distribution(water_requirements, maximum_difference, total_water, mid):
    remaining_water = total_water
    for requirement in water_requirements:
        if requirement > mid:
            return False
        remaining_water -= min(mid, requirement)
    return remaining_water >= 0


def distribute_water(zone, water_requirements, maximum_difference, total_water, min_water):
    if zone >= len(water_requirements):
        return

    if zone * 2 + 1 >= len(water_requirements):
        # Leaf node, distribute the remaining water
        water = min(total_water, min_water, water_requirements[zone])
        water_requirements[zone] -= water
        return

    left_child = zone * 2 + 1
    right_child = zone * 2 + 2

    min_requirement = max(0, water_requirements[zone] - maximum_difference)
    max_requirement = min(water_requirements[zone] + maximum_difference, water_requirements[zone])

    left_water = min(total_water, max_requirement)
    right_water = total_water - left_water

    distribute_water(left_child, water_requirements, maximum_difference, left_water, min_water)
    distribute_water(right_child, water_requirements, maximum_difference, right_water, min_water)


# Read input
N, K = map(int, input().split())
water_requirements = list(map(int, input().split()))

# Initialize the total water as the sum of all requirements
total_water = sum(water_requirements)

# Initialize the minimum and maximum values for the binaryApologies once again for the incomplete response. The code provided below is the continuation of the previous code snippet:

# search
low = 0
high = sum(water_requirements)

while low <= high:
    mid = (low + high) // 2
    if is_valid_distribution(water_requirements, K, total_water, mid):
        low = mid + 1
    else:
        high = mid - 1

# If the minimum water requirement exceeds the total water available, print -1
if low > total_water:
    print(-1)
else:
    min_water = low

    # Reset the water requirements list
    distributed_water = water_requirements.copy()

    # Distribute the water based on the minimum water requirement
    distribute_water(0, distributed_water, K, total_water, min_water)

    # Check if all water requirements have been met
    if sum(distributed_water) == 0:
        print(*water_requirements)
    else:
        print(-1)