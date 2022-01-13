print ("--------")
band_name = input ("please enter a band name")
print (band_name)
print ("--------")
# this won't work:
# metal_bands = ["amon amarth, bring me the horizon, tool,"]
# but this will:
metal_bands = ["amon amarth", "bring me the horizon", "tool"]
if band_name in metal_bands:  
    print("True") 
else: 
    print("fales")    