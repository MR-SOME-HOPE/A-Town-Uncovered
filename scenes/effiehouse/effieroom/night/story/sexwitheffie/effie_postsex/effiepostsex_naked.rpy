## Effie Post Sex (naked) ##
label lbl_effie_post_sex:
    show povn sad_talk at left
    with dissolve
    show effn bored at right
    with dissolve
    pov "I guess I should head home now."
    show povn bored at left
    show effn neutral_talk at right
    eff "Yeah, I don't think so."
    show povn confused_talk at left
    show effn neutral at right
    pov "Wait, what? Why not?"
    show povn confused at left
    show effn smirk_talk at right
    eff "Believe me, I'm not trying to hold you captive or anything but my dad's home."
    show povn confused_talk at left
    show effn smirk at right
    pov "And? Isn't that a reason for me to skidaddle?"
    show povn confused at left
    show effn bored_talk at right
    eff "He doesn't know you're here. Trust me, you don't wanna risk getting caught by him."
    show povn confused_talk at left
    show effn bored at right
    pov "Is he THAT bad?"
    show povn confused at left
    show effn bored_talk at right
    eff "Well... only to guys."
    show povn sad at left
    eff "Any guys I bring home really. It doesn't matter if you're my boyfriend or a study buddy."
    eff "He'll literally beat the shit out of you if he catches you."
    show povn sad_talk at left
    show effn bored at right
    pov "Oh my God. Has that happened before?"
    show povn sad at left
    show effn bored_talk at right
    eff "Nine times out of ten he does. The last time I had a guy over, he gave him three black eyes."
    show povn confused_talk at left
    show effn bored at right
    pov "Three?"
    show povn sad at left
    show effn bored_talk at right
    eff "Yeah, one on each of his eyex plus another black eye on top of his first black eye."
    show effn angry_talk at right
    eff "I nearly threw up looking at it."
    show povn bored_talk at left
    show effn bored at right
    pov "... Is he still alive."
    show povn sad at left
    show effn neutral_talk at right
    eff "I think he escaped wishing he had died instead."
    eff "So yeah. I guess we'll be sleeping together tonight."
    show povn confused_talk at left
    show effn neutral at right
    pov "Can't I climb through the window?"
    show povn bored at left
    show effn neutral_talk at right
    eff "Yeah, about that. It won't budge. Guess you have no choice."

    jump lbl_effie_post_sex_if

label lbl_effie_post_sex_if:
    $ main_story = 14
    $ gtime = 0
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    call lbl_next_date
    if effie_points >= 3:
        jump lbl_effie_post_sex_2
    else:
        scene black
        with fade
        $ skill_int_times = 0
        $ skill_sta_times = 0
        $ skill_luc_times = 0
        $ hitomibeach_day = 0
        call lbl_skill_items

        jump lbl_effieroom_day_setup

label lbl_effie_post_sex_2:
    show effn smirk_talk at right
    eff "So... you wanna keep fucking?"

    menu:
        "Hell to the fuckin' yeah!":
            jump lbl_effie_post_sex_3
        "No, I'm pretty tired.":
            show povn sad_talk at left
            show effn bored at right
            pov "I don't think I can cum a second round."
            show povn sad at left
            show effn angry_talk at right
            eff "You need to work on your stamina."
            scene black
            with fade

            jump lbl_effie_post_sex_end

label lbl_effie_post_sex_3:

    scene bg effieroom_nightlightson
    with fade
    show bg hsceneeffiepostsex_1
    with dissolve
    $ renpy.pause(4,hard=True)
    show bg hsceneeffiepostsex_2
    with dissolve
    $ renpy.pause(4,hard=True)
    show bg hsceneeffiepostsex_3
    with dissolve
    $ renpy.pause(4,hard=True)

    scene black
    with dissolve
    $ renpy.pause()

    jump lbl_effie_post_sex_end

label lbl_effie_post_sex_end:
    $ skill_int_times = 0
    $ skill_sta_times = 0
    $ skill_luc_times = 0
    $ hitomibeach_day = 0
    $ gtime = 0
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    call lbl_skill_items
    call lbl_next_date

    jump lbl_effieroom_day_setup
