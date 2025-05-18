## The Final Group Hug
label lbl_the_final_group_hug:
    scene bg schoolhallway1_day
    with fade
    show pov neutral at left
    show eff neutral_talk at Position(xpos=900)
    show jac smirk at Position(xpos=1200)
    show edw neutral at Position(xpos=1500)
    show col smirk at Position(xpos=1800)
    with dissolve
    eff "[povname]!"

    show eff neutral
    show jac smirk_talk
    jac "Buddy!"

    show jac smirk
    show edw neutral_talk
    edw "There’s the man!"

    show edw neutral
    show col smirk_talk
    col "Hey, big guy."

    show pov neutral_talk
    show col smirk
    pov "Sup, guys."
    show pov embarrassed_talk
    pov "Here we are, aye."

    show pov embarrassed
    show jac bored_talk
    jac "Can’t believe we still have to be here."

    show jac embarrassed
    show eff sad_talk
    eff "I’m really sorry about your..."
    eff "About everything that’s happened recently."

    show pov embarrassed_talk
    show eff embarrassed
    pov "Hey, we’re all here together now."
    pov "It’ll be fine."

    show pov confused
    show eff confused
    show edw neutral_talk
    edw "Did you hear, the TRC is back, I’ve got my internship there starting back up today."

    show pov neutral_talk
    show jac smirk
    show eff neutral
    show edw smirk
    pov "Congrats, Ed."

    show pov neutral
    show col smirk_talk
    col "I managed to run a successful fundraiser for the town and to help any families that have been struck by the blow rough."

    show pov smirk_talk
    show col smirk
    pov "Yeah, I saw. That’s super cool of you, Cole."
    pov "Didn’t know you had such a heart."

    show pov smirk
    show col smirk_talk
    col "Oh, pssh. C’mon, man."
    col "If there’s one thing I’m really good at."
    col "It’s making money."

    show pov confused
    show eff embarrassed_talk
    eff "And how are you, [povname]?"

    show pov embarrassed_talk
    show eff embarrassed
    pov "I’m-"
    pov "Good."
    pov "And you?"

    show pov embarrassed
    show eff embarrassed_talk
    eff "I’m... good too."

    show pov confused
    show eff confused
    show jac sad_talk
    jac "I’m not."
    jac "I overheard someone say something about an exam?"
    jac "I didn’t do jack shit all break."

    show pov smirk
    show jac sad
    show eff bored_talk
    eff "Really, Jacob?"

    show jac shocked_talk
    show eff smirk
    jac "This is serious!"

    show jac bored
    show edw smirk_talk
    edw "You need to chill, dude."

    show pov neutral_talk
    show edw smirk
    pov "Hahahaha!"
    show jac smirk
    pov "Let’s get the rest of the year over with."

    show pov shocked
    show eff smirk_talk
    eff "Group hug!!"

    show pov shocked_talk
    show jac smirk
    pov "Whaaa?!"

    show pov embarrassed
    show jac smirk_talk
    show edw shocked
    jac "WHoooh!"

    show jac smirk
    show col smirk_talk
    col "Oh why not! Lemme get in there!"
    
    show col smirk
    show edw sad_talk
    edw "I’m not really a hug-"

    scene bg thefinalgrouphug_1
    with fade
    $ renpy.pause()

    scene black
    with fade

    $ main_story = 136

    jump lbl_credits
