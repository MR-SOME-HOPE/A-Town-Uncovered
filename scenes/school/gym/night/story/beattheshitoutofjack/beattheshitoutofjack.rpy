## Beat the Shit out of Jack ##
label lbl_beat_the_shit_out_of_jack:
    default beattheshitoutofjack_lose = 0

    scene bg schoolgymdoor_night
    with fade
    show pov angry
    with dissolve
    pov "{i}This has to end...{/i}"
    pov "{i}Jack isn't going to listen to reason, so I'm going to have to do this the old fashioned way.{/i}"
    pov "{i}It's my fault Miss Allaway was dragged into this mess in the first place so it's my job to get her out...{/i}"
    show pov sad
    pov "{i}As long as the rest of the guys don't gang up on me I should be fine.{/i}"
    show pov confused
    pov "{i}Question now is, am I ready to do this in the first place?{/i}"
    show pov embarrassed
    pov "{i}Worst comes to worst, I can just pretend it's a casual match on the fight club, got too cocky and lost.{/i}"
    pov "{i}But if I go all out I won't be able to stop until it's over...{/i}"
    show pov angry
    pov "{i}Fuck... are you ready, [povname]?{/i}"

    menu:
        "Let's kick his ass":
            pov "{i}Alright, you can do this. Let's fuck his shit up.{/i}"

            jump lbl_beat_the_shit_out_of_jack_2
        "Let's do it another time":
            if skill_strmax <= 15:
                pov "{i}Probably a good idea to get more in shape...{/i}"
                pov "{i}I'll head inside and build up my strength but I won't engage Jack just yet...{/i}"

                $ renpy.notify("New Objective: Increase your Max Strength Limit")

                $ missallaway_path = 19.1

                jump lbl_schoolgym_night_setup

            elif skill_str <= 15:
                pov "{i}I should probably rest up a little.{/i}"
                pov "{i}I'm just a little weak after today.{/i}"
                pov "{i}As much as I think it's floozy, I should ask Grundle Sam if he has a totem that'll help me.{/i}"
                pov "{i}I may need as much help as I can get.{/i}"
                pov "{i}Odin, I'm talking about you too.{/i}"
                $ renpy.notify("New Objective: Increase your Max Strength Points")

                jump lbl_schoolyard_night_setup

            else:
                pov "{i}Damnit, I can't do it.{/i}"
                pov "{i}fuckin' syched myself up for tonight-{/i}"
                pov "{i}Damn... maybe tomorrow night.{/i}"
                pov "{i}What am I frikkin' afraid of.{/i}"
                $ renpy.notify("New Objective: Come back another time")

                jump lbl_schoolyard_night_setup

