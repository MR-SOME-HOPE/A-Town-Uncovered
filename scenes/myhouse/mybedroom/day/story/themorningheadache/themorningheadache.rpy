label lbl_the_morning_headache:
    scene black
    with fade
    #if winc == 1:
        #"The screen fades back in to reveal your sleeping body on the floor, Mom is trying to get you to wake up, worried sick."
    #else:
        #"The screen fades back in to reveal your sleeping body on the floor, [missus] is trying to get you to wake up, worried sick."

    mum "...swee-"
    mum "…tie?"
    mum "-eetie?"
    mum "[povname]?"
    mum "Come on, please wake up!"

    pov "Mmnn…"
    pov "What?"

    #show bg themorningheadache_temp1
    scene bg themorningheadache_shot1
    with fade

    mum "Oh thank God, [povname]!"
    #if winc == 1:
        #"Mom pulls you into a tight hug."
    #else:
        #"[missus] pulls you into a tight hug."
    scene bg themorningheadache_shot2_1
    pov "Wha-"
    pov "What’s going on?"
    scene bg themorningheadache_shot2_2
    mum "I should be asking you that!"
    mum "I come back to wake you up and I found you  on the floor like this!"
    mum "Are you okay?!"
    mum "Did you have seizure?!"
    mum "Should I call an ambulance?!"
    scene bg themorningheadache_shot2_1

    if winc == 1:
        pov "N-No, Mom. I am fine…"
    else:
        pov "N-No, [missus]. I am fine…"
    pov "I uh…"

    #"You sneak a look at the window’s closed blinds."

    #show bg themorningheadache_temp4

    pov "I must have sleep walked or something, I am okay…"
    scene bg themorningheadache_shot2_2
    mum "Oh, darling… "

    scene bg themorningheadache_shot3_1 with fade
    #"She pulls you into another hug."

    #show bg themorningheadache_temp3

    mum "Don’t you worry now, you are safe here."

    pov "…"
    scene bg themorningheadache_shot3_2
    pov "Am I?"
    scene bg themorningheadache_shot3_1
    mum "Of course you are!"
    mum "I would never allow anything to happen to you."
    mum "Not while I have a breath left in my body."

        #"-If Mom has been romanced-"
    if mum_path >= 31:
        mum "You are far too important for me to lose you, [povname]"
        if winc == 1:
            "Mom then reaches in and gives you a sweet kiss."
        else:
            "[missus] then reaches in and gives you a sweet kiss."

        mum "I sort of expect you to know that by now."

        #=RESULT END#=

    scene bg themorningheadache_shot3_3

    mum "Now come on. It’s a bright day out and you still have things to do, sweetie."
    mum "I’ll make you your favorite breakfast, so get ready and come downstairs."

    #show bg themorningheadache_temp4
    scene bg themorningheadache_shot3_4

    pov "Y-yeah.. okay-"
    pov "I'm- I'm fine, really-"
    pov "J-Just a long night. "
    pov "I-I’ll be down in a bit…"

    #if winc == 1:
        #if mum_path >= 31:
            #"Mom is reluctant to leave but she does so after kissing your lips and leaves the room looking worried."
        #else:
            #"Mom is reluctant to leave but she does so after kissing your forehead and leaves the room looking worried."
    #else:
        #if mum_path >= 31:
            #"[missus] is reluctant to leave but she does so after kissing your lips and leaves the room looking worried."
        #else:
            #"[missus] is reluctant to leave but she does so after kissing your forehead and leaves the room looking worried."
    scene bg themorningheadache_shot4 with fade
    pov "…"

    #"You look back towards the window, inspecting it for any signs of what happened last night."

    pov "{i}It really must've been a nightmare.{/i}"
    pov "{i}The- the message is gone.{/i}"
    pov "{i}Yeah, that's it. Just a fucking nightmare hallucination.{/i}"
    pov "{i}What- is in this town's drinking water...?{/i}"
    pov "{i}I feel something stuck to my back..{/i}"

    #"You reach behind you to find the polaroid from last night."

    #show bg themorningheadache_temp5
    scene bg themorningheadache_shot5 with fade

    pov "This… This isn’t happening!"

    #"You tried to calm yourself down only to look down at the ground under the window, where the polaroid ominously was, waiting for you to pay attention to it."

    pov "No, no, no, no, no, no, no, no, no!"

    #"You slowly pick it up, the haunting image of you sleeping while the picture was taken from the inside of your room is just as haunting as the lipstick mark and Xina’s signature."

    pov "Please God, let it be a dream…"

    #"You turn the picture around, where yet another message is written, this in the same penmanship as Xina’s signature. “To my beloved sacrifice, I’m coming for you~ And you are going to regret running away from me!”."
    scene bg themorningheadache_shot6 with dissolve
    pov "…"
    pov "Oh, balls…"

    $ main_story = 69
    $ townmap_enabled = 0

    jump lbl_mybedroom_day_setup
