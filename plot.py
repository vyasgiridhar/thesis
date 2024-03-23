import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def plot_memory():
    # Function to calculate M
    def calculate_M(s, m):
        return ((12 * s - 8 * m + 17) * 32) / (8 * 1024)

    # Values for m and s
    m = 6
    s_values = range(1, 1400)  # Values of s from 1 to 1000

    # Calculate M for each s value
    M_values = [calculate_M(s, m) for s in s_values]
    plt.figure(figsize=(10, 6))

    # Plotting the original line
    plt.plot(s_values, M_values, label='Consumption Model', color='blue')

    # Plotting another line with different color only until s=100
    s_values_partial = range(1, 835)  # Values of s from 1 to 100
    M_values_partial = [calculate_M(s, m) for s in s_values_partial]
    plt.plot(s_values_partial, M_values_partial, label='Practical Limit', color='orange')

    # Adding a horizontal line at M = 48
    plt.axhline(y=48, color='green', linestyle='--', label='M = 48')
    plt.text(0, 50, 'Max Available Memory', color='black', fontsize=12, va='center')

    # Calculating the intersection point
    intersection_s = 835
    intersection_M = calculate_M(intersection_s, m)
    print(intersection_M)
    # Adding a horizontal line at memory = 4.566 KB, stopping at the intersection point
    plt.axhline(y=intersection_M, color='orange', linestyle='--', xmax=intersection_s / max(s_values))

    # Adding a vertical line at tile_size = 100, stopping at the intersection point
    plt.axvline(x=835, color='orange', linestyle='--', ymax=intersection_M / max(M_values))

    plt.text(840, 36, 'Practical Limit', color='black', fontsize=12, va='center')

    plt.xlabel('Tile Size')
    plt.ylabel('Memory in KB')
    plt.title('Memory Consumption vs Tile Size')
    plt.legend()
    plt.grid(True)

    plt.savefig('figures/memory_6.png')

def plot_strong_scaling():
    # Given data
    data = [
        {'memory_send': 1.3040075302124023, 'memory_get': 0.13414263725280762, 'compute': 0.0009646415710449219, 'PE_WIDTH': 49, 'PE_HEIGHT': 394, 'TILE_SIZE': 100, 'device_min_time': 1.461564, 'device_mean_time': 1.4615680253807108, 'device_max_time': 1.461571},
        {'memory_send': 0.35059452056884766, 'memory_get': 0.05960536003112793, 'compute': 0.0010902881622314453, 'PE_WIDTH': 11, 'PE_HEIGHT': 201, 'TILE_SIZE': 200, 'device_min_time': 2.070809, 'device_mean_time': 3.9120610452284037, 'device_max_time': 3.980017},
        {'memory_send': 0.22172808647155762, 'memory_get': 0.039269208908081055, 'compute': 0.0012493133544921875, 'PE_WIDTH': 2, 'PE_HEIGHT': 410, 'TILE_SIZE': 300, 'device_min_time': 3.942177, 'device_mean_time': 8.117620015853658, 'device_max_time': 8.442716},
        {'memory_send': 0.5876154899597168, 'memory_get': 0.03474831581115723, 'compute': 0.0011088848114013672, 'PE_WIDTH': 1, 'PE_HEIGHT': 435, 'TILE_SIZE': 400, 'device_min_time': 2.41828, 'device_mean_time': 14.087057298850574, 'device_max_time': 15.161431},
        {'memory_send': 0.13598918914794922, 'memory_get': 0.027393817901611328, 'compute': 0.0009591579437255859, 'PE_WIDTH': 1, 'PE_HEIGHT': 276, 'TILE_SIZE': 500, 'device_min_time': 2.09627, 'device_mean_time': 20.94484203985507, 'device_max_time': 23.552135},
        {'memory_send': 0.11241602897644043, 'memory_get': 0.027078628540039062, 'compute': 0.0009317398071289062, 'PE_WIDTH': 1, 'PE_HEIGHT': 190, 'TILE_SIZE': 600, 'device_min_time': 2.552874, 'device_mean_time': 29.46246160526316, 'device_max_time': 34.047623},
        {'memory_send': 0.0963294506072998, 'memory_get': 0.018555402755737305, 'compute': 0.001041412353515625, 'PE_WIDTH': 1, 'PE_HEIGHT': 136, 'TILE_SIZE': 700, 'device_min_time': 4.393447, 'device_mean_time': 40.19359054411764, 'device_max_time': 46.583751},
        {'memory_send': 0.08830022811889648, 'memory_get': 0.023576974868774414, 'compute': 0.0009660720825195312, 'PE_WIDTH': 1, 'PE_HEIGHT': 105, 'TILE_SIZE': 800, 'device_min_time': 4.481978, 'device_mean_time': 50.833811600000004, 'device_max_time': 60.621101},
        {'memory_send': 0.08466649055480957, 'memory_get': 0.01660752296447754, 'compute': 0.0010573863983154297, 'PE_WIDTH': 1, 'PE_HEIGHT': 91, 'TILE_SIZE': 835, 'device_min_time': 14.726078, 'device_mean_time': 58.1243399010989, 'device_max_time': 66.198708}
    ]

    # Extracting data
    time = np.array([measurement["device_mean_time"] for measurement in data])
    resources = np.array([measurement["PE_HEIGHT"] * measurement['PE_WIDTH'] for measurement in data])

    # Plotting the empirical data
    plt.figure(figsize=(10, 6))
    plt.plot(resources, time, marker='o', linestyle='-', label='Empirical Data')

    plt.xlabel('Number of Resources (Resource Rectangle)')
    plt.ylabel('Execution Time (s)')
    plt.title('Strong Scaling: Execution Time (s) vs Resources')
    plt.yscale('log')
    plt.grid(True)
    plt.legend()
    plt.savefig('figures/strong_scaling.png')

