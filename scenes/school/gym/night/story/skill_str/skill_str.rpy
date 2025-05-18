## Increase STR ##
label lbl_schoolgym_night_crowd:
    show btn_schoolgym_night_brock_idle2
    show btn_schoolgym_night_coach_idle2
    show btn_schoolgym_night_jack_idle2
    show btn_schoolgym_night_phil_idle2
    if gtime == 2:
        "Who would you like to fight?"

        menu:
            "Phil the Lightweight":
                jump lbl_skills_str_1
            "Jack the Middleweight":
                jump lbl_skills_str_2
            "Brock the Heavyweight":
                jump lbl_skills_str_3
            "I don't want to fight.":
                jump lbl_schoolgym_night_setup
    else:
        pov "{i}I'm too tired to fight. Maybe I'll come back tomorrow.{/i}"

        jump lbl_schoolgym_night_setup

## STRENGTH
label lbl_skills_str_1:

    scene bg skills_str_1
    with fade
    $ renpy.pause ()
    if skill_strmax >= 11:
        scene bg skills_str_4
        with fade
        "Phil is too weak for you and didn't challenge your STR enough."
        "Your STR Max Limit stays the same."
    elif not (day == 1 or day == 2 or day == 3 or day == 4 or day == 5) or day == 6:
        scene bg skills_str_5
        with fade
        "You got yourself knocked the hell out by a lucky punch."
        if not (day == 1 or day == 2 or day == 3 or day == 4 or day == 5 or day == 6):
            "Today was one of those sluggish days, better luck next time."

        jump lbl_skills_str_end
    else:
        scene bg skills_str_4
        with fade
        "You successfully increased your STR Max Limit."
        $ skill_strmax += 1
        if skill_strmax >= 20:
            $ skill_strmax == 20

    jump lbl_skills_str_end

label lbl_skills_str_2:

    scene bg skills_str_2
    with fade
    $ renpy.pause ()
    if skill_strmax >= 16:
        scene bg skills_str_4
        with fade
        "Jack is too weak for you and didn't challenge your STR enough."
        "Your STR Max Limit stays the same."
    elif not (day == 0 or day == 1 or day == 4 or day == 5):
        scene bg skills_str_5
        with fade
        "You got yourself knocked the hell out by a lucky punch."
        if not (day == 0 or day == 1 or day == 4 or day == 5):
            "Today was one of those sluggish days, better luck next time."

        jump lbl_skills_str_end
    else:
        scene bg skills_str_4
        with fade
        "You successfully increased your STR Max Limit."
        $ skill_strmax += 1
        if skill_strmax >= 20:
            $ skill_strmax == 20

    jump lbl_skills_str_end

label lbl_skills_str_3:

    scene bg skills_str_3
    with fade
    $ renpy.pause ()
    if skill_strmax >= 20:
        scene bg skills_str_4
        with fade
        "You've already reached your STR Max Limit."
        ## Allaway Wants a Warrior
        if missallaway_path == 12.5:
            $ townmap_enabled = 0
            $ ibecomethewarrior_beatbrock = 2
    elif skill_strmax <= 15 or not (day == 2 or day == 6):
        scene bg skills_str_5
        with fade
        "You got yourself knocked the hell out by a lucky punch."
        if skill_strmax <= 15:
            "Your STR Max Limit is too low too perform at this level."
        elif not day == 2 or day == 6:
            "Today was one of those sluggish days, better luck next time."
        ## Allaway Wants a Warrior
        if missallaway_path == 12.5:
            $ ibecomethewarrior_beatbrock = 1
    else:
        scene bg skills_str_4
        with fade
        "You successfully increased your STR Max Limit."
        $ skill_strmax += 1
        if skill_strmax >= 20:
            $ skill_strmax == 20
        ## Allaway Wants a Warrior
        if missallaway_path == 12.5:
            $ townmap_enabled = 0
            $ ibecomethewarrior_beatbrock = 2

    jump lbl_skills_str_end

label lbl_skills_str_end:
    $ gtime += 1
    $ renpy.notify("You can currently hold [skill_strmax] STR points")

    scene bg schoolgym_nightlightson
    with fade

    jump lbl_schoolgym_night_setup
