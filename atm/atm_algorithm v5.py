def withdraw(amount):
    two_hundred_notes = 0
    hundred_notes = 0
    fifty_notes = 0
    twenty_notes = 0
    ten_notes = 0

    total_notes = 0  

    while amount >= 10 and total_notes < 50:
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

    if total_notes >= 50:
        return "Cannot issue more than 50 banknotes(ya 3m lo zadt alflos adyny shoyh blyz *-*)."

    return [two_hundred_notes, hundred_notes, fifty_notes, twenty_notes, ten_notes]

print(withdraw(1230))
print(withdraw(7170))
print(withdraw(11910))

    #                             _ 
    #                         _-' "'-,       
    #                      _-' | d$$b |  
    #                   _-'    | $$$$ |    
    #                _-'       | Y$$P |  
    #             _-'|         |      |
    #          _-'  _*         |      |
    #       _-' |_-"      __--''\    /
    #    _-'         __--'     __*--'
    #  -'       __-''    __--*__-"`
    # |    _--''   __--*"__-'`  
    # |_--"  .--=`"__-||"  
    # |      |  |\\   ||
    # | .dUU |  | \\ //
    # | UUUU | _|___//
    # | UUUU |  |   
    # | UUUU |  |         [MERO]
    # | UUUU |  |
    # | UUUU |  |
    # | UUUU |  |
    # | UUP' |  |
    # |   ___^-"`
    #  ""'  

#             .-.____________________.-.
#      ___ _.' .-----.    _____________|======+----------------+
#     /_._/   (      |   /_____________|      |                |
#       /      `  _ ____/                     |   3ayz anam    |
#      |_      .\( \\                         |________________|
#     .'  `-._/__`_// 
#   .'       |""""'
#  /        /
# /        |
# |        '
# |         \
# `-._____.-