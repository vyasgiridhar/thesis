import matplotlib.pyplot as plt

def plot_memory():
    # Function to calculate M
    def calculate_M(s, m):
        return ((12 * s - 8 * m + 17) * 32) / (8 * 1024)

    # Values for m and s
    m = 6
    s_values = range(1, 1400)  # Values of s from 1 to 1000

    # Calculate M for each s value
    M_values = [calculate_M(s, m) for s in s_values]

    # Plotting the original line
    plt.plot(s_values, M_values, label='Theoretical Limit', color='blue')

    # Plotting another line with different color only until s=100
    s_values_partial = range(1, 101)  # Values of s from 1 to 100
    M_values_partial = [calculate_M(s, m) for s in s_values_partial]
    plt.plot(s_values_partial, M_values_partial, label='Practical Limit', color='red')
    # Adding a horizontal line at M = 48
    plt.axhline(y=48, color='green', linestyle='--', label='M = 48')
    plt.text(0, 50, 'Max Available Memory', color='black', fontsize=14, va='center')

    plt.xlabel('Tile Size')
    plt.ylabel('Memory in KB')
    plt.title('Memory Consumption vs Tile Size')
    plt.legend()
    plt.grid(True)

    print(calculate_M(100, 6))
    print(calculate_M(1010, 6))

    plt.savefig('figures/memory_6.png')