def plot_error():
    data_h = {
        'Uniform': {'abs_error': 1.868264121185348e-07, 'max_error': 4.7966837882995605e-05, 'min_error': 4.427134990692139e-05, 'percentile_99_9': 2.7745962142944336e-05},
        'Normal': {'abs_error': 2.1799156257884533e-08, 'max_error': 3.2633543014526367e-06, 'min_error': 2.771615982055664e-06, 'percentile_99_9': 3.2335519790649414e-06},
        'Exponential': {'abs_error': 4.6171714984666323e-07, 'max_error': 2.5480985641479492e-05, 'min_error': 2.1189451217651367e-05, 'percentile_99_9': 2.4333596229553223e-05},
        'Gamma': {'abs_error': 2.1414055595414538e-07, 'max_error': 2.3409724235534668e-05, 'min_error': 4.832446575164795e-05, 'percentile_99_9': 1.9311904907226562e-05},
        'Triangular': {'abs_error': 4.0224753661277646e-07, 'max_error': 4.953145980834961e-05, 'min_error': 7.25090503692627e-05, 'percentile_99_9': 4.933774471282959e-05},
        'Logistic': {'abs_error': 6.66019843720278e-08, 'max_error': 2.0265579223632812e-06, 'min_error': 3.1739473342895508e-06, 'percentile_99_9': 1.9729286432266483e-06},
        'Laplace': {'abs_error': 1.2937622528852444e-08, 'max_error': 2.816319465637207e-06, 'min_error': 2.0563602447509766e-06, 'percentile_99_9': 1.2069940567016602e-06},
        'Pareto': {'abs_error': 3.507981816142092e-08, 'max_error': 6.854534149169922e-06, 'min_error': 5.543231964111328e-06, 'percentile_99_9': 6.8247318267822266e-06}
    }

    # Setting the positions for the points

    # Plotting
    plt.figure(figsize=(10, 8))
    distributions = list(data_h.keys())
    y = np.arange(len(distributions))    
    max_error = np.array([data_h[d]["max_error"] for d in distributions])
    min_error = np.array([data_h[d]["min_error"] for d in distributions])
    plt.errorbar(max_error, y, xerr=np.abs(max_error - min_error), fmt='o', label='Hardware error rates: Range (Max - Min)', capsize=5, color='orange')

    plt.yticks(y, distributions)
    plt.ylabel('Distributions')
    plt.xlabel('Error')
    plt.title('Minimum and Maximum Error Metrics for Different Distributions')
    plt.legend()

    plt.tight_layout()
    plt.savefig('figures/error_distributions.png')


