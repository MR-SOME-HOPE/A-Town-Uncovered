## Before The Beach Party
label lbl_before_the_beach_party:
    #-Scene takes place on that week’s friday when Mc gets to Effie’s house only to find Effie’s Dad waiting for him-
    ## SPRITEWORK

    show pov neutral at left
    show effdad angry_talk at right
    with dissolve
    effdad "Ah, you are here. About time."
    show pov shocked_talk at left
    show effdad bored at right
    pov "Y-Yes, hello, sir..."
    show pov embarrassed_talk at left
    show effdad confused at right
    pov "Is Effie ready yet?"
    show pov embarrassed at left
    show effdad confused_talk at right
    effdad "Shouldn’t take too long now. Now, blow into this thing."
    show pov embarrassed_talk at left
    show effdad bored at right
    pov "Are you actually using a breathalyzer on me, before we even get to the party?"
    show pov embarrassed at left
    show effdad confused_talk at right
    effdad "You are taking my little girl out partying. Gotta make sure you aren’t buzzed already."
    show effdad bored_talk at right
    effdad "Now blow in it, if you wanna take her anywhere."
    show pov bored_talk at left
    show effdad bored at right
    pov "Ugh, fine..."
    show pov smirk_talk at left
    show effdad smirk at right
    pov "Happy?"
    show pov smirk at left
    show effdad confused_talk at right
    effdad "Hmm... Nothing on you for now."
    show pov bored at left
    show effdad bored_talk at right
    effdad "Hope you remember, I’m serious about testing you with it when you come back."
    show pov bored_talk at left
    show effdad bored at right
    pov "You’ll find nothing on it now, and neither will you then."
    show pov bored at left
    show effdad bored_talk at right
    effdad "Good."


    #-Effie appears on the scene-

    show pov embarrassed at left
    show effdad confused at Position(xpos=1500)
    show eff neutral_talk at Position(xpos=1600)
    with dissolve
    eff "Hey, [povname]. Ready to go?"
    show effdad bored_talk at Position(xpos=1500)
    show eff bored at Position(xpos=1600)
    effdad "You two remember the rules?"
    show effdad bored at Position(xpos=1500)
    show eff bored_talk at Position(xpos=1600)
    eff "Yes, Dad..."
    show effdad bored_talk at Position(xpos=1500)
    show eff bored at Position(xpos=1600)
    effdad "Alright, I’ll be waiting, then."
    show pov embarrassed at left
    show effdad smirk_talk at Position(xpos=1500)
    effdad "You two, remember not to have too much fun."


    #-Effie’s Dad leaves the scene-

    show pov confused_talk at left
    show eff bored at right
    hide effdad
    with dissolve
    pov "Really wasn’t expecting him to actually pull the breathalyzer out on me, but I guess I shouldn’t be surprised about anything regarding him, anymore."
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "Yeah, I’m really sorry about that..."
    show pov embarrassed_talk at left
    show eff embarrassed at right
    pov "It’s okay. Are you though?"
    show pov confused at left
    show eff embarrassed_talk at right
    eff "Y-Yeah, just still can’t shake off the bad feeling I told you about."
    show pov confused_talk at left
    show eff confused at right
    pov "I can’t blame you, but tell you what: even with this, I’ll work hard so that we have fun tonight."
    show pov smirk_talk at left
    show eff neutral at right
    pov "It’s our second date, so let’s spend some good time together, alright?"
    show pov neutral at left
    show eff neutral_talk at right
    eff "Yeah, you are right."
    show eff embarrassed_talk at right
    eff "Sorry for bringing the mood down."
    show pov neutral_talk at left
    show eff embarrassed at right
    pov "I have an idea on how we can make the mood a little better~"
    show pov neutral at left
    show eff smirk_talk at right
    eff "Oh? Do tell."


    #-MC kisses Effie right then and there-

    show pov neutral at left
    show eff smirk_talk at right
    eff "Heh, smooth moves there~"
    show eff neutral_talk at right
    eff "Definitely made my night better. Now let’s have some fun."
    show pov smirk_talk at left
    show eff neutral at right
    pov "That’s my Effie!"


    #-Mc and Effie leave the scene only for Effie’s dad to return to it looking displeased as we then fade to black and immediately follow to the next scene-

    scene black
    with fade
    $ renpy.pause()
    "At the beach..."

    $ effie_path = 17

    jump lbl_beach_party_prelude
