## MC x Sister Eating Effie Pre 2
label lbl_mcxsister_eating_effie_pre2:
    if mcxsistereatingeffie_firsttimedone == 0:
        scene bg effiehouseoutside_day
        with fade
        "{i}*Knock knock knock*{/i}"
        show pov neutral at left
        show sis neutral flip at Position(xpos=600)
        show eff neutral_talk at right
        with dissolve
        eff "Guys, what brings you around at this time on a weekend?"
        show sis neutral_talk flip at Position(xpos=600)
        show eff embarrassed at right
        sis "We actually came over to thank you for giving me a place to stay when I was at lowest."
        show sis neutral flip at Position(xpos=600)
        show eff smirk_talk at right
        eff "Awww, girl. You don't need to. You know I love you and you're always welcome to stay here."
        show pov neutral_talk at left
        show sis neutral flip at Position(xpos=600)
        show eff confused at right
        pov "Can we come in, we actually have a small, little thing to give you."
        show pov neutral at left
        show sis neutral flip at Position(xpos=600)
        show eff confused_talk at right
        eff "Oh really? Sure... my dad hasn't come home yet but it's like this some nights. Usually on the weekends."
        show pov neutral at left
        show sis smirk flip at Position(xpos=600)
        show eff neutral at right
        pov "Let's head to your room if that's cool."
        show pov neutral at left
        show eff neutral_talk at right
        eff "Step this way~"

        ## BEDROOM
        scene bg effieroom_day
        with fade
        show pov neutral at left
        show sis neutral flip at Position(xpos=600)
        show eff confused_talk at right
        with dissolve
        eff "So- what's this 'small, little thing'?"
        show sis neutral_talk flip at Position(xpos=600)
        show eff shocked at right
        sis "Take off your shorts and we'll show you."
        show sis neutral flip at Position(xpos=600)
        show eff shocked_talk at right
        eff "Excuse me?"
        show pov smirk at left
        show sis smirk_talk flip at Position(xpos=600)
        show eff shocked at right
        sis "Here, [povname]. Help me with her."
        hide sis
        hide eff
        show pov smirk at left
        eff "Hey!"

        jump lbl_mcxsister_eating_effie

    else:
        scene bg effiehouseoutside_day
        with fade
        "{i}*Knock knock knock*{/i}"
        show pov neutral at left
        show sis neutral flip at Position(xpos=600)
        show eff neutral_talk at right
        with dissolve
        eff "Guys, good to see you again!"
        show sis neutral_talk flip at Position(xpos=600)
        show eff neutral at right
        sis "We hope we're not intruding, we're hoping we could join you for breakfast."
        show sis neutral flip at Position(xpos=600)
        show eff smirk_talk at right
        eff "Oh are you guys hungry?"
        show pov smirk_talk at left
        show eff smirk at right
        pov "Very~"
        show sis smirk flip at Position(xpos=600)
        show eff smirk_talk at right
        eff "Good thing I have plenty to go around, come on in."

        ## BEDROOM
        scene bg effieroom_day
        with fade
        show pov neutral at left
        show sis neutral flip at Position(xpos=600)
        show effpo neutral_talk at right
        with dissolve
        eff "Alright, you two. Eat up!"
        show sis confused_talk flip at Position(xpos=600)
        show effpo neutral at right
        sis "When did you get your shorts off?"
        show pov smirk at left
        show sis smirk flip at Position(xpos=600)
        show effpo smirk_talk at right
        eff "When you least expected."
        eff "C'mon, it's getting cold."

        jump lbl_mcxsister_eating_effie
