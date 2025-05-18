## My Bedroom Calander Day ##
label lbl_mybedroom_calander:

## Test Months
    #$ date = 3
    #$ month += 1
    #if month == 12:
    #    $ month = 0
    #else:
    #    pass
    #"month = [month]"
    #"date = [date]"
    if gtime <= 1:
        scene bg mybedroom_calander_day
        with fade
    else:
        scene bg mybedroom_calander_night
        with fade
    call screen scr_mybedroom_calander

label lbl_mybedroom_calander_exit:
    if gtime <= 1:
        scene bg mybedroom_day
        with fade

        jump lbl_mybedroom_day_setup
    else:
        scene bg mybedroom_night
        with fade

        jump lbl_mybedroom_night_setup

screen scr_mybedroom_calander():
    if gtime <= 1:
        add "bg mybedroom_calander_day"
        imagebutton auto "btn calander_day_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_calander_exit")
    else:
        add "bg mybedroom_calander_night"
        imagebutton auto "btn calander_night_exit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybedroom_calander_exit")
    use hud_overlay

    ## Days of the Week Label
    hbox xpos 230 ypos 152 spacing 20:
        text "Mon" color "2a2d2f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    hbox xpos 440 ypos 152 spacing 20:
        text "Tue" color "2a2d2f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    hbox xpos 660 ypos 152 spacing 20:
        text "Wed" color "2a2d2f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    hbox xpos 880 ypos 152 spacing 20:
        text "Thur" color "2a2d2f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    hbox xpos 1100 ypos 152 spacing 20:
        text "Fri" color "2a2d2f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    hbox xpos 1320 ypos 152 spacing 20:
        text "Sat" color "2a2d2f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    hbox xpos 1540 ypos 152 spacing 20:
        text "Sun" color "2a2d2f" size 60 font "fonts/KGSorryNotSorryChub.ttf"
    if month == 0:
        use calander_january_dates
    elif month == 1:
        use calander_february_dates
    elif month == 2:
        use calander_march_dates
    elif month == 3:
        use calander_april_dates
    elif month == 4:
        use calander_may_dates
    elif month == 5:
        use calander_june_dates
    elif month == 6:
        use calander_july_dates
    elif month == 7:
        use calander_august_dates
    elif month == 8:
        use calander_september_dates
    elif month == 9:
        use calander_october_dates
    elif month == 10:
        use calander_november_dates
    elif month == 11:
        use calander_december_dates

    ## Monday Start (January, April, July)
    if month == 0 or month == 3 or month == 6:
        if date == 0:
            use calander_day_0
        elif date == 1:
            use calander_day_1
        elif date == 2:
            use calander_day_2
        elif date == 3:
            use calander_day_3
        elif date == 4:
            use calander_day_4
        elif date == 5:
            use calander_day_5
        elif date == 6:
            use calander_day_6
        if date >= 7:
            use calander_fullweek
            if date == 7:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_0
            elif date == 8:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_1
            elif date == 9:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_2
            elif date == 10:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_3
            elif date == 11:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_4
            elif date == 12:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_5
            elif date == 13:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_6
            if date >= 14:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_fullweek
                if date == 14:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_0
                elif date == 15:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_1
                elif date == 16:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_2
                elif date == 17:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_3
                elif date == 18:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_4
                elif date == 19:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_5
                elif date == 20:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_6
                if date >= 21:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_fullweek
                    if date == 21:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 22:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 23:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_2
                    elif date == 24:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_3
                    elif date == 25:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_4
                    elif date == 26:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_5
                    elif date == 27:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_6
                    if date >= 28:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_fullweek
                        if date == 29:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_0
                        elif date == 29:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_1
                        elif date == 30 and month == 0 or month == 6:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_2

    ## Tuesday Start (October)
    if month == 9:
        if date == 0:
            hbox xpos 215 ypos 0 spacing -80:
                use calander_day_0
        elif date == 1:
            hbox xpos 215 ypos 0 spacing -80:
                use calander_day_1
        elif date == 2:
            hbox xpos 215 ypos 0 spacing -80:
                use calander_day_2
        elif date == 3:
            hbox xpos 215 ypos 0 spacing -80:
                use calander_day_3
        elif date == 4:
            hbox xpos 215 ypos 0 spacing -80:
                use calander_day_4
        elif date == 5:
            hbox xpos 215 ypos 0 spacing -80:
                use calander_day_5
        if date >= 6:
            hbox xpos 215 ypos 0 spacing -80:
                use calander_day_6start
            if date == 6:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_0
            elif date == 7:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_1
            elif date == 8:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_2
            elif date == 9:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_3
            elif date == 10:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_4
            elif date == 11:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_5
            elif date == 12:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_6
            if date >= 13:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_fullweek
                if date == 13:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_0
                elif date == 14:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_1
                elif date == 15:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_2
                elif date == 16:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_3
                elif date == 17:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_4
                elif date == 18:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_5
                elif date == 19:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_6
                if date >= 20:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_fullweek
                    if date == 20:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_0
                    elif date == 21:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 22:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_2
                    elif date == 23:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_3
                    elif date == 24:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_4
                    elif date == 25:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_5
                    elif date == 26:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_6
                    if date >= 27:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_fullweek
                        if date == 27:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_0
                        elif date == 28:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_1
                        elif date == 29:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_2
                        elif date == 30:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_3

    ## Wednesday Start (May)
    if month == 4:
        if date == 0:
            hbox xpos 430 ypos 0 spacing -80:
                use calander_day_0
        elif date == 1:
            hbox xpos 430 ypos 0 spacing -80:
                use calander_day_1
        elif date == 2:
            hbox xpos 430 ypos 0 spacing -80:
                use calander_day_2
        elif date == 3:
            hbox xpos 430 ypos 0 spacing -80:
                use calander_day_3
        elif date == 4:
            hbox xpos 430 ypos 0 spacing -80:
                use calander_day_4
        if date >= 5:
            hbox xpos 430 ypos 0 spacing -80:
                use calander_day_5start
            if date == 5:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_0
            elif date == 6:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_1
            elif date == 7:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_2
            elif date == 8:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_3
            elif date == 9:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_4
            elif date == 10:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_5
            elif date == 11:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_6
            if date >= 12:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_fullweek
                if date == 12:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_0
                elif date == 13:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_1
                elif date == 14:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_2
                elif date == 15:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_3
                elif date == 16:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_4
                elif date == 17:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_5
                elif date == 18:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_6
                if date >= 19:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_fullweek
                    if date == 19:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_0
                    elif date == 20:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 21:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_2
                    elif date == 22:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_3
                    elif date == 23:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_4
                    elif date == 24:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_5
                    elif date == 25:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_6
                    if date >= 26:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_fullweek
                        if date == 26:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_0
                        elif date == 27:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_1
                        elif date == 28:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_2
                        elif date == 29:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_3
                        elif date == 30:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_4

    ## Thursday Start (February, August)
    if month == 1 or month == 7:
        if date == 0:
            hbox xpos 645 ypos 0 spacing -80:
                use calander_day_0
        elif date == 1:
            hbox xpos 645 ypos 0 spacing -80:
                use calander_day_1
        elif date == 2:
            hbox xpos 645 ypos 0 spacing -80:
                use calander_day_2
        elif date == 3:
            hbox xpos 645 ypos 0 spacing -80:
                use calander_day_3
        if date >= 4:
            hbox xpos 645 ypos 0 spacing -80:
                use calander_day_4start
            if date == 4:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_0
            elif date == 5:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_1
            elif date == 6:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_2
            elif date == 7:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_3
            elif date == 8:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_4
            elif date == 9:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_5
            elif date == 10:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_6
            if date >= 11:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_fullweek
                if date == 11:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_0
                elif date == 12:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_1
                elif date == 13:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_2
                elif date == 14:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_3
                elif date == 15:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_4
                elif date == 16:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_5
                elif date == 17:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_6
                if date >= 18:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_fullweek
                    if date == 18:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_0
                    elif date == 19:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 20:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_2
                    elif date == 21:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_3
                    elif date == 22:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_4
                    elif date == 23:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_5
                    elif date == 24:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_6
                    if date >= 25:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_fullweek
                        if date == 25:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_0
                        elif date == 26:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_1
                        elif date == 27:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_2
                        elif date == 28 and month == 7:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_3
                        elif date == 29 and month == 7:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_4
                        elif date == 30 and month == 7:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_5

    ## Friday Start (March, November)
    if month == 2 or month == 10:
        if date == 0:
            hbox xpos 860 ypos 0 spacing -80:
                use calander_day_0
        elif date == 1:
            hbox xpos 860 ypos 0 spacing -80:
                use calander_day_1
        elif date == 2:
            hbox xpos 860 ypos 0 spacing -80:
                use calander_day_2
        if date >= 3:
            hbox xpos 860 ypos 0 spacing -80:
                use calander_day_3start
            if date == 3:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_0
            elif date == 4:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_1
            elif date == 5:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_2
            elif date == 6:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_3
            elif date == 7:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_4
            elif date == 8:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_5
            elif date == 9:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_6
            if date >= 10:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_fullweek
                if date == 10:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_0
                elif date == 11:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_1
                elif date == 12:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_2
                elif date == 13:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_3
                elif date == 14:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_4
                elif date == 15:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_5
                elif date == 16:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_6
                if date >= 17:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_fullweek
                    if date == 17:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_0
                    elif date == 18:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 19:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_2
                    elif date == 20:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_3
                    elif date == 21:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_4
                    elif date == 22:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_5
                    elif date == 23:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_6
                    if date >= 24:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_fullweek
                        if date == 24:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_0
                        elif date == 25:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_1
                        elif date == 26:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_2
                        elif date == 27:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_3
                        elif date == 28:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_4
                        elif date == 29:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_5
                        elif date == 30 and month == 2:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_6

    ## Saturday Start (June)
    if month == 5:
        if date == 0:
            hbox xpos 1075 ypos 0 spacing -80:
                use calander_day_0
        elif date == 1:
            hbox xpos 1075 ypos 0 spacing -80:
                use calander_day_1
        if date >= 2:
            hbox xpos 1075 ypos 0 spacing -80:
                use calander_day_2start
            if date == 2:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_0
            elif date == 3:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_1
            elif date == 4:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_2
            elif date == 5:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_3
            elif date == 6:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_4
            elif date == 7:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_5
            elif date == 8:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_6
            if date >= 9:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_fullweek
                if date == 9:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_0
                elif date == 10:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_1
                elif date == 11:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_2
                elif date == 12:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_3
                elif date == 13:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_4
                elif date == 14:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_5
                elif date == 15:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_6
                if date >= 16:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_fullweek
                    if date == 16:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_0
                    elif date == 17:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 18:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_2
                    elif date == 19:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_3
                    elif date == 20:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_4
                    elif date == 21:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_5
                    elif date == 22:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_6
                    if date >= 23:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_fullweek
                        if date == 23:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_0
                        elif date == 24:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_1
                        elif date == 25:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_2
                        elif date == 26:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_3
                        elif date == 27:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_4
                        elif date == 28:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_5
                        elif date == 29:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_6

    ## Sunday Start (September, December)
    if month == 8 or month == 11:
        if date == 0:
            hbox xpos 1290 ypos 0 spacing -80:
                use calander_day_0
        if date >= 1:
            hbox xpos 1290 ypos 0 spacing -80:
                use calander_day_1start
            if date == 1:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_0
            elif date == 2:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_1
            elif date == 3:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_2
            elif date == 4:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_3
            elif date == 5:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_4
            elif date == 6:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_5
            elif date == 7:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_day_6
            if date >= 8:
                hbox xpos 0 ypos 165 spacing -80:
                    use calander_fullweek
                if date == 8:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_0
                elif date == 9:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_1
                elif date == 10:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_2
                elif date == 11:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_3
                elif date == 12:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_4
                elif date == 13:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_5
                elif date == 14:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_day_6
                if date >= 15:
                    hbox xpos 0 ypos 330 spacing -80:
                        use calander_fullweek
                    if date == 15:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_0
                    elif date == 16:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_1
                    elif date == 17:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_2
                    elif date == 18:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_3
                    elif date == 19:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_4
                    elif date == 20:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_5
                    elif date == 21:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_day_6
                    if date >= 22:
                        hbox xpos 0 ypos 495 spacing -80:
                            use calander_fullweek
                        if date == 22:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_0
                        elif date == 23:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_1
                        elif date == 24:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_2
                        elif date == 25:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_3
                        elif date == 26:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_4
                        elif date == 27:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_5
                        elif date == 28:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_day_6
                        if date >= 29:
                            hbox xpos 0 ypos 660 spacing -80:
                                use calander_fullweek
                            if date == 29:
                                use calander_day_0
                            if date == 30 and month == 11:
                                use calander_day_1