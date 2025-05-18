## The Aftermath At Home
label lbl_the_aftermath_at_home:
    play music "audio/music/a_family_home.ogg"

    scene bg mylivingroom_day
    with fade
    show pov sad at left
    show sis sad at Position(xpos=1300)
    show mumc embarrassed_talk at right
    mum "Well, [povname]."
    mum "It’s back to uni for you."

    show pov bored
    show sis bored_talk
    show mumc embarrassed
    sis "And I still have work as usual."

    show pov sad
    show sis embarrassed
    show mumc sad_talk
    mum "Things are back to normal..."

    show sis sad_talk
    show mumc sad
    sis "Is it normal?"

    show sis sad
    show mumc embarrassed_talk
    mum "This is the new normal now, honey."
    show mumc sad_talk
    mum "*Sigh*"
    show mumc embarrassed_talk
    mum "We have to keep strong and look forward."
    show pov embarrassed
    show sis embarrassed
    mum "I’ve got some job interviews lined up so I’ve got to prepare for those."

    show pov embarrassed_talk
    show mumc embarrassed
    pov "Not gonna be a stay-at-home [mumrole] anymore, huh?"

    show pov embarrassed
    show mumc embarrassed_talk
    mum "I can’t afford to do that."
    mum "Even with money from the life insurance, we don’t want to start relying solely on it."
    mum "Plus, I need to get out of the house more."

    show pov neutral_talk
    show sis neutral
    show mumc embarrassed
    pov "It’ll be good for you."

    show pov neutral
    show mumc smirk_talk
    mum "We’ll still have nights together!"
    show mumc embarrassed_talk
    mum "And weekends."

    show sis smirk_talk
    show mumc neutral
    sis "Yeah, I guess huh."

    show sis neutral
    show mumc neutral_talk
    mum "Everything’s gonna be alright."
    mum "I promise you that."
    show mumc confused_talk
    mum "Now go on before you’re late."
    
    show pov embarrassed_talk
    show sis neutral
    pov "Seeya later, [missus]."
    pov "I love you."

    show pov neutral
    show sis neutral_talk
    sis "I love you, too, [missus]"

    show pov smirk
    show sis smirk
    show mumc embarrassed_talk
    mum "I love you too, my babies."
    mum "Stay safe, alright?"

    $ main_story = 134

    scene black
    with fade
    $ renpy.pause()
    "At campus..."

    jump lbl_campus_gossip
