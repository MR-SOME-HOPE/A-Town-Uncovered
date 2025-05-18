label lbl_next_date:
    $ date += 1
    if (month == 0 or month == 2 or month == 4 or month == 6 or month == 7 or month == 9 or month == 11) and date == 31:
        $ month += 1
        $ date = 0
        if month == 12:
            $ month = 0
            $ day = 6
    elif (month == 3 or month == 5 or month == 8 or month == 10) and date == 30:
        $ month += 1
        $ date = 0
    elif month == 1 and date == 28:
        $ month += 1
        $ date = 0
