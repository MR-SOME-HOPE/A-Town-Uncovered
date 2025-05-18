## In Trouble By Mom School Trap ##
label lbl_in_trouble_by_mom_school_trap:
    if winc == 0:
        jump lbl_in_trouble_by_mom_school_trap_winc0

    scene bg mylivingroom_day
    show pov shocked at left
    show mum angry_talk at right
    with hpunch
    mum "[povname]! You're in big big trouble, mister!"
    mum "Where the hell have you been?!"
    show pov embarrassed at left
    mum "Why are you always staying out without telling me?!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "Hey, Mom..."
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Don't ‘hey, Mom' me!"
    mum "What do you have to say for yourself?"
    show pov sad_talk at left
    show mum angry at right
    pov "I'm sorry..."
    show pov sad at left
    show mum angry_talk at right
    mum "Where were you?"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I was out at a friend's place."
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Is this the same friend as before?"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "No, Mom. A different friend."
    show pov confused at left
    show mum angry_talk at right
    mum "Is she a girl?"
    show pov confused_talk at left
    show mum angry at right
    pov "Why do you always ask that."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "I want to know! I'm your mother. You don't think I was worried sick about you?"
    show mum angry_talk at right
    mum "I nearly called the cops. Again!"

    menu:
        "Yes, it was a girl.":
            if mum_points >= 4:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
                show pov embarrassed_talk at left
                show mum angry at right
                pov "Yeah, it was a girl."
                show pov shocked at left
                show mum angry_talk at right
                mum "Why do you do this to me, [povname]?"
                show pov embarrassed_talk at left
                show mum angry at right
                pov "It's just a girl, Mom. I promise, nothing happened this time."
                show pov shocked at left
                show mum shocked_talk at right
                mum "This time?!"
                show pov embarrassed at left
                show mum angry_talk at right
                mum "[povname]!"
                mum "Where the hell is your phone? What's the point of having one if you don't call me at the very least?!"
            else:
                show pov embarrassed_talk at left
                show mum angry at right
                pov "Yeah, it was a girl."
                show pov embarrassed at left
                show mum bored at right
                mum "..."
                show mum bored_talk at right
                mum "Is she cute?"
                show pov embarrassed_talk at left
                show mum bored at right
                pov "Very cute, mother. Don't make this awkward, okay?"
                show pov embarrassed_talk at left
                show mum angry at right
                pov "Just friends for now."
                show pov bored at left
                show mum bored_talk at right
                mum "For now."
                show pov embarrassed at left
                show mum confused_talk at right
                mum "I can't wait to meet her."
                mum "Speaking of, where's your phone? Why didn't you call me last night? You owe me that."
        "No, it wasn't a girl.":
            if mum_points >= 4:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
                show pov confused_talk at left
                show mum shocked at right
                pov "No, it wasn't a girl."
                show pov confused at left
                show mum embarrassed_talk at right
                mum "Oh, good."
                show mum embarrassed_talk at right
                mum "You nearly gave me a double heart attack."
                show pov embarrassed at left
                show mum bored_talk at right
                mum "The first one was from when I couldn't find you this morning."
                show mum confused_talk at right
                mum "Where the hell is your phone? Why couldn't you call me last night?"
            else:
                show pov confused_talk at left
                show mum shocked at right
                pov "No, it wasn't a girl."
                show pov confused at left
                show mum confused_talk at right
                mum "A-are you..."
                show mum sad_talk at right
                mum "You can..."
                show pov shocked at left
                show mum embarrassed_talk at right
                mum "You can tell me if you're gay, y'know..."
                show pov shocked_talk at left
                show mum shocked at right
                pov "Mom! I'm not gay."
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "We were playing some video games and we lost track of time. I figured I would stay the night."
                show pov bored at left
                show mum embarrassed_talk at right
                mum "..."
                show pov embarrassed at left
                show mum bored_talk at right
                mum "You could've at least called me."
    show pov embarrassed_talk at left
    show mum bored at right
    pov "I- had no credit. I forgot to recharge it. Sorry."
    show pov shocked at left
    show mum angry_talk at right
    with hpunch
    mum "Well, get that recharged. You have to wash the dishes every night this week, as your punishment."
    show pov sad_talk at left
    show mum angry at right
    pov "{i}*Sigh*{/i} Yes, Mom."
    show pov sad at left
    show mum bored_talk at right
    mum "Now go and get ready for university."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "I love you, sweetie."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "I love you too, Mom. And I'm sorry, again."

    $ townmap_enabled = 1
    $ missallaway_path = 10

    jump lbl_mylivingroom_day_setup

