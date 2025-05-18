## Sleep Variable Changes
label lbl_mybedroom_sleep_variable_changes:
## Stay With Mom Attendance Result
    if (15 <= main_story <= 27 or main_story >= 35) and mum_path == 6:
        ## mompastsunset_attend == 1 & 5 - Missed | 2 & 3 - Refused to go
        if mompastsunset_attend == 0 and mompastsunset_went == 0:
            $ mompastsunset_attend = 5
            $ mum_path = 7

            jump lbl_mybedroom_day_setup
        elif mompastsunset_attend == 4 and mompastsunset_went == 0:
            $ mompastsunset_attend = 1
            $ mum_path = 7

            jump lbl_mybedroom_day_setup
        elif mompastsunset_attend == 2 or mompastsunset_attend == 3:
            $ mum_path = 7

            jump lbl_mybedroom_day_setup
        else:
            pass

## Incest Porno with Mom (Fail Restart)
    elif mum_path == 22.5:
        $ mum_path = 22

## Your relationship with Miss Allaway has decreased by  Ultimatum for a Beatdown Setup
    if missallaway_path == 17.5:
        $ missallaway_path = 18

## Stressed From Work
    if mumsis_path == 2:
        $ mumsis_path = 2.5
    elif mumsis_path == 7 and mowed_lawn == 1:
        $ mumsis_path = 8
    if had_under_table_trio_that_day == 1 and day == 5:
        $ had_under_table_trio_that_day = 0

## Eye to Eye POST
    if principallashley_path == 27 and not 21 <= sister_path <= 22:
        $ principallashley_path = 28
    elif principallashley_path == 12.9:
        $ principallashley_path = 13
    elif principallashley_path == 19.5:
        $ principallashley_path = 19.9
    elif principallashley_path == 20.5:
        $ principallashley_path = 20.9

## Edward VR Headset Mod
    if 3 <= edward_vr_path <= 5:
        $ edward_vr_path += 1

## Lashley Ribbon Mating Press Call
    if lashleyribbonmatingpress_call == 1:
        $ lashleyribbonmatingpress_call = 0

## Hitomi - Do You Know About Webcomics POST
    if hitomi_path == 1.1 or hitomi_path == 1.5:
        if day == 3:
            $ hitomi_path = 2
        else:
            $ hitomi_path = 1.5

## Hitomi - The Start of Something New POST
    elif 2.1 <= hitomi_path <= 2.9:
        if hitomi_path <= 2.6:
            $ hitomi_path += 0.1
        elif hitomi_path >= 2.6:
            $ hitomi_path = 3
    elif hitomi_path == 6 and day == 0:
        $ hitomi_path = 6.1
    elif hitomi_path == 6.9:
        $ hitomi_path = 7
    elif hitomi_path == 7.1:
        $ hitomi_path = 7.5
    elif hitomi_path == 11.5 and day == 6:
        $ hitomi_path = 12
    elif hitomi_path == 12.5 and day == 6:
        $ hitomi_path = 13
    elif hitomi_path == 16.9:
        $ hitomi_path = 17
    elif hitomi_path == 17.9:
        $ hitomi_path = 18

    if not effie_objectives_unlocked:#effie_path == 0 and
        $ max_phone_objectives += 1
        $ effie_objectives_unlocked = True
        if effie_path != 2 and main_story >= 15:
            $ effie_path = 2

## Violette
    if violette_path == 2.5:
        $ violette_path = 3
    elif violette_path == 3.1:
        $ violette_path = 3
    elif violette_path == 5.5:
        $ violette_path = 6
    elif violette_path == 7.9:
        $ violette_path = 8

    return
