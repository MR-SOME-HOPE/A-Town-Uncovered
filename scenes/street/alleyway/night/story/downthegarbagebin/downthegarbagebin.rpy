## Down The Garbage Bin
label lbl_down_the_garbage_bin:
    # MC, Jacob, Effie, Edward, and Cole are all present at the alleyway.
    ## SPRITE
    scene bg streetalleyway_night
    with fade

    show pov neutral at left
    show col neutral_talk at Position(xpos=1000)
    show jac neutral at Position(xpos=1300)
    show eff confused at Position(xpos=1500)
    show edw shocked at Position(xpos=1800)
    with dissolve
    col "Okay, we’re here."
    show col embarrassed_talk at Position(xpos=1000)
    col "I don’t see anything."
    show pov bored at left
    show col smirk_talk at Position(xpos=1000)
    show eff bored at Position(xpos=1500)
    show edw confused at Position(xpos=1800)
    col "Just a lot of graffiti, rubbish, and condoms on the ground."
    show col smirk at Position(xpos=1000)
    show jac bored_talk at Position(xpos=1300)
    jac "Ew, is that yours."
    show col smirk_talk at Position(xpos=1000)
    show jac smirk at Position(xpos=1300)
    col "Don’t be silly, Jacob. Mines are XL."
    show pov neutral at left
    show col smirk at Position(xpos=1000)
    show eff bored_talk at Position(xpos=1500)
    eff "Pssh, okay."
    show col smirk_talk at Position(xpos=1000)
    show jac shocked at Position(xpos=1300)
    show eff smirk at Position(xpos=1500)
    col "Want me to prove it?"
    show pov bored at left
    show col smirk at Position(xpos=1000)
    show edw shocked_talk at Position(xpos=1800)
    edw "Wait- they come in XL?"
    show pov bored_talk at left
    show col bored at Position(xpos=1000)
    show edw shocked at Position(xpos=1800)
    pov "Guys."
    pov "Focus."
    show pov confused_talk at left
    pov "The map says it’s here."
    show pov embarrassed_talk at left
    show jac bored at Position(xpos=1300)
    show eff confused at Position(xpos=1500)
    show edw confused at Position(xpos=1800)
    pov "Maybe there’s a secret entrance here somewhere."
    show pov confused_talk at left
    show col shocked at Position(xpos=1000)
    pov "It’s gotta be around here somewhere, I can sense it."
    show pov confused at left
    show jac embarrassed at Position(xpos=1300)
    show edw confused_talk at Position(xpos=1800)
    edw "What like, a special brink combination that we have to press."
    show jac smirk_talk at Position(xpos=1300)
    show edw smirk at Position(xpos=1800)
    jac "This isn’t Parry Hotter, Edward."
    show col neutral at Position(xpos=1000)
    show jac bored at Position(xpos=1300)
    show eff neutral at Position(xpos=1500)
    jac "We’re not dealing with the witching world."
    show jac smirk at Position(xpos=1300)
    show edw neutral_talk at Position(xpos=1800)
    edw "I feel like it may as well be, to be honest."
    show pov embarrassed at left
    show eff neutral_talk at Position(xpos=1500)
    show edw neutral at Position(xpos=1800)
    eff "It’s not the stupidest idea, who knows, [povname] might be right."
    eff "It’s obvious that there isn’t anything obvious in plain sight so why don’t we try feeling around."
    show pov neutral at left
    show jac bored at Position(xpos=1300)
    show eff embarrassed_talk at Position(xpos=1500)
    eff "We have to look at every nook and cranny for a clue of some sort."
    show col embarrassed at Position(xpos=1000)
    show jac bored_talk at Position(xpos=1300)
    show eff bored at Position(xpos=1500)
    jac "This is disgusting, this is an alleyway may I remind you."
    show jac smirk at Position(xpos=1300)
    show eff bored_talk at Position(xpos=1500)
    eff "The fact that you don’t want to look too thoroughly makes the perfect deterrent for a secret hideout."
    show eff bored at Position(xpos=1500)
    show edw embarrassed_talk at Position(xpos=1800)
    edw "Effie’s right."
    edw "I’ve got some hand sanitizer in my bag, okay?"
    show col smirk_talk at Position(xpos=1000)
    show jac shocked at Position(xpos=1300)
    show edw neutral at Position(xpos=1800)
    col "I’m with Jacob but if it must be done, then done it shall be."
    show pov neutral_talk at left
    show col smirk at Position(xpos=1000)
    pov "Thanks guys."

    scene black
    with fade
    $ renpy.pause()
    "After feeling around and checking every nook and cranny..."

    scene bg streetalleyway_night
    with fade

    show pov shocked at left
    show col shocked_talk at Position(xpos=1000)
    show jac confused at Position(xpos=1300)
    show eff shocked at Position(xpos=1500)
    show edw neutral at Position(xpos=1800)
    col "Wait- everyone!"
    col "Check this out."
    show col shocked at Position(xpos=1000)
    show eff confused_talk at Position(xpos=1500)
    eff "What is it?"
    show pov  at left
    show col  at Position(xpos=1000)
    show jac smirk_talk at Position(xpos=1300)
    show eff confused at Position(xpos=1500)
    show edw shocked at Position(xpos=1800)
    jac "Why are you looking inside the dumpster?"
    show pov embarrassed at left
    show col smirk_talk at Position(xpos=1000)
    show jac bored at Position(xpos=1300)
    show edw smirk at Position(xpos=1800)
    col "Oh, I’m sorry. Maybe I should’ve checked the very obvious and clearly existing door that says ‘Secret Hideout’ on it."
    show pov  at left
    show col shocked_talk at Position(xpos=1000)
    col "C’mon."
    show pov shocked at left
    show col confused_talk at Position(xpos=1000)
    show jac confused at Position(xpos=1300)
    show edw confused at Position(xpos=1800)
    col "Look-"

    ## CG
    # View of inside the empty dumpster, there’s a hole and a ladder leading downwards.
    scene bg downthegarbagebin_1
    with fade

    edw "What the fuck?"
    edw "Who-"
    edw "Where?"

    jac "I’ve been to this part of town many times but never have I realized this was here."
    jac "Holey hell."
    jac "…"
    jac "See what I did there-"
    jac "Hole-"

    eff "Jacob."

    pov "There’s our way in, there’s not a single doubt about it."
    pov "I do wonder how long that’s been there."
    pov "Maybe Hitomi or Hazel knows something about this since they work along this strip."

    jac "I doubt it, though I’ll ask later anyway."

    col "…"
    col "So what now?"

    edw "Are we ready to go in?"

    ## Player gets a choice to go in now or not.

    "The next story sequence is quite long, would you like to proceed now?"

    ## MENU
    menu:
        "Go in now":
            pov "We should go in now."
            pov "Better now than when it’s too late."
            pov "Does anyone else have anything better to do right now?"
            pov "…"
            pov "No? Good, let’s go."

            $ main_story = 158

            jump lbl_not_quite_a_sewer

        "Go in later":
            pov "We found what we needed to find."
            pov "We’ll come back another time once we’ve all mentally prepared a little more."
            pov "Are we all in agreement?"

            "Everyone" "Yup."

            pov "Okay, I’ll text everyone and we’ll meet up at the hideout before heading here together."
            pov "Make sure everyone is ready to go at a moment’s notice."

            $ main_story = 157.5

            jump lbl_street_night_setup

label lbl_down_the_garbage_bin_ready:
    # MC, Jacob, Effie, Edward, and Cole are all present at the alleyway.
    ## SPRITE

    scene black
    with fade
    $ renpy.pause()
    "After calling everyone to meet at the alleyway..."

    scene bg streetalleyway_night
    with fade

    show pov smirk_talk at left
    show col confused at Position(xpos=1000)
    show jac embarrassed at Position(xpos=1300)
    show eff smirk at Position(xpos=1500)
    show edw embarrassed at Position(xpos=1800)
    with dissolve
    pov "Alright, gang."
    show pov embarrassed_talk at left
    show jac embarrassed at Position(xpos=1300)
    pov "Let's head down."
    show pov smirk_talk at left
    show col embarrassed at Position(xpos=1000)
    show eff smirk at Position(xpos=1500)
    pov "No objections, right?"
    show pov confused_talk at left
    show jac bored at Position(xpos=1300)
    pov "..."
    show pov embarrassed_talk at left
    show eff neutral at Position(xpos=1500)
    show edw neutral at Position(xpos=1800)
    pov "Okay, I'll go first."

    $ main_story = 158

    jump lbl_not_quite_a_sewer
