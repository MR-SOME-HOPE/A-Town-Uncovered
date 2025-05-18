## Caught Allaway with Jack ##
label lbl_caught_allaway_with_jack:

    scene bg schoolbathroommale_day
    with fade
    show pov confused at left
    with dissolve
    mis "Mhm- mhm- mhm- {i}*sniff*{/i}"
    mis "{i}*Sniff* *sobs*{/i}"

    menu:
        "Hello?":
            pass
        "Miss Allaway?":
            pass
        "Hey, are you alright?":
            pass
    pov "Miss?"
    pov "W-what are you doing in the men's bathroom stall?"
    show pov confused at left
    show mis sad_talk at right
    with dissolve
    mis "Shh.. shh... {i}*sniff*{/i}"
    mis "I just wanted to... get away. {i}*sniff*{/i}"
    mis "The ladies' room is already packed with students and I- didn't want them to hear me.."
    mis "{i}*Sniff*{/i} I- I'm sorry..."
    show pov sad_talk at left
    show mis sad at right
    pov "What is going on?"

    menu:
        "You can tell me.":
            show pov embarrassed_talk at left
            pov "You can tell me if something's bothering you."
        "Did I do something wrong?":
            pov "Did I do something wrong? Did I hurt you because if I did-"
        "Did someone hurt you?":
            show pov angry_talk at left
            pov "Did someone hurt you? Because if they did- I swear I'm gonna-"
    if missallaway_points >= 3:
        $ missallaway_points -= 3
    else:
        $ missallaway_points = 0
    $ renpy.notify("Your relationship with Miss Allaway has decreased by 3")
    show pov shocked at left
    show mis sad_talk at right
    mis "[povname]! Just... please!"
    mis "Don't pressure me!"
    show pov sad at left
    mis "I don't want to be interrogated right now."
    show mis sad at right
    mis "..."
    show pov sad_talk at left
    pov "Okay..."
    show pov sad at left
    show mis sad_talk at right
    mis "I-"
    mis "We-"
    mis "We n-"
    show pov confused at left
    mis "We need to talk."
    mis "In the classroom... I can't be seen in here."
    show mis sad at right
    pov "..."

    jump lbl_flashback_to_blackmail
