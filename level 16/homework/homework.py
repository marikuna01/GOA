# for i in range(1, 21):  # range(1, 21) ნიშნავს 1-დან 20-მდე (21 არ შედის)
   # print(i)

   # for i in range(1, 21, 2): 
   # print(i)

# for ციკლი გამოიყენება იმ შემთხვევაში, როცა ვიცით, რამდენჯერ უნდა შესრულდეს ციკლი.
# მაგ: ვიგებ რაოდენობას ან დიაპაზონს წინასწარ (range, სია და სხვ.)

# while ციკლი კი იმ შემთხვევაში გამოიყენება, როცა ზუსტად არ ვიცით რამდენჯერ უნდა იმეორდეს,
# და ციკლი გაგრძელდება მანამ, სანამ გარკვეული პირობა მართალია (True)

# "Forever loop" ნიშნავს უსასრულო ციკლს, რომელიც არ ჩერდება, სანამ პროგრამა არ შევაჩერებთ ხელით
# ან ციკლში არ ჩავდებთ პირობას რომელიც ცვლიანს შეცვლის და ციკლს გააჩერებს. 

# მაგალითად, ეს არის უსასრულო ციკლი:
#while True:
   # print("ეს ციკლი არასდროს გაჩერდება, თუ არ დავამატებთ break-ს ან არ გავაჩერებთ პროგრამას")

  #  counter = 15
 # while counter <= 20:
   # print(counter)
   # counter += 1  # ყოველ ციკლში counter იზრდება 1-ით







   for i in range(1,20):
    print(i)

for i in range(1,20,2):
    print(i)

# For ციკლს ვიყენებთ, როდესაც ვიცით კოდი რამდენჯერ გვინდა გავუშვათ, ხოლო while ციკლს ვიყენებთ,
# როდესაც არ ვიცით

random_number = int(input('please enter a number: 1-20'))

while random_number == 30:
    random_number = random_number + 1

number = 15
for i in range(15):
    number = number + 1
number = input('ss')

while 2 > 1: #can use Ctrl + c to stop terminal
    print(1)

counter = 15
while counter <= 20:
    print(counter)
    counter = counter + 1