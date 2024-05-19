age_input = int(input("Enter your age:"))
maximum_heart = 220 - age_input
targetlow_heart = maximum_heart * 0.50
targethigh_heart = maximum_heart * 0.85
print("Your maximum heart rate is", maximum_heart, "bpm")
print("Your target heart rate is",targetlow_heart,"-",targethigh_heart,"bpm")
