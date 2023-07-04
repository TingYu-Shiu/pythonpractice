my_passwd = 'isaac'
assert len(my_passwd) >10, 'password is too short'
# assert 沒達成條件，產生error

'''
my_passwd = 'isaac'
if len(my_passwd) < 10:
    raise Exception('password is too short')
# raise exception 達成條件，產生error
'''