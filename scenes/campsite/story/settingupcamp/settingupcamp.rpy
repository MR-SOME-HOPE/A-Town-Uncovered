## Setting Up Camp
label lbl_setting_up_camp:
    scene bg campsite_1
    with fade

    show pov neutral at left
    show sis bored at Position(xpos=1300)
    show mumc neutral_talk at right
    with dissolve
    mum "Well, here we are. A nice open clearing, a good distance away from the cliff itself."

    show pov neutral_talk at left
    show mumc neutral at right
    pov "Yeah! It looks like a pretty good spot. I never knew about this place."

    show pov neutral at left
    show mumc neutral_talk at right
    if winc == 0:
        mum "Why don’t you grab the stuff from the car and set up the tent, guys."
    else:
        mum "Why don’t you grab the stuff from the car and set up the tent, kids."

    show pov confused at left
    show sis bored_talk at Position(xpos=1300)
    show mumc bored at right
    sis "{i}*Groans*{/i}"

    show sis sad at Position(xpos=1300)
    show mumc bored_talk at right
    mum "[sister]."

    show sis sad_talk at Position(xpos=1300)
    show mumc bored at right
    if winc == 0:
        sis "I haven’t even had breakfast yet, [missus]."
    else:
        sis "I haven’t even had breakfast yet, mom."
    sis "I’m tired as hell-"
    sis "And now I have to-"

    show pov confused_talk at left
    show sis sad at Position(xpos=1300)
    show mumc neutral at right
    pov "Don’t be such a sourpuss immediately, [sister]."
    show pov neutral_talk at left
    show sis bored at Position(xpos=1300)
    pov "It’s not that hard, just carry the stuff out and I’ll pitch the tent."

    show pov confused at left
    show mumc shocked_talk at right
    mum "You know what?"
    show pov shocked at left
    show sis shocked at Position(xpos=1300)
    show mumc embarrassed_talk at right
    mum "Are you alright with that, [povname]? Are you able to all do that by yourself?"

    show pov shocked_talk at left
    show sis smirk at Position(xpos=1300)
    show mumc neutral at right
    pov "Huh?!"

    show pov embarrassed at left
    show sis confused at Position(xpos=1300)
    show mumc neutral_talk at right
    mum "I think I have a better idea for [sister] to do."

    show pov embarrassed_talk at left
    show mumc neutral at right
    pov "Yeah, yeah. I’ll manage. You two just relax or something."

    show pov confused at left
    show mumc smirk_talk at right
    mum "Okie dokie! C’mon, [sister]. I’ll take you somewhere you’re gonna love."
    mum "Maybe this alone will convince you that this trip is worth it."

    show pov bored at left
    show sis smirk_talk at Position(xpos=1300)
    show mumc neutral at right
    sis "Fine, see you, loser."

    show pov shocked_talk at left
    show sis smirk at Position(xpos=1300)
    pov "Wait- where are you guys going?"
    pov "You're gonna leave me here? I thought you're gonna do something else here."

    show pov confused at left
    show sis neutral at Position(xpos=1300)
    show mumc neutral_talk at right
    mum "We’re gonna go down this path here, when you’re done, just meet us at the end of this path, you can’t miss us."
    mum "[sister] and I will have some girl on girl bonding time."

    show pov bored_talk at left
    show mumc neutral at right
    pov "{i}*Sigh*{/i} Alright, you girls have fun."
    pov "I’ll have this up in- two to three business days."

    show pov bored at left
    show mumc neutral_talk at right
    mum "Don’t take too long."

    # They both leave.
    hide sis
    hide mumc
    with dissolve

    show pov bored_talk at left
    pov "Great. Where the fuck are the instructions-"
    show pov bored
    pov "..."
    show pov confused_talk at left
    pov "I think this is…"
    pov "Swedish?"
    show pov bored_talk at left
    pov "At least there’s pictures…"

    ## SCENE END

    $ mumsiscamp_path = 4

    jump lbl_the_natural_spring
