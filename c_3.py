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
    c_3 = read_file_data('kumarre4_c3.csv')
    time = []
    brightness = []
    brightness_err = []
    brightness_frac = []
    brightness_frac_err = []
    for line in c_3:
        line = line.replace('\n', '')
        line = line.split(',')
        time.append(float(line[0]))
        brightness.append(float(line[1]))
        brightness_err.append(float(line[2]))
        brightness_frac.append(float(line[3]))
        brightness_frac_err.append(float(line[4]))

    min_brightness = min(brightness)
    time_bright = {time[i]: brightness[i] for i in range(len(time))}
    time_bright_frac = {time[i]: brightness_frac[i] for i in range(len(time))}

    this_sec = {}
    for key in time_bright:
        if 137 <= key <= 138:
            this_sec[key] = time_bright[key]

    min_1 = min(this_sec, key=this_sec.get)

    this_sec = {}
    for key in time_bright:
        if 286 <= key <= 287:
            this_sec[key] = time_bright[key]

    min_2 = min(this_sec, key=this_sec.get)

    this_sec = {}
    for key in time_bright:
        if 430 <= key <= 440:
            this_sec[key] = time_bright[key]

    min_3 = min(this_sec, key=this_sec.get)

    this_sec = {}
    for key in time_bright:
        if 585 <= key <= 587:
            this_sec[key] = time_bright[key]

    min_4 = min(this_sec, key=this_sec.get)

    this_sec = {}
    for key in time_bright:
        if 730 <= key <= 740:
            this_sec[key] = time_bright[key]

    min_5 = min(this_sec, key=this_sec.get)

    this_sec = {}
    for key in time_bright:
        if 880 <= key <= 900:
            this_sec[key] = time_bright[key]

    min_6 = min(this_sec, key=this_sec.get)

    periods = [min_2 - min_1, min_3 - min_2, min_4 - min_3, min_5 - min_4, min_6 - min_5]
    period = numpy.mean(periods)

    print(period)

    plt.errorbar(numpy.array(time), numpy.array(brightness), yerr=numpy.array(brightness_err),
                 linestyle='None', marker='.', markersize=1, alpha=0.5)
    plt.xlabel('Time (days)')
    plt.ylabel('Brightness (solar luminosity)')
    plt.axhline(min_brightness, linestyle='--', linewidth=0.5)
    plt.title('C_3 Light Data')
    plt.savefig('c3_brightness.png', dpi=450)
    plt.show()

    min_brightness_frac = min(brightness_frac)
    plt.errorbar(numpy.array(time), numpy.array(brightness_frac), yerr=numpy.array(brightness_frac_err),
                 linestyle='None', marker='.', markersize=1, alpha=0.5)
    plt.xlabel('Time (days)')
    plt.ylabel('Brightness Fraction(solar luminosity)')
    plt.axhline(min_brightness_frac, linestyle='--', linewidth=0.5)
    plt.title('C_3 Light Data')
    plt.savefig('c3_brightness_frac.png', dpi=450)
    plt.show()

    this_time = []
    this_brightness = []
    this_brightness_frac = []
    this_brightness_err = []
    this_brightness_frac_err = []
    for i in range(len(time)):
        if 436 <= time[i] <= 436.71:
            this_time.append(time[i])
            this_brightness.append(brightness[i])
            this_brightness_frac.append(brightness_frac[i])
            this_brightness_err.append(brightness_err[i])
            this_brightness_frac_err.append(brightness_frac_err[i])

    plt.errorbar(numpy.array(this_time), numpy.array(this_brightness_frac), yerr=numpy.array(this_brightness_frac_err),
                 linestyle='None', marker='.', markersize=1, alpha=0.5)
    plt.xlabel('Time (days)')
    plt.ylabel('Brightness (solar luminosity)')
    plt.axhline(min(this_brightness_frac), linestyle='--', linewidth=0.5)
    plt.savefig('c3_single_transit.png', dpi=450)
    plt.show()

    depth = max(this_brightness_frac) - min(this_brightness_frac)
    print(depth)
