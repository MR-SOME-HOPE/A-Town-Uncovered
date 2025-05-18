label lbl_dude_wheres_my_hitomi:
    #[Comic Book Store, Afternoon - “Dude, Where's My Hitomi?”  - hitomi_path = 19]#17/17.5

    #-Scene is available two days after the previous scene-

    #-upon entering the comic book store the player notices that Hitomi isn’t in
    # the counter and has a little internal dialogue-

    #-Control returns to the player and he now has to enter the nerd cave and
    # talk to Lord Kevlamin in order to continue-

    #-upon clicking on Lord Kev the scene continues proper-

    #-MC, Crugeon, Davendithas and Lord Kev enter the scene-

    ## SPRITE START ##
    scene bg comicbookbackroom_day
    with fade
    show pov confused_talk at left
    show cru confused at Position(xpos=1000)
    show dav bored at Position(xpos=1400)
    show lor smirk at Position(xpos=1800)
    with dissolve
    pov "Hey guys, do you know where Hitomi is?"
    show pov embarrassed at left
    show cru bored_talk at Position(xpos=1000)
    ian "Greetings, [povname]."
    show pov confused at left
    show cru smirk at Position(xpos=1000)
    show dav neutral at Position(xpos=1400)
    dav "{i}*Nod of Hello*{/i}"
    show lor smirk_talk at Position(xpos=1800)
    lor "Ah! The minion of artistry of our noble retainer once again shows his face on our domains!"
    show pov embarrassed_talk at left
    show lor smirk at Position(xpos=1800)
    pov "Dude, I feel you fluctuate a ton in your fantasy speak and fancy word use, every time we meet."
    show pov bored_talk at left
    show cru smirk at Position(xpos=1000)
    pov "Either you go full-on with it and I barely understand you or you just sprinkle it in a little."
    show cru smirk_talk at Position(xpos=1000)
    show dav bored at Position(xpos=1400)
    show lor neutral at Position(xpos=1800)
    ian "It’s something you get used to and then you barely notice that it’s there afterwards."
    show pov embarrassed at left
    show cru neutral_talk at Position(xpos=1000)
    show lor smirk at Position(xpos=1800)
    ian "Just like with Davendithas’ physical communication."
    show pov bored at left
    show cru smirk at Position(xpos=1000)
    show lor  at Position(xpos=1800)
    dav "*Nod of Affirmation*"
    show lor neutral_talk at Position(xpos=1800)
    lor "Even for a talented wordsmith and master of the elvish, dwarvish, orcish and space octopusianic tongues such as myself, the struggles of the lexicon can be a challenge unlike any other!"
    show lor confused_talk at Position(xpos=1800)
    lor "Nevertheless, it is not a challenge I shy away from and I leap forth into its treacherous caress!"
    show lor smirk_talk at Position(xpos=1800)
    lor "Now, are you here to mock my manner of speech or did you want something?"
    show pov confused_talk at left
    show lor smirk at Position(xpos=1800)
    pov "Uhh… Yeah, I asked you if you had seen Hitomi, remember?"
    show pov confused at left
    show lor neutral_talk at Position(xpos=1800)
    lor "She indeed crossed the threshold of our domains by the hours of third breakfast with a quest to deliver upon a warrior of mighty steel to meet her upon the edge of the lands where the eyes of raw close upon the age of twilight."
    show pov bored_talk at left
    show cru smirk at Position(xpos=1000)
    show lor smirk at Position(xpos=1800)
    pov "…"
    pov "Translation, you guys?"
    show pov confused at left
    show cru smirk_talk at Position(xpos=1000)
    ian "She asked us to tell you that she would wait for you at the beach if you happened to show up today."
    show pov bored at left
    show cru smirk at Position(xpos=1000)
    show lor smirk at Position(xpos=1800)
    dav "*Nod of Affirmation*"
    show pov bored_talk at left
    pov "Great, thanks…"
    pov "Did she say anything else?"
    show pov bored at left
    show lor neutral_talk at Position(xpos=1800)
    lor "The maiden in question failed to further deliver quest information of any kind; however, it was easy to spot that a level 46 gremlin of confusion has casted upon her its maleficium of peculiarity as she embarked on her quest outside the holy domain."
    show pov confused_talk at left
    show cru confused at Position(xpos=1000)
    show lor neutral at Position(xpos=1800)
    pov "…"
    pov "Ian?"
    show pov confused at left
    show cru embarrassed_talk at Position(xpos=1000)
    ian "She didn’t say anything else but there was something weird about her as she left the store."
    show pov bored_talk at left
    show cru embarrassed at Position(xpos=1000)
    pov "Could you tell what it was?"
    show pov bored at left
    show lor confused_talk at Position(xpos=1800)
    lor "My Dark Elven eyes failed to detect so."
    show pov smirk at left
    show cru smirk_talk at Position(xpos=1000)
    show lor neutral at Position(xpos=1800)
    ian "I couldn’t tell either, could you Davendithas?"
    show pov confused at left
    show cru smirk at Position(xpos=1000)
    show dav neutral at Position(xpos=1400)
    dav "{i}*Nod of Affirmation*{/i}"
    show pov confused_talk at left
    show dav bored at Position(xpos=1400)
    pov "Really? What was it?"
    show pov confused at left
    show dav neutral at Position(xpos=1400)
    dav "*Series of Very Complex Gestures You Are Not Able to Follow*"
    show pov shocked at left
    show cru confused_talk at Position(xpos=1000)
    show dav bored at Position(xpos=1400)
    ian "Really?"
    show cru shocked_talk at Position(xpos=1000)
    show lor confused at Position(xpos=1800)
    ian "My, I never would have guessed…"
    show pov bored at left
    show cru embarrassed_talk at Position(xpos=1000)
    show lor smirk at Position(xpos=1800)
    ian "In some ways I’m glad for her but it’s clear she is going through a lot."
    show cru embarrassed at Position(xpos=1000)
    show lor confused_talk at Position(xpos=1800)
    lor "Once again, Davendithas dazzles us with his skill at reading the hearts of others and proves to be a master of insight and the true wielder of knowledge of the female psyche."
    lor "For this show of skill and talent, I shall reward thee with the honor of first pick during our next draft tournament."
    show pov smirk at left
    show cru confused at Position(xpos=1000)
    show dav neutral at Position(xpos=1400)
    show lor neutral at Position(xpos=1800)
    dav "*Fist Pump of Self Celebration*"
    show pov bored_talk at left
    pov "Uhhh… Anyone care to translate?"

    #-The three nerds all smile-
    show pov smirk at left
    show cru neutral at Position(xpos=1000)
    show lor neutral at Position(xpos=1800)
    ian "Nah, we are just fucking with you."
    show pov confused at left
    show cru smirk at Position(xpos=1000)
    show dav bored at Position(xpos=1400)
    show lor neutral_talk at Position(xpos=1800)
    lor "A devilish ploy to mess with an unsuspecting opponent, my congratulations go to you again, Knight Davendithas!"
    show dav neutral at Position(xpos=1400)
    show lor neutral at Position(xpos=1800)
    dav "*Nod of Appreciation*"
    show pov confused_talk at left
    show cru confused at Position(xpos=1000)
    show lor smirk at Position(xpos=1800)
    pov "Wait, so do you actually know what was weird about her?"
    show pov confused at left
    show dav bored at Position(xpos=1400)
    dav "{i}*Shrug of Lack of Knowledge*{/i}"
    show pov bored_talk at left
    show cru neutral at Position(xpos=1000)
    pov "Great…"
    pov "Well, thanks anyway I suppose…"
    show pov bored at left
    show lor confused_talk at Position(xpos=1800)
    lor "You may now leave our domains at your earliest convenience."
    show pov bored_talk at left
    show cru smirk at Position(xpos=1000)
    pov "Yeah, yeah, I’m going…"

    #-MC exits the scene-
    scene black with fade
    $ renpy.pause()
    "At the beach..."

    $ townmap_enabled = 0

    $ hitomi_path = 17.6

    #=SCENE END=
    jump lbl_beachmain_day_setup
