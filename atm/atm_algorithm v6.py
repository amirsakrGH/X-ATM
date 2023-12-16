def withdraw(amount):
    two_hundred_notes = 0
    hundred_notes = 0
    fifty_notes = 0
    twenty_notes = 0
    ten_notes = 0
    total_notes = 0  
    while amount >= 10:
        if amount >= 200 and (total_notes == 0 or two_hundred_notes / total_notes < 0.6):
            amount -= 200
            two_hundred_notes += 1
            total_notes += 1
        elif amount >= 100 and (total_notes == 0 or hundred_notes / total_notes < 0.2):
            amount -= 100
            hundred_notes += 1
            total_notes += 1
        elif amount >= 50 and (total_notes == 0 or fifty_notes / total_notes < 0.2):
            amount -= 50
            fifty_notes += 1
            total_notes += 1
        elif amount >= 20 and (total_notes == 0 or twenty_notes / total_notes < 0.2):
            amount -= 20
            twenty_notes += 1
            total_notes += 1
        elif amount >= 10:
            amount -= 10
            ten_notes += 1
            total_notes += 1
    
    return total_notes

if withdraw(1544515) <= 50:
    print ('Total')
else:
    print('Cannot issue more than 50 banknotes(ya 3m lo zadt alflos adyny shoyh blyz *-*).')
