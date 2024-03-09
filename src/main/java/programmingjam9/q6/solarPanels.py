def update_efficiency(solar_panels, panel_index, new_efficiency):
    solar_panels[panel_index - 1] = new_efficiency

def get_max_efficiency(solar_panels, start_index, end_index):
    return max(solar_panels[start_index - 1:end_index])

def get_avg_efficiency(solar_panels, start_index, end_index):
    return sum(solar_panels[start_index - 1:end_index]) / (end_index - start_index + 1)

# Read input
N, Q = map(int, input().split())
solar_panels = list(map(float, input().split()))

# Process operations
for _ in range(Q):
    operation = list(map(float, input().split()))
    op_type = int(operation[0])

    if op_type == 1:
        panel_index = int(operation[1])
        new_efficiency = operation[2]
        update_efficiency(solar_panels, panel_index, new_efficiency)
    elif op_type == 2:
        start_index = int(operation[1])
        end_index = int(operation[2])
        max_efficiency = get_max_efficiency(solar_panels, start_index, end_index)
        print(f"{max_efficiency:.1f}")
    elif op_type == 3:
        start_index = int(operation[1])
        end_index = int(operation[2])
        avg_efficiency = get_avg_efficiency(solar_panels, start_index, end_index)
        print(f"{avg_efficiency:.1f}")