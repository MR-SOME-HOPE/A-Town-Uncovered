## Effie Side Story Throwaway Conversations Cafe Inside ##

## Sweet Talk
label lbl_cafeinside_day_effie_sweettalk:
    if skill_cha >= 3:
        if effie_points <= 9:
            $ effie_points += 1
        else:
            $ effie_points = 10
        $ skill_cha -= 3
        show pov smirk_talk at left
        with dissolve
        show effw confused at right
        call lbl_cafeinside_counter_check
        with dissolve

        pov "Hey gorgeous, I'm craving something sweet, something I can sink my teeth into."
        show effw neutral at right
        pov "How about you?"
        show pov smirk at left
        show effw smirk_talk at right
        eff "Would you like a cherry with that 'cheese' cake."
        show pov neutral_talk at left
        show effw neutral at right
        pov "Haha, I try."
        show pov neutral at left
        show effw neutral_talk at right
        eff "I would be lying if I said it didn't work a little."
        $ renpy.notify("You used 3 Charisma Points\nYour relationship with Effie has increased")
    else:
        show pov embarrassed_talk at left
        with dissolve
        show effw bored at right
        call lbl_cafeinside_counter_check
        with dissolve

        pov "Hey, you... gorgeous.. you. How is it hanging, yo?"
        show pov embarrassed at left
        show effw bored_talk at right
        eff "Uhh.. hi, [povname]. What can I get for you today?"
        show pov embarrassed_talk at left
        show effw bored at right
        pov "How about you, you.. sweet thang."
        show pov embarrassed at left
        show effw bored_talk at right
        eff "Stop. Please."
        show pov embarrassed_talk at left
        show effw bored at right
        pov "Suree thaang."
        $ renpy.notify("You need 3 Charisma Points")

    jump lbl_cafeinside_day

## Fun Later
label lbl_cafeinside_day_effie_funlater:
    default effie_funlater = 0
    if effie_points == 0 or main_story <= 13:
        show pov smirk_talk at left
        with dissolve
        show effw neutral at right
        call lbl_cafeinside_counter_check
        with dissolve

        pov "I was wondering if you wanted to have some more fun tonight."
        show pov embarrassed at left
        show effw bored_talk at right
        eff "Um.. actually. I'm kind of busy with my coursework. Maybe another time?"
        show pov embarrassed_talk at left
        show effw neutral at right
        pov "Oh, right. For sure."
    else:
        show pov smirk_talk at left
        with dissolve
        show effw smirk at right
        call lbl_cafeinside_counter_check
        with dissolve

        pov "I was wondering if you wanted to have some more fun tonight."
        show pov smirk at left
        show effw neutral_talk at right
        eff "Oooh, sounds great. Meet me outside my house just after the sun sets."
        show pov smirk_talk at left
        show effw smirk at right
        pov "Awesome, I'll see you then."
        $ effie_funlater = 1
        $ effie_path = 1
        $ renpy.notify("New Objective: Meet Effie Outside her House at Night")

    jump lbl_cafeinside_day
