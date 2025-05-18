## Recent Rumours ##
label lbl_recent_rumours:

    scene bg chalkboard_day
    with fade
    show mis confused_talk_forward_1
    with dissolve
    mis "Good morning, class."
    show mis bored_talk_forward_1
    mis "Before we begin today's lesson, I have been made aware of a series of rumors spreading through the hallways."
    mis "The university staff and faculty have come to a conclusion that we should try and clear these rumors up before they get out of control."
    show mis confused_talk_forward_1
    mis "We have been made aware that pictures of a certain individual have been shared across social platforms."
    show mis bored_talk_forward_1
    mis "And while we understand that this age of technology means everyone has a camera with them at all times."
    show mis confused_talk_forward_1
    mis "That still doesn't mean that you should feel encouraged to take pictures of people in... compromising... positions."
    show mis bored_forward_1
    "{i}*Whiirrrhhh*{/i}"
    show mis shocked_forward_1
    pas "{i}[povname], please report to Director Lashley's office. [povname], please report to the principal's office, immediately. That is all.{/i}"
    mis "..."
    clas "{i}*incomprehensible sniggering*{/i}"
    show mis embarrassed_talk_forward_1
    mis "Oh- well, [povname]. That's you."
    show mis angry_talk_forward_1
    mis "Hey, class! Quiet! Anyone who even breathes another word is going to get detention."
    show mis angry_forward_1
    pov "{i}*Sigh*{/i} Fuck my life."
    $ renpy.notify("New Objective: See Director Lashley in her Office")
    $ gtime = 1
    $ main_story = 44

    jump lbl_schoolhallway1_day_setup
