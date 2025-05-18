## Hang at the Mall Now?
default hangatthemallnow_asked = 0
default hangatthemallnow_location = 0 # 0 is hallway, 1 is classroom

label lbl_hang_at_the_mall_now:
    #This scene only plays out if the player chose to “Take a raincheck” on the previous choice
    if hangatthemallnow_location == 0:
        scene bg schoolhallway1_day
    else:
        scene bg classroom_day

    if hangatthemallnow_asked == 0:
        $ hangatthemallnow_asked = 1
        show pov neutral_talk at left
        with dissolve
        show jac neutral at right
        with dissolve
        show eff neutral at Position(xpos=1300)
        with dissolve
        pov "Hey guys."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Sup dude! Feeling any better?"
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "Getting there."
        show pov neutral at left
        show jac neutral_talk at right
        jac "That’s good to hear!"
        show pov embarrassed at left
        show jac neutral at right
        show eff embarrassed_talk at Position(xpos=1300)
        eff "We are getting pretty worried over here, dude."
        show pov embarrassed_talk at left
        show eff smirk at Position(xpos=1300)
        pov "I know, I know."
        show eff neutral at Position(xpos=1300)
        pov "I’m sorry."
        show pov embarrassed at left
        show eff neutral_talk at Position(xpos=1300)
        eff "It’s alright dude, mental health is always important."
        show eff smirk_talk at Position(xpos=1300)
        eff "What kind of friends would we be if we just dragged you around everywhere regardless of what you're feeling?"
        show pov embarrassed_talk at left
        show jac smirk at right
        show eff neutral at Position(xpos=1300)
        pov "I appreciate you guys, I really do."
        show pov neutral at left
        show jac neutral at right
        show eff neutral_talk at Position(xpos=1300)
        eff "Same for us here!!"
        show pov confused at left
        show jac smirk_talk at right
        show eff neutral at Position(xpos=1300)
        jac "So, you up for those drinks now?"
        show pov embarrassed at left
        show jac confused_talk at right
        show eff smirk at Position(xpos=1300)
        jac "I’m pretty thirsty."
        show jac smirk at right
        show eff smirk_talk at Position(xpos=1300)
        eff "Yeah, I could go for a drink."
        eff "What do you say [povname]?"
    else:
        show pov neutral at left
        with dissolve
        show jac neutral at right
        with dissolve
        show eff neutral at Position(xpos=1300)
        with dissolve

    menu:
        "Head to the mall with them":
            show pov neutral_talk at left
            show jac neutral at right
            show eff neutral at Position(xpos=1300)
            pov "I’d be happy to go out with you guys."
            show pov embarrassed_talk at left
            show jac smirk at right
            show eff embarrassed at Position(xpos=1300)
            pov "I really need to clear my head."
            show pov neutral at left
            show eff smirk_talk at Position(xpos=1300)
            eff "Well, you came to the right place!"
            show jac confused at right
            show eff neutral_talk at Position(xpos=1300)
            eff "If anyone knows how to clear someone's head, it’s Jacob."
            show pov smirk at left
            show jac smirk_talk at right
            show eff smirk at Position(xpos=1300)
            jac "Well, I do pride myself as the relaxation master and-"
            show pov neutral at left
            show jac bored at right
            show eff smirk_talk at Position(xpos=1300)
            eff "You know, because of how much of an airhead he is already."
            show jac bored_talk at right
            show eff smirk at Position(xpos=1300)
            jac "Hey!"
            show pov smirk at left
            show jac bored at right
            show eff smirk_talk at Position(xpos=1300)
            eff "Nyehehe, too easy."
            show pov smirk_talk at left
            show eff smirk at Position(xpos=1300)
            pov "Heh, alright let’s get going then!"

            jump lbl_mall_with_friends

        "Another raincheck":
            if hangatthemallnow_asked == 0:
                show pov embarrassed_talk at left
                show jac embarrassed at right
                show eff embarrassed at Position(xpos=1300)
                pov "Sorry, guys. I still feel a little overwhelmed."
                show pov embarrassed at left
                show eff embarrassed_talk at Position(xpos=1300)
                eff "That’s fair enough."
                show jac smirk at right
                show eff neutral_talk at Position(xpos=1300)
                eff "Don’t worry about it, [povname]."
                eff "Take as long as you need."
                show jac neutral_talk at right
                show eff neutral at Position(xpos=1300)
                jac "Yeah dude, mental health is important."
                show jac smirk_talk at right
                show eff neutral at Position(xpos=1300)
                jac "We wouldn’t be able to call ourselves your friends if we just forced you to go out and when you really aren’t feeling it."
                show pov embarrassed_talk at left
                show jac smirk at right
                pov "Thanks for being so understanding you guys."
                show pov sad_talk at left
                show jac neutral at right
                show eff neutral at Position(xpos=1300)
                pov "I’m sorry to keep postponing it."
                show pov embarrassed at left
                show eff neutral_talk at Position(xpos=1300)
                eff "It’s cool, man!"
                show eff smirk_talk at Position(xpos=1300)
                eff "I mean, it’s not like the place is gonna close down or anything."
                show eff embarrassed_talk at Position(xpos=1300)
                eff "Take as long as you need, we care about you."
                show pov embarrassed_talk at left
                show eff embarrassed at Position(xpos=1300)
                pov "Thank you."
                show pov neutral at left
                show jac neutral_talk at right
                show eff neutral at Position(xpos=1300)
                jac "You know where to find us if you want to talk or feel good enough to go hang out."
                show pov neutral_talk at left
                show jac neutral at right
                pov "Definitely!"
            else:
                show pov sad_talk at left
                show jac embarrassed at right
                show eff confused at Position(xpos=1300)
                pov "Sorry, guys. Not right now."
                show pov embarrassed at left
                show jac confused at right
                show eff smirk_talk at Position(xpos=1300)
                eff "Well, don't blue ball us dude. We're heading there with or without you."
                show jac confused_talk at right
                show eff smirk at Position(xpos=1300)
                jac "Yeah! Wai- we are?"
                show pov embarrassed at left
                show jac bored_talk at right
                show eff smirk at Position(xpos=1300)
                jac "I don't wanna have to shout drinks every time."

            jump lbl_schoolhallway1_day_setup
