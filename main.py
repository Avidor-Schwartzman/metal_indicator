print ("--------")
band_name = input ("please enter a band name")
print (band_name)

#band_name = band_name.lower()
#print (band_name)

print ("--------")
# this won't work:
# metal_bands = ["amon amarth, bring me the horizon, Tool,"]
# but this will:
metal_bands_lowercase = ["amon amarth", "bring me the horizon", "tool" , "metallica", "megadeth", "iron maiden" , "motorhead"]
metal_bands_uppercase = ["AMON AMARTH", "BRING ME THE HORIZON" , "TOOL" , "METALLICA", "MEGADETH" , "IRON MAIDEN", "MOTORHEAD"]
metal_bands_title = ["Amon Amarth", "Bring Me The Horizon", "Tool", "Metallica", "Megadeth" , "Iron Maiden" , "Motorhead"]
if band_name in metal_bands_lowercase:    
    print("True") 
else: 
    print("false")   
if band_name in metal_bands_uppercase:  
    print("true")  
else:           
    print ("false")    
if band_name in metal_bands_title: 
    print ("true")
else:
    print("false")    
# if the band isnt written in the direcory write: Don`t know
if (band_name in metal_bands_lowercase) or (band_name in metal_bands_uppercase) or (band_name in metal_bands_title):
    print ("true")
else: 
    print ("don`t know")
