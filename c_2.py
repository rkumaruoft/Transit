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

    plt.errorbar(numpy.array(time), numpy.array(brightness),
                 yerr=brightness_err, linestyle='None', marker='.', markersize=1, alpha=0.5)
    plt.xlabel('Time (days)')
    plt.ylabel('Brightness (solar luminosity)')
    plt.axhline(y=brighness_min, color='k', linestyle='--', linewidth=0.2)
    plt.axhline(y=min_2, color='k', linestyle='--', linewidth=0.2)
    plt.title("C_2 Light Data")
    plt.savefig('c2_brightness.png', dpi=450)
    plt.show()

    #planet 1
    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 122 <= time[i] <= 123:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_1 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 245 <= time[i] <= 247:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_2 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 368 <= time[i] <= 371:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_3 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 493 <= time[i] <= 494:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_4 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 617 <= time[i] <= 617.6:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_5 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 740 <= time[i] <= 742:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_6 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 864 <= time[i] <= 866:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_7 = this_time[this_brightness.index(min(this_brightness))]

    periods = [min_2 - min_1, min_3 - min_2, min_4 - min_3, min_5 - min_4, min_6 - min_5, min_7 - min_6]
    print(numpy.mean(periods))

    # planet 1 single transit
    this_brightness_frac = []
    this_brightness_frac_err = []
    this_time = []
    for i in range(len(time)):
        if 616 <= time[i] <= 618:
            this_time.append(time[i])
            this_brightness_frac.append(brightness_frac[i])
            this_brightness_frac_err.append(brightness_frac_err[i])

    plt.figure().set_figwidth(7)
    plt.errorbar(numpy.array(this_time), numpy.array(this_brightness_frac),
                 yerr=this_brightness_frac_err, marker='.', markersize=1, alpha=0.5)

    plt.xlabel('Time (days)')
    plt.ylabel('Brightness (solar luminosity)')
    plt.title("C2/Planet 1 Single Transit")
    plt.savefig('c21_single.png', dpi=500)
    plt.show()

    depth = max(this_brightness_frac) - min(this_brightness_frac)
    print(depth)


    #planet 2
    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 141 <= time[i] <= 144:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_1 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 305 <= time[i] <= 307:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_2 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 467 <= time[i] <= 469:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_3 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 630 <= time[i] <= 632:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_4 = this_time[this_brightness.index(min(this_brightness))]

    this_brightness = []
    this_time = []
    for i in range(len(time)):
        if 792 <= time[i] <= 795:
            this_time.append(time[i])
            this_brightness.append(brightness[i])

    min_5 = this_time[this_brightness.index(min(this_brightness))]

    periods = [min_2 - min_1, min_3 - min_2, min_4 - min_3, min_5 - min_4]
    print(numpy.mean(periods))

    # planet 1 single transit
    this_brightness_frac = []
    this_brightness_frac_err = []
    this_time = []
    for i in range(len(time)):
        if 305 <= time[i] <= 306.2:
            this_time.append(time[i])
            this_brightness_frac.append(brightness_frac[i])
            this_brightness_frac_err.append(brightness_frac_err[i])

    plt.figure().set_figwidth(7)
    plt.errorbar(numpy.array(this_time), numpy.array(this_brightness_frac),
                 yerr=this_brightness_frac_err, marker='.', markersize=1, alpha=0.5)

    plt.xlabel('Time (days)')
    plt.ylabel('Brightness (solar luminosity)')
    plt.title("C2/Planet 2 Single Transit")
    plt.savefig('c22_single.png', dpi=500)
    plt.show()

    depth = max(this_brightness_frac) - min(this_brightness_frac)
    print(depth)