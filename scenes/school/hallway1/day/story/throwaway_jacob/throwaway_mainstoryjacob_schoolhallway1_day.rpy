## Jacob Main Story Throwaway Conversations School Hallway 1 ##
default sexaroundtownjacob = 0

## Sex Around Town jacob
label lbl_schoolhallway1_day_jacob_sexworld:
    if sexaroundtownjacob == 0:
        show pov shocked_talk at left
        with dissolve
        show jac neutral at right
        with dissolve
        pov "Ummmmmmmmmm... Jacob?"
        show pov shocked at left
        show jac smirk_talk at right
        jac "Yeeeeeesss, [povname]?"
        show pov shocked_talk at left
        show jac confused at right
        pov "Why are- people all of sudden... fucking at school?"
        pov "Where are all the teachers?"
        show pov shocked at left
        show jac confused_talk at right
        jac "What? Since when was fucking so bad?"
        show pov shocked_talk at left
        show jac confused at right
        pov "At school, in public, for everyone to see?"
        show pov angry_talk at left
        show jac shocked at right
        pov "Like... always?"
        show pov angry at left
        show jac confused_talk at right
        jac "What are you on, dude? Where's this shame coming from?"
        show pov sad_talk at left
        show jac confused at right
        pov "Is today like a special day or something?"
        show pov embarrassed_talk at left
        show jac smirk at right
        pov "Like Annual Sex Day?"
        show pov confused at left
        show jac confused_talk at right
        if day == 0:
            jac "I mean... it's Monday."
        elif day == 1:
            jac "I mean... it's Tuesday."
        elif day == 2:
            jac "I mean... it's Wednesday."
        elif day == 3:
            jac "I mean... it's Thursday."
        else:
            jac "I mean... it's Friday."
        show pov bored at left
        show jac smirk_talk at right
        jac "Does that count?"
        show pov angry_talk at left
        show jac shocked at right
        pov "Where the hell is Effie? She can tell me what the fuck is going on."
        show pov angry at left
        show jac confused_talk at right
        jac "In class?"
        show pov shocked at left
        show jac smirk_talk at right
        jac "You should hurry and make your quickie sesh an extra quickie one?"
        jac "Class is officially about to start."
        show pov angry_talk at left
        show jac shocked at right
        pov "You fucking wish, Jacob."
        show pov shocked at left
        show jac embarrassed_talk at right
        jac "I have, on the way to school."
        show pov shocked at left
        show jac neutral at right
        pov "..."
        show pov angry_talk at left
        show jac shocked at right
        pov "Get out of my way, I need to speak with her."
        show pov angry at left
        show jac embarrassed_talk at right
        jac "Whoa, man. I'm a little scared of you now. You got that look in your eye."

        $ sexaroundtownjacob = 1

    else:
        show pov bored at left
        with dissolve
        show jac smirk_talk at right
        with dissolve
        jac "Thought you were gonna- hehehe- 'talk' with Effie."
        show pov bored_talk at left
        show jac smirk at right
        pov "Yeah, I am because obviously you're no help."
        show pov bored at left
        show jac smirk_talk at right
        jac "You're stalling."
        jac "You must've gotten out of the wrong side of the bed."

    jump lbl_schoolhallway1_day
