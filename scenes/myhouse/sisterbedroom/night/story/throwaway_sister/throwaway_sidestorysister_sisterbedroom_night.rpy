## Sister Side Story Throwaway Conversations Sister Bedroom Night ##

##############################################
## Ask about Mom at the Park
label lbl_sisterbedroom_night_sister_mompark:
    show pov confused_talk at left
    show sis confused at right
    with dissolve
    if winc == 0:
        pov "Hey... have you seen [missus]?"
    else:
        pov "Hey... have you seen Mom?"
    show pov confused at left
    show sis confused_talk at right
    sis "Nope? Isn't she in her room?"
    show pov confused_talk at left
    show sis bored at right
    pov "She isn't. I looked around the house and she's no where to be seen."
    show pov confused at left
    show sis bored_talk at right
    sis "Maybe she went out."
    show pov confused_talk at left
    show sis bored at right
    pov "I'll go out and look for her, she wouldn't have gone out without telling us."
    if sister_points >= 4:
        show pov confused at left
        show sis smirk_talk at right
        sis "Don't be too worried honey, our daughter is a strong, independent, woman now."
        show pov bored at left
        sis "You need to let her go."
    else:
        show pov bored at left
        show sis smirk_talk at right
        sis "I know you need your nightly breastfeed but I think it's time to grow up, [povname]."
        sis "Look- to ease you out of the habit, I'll buy some powdered milk for you."
    show pov bored_talk at left
    show sis smirk at right
    pov "Eh- shove it up yours, [sister]. I'll just see you later."
    if sister_points >= 7:
        show pov confused at left
        show sis smirk_talk at right
        sis "I totally won't utilize the time everyone's out to not watch porn on full volume."
        show pov bored_talk at left
        show sis smirk at right
        pov "I didn't need to know that."
        show pov bored at left
        show sis smirk_talk at right
        sis "You're just jealous."
    else:
        show pov bored at left
        show sis bored_talk at right
        sis "Whatever. Take your time,"
        show pov confused at left
        show sis smirk_talk at right
        sis "I totally won't sneak into your room and change something that you won't notice until a month later."
        show pov bored at left
        sis "Y'know, pyschological horror."

    jump lbl_sisterbedroom_night_setup

##############################################
## Mom x Sister x MC Boxfort Setup - SISTER
label lbl_momxsisxmc_boxfort_presister:
    show pov smirk_talk at left
    show sis confused at right
    with dissolve
    pov "Hey, [sister]. Is [missus] busy?"
    show pov smirk at left
    show sis smirk_talk at right
    sis "Why? Are you horny too?"
    show pov smirk_talk at left
    show sis smirk at right
    pov "Let's give her a formal invitation to our fort."
    show pov smirk at left
    show sis smirk_talk at right
    sis "Good idea, [povname]."
    show sis smirk at right
    sis "..."
    show pov shocked at left
    show sis neutral_talk at right
    with hpunch
    if winc == 1:
        sis "MOM!"
    else:
        sis "[missus]!"
    scene bg myhallway_night
    with fade
    show pov smirk at left
    show sis neutral flip
    show mum shocked_talk at right
    mum "Wh- wha- what's going on? Is anyone hurt?!"
    show pov embarrassed_talk at left
    show sis neutral flip
    show mum confused at right
    pov "Oh- no. Didn't mean to worry you~"
    show pov neutral at left
    show sis embarrassed_talk flip
    show mum shocked at right
    sis "We just wanted to ask if you wanted to join us in the-"
    show pov smirk at left
    show sis neutral flip
    show mum shocked_talk at right
    mum "Yes."
    show mum neutral_talk at right
    mum "1 million times yes~"
    show pov embarrassed at left
    show mum embarrassed_talk at right
    if winc == 1:
        mum "How could I ever say no to my two beautiful babies?"
    else:
        mum "How could I ever say no to you two?"
    show pov smirk at left
    show sis neutral_talk flip
    show mum neutral at right
    sis "Alright, let's go play!"

    jump lbl_momxsisterxmc_boxfort
