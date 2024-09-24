
planet1 = "Closest to Sun"
print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

#Slicing a String , get a substring from string
print(planet1[:7])
print(planet1[:])
print(planet1[1:5])
print(planet1[7:-1])
print(planet1[11:])

#Slicing List or Array
devops = ["AWS", "Ansible","Terraform","Azure","Jenkins","Bash"]
print(devops[:])
print(devops[1:3])
print(devops[:-2])
print(devops[1:6])
#Slicing Tuple
planets = ("Mars", "jupiter","Mercury","Earth","Sun","Moon")
print(planets[2:4])
print(planets[:])
print(planets[2:5][0][0:5])


#Slicing Dictionary

skills = {
    "DevOps":("Ansible","jenkins","Terraform","Bash"),
    "Cloud":["AWS","Azure","Google Cloud"],
    "Database":["MySQL","PostgreSQL","MongoDB"],
    "OS":("Windows","Linux","MacOS")
}

print(skills)
print(skills["DevOps"])
print(skills["Cloud"])
print(skills["DevOps"][1:-2])

