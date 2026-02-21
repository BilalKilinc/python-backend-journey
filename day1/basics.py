#değerlerin birbirleri ile yer değiştirmesi

a = 3 
b = 4 
a,b=b,a

print(a,b)
###############
i=1
i += 1 # i= i + 1
print(i)
###############

a = "python programming language"

print(a[2:20:2])  #2. indexten 20. indexe kadar 2'şer atlayarak yazdırır

#a[0] = "P" stringler değiştirilemez, bu yüzden hata verir

print(1,2,3,4,5,6,7,8,9,sep="---") #sep parametresi ile araya istediğimiz karakteri koyabiliriz

#FORMATLAMA
name = "Ali"
age = 25
print("My name is {} and I am {} years old.".format(name, age)) #format fonksiyonu ile değişkenleri sırasıyla yerleştirebiliriz
print(f"My name is {name} and I am {age} years old.") #f-string ile daha kolay bir şekilde değişkenleri yerleştirebiliriz
a = 10
b = 20 
print("the sum of {:.2f} and {:.2f} is {:.2f}".format(a,b,a+b)) #format fonksiyonu ile sayıları 2 ondalık basamağa yuvarlayarak yazdırabiliriz


x = int(input("bir sayı giriniz ")) #int olarak belirtilmeden yazılırsa string olarak kabul edilir
print("girilen sayı=",x)