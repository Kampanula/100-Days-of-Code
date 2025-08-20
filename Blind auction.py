participant = {}

other_person = True
biggest_value = 0
biggest_value_name = ""
while other_person:
    name = input("Type your name").lower()
    bid = int(input("Type your bid"))
    another_bid = input("There are other user who want to bid?").lower()
    print("\n" * 5)
    if another_bid == "no":
        other_person = False
    participant[name] = bid

for k, v in participant.items():
    if v > biggest_value:
        biggest_value = v
        biggest_value_name = k

print(biggest_value_name,biggest_value )
