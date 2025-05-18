## Morning Dad ###
label lbl_morning_dad:
    if winc == 0:
        jump lbl_morning_dad_winc0
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "What was that noise?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "Oh yeah, don't worry about that, she's awake now."
    hide mum neutral
    show pov bored at left
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "Morning."
    show mum neutral_talk at right
    show dad neutral at Position(xpos=1300)
    mum "Morning, sweetie."
    show pov bored at left
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "I've got to run. I'm late for work."
    show dad neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Don't you want any breakfast?"
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "You didn't cook anything, did you?"
    show dad neutral at Position(xpos=1300)
    show mum sad_talk at right
    mum "Well, no..."
    show dad angry_talk at Position(xpos=1300)
    show mum sad at right
    dad "Then what the fuck are you wasting my time for?"
    dad "And [povname]?"

    menu:
        "Yeah?":
            $ morningdad_donttalktomom = 0
            show pov bored_talk at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "Yeah?"
            show pov bored at left
            show dad angry_talk at Position(xpos=1300)
            show mum sad at right
            dad "Don't fuck about at university, alright? It's your first day."
        "Don't talk to Mom like that!":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            $ morningdad_donttalktomom = 1
            show pov angry_talk at left
            show dad angry at Position(xpos=1300)
            show mum embarrassed at right
            pov "Don't talk to Mom like that!"
            show pov angry at left
            show dad angry_talk at Position(xpos=1300)
            show mum sad at right
            dad "Shut up, [povname]! It's too early in the morning for your bullshit."
            dad "Just..."
            dad "Don't fuck about at university, alright? It's your first day."
    show dad angry at Position(xpos=1300)
    show mum angry_talk at right
    mum "Oh hush up, he won't get into trouble."
    show dad angry_talk at Position(xpos=1300)
    show mum angry at right
    dad "Like I said, don't mess around. We've got a good thing going here, good opportunities."
    dad "Do well at university, or I swear to God..."
    show pov bored_talk at left
    show dad angry at Position(xpos=1300)
    show mum angry at right
    pov "Don't worry, Dad. I'll do my best."
    hide dad angry
    show pov sad at left
    show mum embarrassed_talk at right
    mum "I'm sure he's just joking."
    show pov sad_talk at left
    show mum sad at right
    pov "I don't think you've noticed, but ever since I started UNI, he hasn't exactly become the joking type. You know that."
    show pov sad at left
    show mum sad_talk at right
    mum "Yeah, well, I thought I knew a lot of stuff about him. I guess people change, not always for the better."
    show pov sad_talk at left
    show mum sad at right
    pov "He's always picking on me, never [sister]."
    show pov sad at left
    show mum sad_talk at right
    mum "He just wants you to be strong and successful like he is."
    mum "To someday make sacrifices for your own family. He's the ‘toughen up' kind of guy."
    show pov neutral_talk at left
    show mum sad at right
    pov "He could at least crack a smile every once in a while."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Hahaha! I guess he's hiding it behind that mustache of his."
    mum "C'mon, don't be late for your first day. Make sure you leave with ample amount of time."
    mum "Here's your backpack with your map and phone still inside, you must've left it downstairs last night."
    show pov confused_talk at left
    show mum neutral at right
    pov "Huh, that's weird. I swear I dropped it off in my room."
    show pov confused at left
    show mum bored_talk at right
    mum "Well, make sure you don't leave it around again, or you'll lose all of them."
    mum "Now go and get to your university before you get in trouble."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Fine fine. Love you, Mom."
    show pov neutral at left
    show mum neutral_talk at right
    mum "I love you too, [povname]."
    $ main_story = 5
    $ hud_enabled = 1
    $ renpy.notify("New Objective: Go to University")
    $ renpy.pause (1,hard=True)
    $ renpy.notify("New Items Obtained: Map, Bag, Phone")
    $ renpy.pause (1,hard=True)
    $ renpy.notify("New Contacts: Mom, Sister, Dad")
    $ renpy.pause (1,hard=True)
    $ renpy.notify("Current Balance: $[inventory.money]")
    $ renpy.pause (1,hard=True)

    jump lbl_mykitchen_day

