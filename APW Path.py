import math


def apw(site_lat, site_long, mag_inclination, mag_declination):
    ls = site_lat * (math.pi / 180)
    lo = site_long * (math.pi / 180)
    im = mag_inclination * (math.pi / 180)
    dm = mag_declination * (math.pi / 180)

    mag_colatitude = math.atan(2 / math.tan(im))
    p = mag_colatitude
    p_show = mag_colatitude * (180 / math.pi)

    print("The magnetic co-latitude is " + str(p_show) + ".")

    pole_lat = math.asin(math.sin(ls) * math.cos(p) + math.cos(ls) * math.sin(p) * math.cos(dm))
    lp = pole_lat
    pole_lat_show = pole_lat * (180 / math.pi)
    print("The pole latitude is " + str(pole_lat_show) + ".")

    long_diff = math.asin((math.sin(p) * math.sin(dm)) / math.cos(lp))
    beta = long_diff * (180 / math.pi)
    print("The longitudinal difference is " + str(beta) + ".")

    if math.cos(p) >= (math.sin(ls) * math.sin(lp)):
        polar_long = site_long + beta
        print("cos p >= sin(ls)sin(lp)")
        print("cos p = " + str(math.cos(p)) + " , sin(ls) =" + str(math.sin(ls)) + " , sin(lp) = " + str(math.sin(lp)) + ' sin(ls)sin(lp) =' + str(math.sin(ls) * math.sin(lp)))
        print("The polar longitude is " + str(polar_long) + ".")
    else:
        polar_long = site_long + 180 - beta
        print("cos p <= sin(ls)sin(lp)")
        print("cos p = " + str(math.cos(p)) + " , sin(ls) =" + str(math.sin(ls)) + " , sin(lp) = " + str(math.sin(lp)) + ' sin(ls)sin(lp) =' + str(math.sin(ls) * math.sin(lp)))
        print("The polar longitude is " + str(polar_long) + ".")

    print("The apparent coordinates for the latitude and longitude for the pole is " + str(pole_lat_show) + ", " + str(
        polar_long) + ".")


obs = int(input("Enter the total number of observations. "))
i = 0
while i < obs:
    site_lat = float(input("Enter Site Latitude. "))
    site_long = float(input("Enter Site Longitude. "))
    mag_inclination = float(input("Enter Magnetic Inclination. "))
    mag_declination = float(input("Enter Magnetic Declination. "))
    print(apw(site_lat, site_long, mag_inclination, mag_declination))
    print(" ")

    i = i + 1
