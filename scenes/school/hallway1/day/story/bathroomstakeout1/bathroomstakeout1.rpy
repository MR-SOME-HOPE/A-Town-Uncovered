label lbl_bathroom_stakeout_1:
    ## IF principallashley_path == 7 ##
    ###-Button of  Lashley - Player stumbles upon Lashley when approaching the bathrooms, she is looking shifty and out of place just standing next to the door to the girl's restroom-

    scene bg bathroomstakeout_1
    with fade
    show pri confused_talk at right
    with dissolve
    pri "It's about time for her to come, if my sources are right…"
    show pri shocked at right
    pov "Director Lashley?"
    show pri shocked_talk at right
    pri "Gah!"
    show pov confused at left
    with dissolve
    show pri embarrassed_talk at right
    pri "W-What, [povname]?!"
    show pri sad_talk at right
    pri "Don't appear out of nowhere like that! You are going to give me a heart attack!"
    show pov embarrassed_talk at left
    show pri embarrassed at right
    pov "Sorry, sorry! I didn't mean to scare you."
    show pov confused_talk at left
    show pri shocked at right
    pov "Though, to be fair here; you are the one standing in the middle of the hallway, all shifty like."
    pov "What are you doing?"
    show pov confused at left
    show pri sad_talk at right
    pri "{i}*Sigh.*{/i}"
    pri "Stealth has never been a strong suit of mine."
    show pri bored_talk at right
    pri "Well, if you must know: I'm currently working on seizing the operations of a certain student."
    show pov confused_talk at left
    show pri angry at right
    pov "Drugs?"
    show pov confused at left
    show pri angry_talk at right
    pri "Worse, a sex for favor operation."
    show pov confused_talk at left
    show pri angry at right
    pov "Prostitution, really?"
    pov "Nowadays you just have to open a cosplay webcam channel and tease guys who are willing to pay thousands for it."

    ##-If is aware of Sisters Livestreams 'sister_path = 5'-
    if sister_path >= 6:
        show pri confused at right
        pov "{i}*Mumbling to self*{/i} I speak from personal experience, now that I think about it…"
        show pov shocked at left
        show pri confused_talk at right
        pri "What's that?"
        show pov embarrassed_talk at left
        show pri confused at right
        pov "N-Nothing!"
        pov "I didn't say anything!"

    show pov embarrassed at left
    show pri bored_talk at right
    pri "Well, that does happen here as well. But there is not much I can do as long as it's outside of university premises or the girls hide their faces."
    show pov confused at left
    show pri confused_talk at right
    pri "No, this is something that has come to my attention rather recently."
    show pov shocked at left
    pri "There seems to be a student giving out her body in exchange of money and other services."
    show pri bored_talk at right
    pri "so I’m in the middle of mounting a stakeout operation to find out who it is."
    show pov confused_talk at left
    show pri smirk at right
    pov "And punish them for it?"
    show pov confused at left
    show pri embarrassed_talk at right
    pri "Well, yes and no."
    show pov shocked at left
    show pri angry_talk at right
    pri "My main goal is to find out why exactly is she willing to sell something as sacred as her body."
    show pov embarrassed at left
    show pri smirk_talk at right
    pri "It is not my place to judge you for your decisions, however, if a student has found themselves in such a struggling financial situation that they see prostitution as a viable option, it is my duty as God's follower to show them there is a different way."
    show pri bored_talk at right
    pri "This sort of things tend to follow you for the rest of your life."
    show pri sad_talk at right
    pri "I don’t want the poor girl to suddenly wake up one day, unable to live with herself for the mistakes she did when she was young. Or for the burden of being known around the university as a whore, to slowly chip away at her sanity."
    pri "People can be rather ruthless, especially at this time in your lives."
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "There’s also the possibility the girl simply enjoys sex, you know?"
    show pov embarrassed at left
    show pri angry_talk at right
    pri "Not my place to judge, but you have to admit."
    pri "There is a time and place for everything; and a university bathroom is no place to be having sex for money."
    pri "Much less under my watch."
    show pov embarrassed_talk at left
    show pri angry at right
    pov "True enough, I guess."
    show pov embarrassed at left
    pov "..."
    show pov embarrassed_talk at left
    show pri angry at right
    pov "So…"
    show pri confused at right
    pov "You are just going to wait until a girl just so happens to enter the restroom with a guy in toe?"
    show pov confused at left
    show pri confused_talk at right
    pri "Don’t be silly, [povname]."
    show pov shocked at left
    show pri smirk_talk at right
    pri "No, I’m waiting for my chance to slip into the restroom unnoticed and wait for my suspects to arrive."
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "Don’t you have paperwork or something else to do toda-"
    show pov shocked at left
    show pri shocked_talk at right
    pri "No one's looking, quickly hide!"
    show pov shocked_talk at left
    show pri shocked at right
    pov "W-Wait, I’m coming in too?!"

    #$ principallashley_path = 8

    jump lbl_trapped_in_the_stalls
    #=SCENE END=
