## The Last Training Session
label lbl_the_last_training_session:
    ## SPRITES

    show povlg neutral at left
    show vio bored_talk at right
    with dissolve
    vio "Hello there, [povname]."
    show povlg embarrassed at left
    vio "Today’s the last day of your training…"
    show vio smirk_talk at right
    vio "It’s a little bit of a bittersweet moment."
    show povlg embarrassed_talk at left
    show vio smirk at right
    pov "Yeah, can’t believe this is it after today."
    show povlg embarrassed at left
    show vio smirk_talk at right
    vio "Well, the training part that is."
    show povlg neutral at left
    show vio smirk_talk at right
    vio "You’re always welcome to visit the beach as a simple beach goer or even as a volunteer."
    show povlg neutral_talk at left
    show vio smirk at right
    pov "That’s true."
    show povlg embarrassed_talk at left
    show vio neutral at right
    pov "It’s not goodbye."
    show povlg neutral_talk at left
    pov "It’s- see you next time."
    show povlg neutral at left
    show vio neutral_talk at right
    vio "Exactly!"
    show povlg smirk at left
    show vio bored_talk at right
    vio "So no tears."
    show povlg neutral at left
    show vio sad_talk at right
    vio "*Sniff*"
    show povlg smirk_talk at left
    show vio neutral at right
    pov "Why’d you say no tears and then immediately shed a tear?"
    show povlg smirk at left
    show vio neutral_talk at right
    vio "I was trying to prevent myself from crying but here we are."
    show povlg neutral_talk at left
    show vio neutral at right
    pov "It’s okay."
    pov "You still look super brave and strong."
    show povlg neutral at left
    show vio neutral_talk at right
    vio "Whether you cry or not doesn’t make you stronger or braver, [povname]."
    show povlg embarrassed at left
    show vio smirk_talk at right
    vio "Tsk tsk tsk."
    show vio embarrassed_talk at right
    vio "Think of that as your final lesson of life."
    show povlg confused at left
    vio "Things on the beach, and in life can get overwhelming and out of hand."
    show povlg neutral at left
    show vio bored_talk at right
    vio "But stay calm, keep a level head."
    show vio neutral_talk at right
    vio "You can overcome anything."
    show povlg embarrassed at left
    show vio shocked_talk at right
    vio "And don’t take that to mean that everything you do will be successful."
    show povlg neutral at left
    show vio smirk_talk at right
    vio "It means anything you do is possible within your abilities."
    show vio shocked_talk at right
    vio "Remember and trust your abilities."
    show povlg neutral_talk at left
    show vio shocked at right
    pov "Got it."
    show vio neutral at right
    pov "I’ll remember that to the day I meet my grave."
    show povlg neutral at left
    show vio smirk_talk at right
    vio "Good."
    show povlg shocked at left
    show vio confused_talk at right
    vio "Wanna do another 30 laps to the shore and back for old time’s sakes?"
    show povlg embarrassed_talk at left
    show vio confused at right
    pov "Uhm…"
    show vio shocked at right
    pov "Not really."
    show povlg smirk_talk at left
    show vio bored at right
    pov "Can’t we just spend our time together watching over the beach?"
    show povlg smirk at left
    show vio smirk_talk at right
    vio "Hahaha, no."
    show povlg bored at left
    show vio angry_talk at right
    vio "30 LAPS!"
    show vio smirk_talk at right
    vio "Let’s go!"
    show vio neutral_talk at right
    vio "I’ll race ya this time!"

    ## Violette runs off.
    hide vio
    with dissolve
    show povlg bored_talk at left
    pov "Ah shit, here we go again."

    ## Fade to black
    scene black
    with fade
    $ renpy.pause()
    "After one last training session with Violette…"
    $ renpy.pause()
    "Thank you for playing Violette's story. I hope you enjoyed her."

    ## SCENE END
    $ gtime = 2

    $ violette_path = 16

    jump lbl_townmap_setup
