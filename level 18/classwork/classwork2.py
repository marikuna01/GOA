
password = "secret123"
guess = input("შეიყვანე პაროლი: ")

# სანამ პაროლი არ დაემთხვევა
while guess != password:
    guess = input("არასწორია, სცადე ხელახლა: ")

print("სწორია!.")


