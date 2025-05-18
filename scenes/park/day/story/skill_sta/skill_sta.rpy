## Increase STA ##
label lbl_park_day_path:
    ## Finding A Job
    if main_story == 20:
        pov "{i}I shouldn't spend my time going for a run.{/i}"
        pov "{i}I need to see if there's a job opening at the mall.{/i}"

        jump lbl_park_day_setup
    ## Sex World
    elif main_story == 33:
        pov "{i}Now's not the time to go for a run, I need to find answers around town.{/i}"

        jump lbl_park_day_setup

    ## Haven't Run Yet
    elif skill_sta_times == 0:
        "How many laps do you want to run?"

        menu:
            "1 Lap":
                jump lbl_skills_sta_1
            "2 Laps":
                jump lbl_skills_sta_2
            "3 Laps":
                jump lbl_skills_sta_3
            "I don't want to run.":
                jump lbl_park_day_setup
    ## Already Ran
    elif skill_sta_times == 1:
        pov "{i}I've had enough running for one day.{/i}"

        jump lbl_park_day_setup

## STAMINA
label lbl_skills_sta_1:

    scene bg skills_sta_1
    with fade
    $ renpy.pause ()
    if skill_stamax >= 11:
        scene bg skills_sta_2
        with fade
        "1 Lap wasn't long enough and didn't challenge your STA enough."
        "Your STA Max Limit stays the same."
    elif not (day == 0 or day == 1 or day == 2 or day == 3 or day == 5 or day == 6):
        scene bg skills_sta_3
        with fade
        "You collapsed from exhaustion, but you a'ight."
        if not day == 0 or day == 1 or day == 2 or day == 3 or day == 5 or day == 6:
            "Today was one of those tiring days, better luck next time."

        jump lbl_skills_sta_end
    else:
        scene bg skills_sta_2
        with fade
        "You successfully increased your STA Max Limit."
        $ skill_stamax += 1
        if skill_stamax >= 20:
            $ skill_stamax == 20

    jump lbl_skills_sta_end

label lbl_skills_sta_2:

    scene bg skills_sta_1
    with fade
    $ renpy.pause ()
    if skill_stamax >= 16:
        scene bg skills_sta_2
        with fade
        "2 Lap wasn't long enough and didn't challenge your STA enough."
        "Your STA Max Limit stays the same."
    elif not (day == 0 or day == 2 or day == 3 or day == 5):
        scene bg skills_sta_3
        with fade
        "You collapsed from exhaustion, but you a'ight."
        if not day == 0 or day == 2 or day == 3 or day == 5:
            "Today was one of those tiring days, better luck next time."

        jump lbl_skills_sta_end
    else:
        scene bg skills_sta_2
        with fade
        "You successfully increased your STA Max Limit."
        $ skill_stamax += 1
        if skill_stamax >= 20:
            $ skill_stamax == 20

    jump lbl_skills_sta_end

label lbl_skills_sta_3:

    scene bg skills_sta_1
    with fade
    $ renpy.pause ()
    if skill_stamax >= 20:
        scene bg skills_sta_2
        with fade
        "You've already reached your STA Max Limit."
    elif skill_stamax <= 15 or not (day == 0 or day == 4):
        scene bg skills_sta_3
        with fade
        "You collapsed from exhaustion, but you a'ight."
        if skill_stamax <= 15:
            "Your STA Max Limit is too low too perform at this level."
        elif not day == 0 or day == 4:
            "Today was one of those tiring days, better luck next time."
    else:
        scene bg skills_sta_2
        with fade
        "You successfully increased your STA Max Limit."
        $ skill_stamax += 1
        if skill_stamax >= 20:
            $ skill_stamax == 20

    jump lbl_skills_sta_end

label lbl_skills_sta_end:
    ## A Predicatable Realization
    if effie_path == 2 and main_story >= 22:
        $ a_predicatable_realization_jogged = 1

    $ gtime += 1
    $ skill_sta_times = 1
    $ renpy.notify("You can currently hold [skill_stamax] STA points")
    if gtime == 1:
        scene bg park_day
        with fade

        jump lbl_park_day_setup
    elif gtime == 2:
        scene bg park_night
        with fade

        jump lbl_park_night_setup