label lbl_in_trouble_by_mom_school_trap_winc0:

    scene bg mylivingroom_day
    with hpunch
    show pov shocked at left
    show mum angry_talk at right
    mum "[povname]! You're in big big trouble, mister!"
    mum "Where the hell have you been?!"
    show pov embarrassed at left
    mum "Why are you always staying out without telling me?!"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "Hey, [missus]..."
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Don't ‘hey, [missus]' me!"
    mum "What do you have to say for yourself?"
    show pov sad_talk at left
    show mum angry at right
    pov "I'm sorry..."
    show pov sad at left
    show mum angry_talk at right
    mum "Where were you?"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "I was out at a friend's place."
    show pov embarrassed at left
    show mum angry_talk at right
    mum "Is this the same friend as before?"
    show pov embarrassed_talk at left
    show mum angry at right
    pov "No, [missus]. A different friend."
    show pov confused at left
    show mum angry_talk at right
    mum "Is she a girl?"
    show pov confused_talk at left
    show mum angry at right
    pov "Why do you always ask that."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "I want to know! I'm your [mumrole]. You don't think I was worried sick about you?"
    show mum angry_talk at right
    mum "I nearly called the cops. Again!"

    menu:
        "Yes, it was a girl.":
            if mum_points >= 4:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
                show pov embarrassed_talk at left
                show mum angry at right
                pov "Yeah, it was a girl."
                show pov shocked at left
                show mum angry_talk at right
                mum "Why do you do this to me, [povname]?"
                show pov embarrassed_talk at left
                show mum angry at right
                pov "It's just a girl, [missus]. I promise, nothing happened this time."
                show pov shocked at left
                show mum shocked_talk at right
                mum "This time?!"
                show pov embarrassed at left
                show mum angry_talk at right
                mum "[povname]!"
                mum "Where the hell is your phone? What's the point of having one if you don't call me at the very least?!"
            else:
                show pov embarrassed_talk at left
                show mum angry at right
                pov "Yeah, it was a girl."
                show pov embarrassed at left
                show mum bored at right
                mum "..."
                show mum bored_talk at right
                mum "Is she cute?"
                show pov embarrassed_talk at left
                show mum bored at right
                pov "Very cute, [missus]. Don't make this awkward, okay?"
                show pov embarrassed_talk at left
                show mum angry at right
                pov "Just friends for now."
                show pov bored at left
                show mum bored_talk at right
                mum "For now."
                show pov embarrassed at left
                show mum confused_talk at right
                mum "I can't wait to meet her."
                mum "Speaking of, where's your phone? Why didn't you call me last night? You owe me that."
        "No, it wasn't a girl.":
            if mum_points >= 4:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
                show pov confused_talk at left
                show mum shocked at right
                pov "No, it wasn't a girl."
                show pov confused at left
                show mum embarrassed_talk at right
                mum "Oh, good."
                show mum embarrassed_talk at right
                mum "You nearly gave me a double heart attack."
                show pov embarrassed at left
                show mum bored_talk at right
                mum "The first one was from when I couldn't find you this morning."
                show mum confused_talk at right
                mum "Where the hell is your phone? Why couldn't you call me last night?"
            else:
                show pov confused_talk at left
                show mum shocked at right
                pov "No, it wasn't a girl."
                show pov confused at left
                show mum confused_talk at right
                mum "A-are you..."
                show mum sad_talk at right
                mum "You can..."
                show pov shocked at left
                show mum embarrassed_talk at right
                mum "You can tell me if you're gay, y'know..."
                show pov shocked_talk at left
                show mum shocked at right
                pov "[missus]! I'm not gay."
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "We were playing some video games and we lost track of time. I figured I would stay the night."
                show pov bored at left
                show mum embarrassed_talk at right
                mum "..."
                show pov embarrassed at left
                show mum bored_talk at right
                mum "You could've at least called me."
    show pov embarrassed_talk at left
    show mum bored at right
    pov "I- had no credit. I forgot to recharge it. Sorry."
    show pov shocked at left
    show mum angry_talk at right
    with hpunch
    mum "Well, get that recharged. You have to wash the dishes every night this week, as your punishment."
    show pov sad_talk at left
    show mum angry at right
    pov "{i}*Sigh*{/i} Yes, [missus]."
    show pov sad at left
    show mum bored_talk at right
    mum "Now go and get ready for university."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "I love you, sweetie."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "I love you too, [missus]. And I'm sorry, again."

    $ townmap_enabled = 1
    $ missallaway_path = 10

    jump lbl_mylivingroom_day_setup