label lbl_beat_the_shit_out_of_jack_2:

    scene bg schoolgym_nightlightson
    with fade
    show pov angry at left
    with dissolve
    show jack smirk_talk at right
    with dissolve
    jack "Well, look what the bitch dragged in."
    jack "And here I was wondering when you were going to show up."
    jack "I knew it was about time that she'd cry to you about me."
    show jack confused_talk at right
    jack "She's so fragile, I don't know how long she'll last in this line of work."
    show pov angry_talk at left
    show jack confused at right
    pov "Shut the fuck up, you cocksucker."
    show jack smirk at right
    pov "What are you doing to her?! What the fuck do you have her doing?!"
    show pov angry at left
    show jack smirk_talk at right
    jack "Geez Louise, calm your ass down."
    jack "I'm not fucking her if that's what you're wondering."
    jack "I don't know what you see in her but she's definitely not my type."
    jack "But hey, whatever floats your boat, right?"
    jack "Some of us have more mommy issues than others."
    show pov angry_talk at left
    show jack confused at right
    pov "What. Are. You. Doing. To. Her?!"
    show pov angry at left
    show jack confused_talk at right
    jack "Keep going, you're gonna burst a neck vein with how tense you're being."
    show pov angry at left
    show jack confused at right
    show coa angry_talk
    coa "Now listen here, you pair of pussies."
    coa "This place is for men, not drama queens."
    coa "So whatever issues you have outside the circle, you better take it outside!"
    show jack smirk_talk at right
    show coa angry
    jack "I wonder what face she is going to make when I tell her I beat your ass tonight!"
    show pov angry_talk at left
    show jack smirk at right
    pov "And I wonder what deformed face you'll end up with once I kick it back into your skull!"
    show pov angry at left
    show jack bored at right
    show coa angry_talk
    coa "Did you two idiots not hear me?!"
    coa "The moment one of you does anything without my say so is the moment the two of you are suspended from this club!"
    show jack angry at right
    coa "Now quit yapping and get the fuck in that circle."
    coa "You came here to get your knuckles bloody and your eye black, not test which of you dickless losers has the bigger dick."
    coa "Now fight!"

    scene bg beattheshitoutofjack_1
    with fade
    $ renpy.pause()
    if skill_str <= 15 and skill_sta <= 15:
        show bg beattheshitoutofjack_2
        with hpunch
        $ renpy.pause()
        scene black
        with fade
        $ renpy.pause()
        show bg beattheshitoutofjack_5
        with dissolve
        $ renpy.pause(0.3,hard=True)
        scene black
        with fade
        $ renpy.pause()
        show bg beattheshitoutofjack_6
        with dissolve
        $ renpy.pause(0.6,hard=True)
        scene black
        with fade
        $ renpy.pause()
        show bg beattheshitoutofjack_7
        with dissolve
        bro "Hey..."
        bro "Yo, little bro?"
        show bg beattheshitoutofjack_8
        bro "You still among the living?"
        show bg beattheshitoutofjack_9
        pov "M-Mmm..."
        pov "Brock?"
        show bg beattheshitoutofjack_10
        bro "Hey dude!"
        show bg beattheshitoutofjack_11
        bro "Don't scare me like that, man!"
        show bg beattheshitoutofjack_8
        bro "Here I was starting to think I was going to have to call an ambulance."
        show bg beattheshitoutofjack_9
        pov "What happened?"
        show bg beattheshitoutofjack_11
        bro "Jack got you on the jaw after a few blows and pounded your chest a bit, it was lights out before you hit the floor so at least be thankful about that."
        show bg beattheshitoutofjack_12
        pov "Where is everybody?"
        show bg beattheshitoutofjack_11
        bro "It's the morning, ma dude."
        bro "Well, matches were already ending when you showed up so once you got knocked out the coach dispersed us for the night, I stayed behind to try and help you get up."
        show bg beattheshitoutofjack_2
        pov "Really?"
        show bg beattheshitoutofjack_10
        bro "Effie asked me to look after you once she heard you were coming here."
        show bg beattheshitoutofjack_9
        pov "Oh..."
        pov "Well... I'm not sure how to feel about that part."
        pov "I'll be sure to thank her when I see her."
        show bg beattheshitoutofjack_8
        bro "I've known her for a few years and she really care about her friends."
        bro "Plus, I'm not about to let a fellow fighter just spend the whole day passed out in the gym."
        show bg beattheshitoutofjack_10
        bro "You managed to knock me out at least once already so you got a ton of respect on my end."
        show bg beattheshitoutofjack_9
        pov "Thanks, Brock."
        pov "That means a lot coming from you..."
        show bg beattheshitoutofjack_12
        pov "And I guess, sorry for beating you?"
        show bg beattheshitoutofjack_11
        bro "Still, I'm kind of surprised you got beaten by Jack."
        bro "He's good, stronger than he looks but I can still wipe the floor with him with little effort."
        bro "But to be fair, he has learnt a few new tricks. He's definitely a slippery bastard."
        show bg beattheshitoutofjack_12
        pov "No kidding. I thought I could take him out with a well-timed hook."
        show bg beattheshitoutofjack_11
        bro "It was just landing the shot that you seemed to have a problem with."
        show bg beattheshitoutofjack_8
        bro "Some nights you have it good, and some you have it bad."
        bro "Tonight was one of your bad night nights."
        show bg beattheshitoutofjack_7
        bro "Listen..."
        bro "I'm going to give it to you straight, that whole fight was kind of sad."
        show bg beattheshitoutofjack_13
        pov "Ouch..."
        show bg beattheshitoutofjack_7
        bro "Hey, no offence or whatever bullshit."
        show bg beattheshitoutofjack_11
        bro "I don't know what's happening between you two, but if you want to beat up Jack, you're going to have to work a little on your speed."
        bro "Do you have a lucky charm?"
        show bg beattheshitoutofjack_9
        pov "I have a totem...? Does that count?"
        show bg beattheshitoutofjack_10
        bro "Only if you believe, little bud."
        show bg beattheshitoutofjack_8
        bro "Can you stand up?"
        show bg beattheshitoutofjack_9
        pov "I think so..."
        show bg beattheshitoutofjack_10
        bro "Good!"
        bro "Let's go, I'll help you get home."
        show bg beattheshitoutofjack_9
        pov "I appreciate it, seriously, dude. My head is still fuckin' vibrating"
        show bg beattheshitoutofjack_10
        bro "Don't even sweat about it, little bro."
        show bg beattheshitoutofjack_8
        bro "Just don't pass out on me on the way, ok?"
        show bg beattheshitoutofjack_9
        pov "No promises."
        $ beattheshitoutofjack_lose = 1
        scene black
        with fade
        $ renpy.pause()
        "After driving you back home..."
        scene bg myhousefront_day
        with fade
        $ renpy.pause()
        $ gtime = 0
        if day <= 5:
            $ day += 1
        else:
            $ day = 0
        call lbl_next_date
        call lbl_skill_items

        jump lbl_myhousefront_day_setup
    else:
        show bg beattheshitoutofjack_4
        with vpunch
        pov "How's it feel, you jackass?!"
        show bg beattheshitoutofjack_3
        coa "Alright, alright! That's enough, big guy!"
        show bg beattheshitoutofjack_4
        pov "You better stay away from her, or I'll come back - and you won't be getting up next time, you piece of shit!"
        scene bg schoolgym_nightlightson
        show bro confused_talk flip at left
        show pov angry at Position(xpos=700)
        show coa bored at right
        bro "Bro, chill!"
        bro "He's down! He's out of it!"
        show bro shocked flip at left
        show pov angry_talk at Position(xpos=700)
        pov "Go near her again, motherfucker!"
        pov "I fucking dare you!"
        show bro bored flip at left
        show pov angry at Position(xpos=700)
        show coa angry_talk at right
        coa "Alright, I've had enough of this dumbass."
        show coa bored_talk at right
        coa "Get him out of my gym. He's done for tonight!"
        show bro embarrassed_talk flip at left
        show coa bored at right
        bro "Right away, Coach."

        jump lbl_down_to_his_level
