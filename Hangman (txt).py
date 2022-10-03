import random

def missing_letter(guess):
    for index, word in enumerate(word_to_guess):
        for i, letter in enumerate(guess):
            if word_to_guess[index] == guess[i]:
                list[index] = (letter.upper())
    return ('').join(list)

language_list = ["English", "Spanish", "Russian", "Japanese", "Chinese", "Korean",
"Arabic", "French", "German", "Hokkien", "Turkish", "Yiddish", "Telugu",
"Croatian", "Hindi", "Ukrainian"]
country_list = ['United States', 'Afghanistan', 'Albania', 'Algeria',
                'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica',
                'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
                'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
                'Bosnia And Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'Brunei Darussalam',
                'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
                'Cayman Islands', 'Central African Rep', 'Chad', 'Chile', 'China', 'Christmas Island',
                'Cocos Islands', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Cote D`ivoire',
                'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica',
                'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
                'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands Malvinas', 'Faroe Islands', 'Fiji', 'Finland',
                'France', 'French Guiana', 'French Polynesia', 'French S. Territories', 'Gabon', 'Gambia', 'Georgia',
                'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam',
                'Guatemala', 'Guinea', 'Guinea-bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong',
                'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel',
                'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
                'Korea North', 'Korea South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
                'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau',
                'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
                'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montserrat', 'Morocco', 'Mozambique',
                'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles',
                'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue',
                'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan',
                'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines',
                'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania',
                'Russian Federation', 'Rwanda', 'Saint Kitts And Nevis', 'Saint Lucia', 'St Vincent/Grenadines',
                'Samoa', 'San Marino', 'Sao Tome', 'Saudi Arabia', 'Senegal', 'Seychelles',
                'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
                'South Africa', 'Spain', 'Sri Lanka', 'St. Helena', 'St.Pierre', 'Sudan', 'Suriname',
                'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan', 'Tajikistan',
                'Tanzania', 'Thailand', 'Togo', 'Tokelau', 'Tonga', 'Trinidad And Tobago', 'Tunisia',
                'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
                'United Kingdom', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City State', 'Venezuela',
                'Viet Nam', 'Virgin Islands British', 'Virgin Islands U.S.', 'Western Sahara', 'Yemen',
                'Yugoslavia', 'Zaire', 'Zambia', 'Zimbabwe'
]
#If you want to use the given word bank, uncomment out lines below

# ask = input("What Category? (Language or Country): ").lower()

# if ask == "language" or ask == "l":
#     word_to_guess = (random.choice(language_list))
# elif ask == "country" or ask == "c":
#     word_to_guess = (random.choice(country_list))
# elif ask == "quit":
#     exit()
# else: print("I don't understand!"); exit()

# Set word to guess here
word_to_guess = 'Tennessee'.lower()

Guesses = []
num_guesses = 0

list = ['_'] * len(word_to_guess.lower())

print(''.join(list))


guess = input(f'Guess Letter (or word): ').lower()
guess = guess[0] if len(guess) > 1 and guess != word_to_guess else guess

while num_guesses < 6:

    for i in (word_to_guess):

        if guess in word_to_guess and guess != word_to_guess and guess not in Guesses:
            print(f'CORRECT! "{guess.upper()}" is in the word')
            Guesses.append(guess)
            print(f'Guesses: {Guesses}')
            print(missing_letter(guess))
            break
        if guess in Guesses:
            print("You already guessed that!")
            guess = input("Guess Letter (or word): ").lower()
            guess = guess[0] if len(guess) > 1 and guess != word_to_guess else guess
        elif guess == word_to_guess:
            print(f'Winner! {word_to_guess.upper()} is correct!')
            exit()
        elif guess not in word_to_guess:
            Guesses.append(guess)
            print(f'SORRY. That letter is not in the word.')
            print(f'Guesses: {Guesses}')
            print(missing_letter(guess))
            num_guesses += 1
            if num_guesses == 1:
                print(f'''
                |-----|
                |     o         
                |    
                |
                |
                |____________
                ''')
            elif num_guesses == 2:
                print(f'''
                |-----|
                |     o         
                |     |
                |
                |
                |____________
                ''')
            elif num_guesses == 3:
                print(f'''
                |-----|
                |     o         
                |    -|
                |
                |
                |____________
                ''')
            elif num_guesses == 4:
                print(f'''
                |-----|
                |     o         
                |    -|-
                |
                |
                |____________
                ''')
            elif num_guesses == 5:
                print(f'''
                |-----|
                |     o         
                |    -|-
                |    |
                |
                |____________
                ''')
            elif num_guesses >= 6 and guess not in word_to_guess and guess != word_to_guess:
                print(f'''
                                |-----|
                                |     o         
                                |    -|-
                                |    | |
                                |
                                |____________
                                ''')
                print(f'You lose! The word was {word_to_guess.upper()}.')
                exit()
            break

    guess = input("Guess Letter (or word): ").lower()
    guess = guess[0] if len(guess) > 1 and guess != word_to_guess else guess







