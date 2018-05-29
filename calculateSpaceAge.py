# calculates your age on each of the 8 planets

age = int(input("How old are you in seconds?: "))
print("===================================================")

mercury_days_per_year = 87.969257175
mercury_seconds_per_year = mercury_days_per_year*24*60*60
mercury_age = age/mercury_seconds_per_year
print("Age on Mercury: ", mercury_age, "Earth years old")

venus_days_per_year = 224.700799215
venus_seconds_per_year = venus_days_per_year*24*60*60
venus_age = age/venus_seconds_per_year
print("Age on Venus: ", venus_age, "Earth years old")

earth_days_per_year = 365.25
earth_seconds_per_year = 31557600
earth_age = age/earth_seconds_per_year
print("Age on Earth: ", earth_age, "Earth years old")

mars_days_per_year = 686.96797095
mars_seconds_per_year = mars_days_per_year*24*60*60
mars_age = age/mars_seconds_per_year
print("Age on Mars: ", mars_age, "Earth years old")

jupiter_days_per_year = 4332.82012875
jupiter_seconds_per_year = jupiter_days_per_year*24*60*60
jupiter_age = age/jupiter_seconds_per_year
print("Age on Jupiter: ", jupiter_age, "Earth years old")

saturn_days_per_year = 10755.6986445
saturn_seconds_per_year = saturn_days_per_year*24*60*60
saturn_age = age/saturn_seconds_per_year
print("Age on Saturn: ", saturn_age, "Earth years old")

uranus_days_per_year = 30687.1530015
uranus_seconds_per_year = uranus_days_per_year*24*60*60
uranus_age = age/uranus_seconds_per_year
print("Age on Uranus: ", uranus_age, "Earth years old")

neptune_days_per_year = 60190.029630000005
neptune_seconds_per_year = neptune_days_per_year*24*60*60
neptune_age = age/neptune_seconds_per_year
print("Age on Neptune: ", neptune_age, "Earth years old")

print("===================================================")
print()
