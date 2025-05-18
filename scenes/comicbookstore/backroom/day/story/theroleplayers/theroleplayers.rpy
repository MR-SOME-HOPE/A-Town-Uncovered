## The Roleplayers ##
label lbl_the_roleplayers:
    show jac neutral_talk flip at Position(xpos=600)
    with dissolve
    show pov embarrassed at left
    with dissolve
    show lor angry at right
    with dissolve
    jac "Hey guys, meet my new friend, [povname]."
    show jac bored flip at Position(xpos=600)
    show pov bored at left
    show lor angry_talk at right
    idk "Jacob! Who is this fiend? How dare you bring an outsider into our dungeon of solitude and sanctuary."
    show jac smirk_talk flip at Position(xpos=600)
    show pov neutral at left
    show lor bored at right
    jac "Look, Kev. He's with me - new kid from uni. I thought I'd bring him here to meet some of you guys. Maybe he'll grow on you."
    show jac smirk flip at Position(xpos=600)
    show lor bored_talk at right
    idk "I have my suspicions but an ally of Jacob is an ally of ours."
    show jac smirk_talk flip at Position(xpos=600)
    show lor bored at right
    jac "Badass. [povname], this is Kev."
    show jac bored flip at Position(xpos=600)
    show pov embarrassed at left
    show lor bored_talk at right
    lor "Lord Kevlamin to you peasant. You shall refer to me as your Lord and you shall respect my kingdom."
    show jac bored_talk flip at Position(xpos=600)
    show lor angry at right
    ## 18 Years Old
    jac "He likes to roleplay." # and he's 20."
    show jac bored flip at Position(xpos=600)
    show lor angry_talk at right
    lor "I told you! It's not roleplay. It's a second life away from the terrors of what you peasants call reality."
    show jac bored_talk flip at Position(xpos=600)
    show lor angry at right
    jac "Yeah, whatever."
    jac "These guys are alright though you would never find me playing along with their dorkistry."
    show jac bored flip at Position(xpos=600)
    show lor angry_talk at right
    lor "I can hear you, Jacob."
    show jac bored_talk flip at Position(xpos=600)
    show lor angry at right
    jac "Shove a Twinky up yours, pal."
    hide lor angry
    show jac smirk_talk flip at Position(xpos=600)
    jac "Still love you, bro."
    show jac neutral_talk flip at Position(xpos=600)
    show pov neutral at left
    show cru bored at right
    ## 19 Years Old
    jac "This here's Crugeon, Crug for short." # He's 21 years old."
    show jac neutral flip at Position(xpos=600)
    show cru bored_talk at right
    cru "My real name is Ian. I didn't really get to choose my roleplayer name. It was ‘blessed' upon me by Lord Kevlamin."
    show jac smirk_talk flip at Position(xpos=600)
    show cru bored at right
    jac "It's a nice name, very strong, manly name."
    show jac smirk flip at Position(xpos=600)
    show pov embarrassed at left
    show cru bored_talk at right
    cru "I hate this name."
    show cru embarrassed at right
    lor "Look Crug, if you hate the name, why don't you go whine about it elsewhere and forever be banished."
    show jac neutral flip at Position(xpos=600)
    cru "..."
    show cru embarrassed_talk at right
    cru "It's nice to meet you..."
    show pov embarrassed_talk at left
    show cru neutral at right
    pov "[povname]."
    show pov embarrassed at left
    show cru neutral_talk at right
    cru "[povname]."
    hide cru neutral_talk
    show jac neutral_talk flip at Position(xpos=600)
    show pov neutral at left
    jac "And lastly but not leastly."
    show jac neutral_talk flip at Position(xpos=600)
    show dav neutral at right
    ## 18 Years Old
    jac "This faceless piece of work right here is who we all mutually agree to call, Davendithas." # He's... in his early 20s, I can't remember."
    show jac neutral flip at Position(xpos=600)
    show pov neutral_talk at left
    pov "Davendithas, what a mouthful. Haha, it's nice to meet you."
    show pov neutral at left
    dav "..."
    show pov bored at left
    pov "..."
    show pov neutral_talk at left
    pov "I said it's nice to meet you."
    show pov neutral at left
    dav "..."
    show pov confused_talk at left
    pov "It's nic- can he hear me with that on?"
    show jac neutral_talk flip at Position(xpos=600)
    show pov confused at left
    jac "Perfectly. He just doesn't talk. I guess he's in character? Who knows, he just showed up like that one day and Kev adopted him like a stray puppy."
    show jac neutral flip at Position(xpos=600)
    show pov bored_talk at left
    pov "Huh... I guess that's unsettling."
    show jac neutral_talk flip at Position(xpos=600)
    show pov bored at left
    jac "Don't worry, he's harmless. Pretty chill person to open up to and cry on his shoulder if need be."
    show jac neutral flip at Position(xpos=600)
    show pov confused_talk at left
    pov "You've done that with him?"
    show jac neutral_talk flip at Position(xpos=600)
    show pov bored at left
    jac "Haters gonna hate."
    hide dav neutral
    jac "Anyways. I'm gonna pick up my fap material and head on home. Stay and mingle if you wish."
    show pov embarrassed at left
    jac "Hey Kev!"
    hide jac neutral talk
    show jac neutral flip at Position(xpos=600)
    show lor bored_talk at right
    lor "What is it that you desire?"
    show jac neutral_talk flip at Position(xpos=600)
    show lor confused at right
    jac "[povname] is interested in this card game that you guys play."
    show jac smirk_talk flip at Position(xpos=600)
    jac "Aren't you, [povname]?"

    menu:
        "I like games.":
            if lordkevlamin_points <= 9:
                $ lordkevlamin_points += 1
            else:
                $ lordkevlamin_points = 10
            $ renpy.notify("Relationship with Lord Kevlamin increased.")
            show jac neutral flip at Position(xpos=600)
            show pov neutral_talk at left
            show lor neutral at right
            pov "Yeah, actually. I like games."
            show pov neutral at left
            show lor neutral_talk at right
            lor "Hmm, that's excellent to hear, [povname]. I think Jacob's right, you may actually grow on me."
            lor "Come, I'll show you the basics, it's actually quite simple."

            jump lbl_the_roleplayers_end
        "I'm not into that sort of thing.":
            show jac neutral flip at Position(xpos=600)
            show pov embarrassed_talk at left
            show lor bored at right
            pov "Actually, I'm not really into that sort of thing."
            show pov sad at left
            show lor angry_talk at right
            lor "You dare insult our game?"
            show pov sad_talk at left
            show lor angry at right
            pov "No, no. I didn't insult your game, I was just sayin-"
            show pov bored at left
            show lor bored_talk at right
            lor "Come, let me show you anyway. Allow me to persuade you into our culture."

            jump lbl_the_roleplayers_end

label lbl_the_roleplayers_end:

    scene black
    with fade
    "A few minutes later..."

    scene bg comicbookbackroom_day
    with fade
    show pov neutral at left
    with dissolve
    show lor neutral_talk at right
    with dissolve
    lor "And that's how you play Harem Protector."
    show pov smirk_talk at left
    show lor neutral at right
    pov "This game's actually not all that bad."
    show pov neutral at left
    show lor neutral_talk at right
    lor "It's solely luck based with a pinch of strategy."
    show pov neutral_talk at left
    show lor neutral at right
    pov "I can get into it pretty easily."
    show pov neutral at left
    show lor smirk_talk at right
    lor "Without even breaking a sweat. Come talk to any of us if you want to play anytime. We all rank differently and play with a different deck."
    show pov smirk_talk at left
    show lor smirk at right
    pov "You got it, my Lord."
    $ main_story = 20
    $ renpy.notify("New Contacts: Lord Kevlamin, Crugeon, Davendithas")
    if main_story == 20 and nextday_ajob == 1:
        $ renpy.pause(3,hard=True)
        $ renpy.notify("New Objective: Get Back Home and Talk to Mom in the Afternoon")
    else:
        pass
    $ gtime = 1

    jump lbl_comicbookbackroom_day_setup
