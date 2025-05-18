## Mother Side Story Throwaway Conversations Kitchen ##

## Fixed PC
label lbl_mykitchen_day_mother_fixedpc_0:
    show pov neutral at left
    with dissolve
    show mum embarrassed_talk at right
    with dissolve
    mum "Hey, [povname]. Thanks again for fixing the laptop."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "No problem at all."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "I- um.. I swear I didn't download that video..."
    show pov embarrassed_talk at left
    show mum sad at right
    if winc == 0:
        pov "If you say so, [missus]."
    else:
        pov "If you say so, Mom."

    jump lbl_mykitchen_day

## Mom Past Sunset
label lbl_mykitchen_day_mother_mompastsunset_1_0:
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Hey, [povname]! I can't wait for later, tonight."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Neither can I."
    show pov neutral at left
    show mum smirk_talk at right
    mum "If only time travelling was possible."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "Yeah..."

    jump lbl_mykitchen_day

## Mom Past Sunset (Ignored)
label lbl_mykitchen_day_mother_mompastsunset_2_0:
    show pov sad at left
    with dissolve
    show mum angry at right
    with dissolve
    mum "..."
    show pov sad_talk at left
    if winc == 0:
        pov "[missus]?"
    else:
        pov "Mom?"
    show pov sad at left
    mum "..."

    jump lbl_mykitchen_day

## Sister Left to Effie's House
label lbl_mykitchen_day_mother_sistergone:
    show pov sad_talk at left
    with dissolve
    show mum embarrassed at right
    with dissolve
    pov "Hey, mom."
    show pov embarrassed_talk at left
    show mum sad at right
    pov "How are you feeling..?"
    show pov embarrassed at left
    show mum sad_talk at right
    mum "{i}*Sigh*{/i}"
    show pov embarrassed at left
    mum "I hope my baby's okay."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Effie's a nice girl, I'm sure she's just the friend that [sister] needs right now."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "She is, just give her some time."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "How about you? Are you doing okay?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "As fine as anyone can be."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I'm here for you if you need me, don't be afraid to speak up, promise?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "I promise."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I love you, honey."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "I love you too, mom."

    jump lbl_mykitchen_day
