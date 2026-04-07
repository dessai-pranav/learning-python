import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#
data = pd.read_csv("nato_phonetic_alphabet.csv")
dicti = {row.letter:row.code for (index, row) in data.iterrows()}
print(dicti)
def generate_phonetic():
    user = input("Enter your name: ").upper()
    try:
        new_list =[dicti[letter] for letter in user]
    except KeyError:
        print("sorry only letters in the alphabet please")
        generate_phonetic()
    else:
        print(new_list)
generate_phonetic()


