file = open("/sys/class/thermal/thermal_zone0/temp")
temp =float(file.read()) / 1000
file.close()
print("The temp of cpu : {0:.3f} `C".format(temp))
