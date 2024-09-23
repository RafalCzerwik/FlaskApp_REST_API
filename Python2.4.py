# Create good script to create new list, which only contains users from Poland. Try to do it with
# List Comprehension.


users = [
    {
        'name': 'Kamil',
        'country': 'Poland',
    },
    {'name': 'John',
     'country': 'USA',
     },
    {
        'name': 'Yeti'
    },
]

polish_users = [user['name'] for user in users if user.get('country') == 'Poland']
print(polish_users)

# else

users = ''.join(map(str, polish_users))
print(f'Users from Poland: {users}')


# Display sum of first ten elements starting from element 5:

numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]

ten_elements = numbers[4:14]
result = sum(ten_elements)
print(f'Sum of first ten elements starting from 5: {result}')

# Fill list with powers of 2, n [1..20]

power_of_to_list = [2 ** n for n in range(1, 21)]
print(power_of_to_list)