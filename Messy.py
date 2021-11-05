import pandas as pd 

sid = pd.read_csv (r'StudentInformation.csv') #pandas takes in the data and reads csv file
# print(sid) #prints the data frame


# Question 1: 
print("\nResponses Containing Facebook")
print (sid[sid["6"].str.contains("Facebook")])

print("\nResponses Containing Reddit")
print (sid[sid["6"].str.contains("Reddit")])

print("\nResposnes Containing Reddit OR Facebook")
print (sid[sid["6"].str.contains("Facebook|Reddit")])

print ("\nResponses Containing Reddit AND Facebook")
print (sid[sid["6"].str.contains("Facebook") & sid["6"].str.contains("Reddit")])

# Question 2:
print ("\nResponses Containing Twitter AND Instagram")
print (sid[sid["6"].str.contains("Twitter") & sid["6"].str.contains("Instagram")])

print ("\nResponses Containing Twitter")
print (sid[sid["6"].str.contains("Twitter")])

print("\nResponses Containing Instagram")
print (sid[sid["6"].str.contains("Instagram")])

# Question 3:
print ("\nResponses Containing Viber AND Twitter")
print (sid[sid["6"].str.contains("Viber") & sid["6"].str.contains("Twitter")])

print ("\nResponses Containing Twitter")
print (sid[sid["6"].str.contains("Twitter")])

# Question 4:
print ("\nResponses Containing Instagram")
print (sid[sid["6"].str.contains("Instagram")])

print ("\nResponses Containing Instagram AND Pinterest")
print (sid[sid["6"].str.contains("Instagram") & sid["6"].str.contains("Pinterest")])

# Question 5:
print ("\nResponses Containg Sago't Gulaman")
print (sid[sid["5"].str.contains("gulaman")]) 

print ("\nResponses Containg Yogurt Drink")
print (sid[sid["5"].str.contains("Yoggurt")])

print ("\nResponses Containing Sago't Gulaman AND Yogurt Drink")
print (sid[sid["5"].str.contains("gulaman") & sid["5"].str.contains("Yoggurt")])

print ("\nResponses Containing Sago't Gulaman OR Yogurt Drink")
print (sid[sid["5"].str.contains("gulaman|Yoggurt")])


# Question 6
print ("\nResponses Containg Mango Shake")
print (sid[sid["5"].str.contains("Mango")]) 

print ("\nResponses Containg Melon Juice")
print (sid[sid["5"].str.contains("Melon")]) 

print ("\nResponses Containing Mango Shake AND Melon Juice")
print (sid[sid["5"].str.contains("Mango") & sid["5"].str.contains("Melon")])


# Question 7
print ("\nResponses Containg Coffee")
print (sid[sid["5"].str.contains("Coffee")]) 

print ("\nResponses Containing Soft Drinks AND Coffee")
print (sid[sid["5"].str.contains("Softdrinks") & sid["5"].str.contains("Coffee")])


# Question 8 - Chocolate drink but not Buko juice

print ("\nResponses Containing Chocolate drink AND Buko Juice")
print (sid[sid["5"].str.contains("Chocolate") & sid["5"].str.contains("Buko")])

print("\nResponses Containing Chocolate drink")
print (sid[sid["5"].str.contains("Chocolate")])

print ("\nResponses Containing Buko Juice")
print (sid[sid["5"].str.contains("Buko")])

# Realized I could extra the method of df[df[column].str.contains(word looking for) and thus created main.py]