## Ceremony Dress Up
label lbl_ceremony_dress_up:
    # Before Going In
    scene bg myhousefront_night

    show pov confused_talk

    with dissolve
    pov "Hey, guys. Edward, Jacob, can you hear me?"
    show pov smirk_talk
    pov "I’m a little nervous about what’s gonna go down tonight…"
    show pov embarrassed_talk
    pov "I don’t trust any of this."
    show pov smirk_talk
    pov "No matter how amazing this town seems to be."
    show pov bored_talk
    pov "…"
    show pov confused_talk
    pov "Hello?"
    show pov shocked_talk
    pov "…"
    show pov embarrassed_talk
    pov "Helloooo??"
    show pov bored
    pov "…"
    show pov embarrassed
    pov "{i}Damn, the comms are fried… wonder how long it’s been like that for…{/i}"

    # Enter the house
    scene bg mylivingroom_night # Lights On
    with fade

    show pov neutral at left
    show mum neutral_talk at right
    mum "Hey, [povname]."
    mum "Are you ready?"
    show pov bored_talk at left
    show mum confused at right
    pov "*Sigh* I guess."
    show pov confused at left
    show mum smirk_talk at right
    mum "Why the worried face? It’ll be okay."
    show pov embarrassed_talk at left
    show mum smirk at right
    pov "I don’t know, I can’t help but worry about it."
    show pov confused_talk at left
    show mum confused at right
    pov "Last time I was here, I nearly died so excuse me for feeling on edge."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "Oh, honey. There’ll be plenty of time to edge later tonight."
    show mum bored at right
    mum "…"
    show mum neutral_talk at right
    mum "I’ve picked out your outfit for tonight, I hope you like it."
    show pov shocked_talk at left
    show mum neutral at right
    pov "Oh- um… that’s quite… revealing."
    show pov embarrassed at left
    show mum shocked_talk at right
    mum "Yeah, I know it looks a little uncomfortable but it’ll only be for an hour tops."
    show mum neutral_talk at right
    mum "Then you’re free to take it off if someone doesn’t take it off you first."
    show pov shocked_talk at left
    show mum neutral at right
    pov "Err-"
    show pov embarrassed at left
    show mum smirk_talk at right
    mum "Hehe, don’t be embarrassed, we’ll all be wearing something revealing so it’s not like you’ll be too overdressed."
    show mum neutral_talk at right
    mum "I picked out something new for myself as well."
    show pov neutral at left
    show mum confused_talk at right
    mum "I bet you’ll like it."
    show pov smirk at left
    show mum smirk_talk at right
    mum "Well, get to it. Put it on."
    show pov smirk_talk at left
    show mum smirk at right
    pov "What here?"
    show pov neutral at left
    show mum neutral_talk at right
    mum "Where else, ya silly goose."

    # You both start stripping and changing in the living room into your ceremonial attire.
    hide pov
    hide mum
    with dissolve
    ## Use povsa (pov sex attire) and mumsa (mum sex attire)
    show povsa embarrassed at left
    show mumsa neutral_talk at right
    with dissolve
    mum "Oh my goodness, you are soooo handsome."
    show mumsa smirk_talk at right
    mum "Where do you get your good looks from?"
    show mumsa neutral_talk at right
    mum "Oh yeah, me~ Hehehehe~"
    mum "I’m guessing from the looks of things you like how I look too?"
    show povsa embarrassed_talk at left
    show mumsa smirk at right
    pov "Sorry, it just kinda… popped up."
    show povsa neutral at left
    show mumsa smirk_talk at right
    mum "Hahaha, I know it’s a compliment, baby."
    mum "You’re really so cute being shy and all, like a little baby who’s only discovering things about the real world."
    show povsa smirk at left
    show mumsa neutral_talk at right
    mum "It brings back a lot of memories."
    show povsa smirk_talk at left
    show mumsa neutral at right
    pov "Is that really what I sound like… no matter how much I try and get used to it, this universe really is on another level of ‘comfortable’ to say the least."
    show povsa smirk at left
    show mumsa smirk_talk at right
    mum "I can’t imagine how conservative the other world is, it honestly sounds like a nightmare, to have no freedom?"
    show povsa smirk_talk at left
    show mumsa neutral at right
    pov "We have freedom, just-"
    show povsa neutral at left
    show mumsa embarrassed_talk at right
    mum "I guess our definitions of freedom are different."
    show mumsa neutral_talk at right
    mum "I love you nevertheless."
    show povsa neutral_talk at left
    show mumsa embarrassed at right
    pov "I love you too, [missus]."
    show povsa shocked_talk at left
    show mumsa confused at right
    pov "Uhm…"
    pov "I’ll probably be leaving with Effie tonight as soon as I find her but…"
    show povsa embarrassed_talk at left
    show mumsa embarrassed at right
    pov "Would we be able to have sex before I go?"
    show povsa embarrassed at left
    show mumsa smirk_talk at right
    mum "I would love nothing more, baby."
    show mumsa neutral_talk at right
    mum "We’ll have our fun at the ceremony, okay?"
    show mumsa smirk_talk at right
    mum "We don’t wanna be running late."
    show povsa smirk at left
    mum "Stay hard for me until then, okay?"

    if winc == 0:
        show povsa smirk_talk at left
        show mumsa smirk at right
        pov "Okay, [missus]."
    else:
        show povsa embarrassed_talk at left
        show mumsa neutral at right
        pov "Okay, mom."

    show povsa neutral at left
    show mumsa neutral_talk at right
    mum "Alright, let’s go. Don’t forget anything."
    show povsa neutral at left
    pov "I think I have all that I really need."

    scene black
    with fade
    $ renpy.pause()
    "At the park..."

    $ main_story = 135

    jump lbl_second_safer_ceremony
