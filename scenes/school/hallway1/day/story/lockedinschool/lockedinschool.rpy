## Locked in School ##
label lbl_locked_in_school:

    scene bg schoolhallway1_dayempty
    with fade
    show pov neutral at left
    with dissolve
    show mis confused at right
    with dissolve
    mis "..."
    show pov confused at left
    show mis confused_talk at right
    mis "That's funny... the door is locked..."
    show pov shocked at left
    show mis angry at right
    with vpunch
    mis "..."
    show mis angry_talk at right
    mis "I- I can't get it opened?"
    show pov confused_talk at left
    show mis sad at right
    pov "Here, let me try."
    show pov angry at left
    with vpunch
    pov "..."
    show pov embarrassed_talk at left
    show mis shocked at right
    pov "Not to look like a total weakling but, yeah..."
    show pov sad_talk at left
    pov "This door ain't budging."
    show pov confused at left
    show mis sad_talk at right
    mis "They couldn't have locked us in here?!"
    mis "Someone must've knew we were in here, right?!"
    show pov shocked at left
    show mis shocked_talk at right
    with hpunch
    mis "HELLO?! IS ANYONE ELSE IN THIS BUILDING?!"
    show pov embarrassed_talk at left
    show mis shocked at right
    pov "Miss, miss. Slow down. Why don't you just call the university... or whoever?"
    show pov confused at left
    show mis embarrassed_talk at right
    mis "My... phone is dead. Flat. Deceased."
    show pov confused_talk at left
    show mis embarrassed at right
    pov "Do you remember any of the phone numbers to any of the teachers or Director Lashley?"
    show pov embarrassed at left
    show mis angry_talk at right
    mis "Does it look like I remember the numbers?!"
    show mis confused_talk at right
    mis "{i}*Sigh*{/i}... think... think... think..."
    show pov neutral at left
    show mis confused at right
    pov "..."
    show pov smirk_talk at left
    show mis confused at right
    pov "I guess I'm staying the night, and only after our second date."
    show pov smirk at left
    mis "..."
    if skill_cha >= 7:
        show pov smirk at left
        show mis confused_talk at right
        mis "You don't know when to quit it, do you? {i}*Sigh*{/i}"
        show mis sad_talk at right
        mis "I guess I can't help that your teenage hormones are attracted to my mature body."
    else:
        show pov shocked at left
        show mis angry_talk at right
        mis "Don't you fuckin' dare bring on that playboy sass with me, young man."
        mis "As much as how alone we are at the moment and that whatever happens in here stays in here... I-"
        mis "I-"
        mis "Fuck... I don't know how to finish that."
    show pov embarrassed at left
    show mis bored_talk at right
    mis "Don't get... ahead of yourself, I'm warning you, [povname]."
    show pov embarrassed_talk at left
    show mis bored at right
    pov "Okay, okay. I don't know why you're getting so steamy over it, I'm just messing around."
    pov "We're only humans. Stupid stuff comes out of us sometimes."
    show pov neutral_talk at left
    pov "Like bullshit... and shit... and wee... and jiz-"
    show pov embarrassed at left
    show mis angry_talk at right
    mis "Can you... not talk for one second and let me think of a solution..."

    scene black
    "4 seconds later..."

    scene bg schoolhallway1_dayempty
    show pov bored at left
    show mis sad_talk at right
    mis "We're trapped here forever."
    show pov embarrassed at left
    show mis shocked_talk at right
    if winc == 0:
        mis "Can't you call your [dadrole]s or something?"
    else:
        mis "Can't you call your parents or something?"
    show pov embarrassed_talk at left
    show mis shocked at right
    pov "I... ran out of credit."
    show pov confused at left
    show mis angry_talk at right
    mis "Well, that's just great, isn't it."
    show pov confused_talk at left
    show mis angry at right
    pov "You're the one with a flat battery!"
    show pov confused at left
    show mis angry_talk at right
    mis "These batteries suck dick, [povname]! Have you ever thought of that?!"
    show pov sad at left
    show mis sad_talk at right
    mis "I just want to cry in a corner..."
    mis "My couch..."
    mis "My hot cocoa..."
    show pov embarrassed at left
    mis "My blanky..."
    mis "My Webflicks..."
    show pov confused at left
    mis "I'm going to be behind schedule now..."
    show pov embarrassed at left
    show mis sad at right
    pov "..."
    show pov embarrassed_talk at left
    pov "But hey, we have the whole university to ourselves! It looks so weird when there's no one here."
    show pov smirk_talk at left
    pov "Like the apocalypse."
    show pov neutral at left
    show mis sad_talk at right
    mis "... I like the apocalypse."
    show pov neutral_talk at left
    show mis embarrassed at right
    pov "That's the spirit."
    show pov embarrassed_talk at left
    show mis embarrassed at right
    pov "Hmmm.. I guess there's not much for us to do other than to stay the night and head home as soon as the doors are unlocked."
    show pov embarrassed at left
    show mis sad_talk at right
    mis "This sucks..."
    show pov embarrassed_talk at left
    show mis confused at right
    pov "Could be worse."
    show pov smirk_talk at left
    show mis shocked at right
    pov "I could be Jacob."
    show pov smirk at left
    show mis embarrassed_talk at right
    mis "Hahahaha!"
    mis "I feel so terrible for laughing at that!"
    mis "But I don't care, bahahahaha!"
    mis "Poor Jacob."
    show mis smirk_talk at right
    mis "Can you believe he actually went around and tried to coin the nickname, ‘BJ'?"
    show pov neutral_talk at left
    show mis embarrassed at right
    pov "I remember that. That was a weird day."
    show pov embarrassed_talk at left
    show mis confused at right
    pov "That was the first day I met you."
    show pov smirk at left
    show mis smirk_talk at right
    mis "Oh, don't be so sappy, [povname]. That was the first day of term, of course it'd be the first day you'd meet me."
    show mis embarrassed at right
    pov "..."
    show pov neutral_talk at left
    pov "Let's just make the most of tonight."
    $ missallaway_path = 9

    jump lbl_trapped_with_allaway