### NO WINC ###
label lbl_morning_dad_winc0:
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "What was that noise?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "Oh yeah, don't worry about that, she's awake now."
    hide mum neutral
    show pov bored at left
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "Morning."
    show mum neutral_talk at right
    show dad neutral at Position(xpos=1300)
    mum "Morning, sweetie."
    show pov bored at left
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "I've got to run. I'm late for work."
    show dad neutral at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Don't you want any breakfast?"
    show dad neutral_talk at Position(xpos=1300)
    show mum neutral at right
    dad "You didn't cook anything, did you?"
    show dad neutral at Position(xpos=1300)
    show mum sad_talk at right
    mum "Well, no..."
    show dad angry_talk at Position(xpos=1300)
    show mum sad at right
    dad "Then what the fuck are you wasting my time for?"
    dad "And [povname]?"

    menu:
        "Yeah?":
            $ morningdad_donttalktomom = 0
            show pov bored_talk at left
            show dad neutral at Position(xpos=1300)
            show mum neutral at right
            pov "Yeah?"
            show pov bored at left
            show dad angry_talk at Position(xpos=1300)
            show mum sad at right
            dad "Don't fuck about at university, alright? It's your first day."
        "Don't talk to [missus] like that!":
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            $ morningdad_donttalktomom = 1
            show pov angry_talk at left
            show dad angry at Position(xpos=1300)
            show mum embarrassed at right
            pov "Don't talk to [missus] like that!"
            show pov angry at left
            show dad angry_talk at Position(xpos=1300)
            show mum sad at right
            dad "Shut up, [povname]! It's too early in the morning for your bullshit."
            dad "Just..."
            dad "Don't fuck about at university, alright? It's your first day."
    show dad angry at Position(xpos=1300)
    show mum angry_talk at right
    mum "Oh hush up, he won't get into trouble."
    show dad angry_talk at Position(xpos=1300)
    show mum angry at right
    dad "Like I said, don't mess around. We've got a good thing going here, good opportunities."
    dad "Do well university, or I swear to God..."
    show pov bored_talk at left
    show dad angry at Position(xpos=1300)
    show mum angry at right
    pov "Don't worry, [dadname]. I'll do my best."
    hide dad angry
    show pov sad at left
    show mum embarrassed_talk at right
    mum "I'm sure he's just joking."
    show pov sad_talk at left
    show mum sad at right
    pov "I don't think you've noticed, but ever since I started UNI, he hasn't exactly become the joking type. You know that."
    show pov sad at left
    show mum sad_talk at right
    mum "Yeah, well, I thought I knew a lot of stuff about him. I guess people change, not always for the better."
    show pov sad_talk at left
    show mum sad at right
    pov "He's always picking on me, never my [sisrole]."
    show pov sad at left
    show mum sad_talk at right
    mum "He just wants you to be strong and successful like he is."
    mum "To someday make sacrifices for your own family. He's the ‘toughen up' kind of guy."
    show pov neutral_talk at left
    show mum sad at right
    pov "He could at least crack a smile every once in a while."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Hahaha! I guess he's hiding it behind that mustache of his."
    mum "C'mon, don't be late for your first day. Make sure you leave with ample amount of time."
    mum "Here's your map, backpack and phone, you must've left it downstairs last night."
    show pov confused_talk at left
    show mum neutral at right
    pov "Huh, that's weird. I swear I dropped it off in my room."
    show pov confused at left
    show mum bored_talk at right
    mum "Well, make sure you don't leave it around again, or you'll lose all of them."
    mum "Now go and get to your university before you get in trouble."
    show pov neutral_talk at left
    show mum neutral at right
    pov "Fine fine. Love you, [missus]."
    show pov neutral at left
    show mum neutral_talk at right
    mum "I love you too, [povname]."
    $ main_story = 5
    $ hud_enabled = 1
    $ renpy.notify("New Objective: Go to University")
    $ renpy.pause (1,hard=True)
    $ renpy.notify("New Items Obtained: Map, Bag, Phone")
    $ renpy.pause (1,hard=True)
    $ renpy.notify("New Contacts: [missus], [sister], [dadname]")
    $ renpy.pause (1,hard=True)
    $ renpy.notify("Current Balance: $[inventory.money]")
    $ renpy.pause (1,hard=True)

    jump lbl_mykitchen_day
