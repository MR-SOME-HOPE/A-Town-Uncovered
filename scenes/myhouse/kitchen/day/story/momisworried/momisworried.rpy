default mainstory_69_atebreakfast = 0

label lbl_mom_is_worried:
    #(this scene only occurs if the player talks with mom in the kitchen before leaving for school)
    scene bg mykitchen_day
    with fade
    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    #if winc == 0:
        #"The MC approaches [missus] looking rather bad and shaken up, worrying [missus] even more."
    #else:
        #"The MC approaches Mom looking rather bad and shaken up, worrying Mom even more."
    show pov sad at left
    with dissolve
    show mum sad_talk at right
    with dissolve
    mum "Seriously honey. If you need to take a day off or something to rest, I can phone your university and let them know."
    show mum sad
    show pov shocked_talk
    pov "No, no…"
    show pov embarrassed_talk
    if winc == 1:
        pov "It’s alright, Mom. Really…"
    else:
        pov "It’s alright, [missus]. Really…"
    pov "I don’t want to make a big deal out of it…"
    pov "… And I don’t want to stay in one place for too long."
    show pov embarrassed
    show mum confused_talk
    mum "What?"
    show mum confused
    show pov bored_talk
    pov "N-Nothing…"
    pov "I better get going."
    show pov bored
    show mum sad_talk
    mum "[povname], seriously, I don’t mind if you need to stay home today!"
    mum "I-I’ll even let you watch tv all day once you wake up!"
    show mum sad

    if mum_path >= 31:
        show mum smirk_talk
        mum "We can cuddle in bed all day if you want."
        mum "O-Or how about a bath together?"
        mum "We can hang out naked all day if you wish!"
        show mum smirk
    show pov embarrassed_talk
    if winc == 1:
        pov "It’s okay, Mom."
    else:
        pov "It’s okay, [missus]."
    pov "I really just need to get out of here…"
    pov "I don’t want to run in late..."
    show pov embarrassed
    show mum confused_talk
    mum "At least eat your breakfast!"
    mum "It would really give me peace of mind if you did…"
    mum "Please, [povname]."
    show mum confused
    show pov neutral
    menu:
        "Eat breakfast.":
            pov "…"
            show pov neutral_talk
            pov "Alright…"
            pov "Just because it was you who made it…"
            show pov neutral
            show mum smirk
            $ add_points("mum_points",2)
            show mum neutral_talk
            mum "Oh thank you, [povname]!"
            show mum smirk_talk
            mum "Now come on, it’s going to get cold."
            show mum smirk
            show pov shocked_talk
            pov "I’m coming, I’m coming…"

                #"If Missus has been romance."
            if mum_path >= 31:
                show mum smirk_talk
                mum "Good, you need all the energy you need."
                mum "With all the fun we've been having lately."
                show mum smirk
                show pov embarrassed_talk
                pov "Mooom, [sister] might hear you."
                mum "Hehehe~"

            scene black
            with fade
            $ renpy.pause(1.5)
            "After breakfast..."
            scene bg mykitchen_day
            with fade
            show pov neutral_talk at left
            with dissolve
            show mum neutral at right
            with dissolve
            pov "Thanks for breakfast, [missus]."
            show mum neutral_talk
            mum "Anytime, sweetie!"
            mum "It’s my job to take care of you and I’m glad to do it!"
            show mum confused_talk
            mum "Would you like to talk about what has you so shaken up?"
            mum "It could help, you know?"
            show pov neutral_talk
            pov "I’d rather just have breakfast and be on my way for now."
            show pov neutral
            show mum neutral_talk
            mum "Alright, I won’t push it."
            show mum neutral
            show pov neutral_talk
            pov "Thanks."

            $ mainstory_69_atebreakfast = 1

        "Go out early.":
            show pov sad_talk
            if winc == 1:
                pov "I’m sorry, Mom…"
            else:
                pov "I’m sorry, [missus]..."
            pov "I really just want to get to university and have this day over with."
            show pov sad
            show mum sad
            $ subtract_points("mum_points",1)
            show mum shocked_talk
            mum "O-Oh…"
            mum "Well…"
            show mum sad
            show pov sad_talk
            pov "Thanks for trying, but I really just need to get out of here for a while."
            show pov sad
            show mum sad_talk
            mum "It’s okay…"
            mum "Have a good day."
            show mum sad
            show pov sad_talk

            pov "I’ll be back soon."
            show pov sad
            #if winc == 1:
                #"The player leaves leaving Mom behind and worried."
            #else:
                #"The player leaves leaving [missus] behind and worried."

    $ main_story = 70
    $ townmap_enabled = 1
    scene black with fade
    jump lbl_townmap_setup