def plot_execution():
    s_u_on_upper_tile = [
        {'memory_send': 0.013970375061035156, 'memory_get': 0.005804538726806641, 'compute': 0.0009729862213134766, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 100, 'device_min_time': 1.359224, 'device_mean_time': 1.349225, 'device_max_time': 1.359224},
        {'memory_send': 0.013950347900390625, 'memory_get': 0.0055773258209228516, 'compute': 0.0009081363677978516, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 200, 'device_min_time': 2.437249, 'device_mean_time': 2.449248, 'device_max_time': 2.437249},
        {'memory_send': 0.014788389205932617, 'memory_get': 0.0060689449310302734, 'compute': 0.0008802413940429688, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 300, 'device_min_time': 4.470254, 'device_mean_time': 4.480255, 'device_max_time': 4.470254},
        {'memory_send': 0.012457609176635742, 'memory_get': 0.005620002746582031, 'compute': 0.0008249282836914062, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 400, 'device_min_time': 7.562572, 'device_mean_time': 7.562571, 'device_max_time': 7.562572},
        {'memory_send': 0.013418912887573242, 'memory_get': 0.006231069564819336, 'compute': 0.0009496212005615234, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 500, 'device_min_time': 11.534599, 'device_mean_time': 11.534598, 'device_max_time': 11.534599},
        {'memory_send': 0.016867399215698242, 'memory_get': 0.00815892219543457, 'compute': 0.0009486675262451172, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 600, 'device_min_time': 16.488045, 'device_mean_time': 16.488046, 'device_max_time': 16.488045},
        {'memory_send': 0.013016939163208008, 'memory_get': 0.008176803588867188, 'compute': 0.0010044574737548828, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 700, 'device_min_time': 22.226555, 'device_mean_time': 22.226556, 'device_max_time': 22.226555},
        {'memory_send': 0.015853166580200195, 'memory_get': 0.00992894172668457, 'compute': 0.0009763240814208984, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 800, 'device_min_time': 28.791741, 'device_mean_time': 28.79174, 'device_max_time': 28.791741},
        {'memory_send': 0.012669563293457031, 'memory_get': 0.007717609405517578, 'compute': 0.0008563995361328125, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 835, 'device_min_time': 31.190484, 'device_mean_time': 31.190755, 'device_max_time': 31.190484}
    ]
    s_u_tile_sizes_one = np.array([measurement["TILE_SIZE"] for measurement in s_u_on_upper_tile])
    s_u_time_send_one = np.array([measurement["device_mean_time"] for measurement in s_u_on_upper_tile])

    h_u_on_upper_tile = [
        {'memory_send': 0.013970375061035156, 'memory_get': 0.005804538726806641, 'compute': 0.0009729862213134766, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 100, 'device_min_time': 1.359224, 'device_mean_time': 1.359224, 'device_max_time': 1.359224},
        {'memory_send': 0.013950347900390625, 'memory_get': 0.0055773258209228516, 'compute': 0.0009081363677978516, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 200, 'device_min_time': 2.437249, 'device_mean_time': 2.437249, 'device_max_time': 2.437249},
        {'memory_send': 0.014788389205932617, 'memory_get': 0.0060689449310302734, 'compute': 0.0008802413940429688, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 300, 'device_min_time': 4.470254, 'device_mean_time': 4.470254, 'device_max_time': 4.470254},
        {'memory_send': 0.012457609176635742, 'memory_get': 0.005620002746582031, 'compute': 0.0008249282836914062, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 400, 'device_min_time': 7.562572, 'device_mean_time': 7.562572, 'device_max_time': 7.562572},
        {'memory_send': 0.013418912887573242, 'memory_get': 0.006231069564819336, 'compute': 0.0009496212005615234, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 500, 'device_min_time': 11.534599, 'device_mean_time': 11.534599, 'device_max_time': 11.534599},
        {'memory_send': 0.016867399215698242, 'memory_get': 0.00815892219543457, 'compute': 0.0009486675262451172, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 600, 'device_min_time': 16.488045, 'device_mean_time': 16.488045, 'device_max_time': 16.488045}, 
        {'memory_send': 0.013016939163208008, 'memory_get': 0.008176803588867188, 'compute': 0.0010044574737548828, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 700, 'device_min_time': 22.226555, 'device_mean_time': 22.226555, 'device_max_time': 22.226555},
        {'memory_send': 0.015853166580200195, 'memory_get': 0.00992894172668457, 'compute': 0.0009763240814208984, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 800, 'device_min_time': 28.791741, 'device_mean_time': 28.791741, 'device_max_time': 28.791741},
        {'memory_send': 0.012669563293457031, 'memory_get': 0.007717609405517578, 'compute': 0.0008563995361328125, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 835, 'device_min_time': 31.190484, 'device_mean_time': 31.190484, 'device_max_time': 31.190484}
    ]

    h_u_tile_sizes_one = np.array([measurement["TILE_SIZE"] for measurement in h_u_on_upper_tile])
    h_u_time_send_one = np.array([measurement["device_mean_time"] for measurement in h_u_on_upper_tile])

    s_full_tile = [
        {'memory_send': 0.013302326202392578, 'memory_get': 0.00579071044921875, 'compute': 0.0009589195251464844, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 100, 'device_min_time': 1.645498, 'device_mean_time': 1.785498, 'device_max_time': 1.645498},
        {'memory_send': 0.013498067855834961, 'memory_get': 0.005787372589111328, 'compute': 0.0008828639984130859, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 200, 'device_min_time': 4.371812, 'device_mean_time': 4.571812, 'device_max_time': 4.371812},
        {'memory_send': 0.013023853302001953, 'memory_get': 0.005686521530151367, 'compute': 0.000896453857421875, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 300, 'device_min_time': 9.307943, 'device_mean_time': 9.307943, 'device_max_time': 9.307943},
        {'memory_send': 0.014001131057739258, 'memory_get': 0.0073049068450927734, 'compute': 0.0011363029479980469, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 400, 'device_min_time': 16.059886, 'device_mean_time': 16.159886, 'device_max_time': 16.059886},
        {'memory_send': 0.015066385269165039, 'memory_get': 0.008021354675292969, 'compute': 0.000946044921875, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 500, 'device_min_time': 24.564892, 'device_mean_time': 24.784892, 'device_max_time': 24.564892},
        {'memory_send': 0.012759685516357422, 'memory_get': 0.007748126983642578, 'compute': 0.0009007453918457031, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 600, 'device_min_time': 35.125045, 'device_mean_time': 35.128745, 'device_max_time': 35.125045},
        {'memory_send': 0.012983083724975586, 'memory_get': 0.009078502655029297, 'compute': 0.0009222030639648438, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 700, 'device_min_time': 47.746, 'device_mean_time': 47.876, 'device_max_time': 47.746},
        {'memory_send': 0.011855363845825195, 'memory_get': 0.007876396179199219, 'compute': 0.0008683204650878906, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 800, 'device_min_time': 62.015335, 'device_mean_time': 62.015335, 'device_max_time': 62.015335},
        {'memory_send': 0.012681722640991211, 'memory_get': 0.008727788925170898, 'compute': 0.0009067058563232422, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 830, 'device_min_time': 66.734375, 'device_mean_time': 66.734375, 'device_max_time': 66.734375},
    ]
    s_f_tile_sizes_one = np.array([measurement["TILE_SIZE"] for measurement in s_full_tile])
    s_f_time_send_one = np.array([measurement["device_mean_time"] for measurement in s_full_tile])


    h_full_tile = [
        {'memory_send': 0.013302326202392578, 'memory_get': 0.00579071044921875, 'compute': 0.0009589195251464844, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 100, 'device_min_time': 1.645498, 'device_mean_time': 1.645498, 'device_max_time': 1.645498},
        {'memory_send': 0.013498067855834961, 'memory_get': 0.005787372589111328, 'compute': 0.0008828639984130859, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 200, 'device_min_time': 4.371812, 'device_mean_time': 4.371812, 'device_max_time': 4.371812},
        {'memory_send': 0.013023853302001953, 'memory_get': 0.005686521530151367, 'compute': 0.000896453857421875, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 300, 'device_min_time': 9.307943, 'device_mean_time': 9.307943, 'device_max_time': 9.307943},
        {'memory_send': 0.014001131057739258, 'memory_get': 0.0073049068450927734, 'compute': 0.0011363029479980469, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 400, 'device_min_time': 16.059886, 'device_mean_time': 16.059886, 'device_max_time': 16.059886},
        {'memory_send': 0.015066385269165039, 'memory_get': 0.008021354675292969, 'compute': 0.000946044921875, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 500, 'device_min_time': 24.564892, 'device_mean_time': 24.564892, 'device_max_time': 24.564892},
        {'memory_send': 0.012759685516357422, 'memory_get': 0.007748126983642578, 'compute': 0.0009007453918457031, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 600, 'device_min_time': 35.125045, 'device_mean_time': 35.125045, 'device_max_time': 35.125045},
        {'memory_send': 0.012983083724975586, 'memory_get': 0.009078502655029297, 'compute': 0.0009222030639648438, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 700, 'device_min_time': 47.746, 'device_mean_time': 47.746, 'device_max_time': 47.746},
        {'memory_send': 0.011855363845825195, 'memory_get': 0.007876396179199219, 'compute': 0.0008683204650878906, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 800, 'device_min_time': 62.015335, 'device_mean_time': 62.015335, 'device_max_time': 62.015335},
        {'memory_send': 0.012681722640991211, 'memory_get': 0.008727788925170898, 'compute': 0.0009067058563232422, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'TILE_SIZE': 830, 'device_min_time': 66.734375, 'device_mean_time': 66.734375, 'device_max_time': 66.734375},
    ]

    h_f_tile_sizes_one = np.array([measurement["TILE_SIZE"] for measurement in h_full_tile])
    h_f_time_send_one = np.array([measurement["device_mean_time"] for measurement in h_full_tile])

    # Calculate theoretical time send for Complete Tiles
    theoretical_time_send_half =  4.38e-5 * s_u_tile_sizes_one ** 2 + 1

    # Create subplots with shared y-axis
    fig, axs = plt.subplots(1, 2, figsize=(15, 6), sharey=True)

    # Plot for half tiles
    axs[0].plot(s_u_tile_sizes_one, s_u_time_send_one, marker='o', linestyle='--', label='Simulator', color='blue')
    axs[0].plot(h_u_tile_sizes_one, h_u_time_send_one, marker='x', linestyle='--', label='Hardware', color='orange')
    axs[0].plot(s_u_tile_sizes_one, theoretical_time_send_half, linestyle='--', label='Theoretical $t_{s}^2$', color='grey')
    axs[0].set_xlabel('Tile Size')
    axs[0].set_ylabel('Kernel Execution Time (us)')
    axs[0].set_title('Half Tiles')
    axs[0].legend()
    axs[0].grid(True)

    theoretical_time_send_full = 1.001e-4 * s_u_tile_sizes_one ** 2

    # Plot for Complete Tiles
    axs[1].plot(s_f_tile_sizes_one, s_f_time_send_one, marker='o', linestyle='--', label='Simulator', color='blue')
    axs[1].plot(h_f_tile_sizes_one, h_f_time_send_one, marker='x', linestyle='--', label='Hardware', color='orange')
    axs[1].plot(s_u_tile_sizes_one, theoretical_time_send_full, linestyle='--', label='Theoretical $t_{s}^2$', color='lightgreen')
    axs[1].set_xlabel('Tile Size')
    axs[1].set_title('Complete Tiles')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()  # Adjust layout for better spacing
    plt.savefig('figures/execution_tiles_comparison.png')

