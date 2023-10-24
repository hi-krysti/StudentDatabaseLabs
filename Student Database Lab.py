name = ['Lola Lopez', 'Muhammad Fadel', 'Otto Becker', 'Yuki Sato']
hometown = ['Mexico City', 'Chicago', 'Munich', 'Kyoto']
fav_food = ['pizza', 'shrimp tacos', 'spaghetti', 'mashed potatoes']

request_again_flag = True
while request_again_flag:

    # print('Here are the students in this class:')
    # for student in name:
    #     print(student)

    index = int(input('Welcome! Which student would you like to learn more about? Enter a number 1-4:\n> '))

    if 0 < index <= len(name):
        student = name[index - 1]
        print(f'Student {index} is {student}. What would you like to know about {student}?')

        while True:
            choice = input('Enter "hometown" or "favorite food". \n> ').lower()

            if choice == 'hometown':
                town = hometown[index - 1]
                print(f'{student} is from {town}.')
                break

            elif choice == 'favorite food':
                food = fav_food[index - 1]
                print(f"{student}'s favorite food is {food}.")
                break

            else:
                print('I am sorry, that entry is invalid. Please try again.')

        while True:
            cont = input('Would you like to learn about another student? Enter "y" or "n". \n> ').lower()
            if cont == 'y':
                break
            if cont == 'n':
                print('OK, goodbye!')
                request_again_flag = False
                break
            else:
                print('I am sorry, that entry is invalid. Please try again.')

    else:
        print('I am sorry, that entry is invalid. Please try again.')