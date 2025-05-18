## Increase CHA ##
label lbl_nightclub_night_dancefloor:
    show btn nightclubdancefloor_night_zariah_idle
    if gtime == 2:
        "How would you like to dance?"

        menu:
            "Casual Dancing":
                jump lbl_skills_cha_1
            "Dirty Dancing":
                jump lbl_skills_cha_2
            "Solo Stand Out":
                jump lbl_skills_cha_3
            "I don't want to dance.":
                jump lbl_nightclubdancefloor_night_setup
    else:
        pov "{i}I'm too tired to dance. Maybe I'll come back tomorrow.{/i}"

        jump lbl_nightclub_night_setup

## CHARISMA
label lbl_skills_cha_1:

    scene bg skills_cha_1
    with fade
    $ renpy.pause ()
    if skill_chamax >= 11:
        scene bg skills_cha_4
        with fade
        "The crowd was full of drunks and didn't challenge your CHA enough."
        "Your CHA Max Limit stays the same."
    elif not (day == 0 or day == 2 or day == 3 or day == 4 or day == 5 or day == 6):
        scene bg skills_cha_5
        with fade
        "You were basically invisible the whole night."
        if not day == 0 or day == 2 or day == 3 or day == 4 or day == 5 or day == 6:
            "Today was one of those bad nights, better luck next time."
    else:
        scene bg skills_cha_4
        with fade
        "You successfully increased your CHA Max Limit."
        $ skill_chamax += 1
        if skill_chamax >= 20:
            $ skill_chamax == 20

    jump lbl_skills_cha_end

label lbl_skills_cha_2:

    scene bg skills_cha_2
    with fade
    $ renpy.pause ()
    if skill_chamax >= 16:
        scene bg skills_cha_4
        with fade
        "The crowd was full of drunks and didn't challenge your CHA enough."
        "Your CHA Max Limit stays the same."
    elif skill_chamax <= 10 or not (day == 0 or day == 3 or day == 4 or day == 6):
        scene bg skills_cha_5
        with fade
        "The girl thought you were a creep and ditched you."
        if skill_chamax <= 10:
            "Your CHA Max Limit is too low too perform at this level."
        elif not day == 0 or day == 3 or day == 4 or day == 6:
            "Today was one of those bad nights, better luck next time."
    else:
        scene bg skills_cha_4
        with fade
        "You successfully increased your CHA Max Limit."
        $ skill_chamax += 1
        if skill_chamax >= 20:
            $ skill_chamax == 20

    jump lbl_skills_cha_end

label lbl_skills_cha_3:

    scene bg skills_cha_3
    with fade
    $ renpy.pause ()
    if skill_chamax >= 20:
        scene bg skills_cha_4
        with fade
        "You've already reached your CHA Max Limit."
    elif skill_chamax <= 15 or not (day == 1 or day == 4):
        scene bg skills_cha_5
        with fade
        "The whole club just stared at you awkwardly."
        if skill_chamax <= 15:
            "Your CHA Max Limit is too low too perform at this level."
        elif not day == 1 or day == 4:
            "Today was one of those bad nights, better luck next time."
    else:
        scene bg skills_cha_4
        with fade
        "You successfully increased your CHA Max Limit."
        $ skill_chamax += 1
        if skill_chamax >= 20:
            $ skill_chamax == 20

    jump lbl_skills_cha_end

label lbl_skills_cha_end:
    $ gtime += 1
    $ renpy.notify("You can currently hold [skill_chamax] CHA points")

    scene bg nightclubdancefloor_night
    with fade

    jump lbl_nightclubdancefloor_night_setup
