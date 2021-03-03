import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV

from process_abf import get_all_sweep_data
from get_spike_data import calculate_spike_rate, get_spike_times_for_epsp, get_spike_times_for_trace


def plot_spike_rates(spike_rates):
    plt.hist(spike_rates, 30)
    plt.show()


def get_all_spike_rates(abf_objects):
    spike_rates = []
    for abf_ob in abf_objects:
        sweep_data = get_all_sweep_data(abf_ob)
        for sweep in sweep_data:
            sweep = get_spike_times_for_trace(sweep)
            rate = calculate_spike_rate(sweep)
            spike_rates.append(rate[0])
    return spike_rates


def calculate_spike_rate_kernel_smoothing(spike_times):
    x_d = np.linspace(0, max(spike_times)+0.5, 1000)
    spike_times = np.array(spike_times)
    model = KernelDensity(bandwidth=0.1, kernel='gaussian')
    model.fit(spike_times[:, None])
    log_dens = model.score_samples(x_d[:, None])
    # plt.fill_between(x_d, np.exp(log_dens))
    # plt.show()
    return np.exp(log_dens)




