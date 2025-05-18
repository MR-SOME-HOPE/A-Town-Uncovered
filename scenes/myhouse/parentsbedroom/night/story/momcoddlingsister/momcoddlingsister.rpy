## Mom Coddling Sister

label lbl_mom_coddling_sister:
    scene bg momcoddlingsister_1
    with dissolve
    $ renpy.pause()
    show bg momcoddlingsister_2
    pov "Oh! There you guys are."
    show bg momcoddlingsister_3
    mum "Hey, honey. You were looking for us?"
    show bg momcoddlingsister_2
    pov "Not really, just wondered where you were."
    pov "Thought you might’ve gone out for the night or something."
    pov "…"
    show bg momcoddlingsister_4
    pov "What’s up with Miss Sleepyhead over there?"
    show bg momcoddlingsister_5
    mum "Oh- well… y’know. Work."
    show bg momcoddlingsister_6
    mum "They’re really pushing her these days."
    mum "They really need to hire more help at that place…"
    show bg momcoddlingsister_7
    if sister_path >= 18:
        pov "At the adult store, right?"
        mum "…"
        show bg momcoddlingsister_8
        mum "Oh- you know about that huh?"
        mum "Uhm... anyway, you don't mind leaving us be, do you, sweetie?"
    else:
        pov "Where does she work again?"
        mum "…"
        show bg momcoddlingsister_8
        mum "Hey- uh. Sorry, but I’m a little tired, honey."
    mum "I just wanna enjoy the movie and hopefully fall asleep, if you don’t mind."
    show bg momcoddlingsister_9
    if winc == 0:
        pov "Oh- yeah sure. Sorry to bother you, [missus]."
    else:
        pov "Oh- yeah sure. Sorry to bother you, Mom."
    show bg momcoddlingsister_8
    mum "Hey, [povname]."
    show bg momcoddlingsister_2
    pov "Mm?"
    show bg momcoddlingsister_3
    mum "I love you."
    mum "Always."
    show bg momcoddlingsister_2
    pov "Heh, I love you too, [missus]."
    show bg momcoddlingsister_3
    mum "Dinner’s in the fridge if you haven’t eaten already."
    show bg momcoddlingsister_2
    pov "Alright."
    pov "Goodnight."
    "{i}*Door Thud*{/i}"
    show bg momcoddlingsister_10
    sis "Ooft, thought he’d never leave."
    show bg momcoddlingsister_11
    mum "Hehe, don’t worry, baby. You can keep sucking now."
    show bg momcoddlingsister_10
    sis "Yes, Mommy."
    show bg momcoddlingsister_1
    sis "{i}*Chu- chu--op*{/i} Mmmph"

    $ mumsis_path = 4

    jump lbl_myhallway_night
