import pandas as pd #if only i had epistemic access to the wolfram language 

df = pd.read_csv (r'StudentInformation.csv') #pandas creates dataframe from the csv file

def filter(a, b, c):
    print (df[df[a].str.contains(b)]) # Event A 
    print (df[df[a].str.contains(c)]) # Event B
    # print (df[df[a].str.contains(b) & df[a].str.contains(c)]) #Event A and B

#Problem 1 - uses Facebook or Reddit 
filter("6", "Facebook", "Reddit")

#Problem 2 - uses Facebook and Instagram
filter("6", "Twitter", "Instagram")
print (df[df["6"].str.contains("Twitter|Instagram")])

#Problem 3 - uses viber given that he/she uses twitter
filter("6", "Viber", "Twitter")


#Problem 4 - uses Instagram but not Pinterest
filter("6", "Instagram", "Pinterest")

#Problem 5 - drinks sagot gulaman or yogurt drink 
filter("5", "gulaman", "Yoggurt")

#Problem 6 - drinks Mango shake and Melon juice [5] "Mango" || "Melon"
filter("5", "Mango", "Melon")
print (df[df["5"].str.contains("Mango|Melon")]) 

#Problem 7 - drinks Soft Drinks given that he/she drinks Coffee [5] "Coffee" || "Softdrinks"
filter("5", "Coffee", "Softdrinks")

#Problem 8 - drinks Chocolate drink but not Buko juice [5] "Chocolate" || "Buko"
filter("5", "Chocolate", "Buko")


#Problem 9 - goes to school By foot (walking) or Jeepney  [7] "walking" || "Jeepney"
filter("7", "walking", "Jeepney")

#Problem 10 - goes to school by Private Car/Vehicle and Grab [7] "Car/Vehicle"  || "Grab"
filter("7", "Car/Vehicle", "Grab")
print (df[df["7"].str.contains("Car/Vehicle|Grab")]) 