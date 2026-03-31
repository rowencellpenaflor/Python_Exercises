"""
Stream donations
Write a function, donate(), that lets an online viewer send a donation to a streamer.
"""

def donate(amount=5, name='Anonymous', msg='',):
    print(f'{name} donated {amount} credits: {msg}')
    
donate(10, msg='gg')