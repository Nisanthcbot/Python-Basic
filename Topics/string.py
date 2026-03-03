#use case is mobile number will be hide in between numbers ex: 91******12 how we can achieve is by index

mobile = "9976071066" 

masked =mobile[:2]+"******"+mobile[-2:]

print(masked)


"""
what here is happening :

we are getting the string by index no [:2] is = 0:2 index so the ans is 99 and we are adding an * for next 6 letter and 
we add the last 2 number of the mobile number by [-2 : 0] -2 is an starting index and 0 is an ending index 


"""


#formatting the text into title case 

song_name ="shape OF You"
artist ="NISANTH M"

print(f"{song_name.title()}-{artist.title()}")

"""
what here is happening:

we are converting the string by using function called .title() this will convert the first letter in to cap and next to lower  
by using f string we are printing  

"""


#Replacing old string into new string by using replace() function 
#use case uber la book Panni irukom in annur ana ipo we have to change the location 

location="Annur"
Fixed_location=location.replace("Annur","Sathy Road")
print(Fixed_location)



#dataset la 1000+ uber id iruku but id la message oda join ah iruku adha adukanum how we can do this 


message = "Uber id is : UB12345 keep is safe"

uber_id= message.split(":")[1].split("keep")[0].strip()

print(uber_id)

"""
we are spliting  the by delimiter by using function called split()

strip() is an function which is used to remove the white space

"""