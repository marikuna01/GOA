# ==  ტოლობა
# !=  არათანაბრობა
# >   მეტობა
# <   ნაკლებობა
# >=  მეტია ან ტოლია
# <=  ნაკლებია ან ტოლია



# and  - და (ორივე პირობა უნდა იყოს ჭეშმარიტი)
# or   - ან (ერთი მაინც უნდა იყოს ჭეშმარიტი)
# not  - არა (აბრუნებს პირობის საწინააღმდეგოს)


a = 10
b = 5
c = 7

# შევადაროთ და გამოვიყენოთ ლოგიკური ოპერატორები
if (a > b and b < c) or not (a == 10):
    print("პირობა შესრულდა")
else:
    print("პირობა არ შესრულდა")




    
   # True and                 # True
   # not False and            # True and True => True
   # (False or True) and      # True
   # True or                  # True
   #  not False and            # True
   # False and                # False
   # not True and             # False
   # (True or False) or       # True
   # (True and False)         # False