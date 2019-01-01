# Creating a dictionary

Attributes= {
 "Song":"Blood, Sweat and Tears" ,
 "Album":"Wings" ,
 "Artist":"BTS" ,
 "ReleaseYear":2016 ,
 "Lenght":3.37 ,
 "Genre":"Pop" ,
 "Lang":"Korean" ,
 "Views":383790274 ,
 "Likes":5000000 ,
 "Peak":1 ,
 "Producer":"Pdogg "
}

for key,val in Attributes.items():
	print(key,"=>",val)


def user(key,val):

  if key in Attributes:

  	if val==Attributes[key]:
  	 print ("True")

  	else:
  	 print("False") 

  else:
    print ("False")	 


key=input("Enter key: ")
value=input("Enter the key value: ")
user(key,value)