def plot_memory_bandwidth():
    data = [
        {'memory_send': 0.011995792388916016, 'memory_get': 0.008997917175292969, 'compute': 0.0008120536804199219, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'size': 830, 'device_min_time': 30.826322, 'device_mean_time': 30.826322, 'device_max_time': 30.826322},
        {'memory_send': 0.023125648498535156, 'memory_get': 0.008764266967773438, 'compute': 0.0009639263153076172, 'PE_WIDTH': 1, 'PE_HEIGHT': 15, 'size': 3320, 'device_min_time': 1.486886, 'device_mean_time': 35.58841866666667, 'device_max_time': 66.719821},
        {'memory_send': 0.049637556076049805, 'memory_get': 0.015784740447998047, 'compute': 0.000896453857421875, 'PE_WIDTH': 1, 'PE_HEIGHT': 55, 'size': 7470, 'device_min_time': 1.358738, 'device_mean_time': 49.55322629090909, 'device_max_time': 66.856208},
        {'memory_send': 0.12793993949890137, 'memory_get': 0.028006553649902344, 'compute': 0.0009822845458984375, 'PE_WIDTH': 1, 'PE_HEIGHT': 153, 'size': 13280, 'device_min_time': 1.469691, 'device_mean_time': 56.423416254901966, 'device_max_time': 66.858298},
        {'memory_send': 0.27542972564697266, 'memory_get': 0.046889305114746094, 'compute': 0.0011260509490966797, 'PE_WIDTH': 1, 'PE_HEIGHT': 351, 'size': 20750, 'device_min_time': 1.53291, 'device_mean_time': 60.10164928774928, 'device_max_time': 66.85012},
        {'memory_send': 0.5485658645629883, 'memory_get': 0.09570193290710449, 'compute': 0.0010666847229003906, 'PE_WIDTH': 1, 'PE_HEIGHT': 703, 'size': 29880, 'device_min_time': 2.40971, 'device_mean_time': 62.41880991180655, 'device_max_time': 67.007532},
        {'memory_send': 0.9447393417358398, 'memory_get': 0.19392085075378418, 'compute': 0.001268148422241211, 'PE_WIDTH': 3, 'PE_HEIGHT': 425, 'size': 40670, 'device_min_time': 19.911224, 'device_mean_time': 63.481088279999994, 'device_max_time': 66.592063},
        {'memory_send': 1.5200650691986084, 'memory_get': 0.26917147636413574, 'compute': 0.0008969306945800781, 'PE_WIDTH': 3, 'PE_HEIGHT': 715, 'size': 53120, 'device_min_time': 26.151752, 'device_mean_time': 64.60962591421911, 'device_max_time': 66.862382},
        {'memory_send': 2.4666779041290283, 'memory_get': 0.4431905746459961, 'compute': 0.001226186752319336, 'PE_WIDTH': 41, 'PE_HEIGHT': 83, 'size': 67230, 'device_min_time': 31.161817, 'device_mean_time': 65.32300378430797, 'device_max_time': 66.986797},
        {'memory_send': 3.62800931930542, 'memory_get': 0.6978654861450195, 'compute': 0.000980377197265625, 'PE_WIDTH': 17, 'PE_HEIGHT': 303, 'size': 83000, 'device_min_time': 31.135512, 'device_mean_time': 65.83146166957872, 'device_max_time': 66.960348},
        {'memory_send': 5.543181419372559, 'memory_get': 1.0171616077423096, 'compute': 0.0010745525360107422, 'PE_WIDTH': 41, 'PE_HEIGHT': 183, 'size': 100430, 'device_min_time': 31.123615, 'device_mean_time': 66.1734687011862, 'device_max_time': 66.94957},
        {'memory_send': 7.7193028926849365, 'memory_get': 1.7436473369598389, 'compute': 0.0012400150299072266, 'PE_WIDTH': 29, 'PE_HEIGHT': 365, 'size': 119520, 'device_min_time': 30.768008, 'device_mean_time': 65.98250607652339, 'device_max_time': 66.592635},
        {'memory_send': 11.053919792175293, 'memory_get': 3.0800509452819824, 'compute': 0.0011034011840820312, 'PE_WIDTH': 18, 'PE_HEIGHT': 817, 'size': 140270, 'device_min_time': 1.974398, 'device_mean_time': 65.43726325418197, 'device_max_time': 66.59183},
        {'memory_send': 15.884877920150757, 'memory_get': 3.9324164390563965, 'compute': 0.0014827251434326172, 'PE_WIDTH': 33, 'PE_HEIGHT': 597, 'size': 162680, 'device_min_time': 12.73713, 'device_mean_time': 66.06818252819653, 'device_max_time': 67.12286},
        {'memory_send': 18.459519624710083, 'memory_get': 3.9828946590423584, 'compute': 0.0016384124755859375, 'PE_WIDTH': 38, 'PE_HEIGHT': 681, 'size': 186750, 'device_min_time': 24.779848, 'device_mean_time': 66.11252101441379, 'device_max_time': 67.082497},
        {'memory_send': 25.454723119735718, 'memory_get': 5.517751932144165, 'compute': 0.001066446304321289, 'PE_WIDTH': 37, 'PE_HEIGHT': 903, 'size': 212480, 'device_min_time': 30.857299, 'device_mean_time': 65.79152248157791, 'device_max_time': 66.683125},
        {'memory_send': 31.651251077651978, 'memory_get': 6.706125736236572, 'compute': 0.0009853839874267578, 'PE_WIDTH': 73, 'PE_HEIGHT': 582, 'size': 239870, 'device_min_time': 30.740972, 'device_mean_time': 65.86283728185755, 'device_max_time': 66.568826},
        {'memory_send': 40.66787624359131, 'memory_get': 8.02257513999939, 'compute': 0.0012598037719726562, 'PE_WIDTH': 109, 'PE_HEIGHT': 489, 'size': 268920, 'device_min_time': 30.882989, 'device_mean_time': 65.97173331464701, 'device_max_time': 66.705903},
        {'memory_send': 50.03248858451843, 'memory_get': 10.09320878982544, 'compute': 0.001294851303100586, 'PE_WIDTH': 70, 'PE_HEIGHT': 949, 'size': 299630, 'device_min_time': 12.327136, 'device_mean_time': 65.72323318721962, 'device_max_time': 66.705225},
        {'memory_send': 59.59386968612671, 'memory_get': 12.667011499404907, 'compute': 0.0021827220916748047, 'PE_WIDTH': 101, 'PE_HEIGHT': 806, 'size': 332000, 'device_min_time': 28.540613, 'device_mean_time': 66.53755845410657, 'device_max_time': 66.86283}
    ]
    def calculate_M(s, m):
        return ((12 * s - 8 * m + 17) * 32) / (8 * 1024)

    # Extracting data
    sizes = [entry['size'] for entry in data]
    memory_send_times = [entry['memory_send'] for entry in data]
    memory_get_times = [entry['memory_get'] for entry in data]
    memory_send_bandwidth = [calculate_M(entry['size'], 6) / entry['memory_send'] for entry in data[3:]]
    memory_get_bandwidth = [((4 * (entry['size'] - 6 + 1) * 32) / (8 * 1024)) / entry['memory_get'] for entry in data[3:]]

    # Creating subplots
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    # Plot transfer times on the left subplot
    axs[0].plot(sizes, memory_send_times, label='Transfer to device', marker='o', color='blue')
    axs[0].plot(sizes, memory_get_times, label='Transfer from device', marker='x', color='orange')
    axs[0].set_xlabel('Size')
    axs[0].set_ylabel('Time (s)')
    axs[0].set_title('Memory Transfer Time vs. time series size')
    axs[0].grid(True)
    axs[0].legend()

    # Plot bandwidth on the right subplot
    axs[1].plot(sizes[3:], memory_send_bandwidth, label='Bandwidth to device', linestyle='--', marker='o', color='green')
    axs[1].plot(sizes[3:], memory_get_bandwidth, label='Bandwidth from device', linestyle='--', marker='x', color='red')
    axs[1].set_xlabel('Size')
    axs[1].set_ylabel('Bandwidth (KB/s)')
    axs[1].set_title('Memory Bandwidth vs. time series size')
    axs[1].grid(True)
    axs[1].legend()

    # Adjust layout
    plt.tight_layout()

    # Save plot
    plt.savefig('./figures/memory_transfer_times_and_bandwidth_subplot.png')

