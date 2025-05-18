## Comparing Flyer Maps
label lbl_comparing_flyer_maps:
    ## SPRITEWORK
    # You arrive back home to the kitchen and find Mum and Sister discussing the flyers

    show pov bored at left
    show sis smirk_talk at Position(xpos=1200)
    show mum confused at Position(xpos=1600)
    with dissolve
    sis "Hey, dude. Did you also receive one of these flyers?"
    show pov bored_talk at left
    show sis smirk at Position(xpos=1200)
    pov "Hmm?"
    show pov shocked at left
    show sis  at Position(xpos=1200)
    show mum confused_talk at Position(xpos=1600)
    mum "The Followers of Master Buukakki. These people are everywhere."
    show mum smirk_talk at Position(xpos=1600)
    mum "And I literally mean everywhere, I couldn’t run my errands without having one of them aggressively sticking these flyers out at me."
    show sis smirk_talk at Position(xpos=1200)
    show mum confused at Position(xpos=1600)
    sis "They’re everywhere in town. I’ve seen them myself too."
    show pov confused_talk at left
    show sis smirk at Position(xpos=1200)
    pov "I actually saw them at the mall too…"
    show pov embarrassed_talk at left
    pov "They didn’t hand it to me, they literally shoved it into me, so of course I had to take it."
    show pov embarrassed at left
    show sis bored_talk at Position(xpos=1200)
    sis "They were going into every store and asking us if we had a flyers board they could put it up on. They said it was related to our industry, at least that’s what Hazel told me."
    show mum bored_talk at Position(xpos=1600)
    mum "I rejected everyone I met whilst I was out but when I came home, I saw it was slipped into our mailbox as well as underneath the front door."
    show sis bored_talk at Position(xpos=1200)
    show mum bored at Position(xpos=1600)
    sis "These people are crazy."
    show pov bored_talk at left
    pov "No kidding. I’ve never seen such aggressive marketing."
    show pov smirk_talk at left
    show sis neutral at Position(xpos=1200)
    pov "But hey, do you recognize where in town this map is?"
    show pov embarrassed_talk at left
    pov "It’s kinda vague and has no labels."
    show pov embarrassed_talk at left
    pov "It’s… odd."
    show pov embarrassed at left
    show sis smirk_talk at Position(xpos=1200)
    sis "I was wondering the same thing!"
    show sis smirk at Position(xpos=1200)
    show mum neutral_talk at Position(xpos=1600)
    mum "Me too, it’s certainly obscure."
    show pov smirk_talk at left
    show mum neutral at Position(xpos=1600)
    pov "Can I see yours?"
    show pov confused at left
    show sis bored_talk at Position(xpos=1200)
    show mum  at Position(xpos=1600)
    sis "Here."
    show pov shocked at left
    show sis bored at Position(xpos=1200)
    pov "…"
    show pov confused_talk at left
    show sis confused at Position(xpos=1200)
    show mum  at Position(xpos=1600)
    pov "W-"
    pov "Wait, hold on…"
    show sis bored at Position(xpos=1200)
    pov "…"
    show pov shocked_talk at left
    show mum confused at Position(xpos=1600)
    pov "They’re different?"
    show pov angry_talk at left
    show sis embarrassed at Position(xpos=1200)
    if winc == 0:
        pov "[missus], can I see yours?"
    else:
        pov "Mom, can I see yours?"
    show pov confused at left
    show mum neutral_talk at Position(xpos=1600)
    mum "Take it, I don’t wanna deal with that."
    show sis neutral at Position(xpos=1200)
    show mum neutral_talk at Position(xpos=1600)
    mum "I’m gonna make dinner."

    ## Mum leaves
    show pov shocked_talk at left
    show sis confused at right
    hide mum
    with dissolve
    pov "Huh…"
    show sis embarrassed at right
    pov "All three flyers are different?"
    show pov confused at left
    show sis smirk_talk at right
    sis "That’s so fucking sus, bro."
    show sis confused_talk at right
    sis "I’ll need to check out all the flyers we have at the register the next time I get into work."
    show pov confused_talk at left
    show sis confused at right
    pov "Hmmm…"
    pov "Yeah, definitely let me know what you find and like how many variants there are."
    show pov smirk at left
    show sis neutral_talk at right
    sis "Will do, chief."
    show pov neutral at left
    show sis neutral at right
    "{i}*Riiiiiingggggg*{/i}"
    show pov shocked_talk at left
    show sis bored at right
    pov "Oh shit, someone’s calling me."
    show pov confused_talk at left
    pov "Here’s your flyer back-"
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Keep it, it’s just trash to me."

    ## You rush upstairs to take the call from Edward


    $ main_story = 148

    jump lbl_edwards_stolen_evidence
