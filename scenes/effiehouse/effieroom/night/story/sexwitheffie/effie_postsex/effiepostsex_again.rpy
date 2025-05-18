## Effie Post Sex Again (MISH) ##
label lbl_effie_post_sex_2_mish:
    show povn neutral_talk at left
    with dissolve
    show effn neutral at right
    with dissolve
    pov "Well, that just as fun, if not better than last time."
    show povn neutral at left
    show effn neutral_talk at right
    eff "Haha, yeah, it really was. Your dick is like the perfect fit."
    show povn smirk_talk at left
    show effn neutral at right
    pov "Maybe we're destined to fuck each other forever."
    show povn smirk at left
    show effn bored_talk at right
    eff "Alright, let's not make any hasty wishes."

    jump lbl_effie_post_sex_2_end

## Effie Post Sex Again (EXIB) ##
label lbl_effie_post_sex_2_exib:
    show povn neutral_talk at left
    with dissolve
    show effn neutral at right
    with dissolve
    pov "Well, that just as fun, if not better than last time."
    show povn neutral at left
    show effn smirk_talk at right
    eff "Haha, yeah. Though it would've been nice if you could've lasted long enough to fuck me inside."
    show povn embarrassed_talk at left
    show effn neutral at right
    pov "Yeah, sorry about that.."
    show povn smirk at left
    show effn bored_talk at right
    eff "It's alright. Maybe next time."

    jump lbl_effie_post_sex_2_end

## Effie Post Sex Again (BJ) ##
label lbl_effie_post_sex_2_bj:
    show pov neutral_talk at left
    with dissolve
    show eff neutral at right
    with dissolve
    pov "Well, that just as fun, if not better than last time."
    show pov neutral at left
    show eff bored_talk at right
    eff "You tasted pretty alright. Maybe next time we can get to taking our clothes off."
    show pov embarrassed_talk at left
    show eff neutral at right
    pov "Yeah, sorry about that.."
    show pov smirk at left
    show eff bored_talk at right
    eff "It's alright. Maybe next time."
    show eff neutral_talk at right
    eff "You can climb out the window this time. I managed to fix it open."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Oh, really? Awesome."
    pov "Well, thanks again for tonight."
    show pov smirk at left
    show eff smirk_talk at right
    eff "No worries, dude. Let's do this again soon."
    $ effie_funlater = 0
    $ gtime = 3

    jump lbl_effiehouseoutside_night_setup

## Effie Post Sex Again (KISS) ##
label lbl_effie_post_sex_2_kiss:
    show pov sad at left
    with dissolve
    show eff bored_talk at right
    with dissolve
    eff "You can climb out the window this time. I managed to fix it open."
    show pov embarrassed_talk at left
    show eff bored at right
    pov "Oh, really?"
    pov "Well, thanks again for tonight, I guess?"
    show pov embarrassed at left
    show eff bored_talk at right
    eff "Yeah, sure. No worries, dude."
    $ effie_funlater = 0
    $ gtime = 3

    jump lbl_effiehouseoutside_night_setup

## Effie Post Sex Again (END) ##
label lbl_effie_post_sex_2_end:
    show effn neutral_talk at right
    eff "You can climb out the window this time. I managed to get it open."

    menu:
        "Awesome, thanks for tonight.":
            show povn neutral_talk at left
            show effn neutral at right
            pov "Oh, really? Awesome."
            pov "Well, thanks again for tonight."
            show povn smirk at left
            show effn smirk_talk at right
            eff "No worries, dude. Let's fuck again soon."
            $ effie_funlater = 0
            $ gtime = 3

            jump lbl_effiehouseoutside_night_setup
        "Wanna continue fucking?":
            show povn smirk_talk at left
            show effn neutral at right
            pov "Wanna continue fucking instead?"
            show povn smirk at left
            show effn smirk_talk at right
            eff "The night's young."

            jump lbl_effie_post_sex_3
