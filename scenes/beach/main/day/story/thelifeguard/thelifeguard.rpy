## The Lifeguard ##
label lbl_the_lifeguard:
    show pov neutral at left
    with dissolve
    pov "{i}This beach looks gorgeous!{/i}"
    pov "..."
    show pov embarrassed at left
    pov "{i}Is this a nudist beach?!{/i}"
    pov "{i}Why is there a nudist beach, just out here, for anyone to come to?{/i}"
    show vio neutral_talk at right
    with dissolve
    idk "Hey! Sorry, but I can't help but notice that you're just standing there, staring at all these people."
    show pov embarrassed_talk at left
    show vio neutral at right
    pov "Oh, I was ju-"
    show pov sad at left
    show vio neutral_talk at right
    idk "I mean, forgive me for making you feel like you're a pervert. I just don't think I've seen you around before."
    show pov bored at left
    idk "I would know: I'm very good with faces and especially brilliant with bodies."
    show vio angry_talk at right
    idk "Are you staring at my boobs?"
    show pov sad_talk at left
    show vio angry at right
    pov "W-What? No."
    show pov sad at left
    show vio smirk_talk at right
    idk "It's okay, feel free to eye-fuck me, anytime you want: That's what anyone ever comes down here for."
    show pov embarrassed at left
    idk "Well, that, and a lot more."
    show vio smirk at right
    pov "..."
    show vio neutral_talk at right
    vio "Oh, excuse my manners, I'm Violette; the town's one and only lifeguard."
    show vio bored at right
    pov "..."
    show vio bored_talk at right
    vio "Okay, so I did say it was okay to eye-fuck me, but, can you please hold a conversation?"
    vio "The changing rooms are over there. Go change out of your clothes and come talk to me when we're equally naked."
    show pov embarrassed_talk at left
    show vio neutral at right
    pov "Alright, give me a second."
    $ violette_path = 1
    $ renpy.notify("New Contact: Violette")
    $ renpy.pause(3,hard=True)
    $ renpy.notify("New Objective: Change out of your Clothes")
    $ renpy.pause(3,hard=True)

    jump lbl_beachmain_day_setup
