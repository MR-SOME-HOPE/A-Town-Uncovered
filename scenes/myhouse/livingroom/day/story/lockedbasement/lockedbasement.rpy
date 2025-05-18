## Locked Basement ##
label lbl_locked_basement:
    if winc == 0:
        jump lbl_locked_basement_winc0

    scene bg lockedbasement_1
    with fade
    $ renpy.pause(0.7,hard=True)
    show bg lockedbasement_2
    $ renpy.pause(0.7,hard=True)
    show bg lockedbasement_1
    pov "What are you doing?"
    show bg lockedbasement_3
    sis "What does it look like? I'm trying to get this door opened."
    show bg lockedbasement_2
    pov "Why?"
    show bg lockedbasement_4
    sis "Why? Because it's in our house and I want to know what's behind it."
    show bg lockedbasement_1
    pov "It's probably the basement or something. It most likely is."
    show bg lockedbasement_3
    sis "I want in."
    show bg lockedbasement_1
    pov "Did you ask Mom for the key?"
    show bg lockedbasement_3
    sis "She said she doesn't have it, it's been locked ever since we moved in."
    show bg lockedbasement_5
    sis "As if you've never wondered or even not cared about what is behind this door."
    show bg lockedbasement_6
    sis "There could be treasure waiting for us!"
    show bg lockedbasement_1

    menu:
        "Sex dungeon.":
            pov "Or it could be a sex dungeon."
            show bg lockedbasement_7
            sis "Yeah, you'd just love to be tied down and whipped."
        "Just junk.":
            pov "Or there could just be junk."
            show bg lockedbasement_7
            sis "Once you step inside, then yeah, there'll be junk."
        "Portal to another sex dimension." if main_story >= 23:
            pov "Or there could be a portal to another dimension where everyone loves to have sex."
            show bg lockedbasement_7
            sis "That's perverted, and stupid."
        "Dead body.":
            pov "Or there could be a dead body."
            show bg lockedbasement_7
            sis "Jeez, you'd fuck anything that had a pulse once."
        "Completely empty.":
            pov "Or it's completely empty."
            show bg lockedbasement_7
            sis "You must be the life of a party, aren't you?"
        "Another door.":
            pov "Or there could be another door behind that door with an even more complicated lock."
            show bg lockedbasement_7
            sis "If there is, I'd lock you in between this door and that."
        "Booty booty.":
            pov "Let's hope it's booty."
            show bg lockedbasement_7
            sis "Cutie patootie, gimme that booty! Mama want diamond encrusted raangs."
    show bg lockedbasement_8
    pov "..."
    show bg lockedbasement_9
    sis "..."
    show bg lockedbasement_8
    pov "..."
    show bg lockedbasement_9
    pov "Mayb-"
    show bg lockedbasement_3
    sis "Shh! I'm concentrating."
    show bg lockedbasement_1
    pov "..."
    show bg lockedbasement_2
    sis "..."
    show bg lockedbasement_1
    pov "Look, let m-"
    show bg lockedbasement_3
    sis "Shut up, [povname]."
    show bg lockedbasement_1
    pov "Alright, alrigh-"
    show bg lockedbasement_3
    sis "Shut'p"
    show bg lockedbasement_1
    pov "Mm."
    show bg lockedbasement_2
    sis "..."
    show bg lockedbasement_1

    menu:
        "Just let me try.":
            pov "Jus-"
        "Maybe if you wiggle it a bit more.":
            pov "Mayb-"
        "Did you get it yet?":
            pov "Did y-"
        "Stay silent":
            pov "..."
    show bg lockedbasement_4
    with hpunch
    sis "Alright fine! Holy shit, you do it then since you know it all."
    show bg lockedbasement_10
    pov "Well, I wouldn't say I know EVERYTHING, but I can get it open in no time."
    show bg lockedbasement_11
    sis "If you say so."
    sis "I'm still getting 80 percent of the treasure."
    show bg lockedbasement_12
    pov "Fuck no, 50-50."
    show bg lockedbasement_13
    sis "In your dreams, baby bro."
    $ sister_path = 7.5
    $ renpy.notify("New Objective: Research how to pick a lock")

    jump lbl_mylivingroom_day_setup

