total_people = int(input(f'Total People?'))
blank_votes = int(input(f'Blank votes?'))
null_votes = int(input(f'Null votes?'))
valid_votes = int(input(f'Valid votes?'))

formula = valid_votes
blank_votes_percentage = (blank_votes*100)/total_people
nulll_votes_percentage = (null_votes*100)/total_people
valid_votes_percentage = (valid_votes*100)/total_people

print(f'''
==============================
Total {total_people}
Valid Votes percentage: {valid_votes_percentage}%.
Null Votes percentage: {nulll_votes_percentage}%.
Blank Votes percentage: {blank_votes_percentage}%.
===============================
''')

