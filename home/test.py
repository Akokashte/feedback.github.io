import pandas as pd
# static/computer_semvi_practical_summary.csv
computer_semiii_practical_summary = pd.read_csv('static/computer_semiii_practical_summary.csv')

subject_1_rating = int(eval(computer_semiii_practical_summary.iloc[8][-1]))
subject_2_rating = int(eval(computer_semiii_practical_summary.iloc[17][-1]))
subject_3_rating = int(eval(computer_semiii_practical_summary.iloc[26][-1]))
subject_4_rating = int(eval(computer_semiii_practical_summary.iloc[35][-1]))
subject_5_rating = int(eval(computer_semiii_practical_summary.iloc[44][-1]))

# The required list named as rating_list
rating_list = subject_1_rating, subject_2_rating, subject_3_rating, subject_4_rating, subject_5_rating
print(rating_list[0], rating_list[1], rating_list[2], rating_list[3], rating_list[4])