def calculate_bikes_distribution(N, S, C, X, scenario):
    # Initialize bikes count at each outlet
    north = N
    south = S
    city_center = C

    # Simulate for 7 days

    if scenario == 1:
        # Calculate bikes returned to each outlet based on Scenario 1
        CC_to_CC = 0.1 * city_center
        CC_to_N = 0.6 * city_center
        CC_to_S = 0.3 * city_center

        # Update the counts of bikes at each outlet based on returns
        city_center += CC_to_CC
        north += CC_to_N
        south += CC_to_S

    elif scenario == 2:
        # Calculate bikes returned to each outlet based on Scenario 2
        N_to_N = 0.6 * north
        N_to_CC = 0.1 * north
        N_to_S = 0.3 * north

        # Update the counts of bikes at each outlet based on returns
        north += N_to_N
        city_center += N_to_CC
        south += N_to_S

    else:
        return 0  # Erroneous input

    # Redistribute bikes if any outlet exceeds X bikes
    if city_center > X:
        extra = city_center - X
        city_center = X
        

    if north > X:
        extra = north - X
        north = X
        
    if south > X:
        extra = south - X
        south = X
        

# Check how many outlets have bikes count at least X
    outlets_at_least_X = len([outlet for outlet in [city_center, north, south] if outlet >= X])
    
    if outlets_at_least_X == 3:
        return 1  # All outlets have more than X bikes
    elif outlets_at_least_X == 0:
        return 2  # No outlet has more than X bikes
    elif outlets_at_least_X == 1:
        return 3  # Only one outlet has more than X bikes
    elif outlets_at_least_X == 2:
        return 4  # Two outlets have more than X bikes
    else:
        return 0  # Should not happen, included for completeness


# Read inputs
N=int(input())
S=int(input())
C=int(input())
X=int(input())
scenario=int(input())
# Calculate and print the result
result = calculate_bikes_distribution(N, S, C, X, scenario)
print(result)


# -----------------------------------------------------------------------------------------

# def calculate_bikes_distribution(N, S, C, X, scenario):
#     # Initialize bikes count at each outlet
#     north = N
#     south = S
#     city_center = C

#     # Simulate for 7 days
#     for _ in range(7):
#         if scenario == 1:
#             # Calculate bikes returned to each outlet based on Scenario 1
#             CC_to_CC = 0.1 * city_center
#             CC_to_N = 0.6 * city_center
#             CC_to_S = 0.3 * city_center

#             # Update the counts of bikes at each outlet based on returns
#             city_center += CC_to_CC
#             north += CC_to_N
#             south += CC_to_S

#         elif scenario == 2:
#             # Calculate bikes returned to each outlet based on Scenario 2
#             N_to_N = 0.6 * north
#             N_to_CC = 0.1 * north
#             N_to_S = 0.3 * north

#             # Update the counts of bikes at each outlet based on returns
#             north += N_to_N
#             city_center += N_to_CC
#             south += N_to_S

#     # Redistribute bikes if any outlet exceeds X bikes
#     excess_bikes = max(0, city_center - X) + max(0, north - X) + max(0, south - X)
#     if excess_bikes > 0:
#         total_excess = city_center + north + south - 3 * X
#         city_center -= (city_center - X) / total_excess * excess_bikes
#         north -= (north - X) / total_excess * excess_bikes
#         south -= (south - X) / total_excess * excess_bikes

#     # Check how many outlets have bikes count at least X
#     outlets_at_least_X = len([outlet for outlet in [city_center, north, south] if outlet >= X])

#     if outlets_at_least_X == 3:
#         return 1  # All outlets have more than X bikes
#     elif outlets_at_least_X == 0:
#         return 2  # No outlet has more than X bikes
#     elif outlets_at_least_X == 1:
#         return 3  # Only one outlet has more than X bikes
#     elif outlets_at_least_X == 2:
#         return 4  # Two outlets have more than X bikes
#     else:
#         return 0  # Should not happen, included for completeness


# # Read inputs
# N = int(input())
# S = int(input())
# C = int(input())
# X = int(input())
# scenario = int(input())

# # Calculate and print the result
# result = calculate_bikes_distribution(N, S, C, X, scenario)
# print(result)






def calculate_bikes_distribution(N, S, C, X, scenario):
    # Initialize bikes count at each outlet
    north = N
    south = S
    city_center = C

    # Simulate for 7 days
    for _ in range(7):
        if scenario == 1:
            # Calculate bikes returned to each outlet based on Scenario 1
            CC_to_CC = 0.1 * city_center
            CC_to_N = 0.6 * city_center
            CC_to_S = 0.3 * city_center

            # Update the counts of bikes at each outlet based on returns
            city_center += CC_to_CC
            north += CC_to_N
            south += CC_to_S

        elif scenario == 2:
            # Calculate bikes returned to each outlet based on Scenario 2
            N_to_N = 0.6 * north
            N_to_CC = 0.1 * north
            N_to_S = 0.3 * north

            # Update the counts of bikes at each outlet based on returns
            north += N_to_N
            city_center += N_to_CC
            south += N_to_S

    # Redistribute bikes if any outlet exceeds X bikes
    excess_bikes = max(0, city_center - X) + max(0, north - X) + max(0, south - X)
    if excess_bikes > 0:
        total_excess = city_center + north + south - 3 * X
        city_center -= (city_center - X) / total_excess * excess_bikes
        north -= (north - X) / total_excess * excess_bikes
        south -= (south - X) / total_excess * excess_bikes

    # Check how many outlets have bikes count at least X
    outlets_at_least_X = len([outlet for outlet in [city_center, north, south] if outlet >= X])

    if outlets_at_least_X == 3:
        return 1  # All outlets have more than X bikes
    elif outlets_at_least_X == 0:
        return 2  # No outlet has more than X bikes
    elif outlets_at_least_X == 1:
        return 3  # Only one outlet has more than X bikes
    elif outlets_at_least_X == 2:
        return 4  # Two outlets have more than X bikes
    else:
        return 0  # Should not happen, included for completeness


# Read inputs
N = int(input())
S = int(input())
C = int(input())
X = int(input())
scenario = int(input())

# Calculate and print the result
result = calculate_bikes_distribution(N, S, C, X, scenario)
print(result)

