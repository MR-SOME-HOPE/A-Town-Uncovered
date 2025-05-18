## Increase INT ##
label lbl_classroom_day_desk:
    #if missallaway_path not in (4, 18, 19, 21) or (17 <= missallaway_path <= 18 and day < 4):#17,17.5
    if insexworld == 0:
        scene bg classroom_day
        if gtime == 1:# and luna_path >= 1
            show btn_classroom_day_luna_idle2
        elif gtime == 0:
            show btn_classroom_day_effie_idle2
    elif insexworld == 1:
        scene bg classroom_daysexworld
        show btn_classroom_day_missallaway_idle2
        if gtime == 0:
            show btn_classroom_daysexworld_effie_idle2
            $ renpy.pause(0.001)


    if IsAllawayInClass():
        show btn_classroom_day_missallaway_idle2
    #elif ( missallaway_path in (4,19) or (17 <= missallaway_path <= 18 and day < 4) ) and insexworld == 0:
    elif not IsAllawayInClass():

        pov "{i}Can't take class if the teacher's not here.{/i}"

        jump lbl_classroom_day_setup


    ## First Day of School
    if main_story == 8:
        pov "{i}I just had class, I don't want to study again.{/i}"

        jump lbl_classroom_day_setup

    ## Find a Job
    elif main_story == 20:
        pov "{i}As much as a good boy I want to be, I should find myself a job.{/i}"
        pov "{i}I'll look at the mall.{/i}"

        jump lbl_classroom_day_setup

    ## End of Year Ass Signment
    elif main_story == 32:
        scene bg chalkboard_day
        with fade

        jump lbl_end_of_year_ass_signment

    ## Look for Answers around Town
    elif main_story == 33:
        pov "{i}Now's not the time to study, I need to find answers around town.{/i}"

        jump lbl_classroom_day_setup


    ## Framed
    elif principallashley_path == 5:
        pov "{i}I have to head to Director Lashley's office.{/i}"
        jump lbl_classroom_day_setup

    ## Skill INT
    elif skill_int_times == 0:
        "How would you like to study?"

        menu:
            "Casual Study":
                jump lbl_skills_int_1
            "Normal Study":
                jump lbl_skills_int_2
            "Intense Study":
                jump lbl_skills_int_3
            "I don't want to study.":
                jump lbl_classroom_day_setup
    elif skill_int_times == 1:
        pov "{i}I've had enough studying for one day.{/i}"

        jump lbl_classroom_day_setup

## INTELLIGENCE
label lbl_skills_int_1:

    scene bg skills_int_1
    with fade
    $ renpy.pause ()
    if skill_intmax >= 11:
        scene bg skills_int_4
        with fade
        "The work is too easy for you and didn't challenge your INT enough."
        "Your INT Max Limit stays the same."
    elif not (day == 1 or day == 2 or day == 3 or day == 4):
        scene bg skills_int_5
        with fade
        "You fell asleep doodling doodles and boobles."
        if not day == 1 or day == 2 or day == 3 or day == 4:
            "Today was one of those long days, better luck next time."

        jump lbl_skills_int_end
    else:
        scene bg skills_int_4
        with fade
        "You successfully increased your INT Max Limit."
        $ skill_intmax += 1
        if skill_intmax >= 20:
            $ skill_intmax == 20

    jump lbl_skills_int_end

label lbl_skills_int_2:

    scene bg skills_int_2
    with fade
    $ renpy.pause ()
    if skill_intmax >= 16:
        scene bg skills_int_4
        with fade
        "The work is too easy for you and didn't challenge your INT enough."
        "Your INT Max Limit stays the same."
    elif skill_intmax <= 10 or not (day == 2 or day == 3):
        scene bg skills_int_5
        with fade
        "You fell asleep listening to the teacher."
        if skill_intmax <= 10:
            "Your INT Max Limit is too low too perform at this level."
        elif not day == 2 or day == 3:
            "Today was one of those long days, better luck next time."
    else:
        scene bg skills_int_4
        with fade
        "You successfully increased your INT Max Limit."
        $ skill_intmax += 1
        if skill_intmax >= 20:
            $ skill_intmax == 20

    jump lbl_skills_int_end

label lbl_skills_int_3:

    scene bg skills_int_3
    with fade
    $ renpy.pause ()
    if skill_intmax >= 20:
        scene bg skills_int_4
        with fade
        "You've already reached your INT Max Limit."
    elif skill_intmax <= 15 or not day == 3:
        scene bg skills_int_5
        with fade
        "You burnt yourself out from overworking."
        if skill_intmax <= 15:
            "Your INT Max Limit is too low too perform at this level."
        elif not day == 3:
            "Today was one of those long days, better luck next time."
    else:
        scene bg skills_int_4
        with fade
        "You successfully increased your INT Max Limit."
        $ skill_intmax += 1
        if skill_intmax >= 20:
            $ skill_intmax == 20

    jump lbl_skills_int_end

label lbl_skills_int_end:
    $ gtime += 1
    $ skill_int_times = 1
    $ renpy.notify("You can currently hold [skill_intmax] INT points")
    if missallaway_path == 16 and skill_intmax >= 19:
        $ missallaway_path = 16.5
    if gtime == 1:
        scene bg classroom_day
        with fade

        jump lbl_classroom_day_setup
    elif gtime == 2:
        scene bg schoolyard_night
        with fade

        jump lbl_schoolyard_night_setup
