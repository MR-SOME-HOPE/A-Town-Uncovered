## Unexpected Crisis
label lbl_unexpected_crisis:
    ## All of a sudden, cries of help from the water are heard, people are being
    # swept deeper into sea by a riptide.

    scene bg unexpectedcrisis_1
    with fade

    idk "HELP!!"
    idk "HEELPP!!"
    vio "Fuck-"
    vio "We’ve got someone out in the rips."
    vio "C’mon, [povname]."
    pov "Right."

    scene black
    with fade
    "You and Violette set out to rescue to helpless person from the strong riptide..."

    ## CG of Violette swimming after the drowning person

    ## CG of MC dragging them onto the beach

    ## CG of Violette giving CPR

    ## CG of person up and coughing up water

    ## Back to SPRITES

    scene bg beachmain_day
    with fade

    show povlg shocked_talk at left
    show vio neutral at right
    with dissolve
    pov "*Huff huff huff*"
    show povlg smirk_talk at left
    pov "My heart was pounding."
    show povlg shocked_talk at left
    show vio embarrassed at right
    pov "That was close!"
    show povlg smirk_talk at left
    pov "Holy shit-"
    show povlg smirk at left
    show vio embarrassed_talk at right
    vio "Phew…"
    show povlg embarrassed at left
    show vio neutral_talk at right
    vio "Good job, [povname]."
    show povlg confused at left
    show vio smirk_talk at right
    vio "Congratulations on a first and successful rescue."
    show povlg shocked_talk at left
    show vio smirk at right
    pov "My-"
    show povlg embarrassed_talk at left
    pov "My hands are shaking."
    show povlg embarrassed at left
    show vio neutral_talk at right
    vio "Hey, it’s all okay now."
    show povlg shocked at left
    vio "You did good."
    show vio smirk_talk at right
    vio "Heheh."
    show povlg embarrassed at left
    show vio neutral_talk at right
    vio "Proud of you."
    show povlg embarrassed_talk at left
    show vio neutral at right
    pov "I-"
    show povlg confused_talk at left
    pov "I didn’t really do anything…"
    show povlg embarrassed_talk at left
    show vio bored at right
    pov "You did most of the work."
    show povlg embarrassed at left
    show vio bored_talk at right
    vio "It’s a team effort, [povname]."
    show vio neutral_talk at right
    vio "No one lifeguard takes all the credit."
    show povlg neutral at left
    show vio bored_talk at right
    vio "It’s not even about the glory, it’s about saving the life no matter what."
    show povlg neutral_talk at left
    show vio neutral at right
    pov "It’s about saving their life, no matter what."
    show povlg smirk_talk at left
    pov "I got it."
    show povlg embarrassed_talk at left
    show vio confused at right
    pov "Watching you was really something-"
    show povlg neutral_talk at left
    show vio bored at right
    pov "I’m so happy to have seen you at work."
    show povlg neutral at left
    show vio smirk_talk at right
    vio "Hmmphehe!"
    show vio neutral_talk at right
    vio "That’s all for today, [povname]..."
    show povlg shocked at left
    vio "You can head on home for the day, I’ve got it all covered now."
    show povlg neutral_talk at left
    show vio smirk at right
    pov "Alright, let’s hope there isn’t any more last second rescues needed as I leave the-"

    # Reporter doesn't have sprites
    show povlg shocked at left
    show vio shocked at right
    with dissolve
    "Reporter" "Wait- hold on."
    "Reporter" "Can I get a word with you two?"
    show povlg confused_talk at left
    pov "Us?"
    show vio smirk_talk at right
    vio "Us?"
    show povlg confused at left
    vio "Why-?"
    show vio smirk at right
    "Reporter" "We just saw that rescue unfold before our very eyes and would love to do a quick new piece on today’s heroes."
    show vio smirk_talk at right
    vio "What’s so special about this rescue, we’re just doing our jobs."
    show povlg shocked at left
    show vio confused at right
    "Reporter" "A senior lifeguard and I assume a lifeguard in training?"
    show vio smirk at right
    "Reporter" "And by the looks of it, the only one this year, Vi?"
    show povlg smirk at left
    "Reporter" "This story could really inspire others in town to sign up for your training program."
    show vio bored at right
    "Reporter" "And I would get an enticing story for tonight."
    show povlg bored at left
    show vio confused at right
    "Reporter" "Doesn’t that sound like a win-win for the both of us?"
    show povlg confused at left
    vio "Hmm- what do you say, [povname]?"
    show povlg smirk_talk at left
    show vio neutral at right
    pov "I get to be on TV?"
    show povlg neutral at left
    "Reporter" "Well, the top half of you is."
    show povlg smirk_talk at left
    show vio smirk at right
    pov "I’ll take it!"

    ## Time skip
    scene black
    with fade
    $ renpy.pause()

    ## SCENE END

    $ violette_path = 10

    jump lbl_love_on_camera_at_the_beach
