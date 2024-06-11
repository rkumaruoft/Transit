import matplotlib.pyplot as plt
import numpy


def read_file_data(filename):
    this_file = open(filename, 'r')
    lines = this_file.readlines()
    lines.pop(0)
    lines.pop(0)
    lines.pop(0)
    return lines


if __name__ == '__main__':
    c_2 = read_file_data('kumarre4_c2.csv')
    time = []
    brightness = []
    brightness_err = []
    brightness_frac = []
    brightness_frac_err = []
    for line in c_2:
        line = line.replace('\n', '')
        line = line.split(',')
        time.append(float(line[0]))
        brightness.append(float(line[1]))
        brightness_err.append(float(line[2]))
        brightness_frac.append(float(line[3]))
        brightness_frac_err.append(float(line[4]))

    brighness_min = min(brightness)

    indexes = []
    count = 0
    for t in time:
        count += 1
        if 494 >= t >= 493:
            indexes.append(count)

    this_min = []
    for index in indexes:
        this_min.append(brightness[index])

    min_2 = min(this_min)

    plt.errorbar(numpy.array(time), numpy.array(brightness), linestyle='none', marker='o', markersize=1)
    plt.xlabel('Time (days)')
    plt.ylabel('Brightness (solar luminosity)')
    plt.axhline(y=brighness_min, color='k', linestyle='--', linewidth=0.2)
    plt.axhline(y=min_2, color='k', linestyle='--', linewidth=0.2)
    plt.show()


    this_min = []
    for index in indexes:
        this_min.append(brightness_frac[index])

    min_2 = min(this_min)
    brightness_frac_min = min(brightness_frac)

    plt.errorbar(numpy.array(time), numpy.array(brightness_frac), linestyle='none', marker='o', markersize=1)
    plt.xlabel('Time (days)')
    plt.ylabel('Brightness Fraction(solar luminosity)')
    plt.axhline(y=brightness_frac_min, color='k', linestyle='--', linewidth=0.2)
    plt.axhline(y=min_2, color='k', linestyle='--', linewidth=0.2)
    plt.show()