def plot_execution():
    def calculate_t(s):
        return s ** 2
    
    s_values = range(1, 100)  # Values of s from 1 to 200


    T_values = [calculate_t(s) for s in s_values]
    
    plt.plot(s_values, T_values, label='Theoretical Execution time', color='blue')

    plt.xlabel('Tile Size')
    plt.ylabel('Time')
    plt.title('Execution Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('figures/execution_6.png')


def plot_flops():
    def calculate_flops(t_s, m):
        return 2 * (6 * (t_s * t_s) + 2 * m + 7 * t_s)

    # Given values
    t_s = [40, 60, 80, 100]
    m = 6

    # Execution time in seconds
    execution_time = [228.40117647058827, 402.39764705882357, 700.964705882353, 1097.0117647058823]
    flops_s = []
    # Calculate FLOPs per second
    for index, data in enumerate(t_s):
        flops_s.append(calculate_flops(data, m) / execution_time[index])

    # Plotting
    plt.plot(t_s, flops_s)
    plt.ylabel('FLOPs per Second')
    plt.xlabel('Tile Size')
    plt.title('FLOPs per Second vs Tile Size')
    plt.savefig('figures/flops.png')


def plot_time():
    import matplotlib.pyplot as plt
    import numpy as np

    # Array of measurements
    measurements_array = [
        {
            "memory_send": 0.01697087287902832,
            "memory_get": 33.220380544662476,
            "cycles_send": 194140,
            "time_send": 228.4,
            "PE_WIDTH": 15,
            "PE_HEIGHT": 29,
            "TILE_SIZE": 40
        },
        {
            "memory_send": 0.012476682662963867,
            "memory_get": 26.701477766036987,
            "cycles_send": 194140,
            "time_send": 228.4,
            "PE_WIDTH": 15,
            "PE_HEIGHT": 29,
            "TILE_SIZE": 40
        },
        {
            "memory_send": 0.017986059188842773,
            "memory_get": 30.294108867645264,
            "cycles_send": 146483,
            "time_send": 172.3329411764706,
            "PE_WIDTH": 29,
            "PE_HEIGHT": 15,
            "TILE_SIZE": 40
        },
        {
            "memory_send": 0.014595985412597656,
            "memory_get": 55.45814847946167,
            "cycles_send": 157674,
            "time_send": 185.4988235294118,
            "PE_WIDTH": 5,
            "PE_HEIGHT": 87,
            "TILE_SIZE": 40
        },
        {
            "memory_send": 0.013283014297485352,
            "memory_get": 15.583291053771973,
            "cycles_send": 146474,
            "time_send": 172.3223529411765,
            "PE_WIDTH": 87,
            "PE_HEIGHT": 5,
            "TILE_SIZE": 40
        },
        {
            "memory_send": 0.013087749481201172,
            "memory_get": 27.490763187408447,
            "cycles_send": 342037,
            "time_send": 402.39647058823533,
            "PE_WIDTH": 5,
            "PE_HEIGHT": 38,
            "TILE_SIZE": 60
        },
        {
            "memory_send": 0.014301061630249023,
            "memory_get": 33.674660444259644,
            "cycles_send": 342038,
            "time_send": 402.39764705882357,
            "PE_WIDTH": 5,
            "PE_HEIGHT": 38,
            "TILE_SIZE": 60
        },
        {
            "memory_send": 0.012195587158203125,
            "memory_get": 23.223490953445435,
            "cycles_send": 334924,
            "time_send": 394.0282352941177,
            "PE_WIDTH": 10,
            "PE_HEIGHT": 19,
            "TILE_SIZE": 60
        },
        {
            "memory_send": 0.015163898468017578,
            "memory_get": 38.69815278053284,
            "cycles_send": 333735,
            "time_send": 392.62941176470594,
            "PE_WIDTH": 2,
            "PE_HEIGHT": 95,
            "TILE_SIZE": 60
        },
        {
            "memory_send": 0.010344505310058594,
            "memory_get": 12.537634372711182,
            "cycles_send": 333485,
            "time_send": 392.33529411764704,
            "PE_WIDTH": 19,
            "PE_HEIGHT": 10,
            "TILE_SIZE": 60
        },
        {
            "memory_send": 0.00803828239440918,
            "memory_get": 17.824519872665405,
            "cycles_send": 595820,
            "time_send": 700.964705882353,
            "PE_WIDTH": 3,
            "PE_HEIGHT": 35,
            "TILE_SIZE": 80
        },
        {
            "memory_send": 0.010763406753540039,
            "memory_get": 17.928269863128662,
            "cycles_send": 595822,
            "time_send": 700.9670588235294,
            "PE_WIDTH": 3,
            "PE_HEIGHT": 35,
            "TILE_SIZE": 80
        },
        {
            "memory_send": 0.009912490844726562,
            "memory_get": 13.190192699432373,
            "cycles_send": 595171,
            "time_send": 700.2011764705883,
            "PE_WIDTH": 7,
            "PE_HEIGHT": 15,
            "TILE_SIZE": 80
        },
        {
            "memory_send": 0.008821249008178711,
            "memory_get": 19.340009927749634,
            "cycles_send": 595820,
            "time_send": 700.964705882353,
            "PE_WIDTH": 3,
            "PE_HEIGHT": 35,
            "TILE_SIZE": 80
        },
        {
            "memory_send": 0.006428956985473633,
            "memory_get": 4.07910418510437,
            "cycles_send": 595159,
            "time_send": 700.1870588235295,
            "PE_WIDTH": 15,
            "PE_HEIGHT": 7,
            "TILE_SIZE": 80
        },
        {
            "memory_send": 0.0075740814208984375,
            "memory_get": 18.72184920310974,
            "cycles_send": 932488,
            "time_send": 1097.0447058823531,
            "PE_WIDTH": 2,
            "PE_HEIGHT": 33,
            "TILE_SIZE": 100
        },
        {
            "memory_send": 0.00600743293762207,
            "memory_get": 17.85796880722046,
            "cycles_send": 932488,
            "time_send": 1097.0447058823531,
            "PE_WIDTH": 2,
            "PE_HEIGHT": 33,
            "TILE_SIZE": 100
        },
        {
            "memory_send": 0.0065157413482666016,
            "memory_get": 6.354620933532715,
            "cycles_send": 932466,
            "time_send": 1097.0188235294117,
            "PE_WIDTH": 6,
            "PE_HEIGHT": 11,
            "TILE_SIZE": 100
        },
        {
            "memory_send": 0.006553173065185547,
            "memory_get": 14.41628384590149,
            "cycles_send": 932480,
            "time_send": 1097.035294117647,
            "PE_WIDTH": 1,
            "PE_HEIGHT": 66,
            "TILE_SIZE": 100
        },
        {
            "memory_send": 0.007203817367553711,
            "memory_get": 3.31563138961792,
            "cycles_send": 932465,
            "time_send": 1097.0176470588237,
            "PE_WIDTH": 11,
            "PE_HEIGHT": 6,
            "TILE_SIZE": 100
        }
    ]

    for measurement in measurements_array:
        measurement["memory_get"] *= 1_000_000  # Convert to microseconds
        measurement["memory_send"] *= 1_000_000  # Convert to microseconds

    time_sends = np.array([measurement["time_send"] for measurement in measurements_array])
    pe_widths = np.array([measurement["PE_WIDTH"] for measurement in measurements_array])
    pe_heights = np.array([measurement["PE_HEIGHT"] for measurement in measurements_array])

    # Plot scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(pe_widths, pe_heights, c=time_sends, cmap='viridis', label='Time Sends')
    plt.colorbar(label='Time Send in us')
    plt.xlabel('PE Width')
    plt.ylabel('PE Height')
    plt.title('Scatter Plot of Time Send vs PE Width and Height')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    memory_sends = np.array([measurement["memory_send"] for measurement in measurements_array])

    # Plot scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(pe_widths, pe_heights, c=memory_sends, cmap='viridis', label='Memory Sends')
    plt.colorbar(label='Memory Send in us')
    plt.xlabel('PE Width')
    plt.ylabel('PE Height')
    plt.title('Scatter Plot of Memory Send vs PE Width and Height')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    memory_gets = np.array([measurement["memory_get"] for measurement in measurements_array])

    # Plot scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(pe_widths, pe_heights, c=memory_gets, cmap='viridis', label='Memory Gets')
    plt.colorbar(label='Memory Get in us')
    plt.xlabel('PE Width')
    plt.ylabel('PE Height')
    plt.title('Scatter Plot of Memory Gets vs PE Width and Height')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    tile_sizes = np.array([measurement["TILE_SIZE"] for measurement in measurements_array])
    # Define the width of the bars
    bar_width = 0.2

    # Set the positions for the bars
    r1 = np.arange(len(tile_sizes))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]

    # Create the bar plot
    plt.bar(r1, memory_sends, color='blue', width=bar_width, edgecolor='grey', label='Memory Sends')
    plt.bar(r2, time_sends, color='orange', width=bar_width, edgecolor='grey', label='Time Sends')
    plt.bar(r3, memory_gets, color='green', width=bar_width, edgecolor='grey', label='Memory Gets')

    # Add xticks on the middle of the group bars
    plt.xlabel('Tile Size', fontweight='bold')
    plt.ylabel('Time', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(tile_sizes))], tile_sizes)
    # Add PE_WIDTH and PE_HEIGHT at the top of each bar plot
    for i in range(len(tile_sizes)):
        plt.text(r1[i], max(memory_sends[i], time_sends[i], memory_gets[i]), f'({pe_widths[i]}, {pe_heights[i]})', ha='center')

    # Create legend & Show graphic
    plt.legend()
    plt.title('Bar Graph of Memory Send, Time Send, and Memory Get vs Tile Size')
    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    plot_time()