def plot_weak_scaling():
    data = [
        {'memory_send': 0.023125648498535156, 'memory_get': 0.008764266967773438, 'compute': 0.0009639263153076172, 'PE_WIDTH': 1, 'PE_HEIGHT': 15, 'size': 3320, 'device_min_time': 1.486886, 'device_mean_time': 35.58841866666667, 'device_max_time': 66.719821},
        {'memory_send': 0.049637556076049805, 'memory_get': 0.015784740447998047, 'compute': 0.000896453857421875, 'PE_WIDTH': 1, 'PE_HEIGHT': 55, 'size': 7470, 'device_min_time': 1.358738, 'device_mean_time': 49.55322629090909, 'device_max_time': 66.856208},
        {'memory_send': 0.12793993949890137, 'memory_get': 0.028006553649902344, 'compute': 0.0009822845458984375, 'PE_WIDTH': 1, 'PE_HEIGHT': 153, 'size': 13280, 'device_min_time': 1.469691, 'device_mean_time': 56.423416254901966, 'device_max_time': 66.858298},
        {'memory_send': 0.27542972564697266, 'memory_get': 0.046889305114746094, 'compute': 0.0011260509490966797, 'PE_WIDTH': 1, 'PE_HEIGHT': 351, 'size': 20750, 'device_min_time': 1.53291, 'device_mean_time': 60.10164928774928, 'device_max_time': 66.85012},
        {'memory_send': 0.5485658645629883, 'memory_get': 0.09570193290710449, 'compute': 0.0010666847229003906, 'PE_WIDTH': 1, 'PE_HEIGHT': 703, 'size': 29880, 'device_min_time': 2.40971, 'device_mean_time': 62.41880991180655, 'device_max_time': 67.007532},
        {'memory_send': 0.9447393417358398, 'memory_get': 0.19392085075378418, 'compute': 0.001268148422241211, 'PE_WIDTH': 3, 'PE_HEIGHT': 425, 'size': 40670, 'device_min_time': 19.911224, 'device_mean_time': 63.481088279999994, 'device_max_time': 66.592063},
        {'memory_send': 1.5200650691986084, 'memory_get': 0.26917147636413574, 'compute': 0.0008969306945800781, 'PE_WIDTH': 3, 'PE_HEIGHT': 715, 'size': 53120, 'device_min_time': 26.151752, 'device_mean_time': 64.60962591421911, 'device_max_time': 66.862382},
        {'memory_send': 2.4666779041290283, 'memory_get': 0.4431905746459961, 'compute': 0.001226186752319336, 'PE_WIDTH': 41, 'PE_HEIGHT': 83, 'size': 67230, 'device_min_time': 31.161817, 'device_mean_time': 65.32300378430797, 'device_max_time': 66.986797},
        {'memory_send': 3.62800931930542, 'memory_get': 0.6978654861450195, 'compute': 0.000980377197265625, 'PE_WIDTH': 17, 'PE_HEIGHT': 303, 'size': 83000, 'device_min_time': 31.135512, 'device_mean_time': 65.83146166957872, 'device_max_time': 66.960348},
        {'memory_send': 5.543181419372559, 'memory_get': 1.0171616077423096, 'compute': 0.0010745525360107422, 'PE_WIDTH': 41, 'PE_HEIGHT': 183, 'size': 100430, 'device_min_time': 31.123615, 'device_mean_time': 66.1734687011862, 'device_max_time': 66.94957},
        {'memory_send': 7.7193028926849365, 'memory_get': 1.7436473369598389, 'compute': 0.0012400150299072266, 'PE_WIDTH': 29, 'PE_HEIGHT': 365, 'size': 119520, 'device_min_time': 30.768008, 'device_mean_time': 65.98250607652339, 'device_max_time': 66.592635},
        {'memory_send': 11.053919792175293, 'memory_get': 3.0800509452819824, 'compute': 0.0011034011840820312, 'PE_WIDTH': 18, 'PE_HEIGHT': 817, 'size': 140270, 'device_min_time': 1.974398, 'device_mean_time': 65.43726325418197, 'device_max_time': 66.59183},
        {'memory_send': 15.884877920150757, 'memory_get': 3.9324164390563965, 'compute': 0.0014827251434326172, 'PE_WIDTH': 33, 'PE_HEIGHT': 597, 'size': 162680, 'device_min_time': 12.73713, 'device_mean_time': 66.06818252819653, 'device_max_time': 67.12286},
        {'memory_send': 18.459519624710083, 'memory_get': 3.9828946590423584, 'compute': 0.0016384124755859375, 'PE_WIDTH': 38, 'PE_HEIGHT': 681, 'size': 186750, 'device_min_time': 24.779848, 'device_mean_time': 66.11252101441379, 'device_max_time': 67.082497},
        {'memory_send': 25.454723119735718, 'memory_get': 5.517751932144165, 'compute': 0.001066446304321289, 'PE_WIDTH': 37, 'PE_HEIGHT': 903, 'size': 212480, 'device_min_time': 30.857299, 'device_mean_time': 65.79152248157791, 'device_max_time': 66.683125},
        {'memory_send': 31.651251077651978, 'memory_get': 6.706125736236572, 'compute': 0.0009853839874267578, 'PE_WIDTH': 73, 'PE_HEIGHT': 582, 'size': 239870, 'device_min_time': 30.740972, 'device_mean_time': 65.86283728185755, 'device_max_time': 66.568826},
        {'memory_send': 40.66787624359131, 'memory_get': 8.02257513999939, 'compute': 0.0012598037719726562, 'PE_WIDTH': 109, 'PE_HEIGHT': 489, 'size': 268920, 'device_min_time': 30.882989, 'device_mean_time': 65.97173331464701, 'device_max_time': 66.705903},
        {'memory_send': 50.03248858451843, 'memory_get': 10.09320878982544, 'compute': 0.001294851303100586, 'PE_WIDTH': 70, 'PE_HEIGHT': 949, 'size': 299630, 'device_min_time': 12.327136, 'device_mean_time': 65.72323318721962, 'device_max_time': 66.705225},
        {'memory_send': 59.59386968612671, 'memory_get': 12.667011499404907, 'compute': 0.0021827220916748047, 'PE_WIDTH': 101, 'PE_HEIGHT': 806, 'size': 332000, 'device_min_time': 28.540613, 'device_mean_time': 66.53755845410657, 'device_max_time': 66.86283}
    ]

    # Extracting data
    resources = [entry['PE_WIDTH'] * entry['PE_HEIGHT'] for entry in data]
    device_mean_time = [entry['device_max_time'] for entry in data]

    # Plotting empirical data
    plt.figure(figsize=(10, 6))
    plt.plot(resources, device_mean_time, marker='o', linestyle='-', label='Empirical data')
    plt.ylim(0, 100)
    # Formatting plot
    plt.title('Execution Time vs Number of Resources')
    plt.xlabel('Number of Resources')
    plt.ylabel('Execution Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig('figures/weak_scaling.png')


def plot_total_execution():
    data = [
        {'memory_send': 0.011995792388916016, 'memory_get': 0.008997917175292969, 'compute': 0.0008120536804199219, 'PE_WIDTH': 1, 'PE_HEIGHT': 1, 'size': 830, 'device_min_time': 30.826322, 'device_mean_time': 30.826322, 'device_max_time': 30.826322},
        {'memory_send': 0.023125648498535156, 'memory_get': 0.008764266967773438, 'compute': 0.0009639263153076172, 'PE_WIDTH': 1, 'PE_HEIGHT': 15, 'size': 3320, 'device_min_time': 1.486886, 'device_mean_time': 35.58841866666667, 'device_max_time': 66.719821},
        {'memory_send': 0.049637556076049805, 'memory_get': 0.015784740447998047, 'compute': 0.000896453857421875, 'PE_WIDTH': 1, 'PE_HEIGHT': 55, 'size': 7470, 'device_min_time': 1.358738, 'device_mean_time': 49.55322629090909, 'device_max_time': 66.856208},
        {'memory_send': 0.12793993949890137, 'memory_get': 0.028006553649902344, 'compute': 0.0009822845458984375, 'PE_WIDTH': 1, 'PE_HEIGHT': 153, 'size': 13280, 'device_min_time': 1.469691, 'device_mean_time': 56.423416254901966, 'device_max_time': 66.858298},
        {'memory_send': 0.27542972564697266, 'memory_get': 0.046889305114746094, 'compute': 0.0011260509490966797, 'PE_WIDTH': 1, 'PE_HEIGHT': 351, 'size': 20750, 'device_min_time': 1.53291, 'device_mean_time': 60.10164928774928, 'device_max_time': 66.85012},
        {'memory_send': 0.5485658645629883, 'memory_get': 0.09570193290710449, 'compute': 0.0010666847229003906, 'PE_WIDTH': 1, 'PE_HEIGHT': 703, 'size': 29880, 'device_min_time': 2.40971, 'device_mean_time': 62.41880991180655, 'device_max_time': 67.007532},
        {'memory_send': 0.9447393417358398, 'memory_get': 0.19392085075378418, 'compute': 0.001268148422241211, 'PE_WIDTH': 3, 'PE_HEIGHT': 425, 'size': 40670, 'device_min_time': 19.911224, 'device_mean_time': 63.481088279999994, 'device_max_time': 66.592063},
        {'memory_send': 1.5200650691986084, 'memory_get': 0.26917147636413574, 'compute': 0.0008969306945800781, 'PE_WIDTH': 3, 'PE_HEIGHT': 715, 'size': 53120, 'device_min_time': 26.151752, 'device_mean_time': 64.60962591421911, 'device_max_time': 66.862382},
        {'memory_send': 2.4666779041290283, 'memory_get': 0.4431905746459961, 'compute': 0.001226186752319336, 'PE_WIDTH': 41, 'PE_HEIGHT': 83, 'size': 67230, 'device_min_time': 31.161817, 'device_mean_time': 65.32300378430797, 'device_max_time': 66.986797},
        {'memory_send': 3.62800931930542, 'memory_get': 0.6978654861450195, 'compute': 0.000980377197265625, 'PE_WIDTH': 17, 'PE_HEIGHT': 303, 'size': 83000, 'device_min_time': 31.135512, 'device_mean_time': 65.83146166957872, 'device_max_time': 66.960348},
        {'memory_send': 5.543181419372559, 'memory_get': 1.0171616077423096, 'compute': 0.0010745525360107422, 'PE_WIDTH': 41, 'PE_HEIGHT': 183, 'size': 100430, 'device_min_time': 31.123615, 'device_mean_time': 66.1734687011862, 'device_max_time': 66.94957},
        {'memory_send': 7.7193028926849365, 'memory_get': 1.7436473369598389, 'compute': 0.0012400150299072266, 'PE_WIDTH': 29, 'PE_HEIGHT': 365, 'size': 119520, 'device_min_time': 30.768008, 'device_mean_time': 65.98250607652339, 'device_max_time': 66.592635},
        {'memory_send': 11.053919792175293, 'memory_get': 3.0800509452819824, 'compute': 0.0011034011840820312, 'PE_WIDTH': 18, 'PE_HEIGHT': 817, 'size': 140270, 'device_min_time': 1.974398, 'device_mean_time': 65.43726325418197, 'device_max_time': 66.59183},
        {'memory_send': 15.884877920150757, 'memory_get': 3.9324164390563965, 'compute': 0.0014827251434326172, 'PE_WIDTH': 33, 'PE_HEIGHT': 597, 'size': 162680, 'device_min_time': 12.73713, 'device_mean_time': 66.06818252819653, 'device_max_time': 67.12286},
        {'memory_send': 18.459519624710083, 'memory_get': 3.9828946590423584, 'compute': 0.0016384124755859375, 'PE_WIDTH': 38, 'PE_HEIGHT': 681, 'size': 186750, 'device_min_time': 24.779848, 'device_mean_time': 66.11252101441379, 'device_max_time': 67.082497},
        {'memory_send': 25.454723119735718, 'memory_get': 5.517751932144165, 'compute': 0.001066446304321289, 'PE_WIDTH': 37, 'PE_HEIGHT': 903, 'size': 212480, 'device_min_time': 30.857299, 'device_mean_time': 65.79152248157791, 'device_max_time': 66.683125},
        {'memory_send': 31.651251077651978, 'memory_get': 6.706125736236572, 'compute': 0.0009853839874267578, 'PE_WIDTH': 73, 'PE_HEIGHT': 582, 'size': 239870, 'device_min_time': 30.740972, 'device_mean_time': 65.86283728185755, 'device_max_time': 66.568826},
        {'memory_send': 40.66787624359131, 'memory_get': 8.02257513999939, 'compute': 0.0012598037719726562, 'PE_WIDTH': 109, 'PE_HEIGHT': 489, 'size': 268920, 'device_min_time': 30.882989, 'device_mean_time': 65.97173331464701, 'device_max_time': 66.705903},
        {'memory_send': 50.03248858451843, 'memory_get': 10.09320878982544, 'compute': 0.001294851303100586, 'PE_WIDTH': 70, 'PE_HEIGHT': 949, 'size': 299630, 'device_min_time': 12.327136, 'device_mean_time': 65.72323318721962, 'device_max_time': 66.705225},
        {'memory_send': 59.59386968612671, 'memory_get': 12.667011499404907, 'compute': 0.0021827220916748047, 'PE_WIDTH': 101, 'PE_HEIGHT': 806, 'size': 332000, 'device_min_time': 28.540613, 'device_mean_time': 66.53755845410657, 'device_max_time': 66.86283}
    ]

    # Extracting data
    sizes = [entry['size'] for entry in data]
    memory_send_times = [entry['memory_send'] for entry in data]
    device_mean_times = [entry['device_max_time'] for entry in data]
    memory_get_times = [entry['memory_get'] for entry in data]

    # Plotting
    plt.figure(figsize=(12, 6))

    bar_width = 0.35
    index = np.arange(len(sizes))

    plt.bar(index, memory_send_times, bar_width, label='Transfer to Device')
    plt.bar(index, device_mean_times, bar_width, bottom=memory_send_times, label='Kernel Execution Time')
    plt.bar(index, memory_get_times, bar_width, bottom=np.array(memory_send_times) + np.array(device_mean_times), label='Transfer from Device')

    plt.xlabel('Time Series Size')
    plt.ylabel('Time (s)')
    plt.title('Total Execution Time vs Time Series Size')
    plt.xticks(index, sizes, rotation=45, ha='right')
    plt.legend()

    plt.tight_layout()
    plt.savefig('figures/total_execution_time.png')
   

def plot_theoretical_execution_model():
    data = [
        {'memory_send': 0.023125648498535156, 'memory_get': 0.008764266967773438, 'compute': 0.0009639263153076172, 'PE_WIDTH': 1, 'PE_HEIGHT': 15, 'size': 3320, 'device_min_time': 1.486886, 'device_mean_time': 35.58841866666667, 'device_max_time': 66.719821},
        {'memory_send': 0.049637556076049805, 'memory_get': 0.015784740447998047, 'compute': 0.000896453857421875, 'PE_WIDTH': 1, 'PE_HEIGHT': 55, 'size': 7470, 'device_min_time': 1.358738, 'device_mean_time': 49.55322629090909, 'device_max_time': 66.856208},
        {'memory_send': 0.12793993949890137, 'memory_get': 0.028006553649902344, 'compute': 0.0009822845458984375, 'PE_WIDTH': 1, 'PE_HEIGHT': 153, 'size': 13280, 'device_min_time': 1.469691, 'device_mean_time': 56.423416254901966, 'device_max_time': 66.858298},
        {'memory_send': 0.27542972564697266, 'memory_get': 0.046889305114746094, 'compute': 0.0011260509490966797, 'PE_WIDTH': 1, 'PE_HEIGHT': 351, 'size': 20750, 'device_min_time': 1.53291, 'device_mean_time': 60.10164928774928, 'device_max_time': 66.85012},
        {'memory_send': 0.5485658645629883, 'memory_get': 0.09570193290710449, 'compute': 0.0010666847229003906, 'PE_WIDTH': 1, 'PE_HEIGHT': 703, 'size': 29880, 'device_min_time': 2.40971, 'device_mean_time': 62.41880991180655, 'device_max_time': 67.007532},
        {'memory_send': 0.9447393417358398, 'memory_get': 0.19392085075378418, 'compute': 0.001268148422241211, 'PE_WIDTH': 3, 'PE_HEIGHT': 425, 'size': 40670, 'device_min_time': 19.911224, 'device_mean_time': 63.481088279999994, 'device_max_time': 66.592063},
        {'memory_send': 1.5200650691986084, 'memory_get': 0.26917147636413574, 'compute': 0.0008969306945800781, 'PE_WIDTH': 3, 'PE_HEIGHT': 715, 'size': 53120, 'device_min_time': 26.151752, 'device_mean_time': 64.60962591421911, 'device_max_time': 66.862382},
        {'memory_send': 2.4666779041290283, 'memory_get': 0.4431905746459961, 'compute': 0.001226186752319336, 'PE_WIDTH': 41, 'PE_HEIGHT': 83, 'size': 67230, 'device_min_time': 31.161817, 'device_mean_time': 65.32300378430797, 'device_max_time': 66.986797},
        {'memory_send': 3.62800931930542, 'memory_get': 0.6978654861450195, 'compute': 0.000980377197265625, 'PE_WIDTH': 17, 'PE_HEIGHT': 303, 'size': 83000, 'device_min_time': 31.135512, 'device_mean_time': 65.83146166957872, 'device_max_time': 66.960348},
        {'memory_send': 5.543181419372559, 'memory_get': 1.0171616077423096, 'compute': 0.0010745525360107422, 'PE_WIDTH': 41, 'PE_HEIGHT': 183, 'size': 100430, 'device_min_time': 31.123615, 'device_mean_time': 66.1734687011862, 'device_max_time': 66.94957},
        {'memory_send': 7.7193028926849365, 'memory_get': 1.7436473369598389, 'compute': 0.0012400150299072266, 'PE_WIDTH': 29, 'PE_HEIGHT': 365, 'size': 119520, 'device_min_time': 30.768008, 'device_mean_time': 65.98250607652339, 'device_max_time': 66.592635},
        {'memory_send': 11.053919792175293, 'memory_get': 3.0800509452819824, 'compute': 0.0011034011840820312, 'PE_WIDTH': 18, 'PE_HEIGHT': 817, 'size': 140270, 'device_min_time': 1.974398, 'device_mean_time': 65.43726325418197, 'device_max_time': 66.59183},
        {'memory_send': 15.884877920150757, 'memory_get': 3.9324164390563965, 'compute': 0.0014827251434326172, 'PE_WIDTH': 33, 'PE_HEIGHT': 597, 'size': 162680, 'device_min_time': 12.73713, 'device_mean_time': 66.06818252819653, 'device_max_time': 67.12286},
        {'memory_send': 18.459519624710083, 'memory_get': 3.9828946590423584, 'compute': 0.0016384124755859375, 'PE_WIDTH': 38, 'PE_HEIGHT': 681, 'size': 186750, 'device_min_time': 24.779848, 'device_mean_time': 66.11252101441379, 'device_max_time': 67.082497},
        {'memory_send': 25.454723119735718, 'memory_get': 5.517751932144165, 'compute': 0.001066446304321289, 'PE_WIDTH': 37, 'PE_HEIGHT': 903, 'size': 212480, 'device_min_time': 30.857299, 'device_mean_time': 65.79152248157791, 'device_max_time': 66.683125},
        {'memory_send': 31.651251077651978, 'memory_get': 6.706125736236572, 'compute': 0.0009853839874267578, 'PE_WIDTH': 73, 'PE_HEIGHT': 582, 'size': 239870, 'device_min_time': 30.740972, 'device_mean_time': 65.86283728185755, 'device_max_time': 66.568826},
        {'memory_send': 40.66787624359131, 'memory_get': 8.02257513999939, 'compute': 0.0012598037719726562, 'PE_WIDTH': 109, 'PE_HEIGHT': 489, 'size': 268920, 'device_min_time': 30.882989, 'device_mean_time': 65.97173331464701, 'device_max_time': 66.705903},
        {'memory_send': 50.03248858451843, 'memory_get': 10.09320878982544, 'compute': 0.001294851303100586, 'PE_WIDTH': 70, 'PE_HEIGHT': 949, 'size': 299630, 'device_min_time': 12.327136, 'device_mean_time': 65.72323318721962, 'device_max_time': 66.705225},
        {'memory_send': 59.59386968612671, 'memory_get': 12.667011499404907, 'compute': 0.0021827220916748047, 'PE_WIDTH': 101, 'PE_HEIGHT': 806, 'size': 332000, 'device_min_time': 28.540613, 'device_mean_time': 66.53755845410657, 'device_max_time': 66.86283}
    ]

    # Extracting data
    sizes = [entry['size'] for entry in data]
    memory_send_times = [entry['memory_send'] for entry in data]
    device_mean_times = [entry['device_max_time'] for entry in data]
    memory_get_times = [entry['memory_get'] for entry in data]

    total_execution_time = np.add(np.add(memory_get_times, device_mean_times), memory_send_times)
    # Define the equation components
    def memory_transfer_time(s):
        return 5.354e-10 * s ** 2 + 4.843e-06 * s + -1.207e-01

    def time_for_compute(s, ts):
        # The below configuration 
        return (1.001e-4 * ts ** 2)

    def memory_fetch_time(s):
        return 1.007e-10 * s ** 2 + 4.400e-06 * s + -1.014e-01

    # Define total runtime equation
    def total_runtime(s, ts):
       return memory_transfer_time(s) + time_for_compute(s, ts) + memory_fetch_time(s)

    # Generate s values
    s_values = np.linspace(830, 332000, 100)  # Adjust the range and number of points as needed
    plt.figure(figsize=(10, 6))

    # Fix ts value
    ts = 830
    # Calculate total runtime for each s value
    total_runtimes = total_runtime(s_values, ts)
    # Plot
    plt.plot(s_values, total_runtimes, color='blue', label="Theoretical execution time")
    plt.plot(sizes, total_execution_time, color='orange', label="Measured execution time")
    plt.xlabel('time series size')
    plt.ylabel('Total Runtime (s)')
    plt.legend()
    # plt.yscale('log')
    plt.title('Total Runtime(s) for different time series sizes')
    plt.grid(True)
    plt.savefig('figures/theoretical_execution_model.png')


def plot_real_world_performance():
    data = [
        {'memory_send': 156.06443858146667, 'memory_get': 27.199196338653564, 'compute': 0.001691579818725586, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 16.524376, 'device_mean_time': 42.704274686605544, 'device_max_time': 43.930931},
        {'memory_send': 154.85263538360596, 'memory_get': 26.737263202667236, 'compute': 0.0016398429870605469, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 40.618607, 'device_mean_time': 42.754014416412, 'device_max_time': 43.743227},
        {'memory_send': 155.4055540561676, 'memory_get': 26.93845534324646, 'compute': 0.001672983169555664, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 40.588358, 'device_mean_time': 42.93402938926406, 'device_max_time': 43.978919},
        {'memory_send': 155.1145613193512, 'memory_get': 26.827099084854126, 'compute': 0.0023229122161865234, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 40.588358, 'device_mean_time': 42.93402938926406, 'device_max_time': 43.978919},
        {'memory_send': 158.8321075439453, 'memory_get': 27.622785806655884, 'compute': 0.0020401477813720703, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 40.455108, 'device_mean_time': 42.806478867941856, 'device_max_time': 43.822939},
        {'memory_send': 152.19291281700134, 'memory_get': 26.63333511352539, 'compute': 0.0016064643859863281, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 40.511402, 'device_mean_time': 42.81415340463794, 'device_max_time': 43.949598},
        {'memory_send': 170.00020956993103, 'memory_get': 27.12411618232727, 'compute': 0.0017528533935546875, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 40.544514, 'device_mean_time': 42.953516586291784, 'device_max_time': 43.795431},
        {'memory_send': 151.39313125610352, 'memory_get': 26.79736042022705, 'compute': 0.002087116241455078, 'PE_WIDTH': 457, 'PE_HEIGHT': 696, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 40.649479, 'device_mean_time': 42.83830259543751, 'device_max_time': 44.041313},
        {'memory_send': 74.8089873790741, 'memory_get': 12.508122682571411, 'compute': 0.0014882087707519531, 'PE_WIDTH': 457, 'PE_HEIGHT': 323, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 27.371265, 'device_mean_time': 42.945597482138865, 'device_max_time': 43.869333},
        {'memory_send': 0.09686565399169922, 'memory_get': 0.020044803619384766, 'compute': 0.0010311603546142578, 'PE_WIDTH': 173, 'PE_HEIGHT': 1, 'series': '/mnt/e1000/home/eidf100/eidf100/giridhar/mp_wse/data/starlightcurves', 'device_min_time': 27.529544, 'device_mean_time': 27.95009662427745, 'device_max_time': 27.988294}
    ]
    # Extracting data
    memory_send_times = [entry['memory_send'] for entry in data]
    device_max_time = [entry['device_max_time'] for entry in data]
    memory_get_times = [entry['memory_get'] for entry in data]

    # Plotting
    fig = plt.figure(figsize=(10, 6))
    ax = plt.gca()
    bar_width = 0.35
    index = np.arange(len(data), dtype=np.int32)

    # Plotting memory_send
    plt.bar(index, memory_send_times, bar_width, label='Transfer to Device')

    # Plotting device_mean_time stacked on top of memory_send
    plt.bar(index, device_max_time, bar_width, bottom=memory_send_times, label='Kernel Execution Time')

    # Plotting memory_get stacked on top of memory_send and device_mean_time
    plt.bar(index, memory_get_times, bar_width, bottom=[memory_send + device_mean for memory_send, device_mean in zip(memory_send_times, device_max_time)], label='Transfer from Device')

    total_execution_time = np.add(np.add(memory_send_times, device_max_time), memory_get_times)
    print(total_execution_time.sum())

    # Adding labels and title
    plt.xlabel('Iteration')
    plt.ylabel('Time in seconds')
    ax.set_xticks(np.arange(len(data), dtype=np.int32))
    plt.title('Iteration runtimes for a series of size 1 Million')
    plt.legend()

    # Show plot
    plt.tight_layout()
    plt.savefig('figures/real_world_execution.png')

def plot_script_time():
    plt.figure(figsize=(4, 6))

    # Data
    compile_time = 166.15961980819702
    execution_time = 111.62644386291504    
    
    # Labels
    labels = ['Average Execution Time']

    # Heights
    heights = np.array([[compile_time], [execution_time]])

    # Colors
    colors = ['skyblue', 'salmon']

    # Create the stacked bar plot
    plt.bar(labels, heights[0], color=colors[0], label='compile time')
    plt.bar(labels, heights[1], bottom=heights[0], color=colors[1], label='execution time')

    # Add labels and title
    plt.ylabel('Seconds')
    plt.title('Average Execution Time of program')
    plt.legend()

    # Show plot
    plt.savefig('figures/average_execution_time.png')


if __name__ == '__main__':
    plot_execution()
    plot_memory_bandwidth()
    plot_memory()
    plot_real_world_performance()
    plot_execution()
    plot_strong_scaling()
    plot_weak_scaling()
    plot_total_execution()
    plot_error()
    plot_script_time()
    plot_theoretical_execution_model()
