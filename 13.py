employee_details = [
        {
            "name": "Srini",
            "age": 22,
            "role": "CEO",
            "address": {
                "door_no": "114/245", 
                "street": "M.T.H Road",
                "city": "Chennai",
                "pincode": "600049" 
             }
        },
        {
            "name": "Honey",
            "age": 22,
            "role": "General Manager",
            "address": {
                "door_no": "114/245", 
                "street": "M.T.H Road",
                "city": "Chennai",
                "pincode": "600049" 
             }
        },
        {
            "name": "Balaji",
            "age": 23,
            "role": "Manager",
            "address": {
                "door_no": "143/21", 
                "street": "street",
                "city": "Chennai",
                "pincode": "372124" 
             }
        },
    ]


print("--------------------------------------------------------")
print(f'{"NAME":<20}{"AGE":<10}{"ROLE":<16}CITY')
print("--------------------------------------------------------")
for emp in employee_details:
    print(f'{emp["name"]:<20}{emp["age"]:<10}{emp["role"]:<16}{emp["address"]["city"]}\n')
