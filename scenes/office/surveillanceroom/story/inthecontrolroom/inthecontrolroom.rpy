## In The Control Room #
label lbl_in_the_control_room:
    scene black
    with fade
    $ renpy.pause()
    "You run across town towards the TRC building and make your way up, searching room after room for Effie..."
    "Instead, you find the control room with Eloise in it."
    ## MC finds the control room that they were searching for. He sees not Xina but Eloise, confused and dazed and in a panic.

    scene bg officesurveillanceroom_daynight
    with fade
    show povn shocked_talk at left
    show elo sad at right
    with dissolve
    pov "Eloise?"
    pov "What-"
    pov "What did you do?!"

    show povn shocked
    show elo shocked_talk
    elo "[povname]?!"
    show elo sad_talk
    elo "I-"
    elo "I didn’t-"
    elo "I-"
    show povn bored
    elo "I don’t know what’s happening-"
    elo "One moment I’m-"
    elo "And then next-"
    elo "I-"
    elo "I don’t know what this is-"
    elo "I didn’t do it!"
    elo "You have to believe me!"
    show povn angry
    elo "I’ve-"
    elo "I’ve tried to stop it-"
    elo "I can’t!"
    elo "I don’t know what I’m doing!"

    show povn angry_talk
    show elo sad
    pov "Why can’t you stop it?!"

    show povn bored
    show elo shocked_talk
    elo "I CAN’T!"
    elo "I-"
    elo "I tried..."
    show povn sad
    show elo sad_talk
    elo "I swear, [povname]. I didn’t do this."
    elo "Someone hacked into our system and initiated the attack."
    elo "I would NEVER do something like this."
    elo "I’m-"
    elo "I’m not a monster."
    elo "You have to believe me!"

    show povn sad_talk
    show elo sad
    pov "I believe you."

    show povn sad
    pov "..."

    show elo sad_talk
    elo "I made- all those androids to serve humanity."
    elo "Yes, they’re sex servants."
    elo "But-"
    elo "Imagine how much more beautiful the world would be if people weren’t angry or depressed or lonely."
    elo "They were made to fulfill a human need that is slowly becoming harder to obtain in this internet age."
    elo "But they are still early in testing and never in a million years did I know they have an aggression trigger."

    show povn sad_talk
    show elo sad
    pov "You have to stop this, Eloise."
    pov "You have to keep trying."

    show povn sad
    show elo sad_talk
    elo "I can’t."
    elo "I really can’t."
    elo "It doesn’t listen to me anymore."
    elo "It listens to itself."

    show povn sad_talk
    show elo sad
    pov "I need to find Effie."
    pov "Do you know where my friend is?"

    show povn sad
    show elo sad_talk
    elo "I-"
    elo "*Gulp*"
    elo "I don’t know... I’ll help you find her."
    elo "If she’s in the building, she should be here somewhere..."

    show elo sad
    "MC notices on one of the screens a room of floating rune rocks on one of the screens." #TEMP2024

    show povn confused_talk
    pov "Wh-"
    pov "What is that?"
    show elo confused
    pov "That doesn’t look normal."

    show povn confused
    show elo confused_talk
    elo "Those are the Resemble Runes."
    elo "Or at least that’s what we call them."
    elo "They’re two identical, connected rocks that appeared in this town one day, just floating above the lake."
    elo "It does not adhere to gravity but we did manage to move it into this building using special, heavy-duty magnetic instruments."

    show povn confused_talk
    show elo confused
    pov "How?"

    show povn confused
    show elo bored_talk
    elo "It floats around like in outer space. It’s extremely abnormal."
    elo "Identical rocks don’t just appear in nature like this."
    elo "Especially ones that float."
    elo "We had to study it and figure out what its purpose is."
    elo "I believe it holds a purpose"

    show povn bored_talk
    show elo confused
    pov "Can you take me to it?"

    show povn bored
    show elo confused_talk
    elo "Why?"
    elo "Sorry but that’s top secret, you shouldn’t even be here!"

    show povn angry_talk
    show elo shocked
    pov "PLEASE!"
    pov "This is life or death, for real!"
    pov "I swear, I would never ask it if it weren’t important to saving my town."

    show povn angry
    show elo sad
    elo "..."
    show povn embarrassed
    show elo sad_talk
    elo "Alright."
    elo "I’ll take you."

    scene black
    with fade
    $ renpy.pause()
    "She takes you to the Rune Room..."

    $ main_story = 128

    jump lbl_the_rune_room
