## Mother Side Story Throwaway Conversations Parents Room Night ##
##########################################################
## Mother Post Side Story Sex
label lbl_parentsbedroom_night_mother_hscene_redo:
    if winc == 0:
        jump lbl_parentsbedroom_night_mother_hscene_redo_winc0
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    hide btn parentsbedroom_night_mother_idle
    with dissolve
    pov "Hey, Mom."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh, hey, [povname]."
    show pov sad_talk at left
    show mum embarrassed at right
    pov "I can't sleep..."
    show pov sad at left
    show mum embarrassed_talk at right
    mum "Naww, really?"
    show pov smirk at left
    show mum smirk_talk at right
    mum "You want Mommy to tuck you in and cuddle beside you?"
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "That would definitely help.."
    show pov neutral at left
    show mum smirk_talk at right
    mum "I'll meet you in bed."
    show pov smirk_talk at left
    show mum smirk at right
    pov "Don't take too long."

    $ mum_bedroomsex = 1

    jump lbl_myhallway_night

### NO WINC ###
label lbl_parentsbedroom_night_mother_hscene_redo_winc0:
    show pov neutral_talk at left
    with dissolve
    show mum neutral at right
    with dissolve
    pov "Hey, [missus]."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh, hey, [povname]."
    show pov sad_talk at left
    show mum embarrassed at right
    pov "I can't sleep..."
    show pov sad at left
    show mum embarrassed_talk at right
    mum "Naww, really?"
    show pov smirk at left
    show mum smirk_talk at right
    mum "You want me to tuck you in and cuddle beside you?"
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "That would definitely help.."
    show pov neutral at left
    show mum smirk_talk at right
    mum "I'll meet you in bed."
    show pov smirk_talk at left
    show mum smirk at right
    pov "Don't take too long."

    $ mum_bedroomsex = 1

    jump lbl_myhallway_night

##############################################
## Mom x Sister x MC Boxfort Setup - MOM
label lbl_momxsisxmc_boxfort_premum:
    show pov sad_talk at left
    show mum smirk at right
    hide btn parentsbedroom_night_mother_idle
    with dissolve
    if winc == 1:
        pov "Hey, mom... wanna play with me?"
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Nawww, is my baby bored?"
    else:
        pov "Hey, [missus]... wanna play with me?"
        show pov embarrassed at left
        show mum smirk_talk at right
        mum "Nawww, is my favourite person bored?"
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "Maybe..."
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Hehehe~ Of course honey, I always have time for you."
    show pov neutral_talk at left
    show mum confused at right
    pov "Yay! I was actually thinking [sister] can join us-"
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "Is that alright?"
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Pssh, is that really a question?"
    show pov neutral at left
    show mum neutral_talk at right
    mum "She's always welcome, the more the merrier!"
    show pov neutral_talk at left
    show mum neutral at right
    pov "C'mon, let's go get her."
    scene bg myhallway_night
    with fade
    $ renpy.pause()
    "{i}*Knock knock*{/i}"
    mum "..."
    show pov neutral at left
    show mum neutral at right
    show sis confused_talk flip
    with dissolve
    sis "What?"
    show pov smirk at left
    show mum neutral_talk at right
    show sis confused flip
    mum "[povname] wants to play."
    show pov embarrassed at left
    show mum confused at right
    show sis confused_talk flip
    sis "Now?"
    show mum confused_talk at right
    show sis confused flip
    mum "Are you busy?"
    show pov neutral at left
    show mum neutral at right
    show sis confused_talk flip
    sis "Well- not really..."
    show pov neutral_talk at left
    show mum shocked at right
    show sis neutral flip
    pov "C'mon, we can hang out in the fort!"
    show pov smirk at left
    show sis neutral_talk flip
    sis "Hmm- I do like the vibes there..."
    show mum embarrassed_talk at right
    show sis neutral flip
    mum "Oooh! Are you sure I'm allowed in there?"
    show pov neutral at left
    show mum neutral at right
    show sis smirk_talk flip
    if winc == 1:
        sis "Wait, you're joining us too, mom? Of course you're welcome into our fort!"
    else:
        sis "Wait, you're joining us too, [missus]? Of course you're welcome into our fort!"
    show pov neutral_talk at left
    show mum smirk at right
    show sis neutral flip
    pov "Then what are we waiting for, girls?"
    show pov smirk_talk at left
    show mum bored at right
    show sis smirk flip
    pov "Race ya'll there!"
    show pov bored at left
    show mum bored_talk at right
    mum "Ah- no running in the house, [povname]. You know better."

    jump lbl_momxsisterxmc_boxfort
