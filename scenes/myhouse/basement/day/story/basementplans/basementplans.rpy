## Basement Plans ##
label lbl_basement_plans:
    default basementplans_promise = 0

    scene bg mybasement_lightsonmessy
    with fade
    show pov bored at left
    with dissolve
    show sis sad_talk at right
    with dissolve
    sis "W-"
    show pov bored_talk at left
    show sis sad at right
    pov "Yup"
    show pov bored at left
    show sis sad_talk at right
    sis "Wher-"
    show pov bored_talk at left
    show sis sad at right
    pov "Just as I suspected."
    show pov bored at left
    show sis sad_talk at right
    sis "Where's the booty?"
    show pov confused_talk at left
    show sis sad at right
    pov "Did you really expect to find treasure in a basement?"
    show pov bored at left
    show sis sad_talk at right
    sis "It's not impossible, [povname]. We could've been the 0.0001 percent."
    show pov bored_talk at left
    show sis sad at right
    pov "I guess today was just not that day."
    show pov bored at left
    show sis sad_talk at right
    sis "{i}*Sigh*{/i}"
    show sis bored_talk at right
    sis "What do we have here."
    show pov confused_talk at left
    show sis bored at right
    pov "The water heater."
    show pov confused at left
    show sis bored_talk at right
    sis "Looks to be some empty boxes."
    show pov bored_talk at left
    show sis bored at right
    pov "Cardboard."
    show pov bored at left
    show sis bored_talk at right
    sis "Just crap scattered everywhere."
    show pov neutral_talk at left
    show sis bored at right
    pov "At least we now know what was behind this door."
    show pov neutral at left
    sis "..."
    show pov confused at left
    show sis bored_talk at right
    sis "We've really gotta clean this up if we wanna utilize this room."
    show pov confused_talk at left
    show sis confused at right
    pov "You actually want to use this cold, lifeless basement?"
    show pov confused at left
    show sis smirk_talk at right
    sis "Why the hell not? Once it's all spruced up, it'll be pretty cozy."
    show pov confused_talk at left
    show sis smirk at right
    pov "Are you going to find some furniture?"
    show pov sad_talk at left
    pov "I'm on minimum wage, I can't really afford to buy furniture left and right."
    show pov confused_talk at left
    show sis confused at right
    pov "Besides, my room is more than comfortable for myself."
    show pov embarrassed at left
    show sis neutral_talk at right
    if winc == 0:
        sis "Aww, c'mon. Don't you want a [povsisrole] lounge?"
        sis "We can totally make this our own! It's not like [dadname]'s ever home to turn it into a man cave."
    else:
        sis "Aww, c'mon. Don't you want a sibling lounge?"
        sis "We can totally make this our own! It's not like Dad's ever home to turn it into a man cave."
    show pov confused_talk at left
    show sis neutral at right
    pov "I don't kn-"
    show pov confused at left
    show sis embarrassed_talk at right
    sis "Just like the old days, [povname]."
    show sis neutral_talk at right
    sis "Remember our old playhouse?"
    show pov shocked at left
    if winc == 0:
        sis "The one [dadname] built for us for our 5th birthday?"
    else:
        sis "The one Dad built for us for our 5th birthday?"
    show pov embarrassed_talk at left
    show sis neutral at right
    pov "Yeah..."
    show pov neutral_talk at left
    show sis smirk at right
    pov "We sorta grew out of that playhouse quite quickly."
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "But weren't those years fun?"
    show pov shocked at left
    show sis embarrassed_talk at right
    if winc == 0:
        sis "My memory's a little blurry but I vividly recall [missus] scolding us for playing doctor."
    else:
        sis "My memory's a little blurry but I vividly recall Mom scolding us for playing doctor."
    show pov shocked_talk at left
    show sis embarrassed at right
    pov "Oh my God! I remember that too! That was-"
    show pov embarrassed_talk at left
    show sis smirk at right
    pov "Sorta embarrassing and confusing back then."
    show pov embarrassed at left
    show sis smirk_talk at right
    sis "It took us a few years to clue in as to why that was so wrong."
    show pov neutral_talk at left
    show sis smirk at right
    pov "Kids really are innocent little fuckers."
    show pov neutral at left
    show sis confused at right
    sis "..."
    show pov bored at left
    show sis confused_talk at right
    if winc == 0:
        sis "You do {i}know{/i} why it's wrong for [povsisrole]s to play doc-"
    else:
        sis "You do {i}know{/i} why it's wrong for siblings to play doc-"
    show pov bored_talk at left
    show sis neutral at right
    pov "Yes, [sister]. I know why, you don't need to spell it out for me."
    show pov bored at left
    show sis neutral_talk at right
    sis "Oh, good. Hehehe, just checking you aren't behind on your sex-ed."
    show pov bored_talk at left
    show sis neutral at right
    pov "Jeez, dude."
    show pov confused at left
    show sis smirk_talk at right
    sis "Anyway, what do you say?"
    show pov confused_talk at left
    show sis bored at right
    pov "We still have question of what are we gonna furnish this place with."
    show pov confused at left
    show sis bored_talk at right
    sis "Bro, bro... bro."
    show pov bored at left
    sis "Bro."
    show pov confused at left
    show sis neutral_talk at right
    sis "Look around you, we've got boxes for days."
    sis "Let's build a fuckin' cardboard box fort!"
    show pov confused_talk at left
    show sis shocked at right
    pov "You can't be serious."
    show pov bored at left
    show sis shocked_talk at right
    sis "What's wrong with a fuckin' cardboard box fort?"
    show pov bored_talk at left
    show sis confused at right
    pov "The problem is-"
    show pov bored at left
    show sis smirk_talk at right
    sis "There is no problem. You're just closed-minded about the idea."
    show pov confused_talk at left
    show sis confused at right
    pov "Aren't you the one that wanted to grow up and be treated like an adult?"
    show pov bored at left
    show sis smirk_talk at right
    sis "I think you're mistaking me for yourself there, [povname]."
    show sis embarrassed_talk at right
    if winc == 0:
        sis "Look, I know it may come as a shock to you, but just because we're [povsisrole]s, w-"
    else:
        sis "Look, I know it may come as a shock to you, but just because we're twins, w-"
    show pov bored_talk at left
    show sis neutral at right
    pov "Okay, I get the point. You don't have to sass me, bitch."
    show pov bored at left
    show sis smirk_talk at right
    sis "Besides, where does it say there's an age limit to a fuckin' cardboard box fort?"
    show sis embarrassed_talk at right
    sis "We're not going to be making some crappy, cramped-ass fort."
    show sis smirk_talk at right
    sis "We're going all out."
    show pov bored_talk at left
    show sis smirk at right
    pov "You wanna box-fort the entirety of this basement?"
    show pov bored at left
    show sis smirk_talk at right
    sis "{i}We're{/i} going to box-fort the fuck out of this basement! It's going to be the greatest fort ever."
    show sis bored at right
    pov "..."
    show sis bored_talk at right
    sis "Don't look at me like that."
    show sis smirk_talk at right
    sis "I know you're totally into this idea, don't act like you're so high and mighty."
    show sis smirk at right
    pov "..."
    show pov embarrassed at left
    sis "..."
    show sis neutral_talk at right
    sis "Eh!"
    show sis neutral_talk at right
    sis "There's the smile I was looking for. I'll take that as a mutual agreement to turn this shithole into our kingdom."
    show pov smirk_talk at left
    show sis smirk at right
    pov "Just for us?"
    show pov smirk at left
    show sis neutral_talk at right
    sis "No outsiders allowed."
    show pov neutral at left
    show sis embarrassed_talk at right
    sis "Just us, [povname]. Promise me?"

    menu:
        "I promise.":
            $ basementplans_promise = 1
            show pov neutral_talk at left
            show sis embarrassed at right
            pov "I promise."
            show sis neutral at right
            if winc == 0:
                pov "No outsiders, no [missus], no [dadname], no friends, no boyfriends or girlfriends."
            else:
                pov "No outsiders, no mom, no dad, no friends, no boyfriends or girlfriends."
            show pov neutral at left
            show sis neutral_talk at right
            sis "No one but us."
            show pov bored at left
            show sis smirk_talk at right
            sis "Promise promise?"
            show pov bored_talk at left
            show sis neutral at right
            pov "I said I promise, [sister]."
            show pov smirk at left
            show sis smirk_talk at right
            sis "Good, just double coating."
        "We'll see.":
            show pov embarrassed_talk at left
            show sis bored at right
            pov "We'll see."
            pov "It's too early to set anything in stone."
            show pov embarrassed at left
            sis "..."
            show sis bored_talk at right
            sis "Not even considering it?"
            show pov embarrassed_talk at left
            show sis bored at right
            pov "I'm not entirely saying no to the rule, I'm just saying, let's see."
            show pov neutral_talk at left
            pov "Give it time and decide in the moment."
            show pov embarrassed at left
            sis "..."
            show pov neutral at left
            show sis neutral_talk at right
            sis "Fine. But considerations are special and rare, okay?"
            show pov neutral_talk at left
            show sis neutral at right
            pov "Fine."
            show pov neutral at left
            show sis neutral_talk at right
            sis "Good."
            show pov neutral_talk at left
            show sis bored at right
            pov "Good."
            show pov bored at left
            show sis bored_talk at right
            sis "I'm glad."

    scene bg mybasement_lightsonmessy
    show pov neutral at left
    show mum neutral_talk at Position(xpos=1300)
    show sis neutral at right
    if winc == 0:
        mum "Oh hello, my little [povdadrole]'s! You got the door unlocked."
    else:
        mum "Oh hello, mini-me's! You got the door unlocked."
    show mum bored_talk at Position(xpos=1300)
    mum "It's quite stuffy and cold down here."
    show pov embarrassed at left
    show mum confused_talk at Position(xpos=1300)
    show sis smirk at right
    mum "You both shouldn't be hanging around here."
    show mum confused at Position(xpos=1300)
    show sis smirk_talk at right
    if winc == 0:
        sis "Well, actually, [missus]. We ARE going to be down here quite a bit."
    else:
        sis "Well, actually, mother. We're ARE going to be down here quite a bit."
    sis "[povname] and I are making this area a chill-out zone for the both of us."
    show mum confused_talk at Position(xpos=1300)
    show sis neutral at right
    mum "...Really?"
    show sis bored at right
    mum "Down here where it's cold and damp?"
    show pov neutral at left
    show mum confused at Position(xpos=1300)
    show sis embarrassed_talk at right
    sis "Yes, we know it's a fixer-upper, but we got this."
    show mum neutral at Position(xpos=1300)
    show sis smirk_talk at right
    sis "Don't we, [povname]?"

    menu:
        "Oh, yeah.":
            show pov smirk_talk at left
            show sis neutral at right
            pov "Oh, yeah. We both totally got this."
            show pov neutral at left
            pov "It'll be a sight for sore eyes when we're done with this place."
            if skill_cha >= 4:
                $ skill_cha -= 4
                $ sister_points += 1
                $ renpy.notify("You used 4 Charisma Points\nYour relationship with [sister] has increased")
        "Only time will tell.":
            show pov neutral_talk at left
            show sis neutral at right
            pov "Only time will tell."
            pov "I prefer to surprise myself with the end result."
            if skill_luc >= 6:
                $ skill_luc -= 6
                $ sister_points += 2
                $ renpy.notify("You used 6 Luck Points\nYour relationship with [sister] has increased by 2")
                $ renpy.pause(3,hard=True)
            elif skill_luc >= 3:
                $ skill_luc -= 3
                $ sister_points += 1
                $ renpy.notify("You used 3 Luck Points\nYour relationship with [sister] has increased")
                $ renpy.pause(3,hard=True)
        "I have low expectations.":
            show pov embarrassed_talk at left
            show sis confused at right
            pov "I have low expectations."
            show pov smirk_talk at left
            show sis embarrassed at right
            pov "Though with [sister]'s female touch, it'll look appealing and welcoming."
            if skill_cha >= 8:
                $ skill_cha -= 8
                $ sister_points += 3
                $ renpy.notify("You used 8 Charisma Points\nYour relationship with [sister] has increased by 3")
            elif skill_cha >= 6:
                $ skill_cha -= 6
                $ sister_points += 2
                $ renpy.notify("You used 6 Charisma Points\nYour relationship with [sister] has increased by 2")
    show pov embarrassed at left
    show mum smirk_talk at Position(xpos=1300)
    show sis smirk at right
    mum "As long as I don't have to come down here and play referee."
    show pov neutral at left
    show mum neutral_talk at Position(xpos=1300)
    show sis neutral at right
    mum "This little project of yours will be a good use of your time, in my opinion."
    mum "It'll teach you how to work as a team and to create a closer bond."
    show mum confused at Position(xpos=1300)
    show sis smirk_talk at right
    if winc == 0:
        sis "You don't need to get all preachy on us, [missus]."
    else:
        sis "You don't need to get all preachy on us, Mom."
    show mum embarrassed_talk at Position(xpos=1300)
    show sis smirk at right
    mum "It's a breath of fresh air seeing the both of you get along every once in awhile."
    show pov neutral_talk at left
    show mum bored at Position(xpos=1300)
    show sis neutral at right
    pov "Naww, c'mon. We don't fight {i}that{/i} much."
    show pov neutral at left
    show sis confused at right
    mum "..."
    show pov embarrassed at left
    show mum neutral_talk at Position(xpos=1300)
    show sis smirk at right
    mum "Speaking of fresh air, it's time to head upstairs into the dining room."
    $ sister_path = 9
    if gtime == 0:
        mum "Lunch is ready."
        $ gtime = 1
        scene black
        with fade
        $ renpy.pause()
        if mowed_lawn == 1:
            scene bg mydiningroom_day
        else:
            scene bg mydiningroom_day_grassy

        jump lbl_mydiningroom_day_setup
    else:
        mum "Dinner is ready."
        $ gtime = 2
        scene black
        with fade
        $ renpy.pause()
        if mowed_lawn == 1:
            scene bg mydiningroom_night
        else:
            scene bg mydiningroom_night_grassy

        jump lbl_mydiningroom_night_setup
