label lbl_meet_jaiden:
    #GeeSeki Note: Originally from military school, she transferred years ago but never really forgot how to behave like a soldier."
    #Her dad is a Sergeant or Lieutenant or some semi-high ranking officer (I don’t know much about ranks)."
    #She trains and exercises a lot, that’s her thing." Calls, MC maggot endearingly."

    #-You walk by a fit looking girl that seems just about ready to go on a run-
    show btn schoolgym_day_jaiden_idle
    $ renpy.pause(0.001)

    show pov confused at left
    with dissolve
    hide btn schoolgym_day_jaiden_idle
    show jai bored_talk at right
    with dissolve
    jai "Hey, you!"
    jai "Maggot!"
    show pov confused_talk at left
    show jai confused at right
    pov "Uhh…"
    pov "Are you talking to me?"
    show pov confused at left
    show jai bored_talk at right
    jai "Affirmative, soldier!"
    jai "I was told some fresh meat was coming, so I figured appropriate to introduce myself."
    show pov sad at left
    show jai neutral_talk at right
    jai "You may refer me to as Jaiden. Future soldier of our nation's proud army - and your worst nightmare if you are unlucky enough to cross me."
    show pov smirk_talk at left
    show jai bored at right
    pov "That's a long-ass title."
    show pov neutral at left
    show jai embarrassed_talk at right
    jai "Just Jaiden is fine."
    show pov neutral_talk at left
    show jai bored at right
    pov "Alright. Jaiden."
    pov "My name is [povname]."
    show pov confused at left
    show jai neutral_talk at right
    jai "Good to meet you, Maggot!"
    show pov confused_talk at left
    show jai bored at right
    pov "What? No, my name is-"
    show pov confused at left
    show jai bored_talk at right
    jai "You have to work your way up the ranks before I go about using your name, all willy-nilly, Maggot."
    jai "Respect is earned, after all."
    show pov confused_talk at left
    show jai confused at right
    pov "So you don’t call everyone maggot?"
    show pov bored at left
    show jai bored_talk at right
    jai "Very few have reached the rank of corporal, I am not much for social interaction when I could be using the time doing something else."
    show pov bored_talk at left
    show jai confused at right
    pov "Like?"
    show pov embarrassed at left
    show jai neutral_talk at right
    jai "Working out!"
    jai "I heard the mayor may reinstitute the town wide decathlon and the marathon for herpes awareness and I am going to destroy the competition."
    show pov neutral_talk at left
    show jai neutral at right
    pov "At least you are using your fitness powers for good."
    show pov neutral at left
    show jai neutral_talk at right
    jai "Of course! I get to kick herpes ass in a metaphorical way by running while also beating any other maggots in a literal sense by coming in first."
    jai "Both sides of the balance, best of both worlds."
    show pov smirk_talk at left
    show jai neutral at right
    pov "You seem like quite the health nut!"
    show pov neutral at left
    show jai neutral_talk at right
    jai "Ha! Don’t misunderstand me!"
    show pov bored at left
    show jai bored_talk at right
    jai "I am not like those hippie communists who mix whatever magic ingredient some so called ‘health guru’ told them into their tea."
    jai "And I am not one of those hulking monstrosities that downs an entire bucket of protein powder with every flex they make."
    show pov neutral at left
    show jai neutral_talk at right
    jai "I work out the way God intended: no chemicals or diets needed."
    jai "I am a woman who loves her burgers but knows how to burn the fat caused by them."
    show pov neutral_talk at left
    show jai neutral at right
    pov "That’s good to know…"
    show pov embarrassed at left
    show jai bored_talk at right
    jai "You wanna touch em?"
    show pov embarrassed_talk at left
    show jai confused at right
    pov "Excuse me?"
    show pov confused at left
    show jai neutral_talk at right
    jai "My abs! They are quite the sight."
    show pov confused_talk at left
    show jai neutral at right
    pov "Uhhh… Maybe later."
    show pov embarrassed at left
    show jai neutral_talk at right
    jai "Hah! Just messing with you [povname], no need to blush like a little girl!"
    show pov bored at left
    show jai bored_talk at right
    jai "So, enough about me. Do you work out?"
    show pov neutral_talk at left
    show jai neutral at right
    pov "I go for runs occasionally."
    show pov bored at left
    show jai bored_talk at right
    jai "Any weights or heavy lifting?"
    show pov bored_talk at left
    show jai confused at right
    pov "Not really my style."
    show pov confused at left
    show jai confused_talk at right
    jai "Nonsense! Those things change your life!"
    show pov confused_talk at left
    show jai confused at right
    pov "Heh, maybe. Sadly I don’t own any and I haven’t seen a gym anywhere in town to consider changing my workout schedule."
    show pov neutral at left
    show jai neutral_talk at right
    jai "I’ll lend you some if you ask nicely there."
    jai "I am sure I have some old low weight ones from where I first started."
    show pov neutral_talk at left
    show jai bored at right
    pov "How much do you lift now?"
    show pov shocked at left
    show jai neutral_talk at right
    jai "Enough to lift two of you."
    jai "Likely throw you like a javelin too."
    show pov shocked_talk at left
    show jai neutral at right
    pov "Wow."
    show pov confused at left
    show jai neutral_talk at right
    jai "Well, don’t mean to cut the conversation short but I have a schedule to keep and personal record to beat."
    jai "At ease, soldier!"
    show pov confused_talk at left
    show jai neutral at right
    pov "Uh… Right, see you later..."
    hide jai
    #-Jaiden leaves with a light jog-
    show pov confused at left
    pov "…"
    show pov confused_talk at left
    pov "I swear, this whole place is filled with weirdos."
    $ jaiden_path = 1
    $ add_contact("Jaiden")
    pause 0.2

    if gtime == 0:
        jump lbl_schoolgym_day_setup
    else:
        jump lbl_schoolyard_day_setup
