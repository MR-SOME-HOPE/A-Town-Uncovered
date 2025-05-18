## Unusually Sleepy

label lbl_unusually_sleepy:
    scene bg myhallway_day
    with fade
    show pov confused_talk at left
    with dissolve
    show sis confused at right
    with dissolve
    pov "Hey, you good?"
    show pov confused at left
    show sis confused_talk at right
    sis "Yeah, you good?"
    show pov embarrassed_talk at left
    show sis confused at right
    pov "Yeah."
    show pov confused_talk at left
    pov "Mom told me you’ve been stressing a lot from work and they’re really pushing you."
    show sis shocked at right
    pov "Saw you coddled up in her arms last night."
    show pov embarrassed at left
    show sis confused_talk at right
    sis "Why are you so concerned about me? I’m fine, just y’know as you said. Stressed and tired."
    show sis embarrassed_talk at right
    sis "I mean, who isn’t nowadays?"
    show pov confused_talk at left
    show sis confused at right
    pov "I can imagine you sleeping more and sleeping early, but with [missus]?"
    show pov confused at left
    show sis bored_talk at right
    sis "Don't you tell me that falling asleep next to [missus] is weird, [povname]."
    sis "I don’t always wanna be alone, y’know."
    show pov embarrassed at left
    sis "[missus] invited me to hang out with her and watch a movie, and that’s that."
    show pov embarrassed_talk at left
    show sis confused at right
    pov "You’ve really gotten close to her these days."
    show pov shocked at left
    show sis bored_talk at right
    sis "Dude, don’t make it weird. She’s our [mumrole]."
    show pov embarrassed at left
    show sis embarrassed_talk at right
    sis "The older you get, the more you see her as just another person and not just a parent."
    show pov bored_talk at left
    show sis confused at right
    pov "You’re like a few minutes older than me."
    show pov bored at left
    show sis smirk_talk at right
    sis "And you’re still salty about it."
    show sis smirk at right
    pov "Hmph."
    show pov shocked at left
    show sis smirk_talk at right
    sis "Anyway, it’s not like you and her haven’t gotten close too."
    show pov shocked_talk at left
    show sis smirk at right
    pov "W-what do you mean."
    show pov shocked at left
    show sis smirk_talk at right
    if winc == 1:
        sis "You have your mother-son times as well, you’re not the only child of hers, y’know."
    else:
        sis "You have your bonding times as well, you’re not the only one she cares for, y’know."
    show pov embarrassed_talk at left
    show sis confused at right
    pov "You know about that?"
    show pov shocked at left
    show sis confused_talk at right
    sis "Why?"
    show sis smirk_talk at right
    sis "Is it meant to be a secret?"
    show pov shocked_talk at left
    show sis confused at right
    pov "I-"
    show pov shocked at left
    show sis embarrassed_talk at right
    sis "Chill, dude."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Why you gotta act so weird about it. You’re actually so suss right now."
    show pov sad_talk at left
    show sis smirk at right
    pov "Why do I feel like you just pulled the reverse card on me?"
    show pov bored at left
    show sis smirk_talk at right
    sis "Always have a spare in my back pocket."
    show pov confused_talk at left
    show sis bored at right
    pov "But you’re wearing a dress… shirt?"
    pov "A really long blouse?"
    show pov confused at left
    show sis bored_talk at right
    sis "I’m talking about the back pocket of my shorts, you idiot."
    sis "Hypothetically speaking."
    show pov embarrassed_talk at left
    show sis bored at right
    pov "Yeah, okay. Um… I’m gonna go."
    show pov embarrassed at left
    pov "…"
    show pov embarrassed_talk at left
    pov "Nice talk."
    show pov embarrassed at left
    show sis bored_talk at right
    sis "Yuh."

    $ mumsis_path = 5

    jump lbl_myhallway_day
