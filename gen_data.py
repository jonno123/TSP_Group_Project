import random
import statistics
import time
import matplotlib.pyplot as plt
import numpy as np


base_score = 125000
base_dec = 0.03
mean_drift = 0.10
line = []
meandata = []
var = 5
def live_plotter(x, mean, line, identifier='',pause_time = 0.1):

    if line == [] :
        plt.ion()
        fig = plt.figure(figsize = (13,6))
        ax = fig.add_subplot(111)

        line2 = ax.plot(x, mean, '-o', alpha=0.8)

        plt.ylabel('Mean Over Time')
        plt.title('Generational Change in Mean'. format(identifier))
        plt.show()
    line2.set_data(x,mean)
    if np.min(mean) <= line2.axes.get_ylim()[0] or np.max(mean) >= line2.axes.get_ylim()[1]:
        plt.ylim([np.min(mean)-np.std(meandata),np.max(mean) + np.std(mean)])
    plt.pause(pause_time)
    return line


for x in range(0, var-1):
    base_score -= base_score*random.uniform(-base_dec, base_dec)
    this_scores = [base_score+(base_score*random.uniform(-mean_drift, mean_drift)) for x in range(1000)]
    mean = statistics.mean(this_scores)

    sd = statistics.stdev(this_scores, mean)
    print(x, int(base_score), int(mean), int(sd))
    time.sleep(1)

    line = live_plotter(x, mean, line, identifier='',pause_time = 0.1)