### NO WINC ###
label lbl_locked_basement_winc0:

    scene bg lockedbasement_1
    with fade
    $ renpy.pause(0.7,hard=True)
    show bg lockedbasement_2
    $ renpy.pause(0.7,hard=True)
    show bg lockedbasement_1
    pov "What are you doing?"
    show bg lockedbasement_3
    sis "What does it look like? I'm trying to get this door opened."
    show bg lockedbasement_2
    pov "Why?"
    show bg lockedbasement_4
    sis "Why? Because it's in our house and I want to know what's behind it."
    show bg lockedbasement_1
    pov "It's probably the basement or something. It most likely is."
    show bg lockedbasement_3
    sis "I want in."
    show bg lockedbasement_1
    pov "Did you ask [missus] for the key?"
    show bg lockedbasement_3
    sis "She said she doesn't have it, it's been locked ever since we moved in."
    show bg lockedbasement_5
    sis "As if you've never wondered or even not cared about what is behind this door."
    show bg lockedbasement_6
    sis "There could be treasure waiting for us!"
    show bg lockedbasement_1

    menu:
        "Sex dungeon.":
            pov "Or it could be a sex dungeon."
            show bg lockedbasement_7
            sis "Yeah, you'd just love to be tied down and whipped."
        "Just junk.":
            pov "Or there could just be junk."
            show bg lockedbasement_7
            sis "Once you step inside, then yeah, there'll be junk."
        "Portal to another sex dimension." if main_story >= 23:
            pov "Or there could be a portal to another dimension where everyone loves to have sex."
            show bg lockedbasement_7
            sis "That's perverted, and stupid."
        "Dead body.":
            pov "Or there could be a dead body."
            show bg lockedbasement_7
            sis "Jeez, you'd fuck anything that had a pulse once."
        "Completely empty.":
            pov "Or it's completely empty."
            show bg lockedbasement_7
            sis "You must be the life of a party, aren't you?"
        "Another door.":
            pov "Or there could be another door behind that door with an even more complicated lock."
            show bg lockedbasement_7
            sis "If there is, I'd lock you in between this door and that."
        "Booty booty.":
            pov "Let's hope it's booty."
            show bg lockedbasement_7
            sis "Cutie patootie, gimme that booty! Mama want diamond encrusted raangs."
    show bg lockedbasement_8
    pov "..."
    show bg lockedbasement_9
    sis "..."
    show bg lockedbasement_8
    pov "..."
    show bg lockedbasement_9
    pov "Mayb-"
    show bg lockedbasement_3
    sis "Shh! I'm concentrating."
    show bg lockedbasement_1
    pov "..."
    show bg lockedbasement_2
    sis "..."
    show bg lockedbasement_1
    pov "Look, let m-"
    show bg lockedbasement_3
    sis "Shut up, [povname]."
    show bg lockedbasement_1
    pov "Alright, alrigh-"
    show bg lockedbasement_3
    sis "Shut'p"
    show bg lockedbasement_1
    pov "Mm."
    show bg lockedbasement_2
    sis "..."
    show bg lockedbasement_1

    menu:
        "Just let me try.":
            pov "Jus-"
        "Maybe if you wiggle it a bit more.":
            pov "Mayb-"
        "Did you get it yet?":
            pov "Did y-"
        "Stay silent":
            pov "..."
    show bg lockedbasement_4
    with hpunch
    sis "Alright fine! Holy shit, you do it then since you know it all."
    show bg lockedbasement_10
    pov "Well, I wouldn't say I know EVERYTHING, but I can get it open in no time."
    show bg lockedbasement_11
    sis "If you say so."
    sis "I'm still getting 80 percent of the treasure."
    show bg lockedbasement_12
    pov "Fuck no, 50-50."
    show bg lockedbasement_13
    sis "In your dreams, [povname]."
    $ sister_path = 7.5
    $ renpy.notify("New Objective: Research how to pick a lock")

    jump lbl_mylivingroom_day_setup
