import random
def randQsn():
    questions=['WHAT DO YOU DO?','ARE YOU MARRIED?','WHY ARE YOU STUDYING ENGLISH?','HOW DID YOU LEARN ENGLISH?','WHAT DO YOU DO IN YOUR FREE TIME?',
               'WHAT/’S THE WEATHER LIKE?','when you will be happy','HOW ARE YOU FEELING?', 'HOW WAS YOUR DAY?']
    rand_item=random.choice(questions)
    print(rand_item)
