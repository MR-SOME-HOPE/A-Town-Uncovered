## Effie's Dad Threatens You
label lbl_effies_dad_threatens_you:
    scene bg suburb_day
    with fade
    ## On the way to school the next day.

    idk "Hey!"

    pov "Huh?"

    ## Effie's Dad appears angry
    show pov confused at left
    show effdad angry_talk at right
    with dissolve
    effdad "Yeah! You, [povname]!"
    show pov confused_talk at left
    show effdad angry at right
    pov "Oh- hi?"
    pov "Can I help you?"
    show pov shocked at left
    show effdad angry_talk at right
    effdad "Yeah, you can."
    effdad "Stay away from Effie, you fucking degenerate."
    show pov shocked_talk at left
    show effdad angry at right
    pov "W-what?"
    pov "What happened? Is- she okay?"
    show pov confused at left
    show effdad smirk_talk at right
    effdad "I heard you two were seen streaking naked and busting ass at the park the other night."
    effdad "She doesn’t need to be hanging around losers like you."
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "If you wanna be an exhibitionist, do it on your own time and away from my darling girl."
    show pov shocked at left
    show effdad smirk_talk at right
    effdad "If I see you near her again, I swear I will fuck you up."
    show pov bored at left
    show effdad angry_talk at right
    effdad "You got me?"
    show pov confused_talk at left
    show effdad angry at right
    pov "Y-yes, sir."
    show pov embarrassed_talk at left
    pov "B-but it’s a whole misunderstanding, I swear. We didn’t-"
    show pov sad at left
    show effdad angry_talk at right
    effdad "Quit it."
    effdad "Stop making excuses and take responsibility for yourself for God’s sake."
    show effdad bored_talk at right
    effdad "Effie needs to focus on graduating and getting on with her life."
    show pov shocked at left
    show effdad angry_talk at right
    effdad "Boys like you are only here to drag her down and I’m not gonna let it happen."
    show pov sad at left
    show effdad bored_talk at right
    effdad "Consider this your only warning, bitch."
    show pov sad_talk at left
    show effdad angry at right
    pov "…"

    ## Eff’s dad leaves.

    # MC inner thoughts
    show pov shocked
    hide effdad
    with dissolve
    pov "What the fuck?"
    show pov smirk
    pov "How did he know?"
    pov "Probably have some alcoholic friends at the park that night, I wouldn’t be surprised. He acts like an alcoholic himself."
    show pov bored
    pov "…"
    show pov angry
    pov "Fuck him."

    ## SCENE ENDS

    $ main_story = 143

    scene black
    with fade
    $ renpy.pause()
    "Arriving at school..."

    jump lbl_mixed_school_reputation
