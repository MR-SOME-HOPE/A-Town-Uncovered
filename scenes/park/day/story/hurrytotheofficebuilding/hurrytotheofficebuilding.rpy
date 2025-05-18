## Hurry To The Office Building
label lbl_hurry_to_the_office_building:
    if not already_in_sexworld:
        "Emerging from the lake, You strip off your soaking wet clothes as you make your way up to the other Edward and Jacob..."
    else:
        scene black
        with fade
        "You strip off your clothes to blend in with the current dimension."
    
    scene bg park_day
    with fade
    show povn angry at left
    show jaccm bored at Position(xpos=1200)
    show edwcm shocked_talk at Position(xpos=1700)
    with dissolve
    edw "[povname]!"
    show edwcm bored_talk
    edw "Or should I say, [povname]."
    
    show povn bored_talk
    show jaccm confused
    show edwcm bored
    pov "Other Edward."
    pov "Other Jacob."

    show povn bored
    show jaccm confused_talk
    jac "Wow, other Jacob?"
    jac "That hurts coming from the other [povname]."

    show povn confused_talk
    show jaccm confused
    pov "Did the other me go through?"

    show povn bored
    show jaccm bored
    show edwcm bored_talk
    edw "Yes, we’ve sent him off to try and stop the invasion from your side."

    show povn confused_talk
    show edwcm bored
    pov "Where is this coming from, the TRC building?"
    
    show povn bored
    show edwcm bored_talk
    edw "Exacto."
    show povn angry
    edw "That’s where Effie is being held captive too."
    edw "I saw her while I was there not too long ago."
    edw "No one saw me catching her being carried away though."
    edw "Xina has lost her shit."
    edw "I overheard her ranting and went on these crazy tangents about things falling out of order."
    edw "Something might’ve cracked in her and she’s moved 10 steps ahead."

    show povn angry_talk
    show edwcm bored
    pov "I’ll go, save Effie, and stop her madness."
    pov "I’ll force her to cease the attack by any means."
    
    show povn angry
    show edwcm bored_talk
    edw "Good."

    show povn bored_talk
    show jaccm confused
    show edwcm bored
    pov "What’s up with the getup, by the way?"

    show povn bored
    jac "Hm?"

    show povn bored_talk
    pov "The masks."

    show povn bored
    show jaccm confused_talk
    jac "It’s our disguises? We can't risk anyone knowing we're doing this."

    show jaccm confused
    pov "..."
    show povn confused_talk
    pov "The other yous’ aren’t wearing disguises."

    show povn bored
    show jaccm smirk_talk
    jac "And that’s what makes us smarter."

    show povn bored_talk
    show jaccm confused
    pov "I gotta go quick-"
    pov "I can’t waste anymore time."

    show povn bored
    show edwcm bored_talk
    edw "I’m gonna keep trying to connect with the other Edward, as long as we find the right frequency together."
    edw "It’s tricky-"

    show jaccm bored_talk
    show edwcm angry
    jac "I’ll stay by in case Edward gets attacked or something, I believe you got this, [povname]."

    show povn bored_talk
    show jaccm bored
    pov "Thanks, guys."
    
    show jaccm angry_talk
    jac "GO!"

    $ main_story = 127

    jump lbl_in_the_control_room
