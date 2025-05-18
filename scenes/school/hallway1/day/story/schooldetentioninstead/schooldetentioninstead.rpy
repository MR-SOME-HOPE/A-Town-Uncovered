## School Detention Instead
label lbl_school_detention_instead:
    scene bg schoolhallway1_day
    with fade
    ## You’re greeted in the hallway by Officer Mina and Director Lashley
    # Use pov, min, and pri for sprites
    show pov confused at left
    show min shocked_talk at Position(xpos=1200)
    show pri confused at Position(xpos=1600)
    with dissolve
    mina "There he is."
    show min neutral at Position(xpos=1200)
    show pri embarrassed_talk at Position(xpos=1600)
    pri "[povname]. Come here."
    show pri neutral_talk at Position(xpos=1600)
    pri "I think you’re pretty familiar with Officer Mina by now."
    show pri bored_talk at Position(xpos=1600)
    pri "I must say, I’m very disappointed in you."
    show pov smirk at left
    show min neutral_talk at Position(xpos=1200)
    show pri shocked at Position(xpos=1600)
    mina "Look, kid. If you want to be a nudist, there’s literally a nudist beach."
    show pov embarrassed at left
    show min smirk_talk at Position(xpos=1200)
    show pri bored at Position(xpos=1600)
    mina "But you can’t just go around in any public setting and throw your junk around in people’s face."
    show pov smirk_talk at left
    show min shocked at Position(xpos=1200)
    pov "What?! Who said I did that?"
    show pov embarrassed at left
    show min smirk_talk at Position(xpos=1200)
    mina "I have had reports. Again."
    show min shocked_talk at Position(xpos=1200)
    mina "{i}*Sigh*{/i}"
    show pov confused at left
    show min smirk_talk at Position(xpos=1200)
    show pri embarrassed at Position(xpos=1600)
    mina "And because I don’t want to do any paperwork, I’ve decided to let your dean take care of it."
    mina "I see you’re a good kid with a clean record and student history."
    show min neutral_talk at Position(xpos=1200)
    mina "So I’m letting you off this one and only last time, [povname]."
    show min smirk_talk at Position(xpos=1200)
    show pri embarrassed at Position(xpos=1600)
    mina "Next time, it’s really gonna affect the rest of your life."
    show min neutral at Position(xpos=1200)
    show pri  at Position(xpos=1600)
    mina "Being on the sex offender’s registry is not something you want to be on."
    show min smirk at Position(xpos=1200)
    show pri smirk_talk at Position(xpos=1600)
    pri "You hear that, [povname]? This is serious."
    show pov sad at left
    show min neutral at Position(xpos=1200)
    show pri bored_talk at Position(xpos=1600)
    pri "Now, thank Officer Mina for letting you off so easily."
    show pov confused at left
    show pri neutral_talk at Position(xpos=1600)
    pov "…"
    show pov smirk_talk at left
    show pri neutral at Position(xpos=1600)
    pov "Thanks, Officer Mina."
    show pov bored at left
    show min shocked at Position(xpos=1200)
    show pri embarrassed_talk at Position(xpos=1600)
    pri "God bless you, Officer."
    pri "I got it from here."
    show min neutral_talk at Position(xpos=1200)
    show pri neutral at Position(xpos=1600)
    mina "I’ll leave you to it, I’ve got criminals to catch."
    show min smirk_talk at Position(xpos=1200)
    show pri shocked at Position(xpos=1600)
    mina "Just kidding, I haven’t had breakfast yet, might grab a bite at the cafe."
    show min smirk_talk at Position(xpos=1200)
    show pri neutral at Position(xpos=1600)
    mina "They have really good croissant sandwiches."
    show min neutral at Position(xpos=1200)
    show pri neutral_talk at Position(xpos=1600)
    pri "Enjoy them!"

    ## Mina leaves.
    show pov confused at left
    hide min
    show pri bored_talk at right
    with dissolve
    pri "Now."
    pri "The consequences."
    show pov smirk_talk at left
    show pri bored at right
    pov "More consequences…"
    show pov sad_talk at left
    pov "I really am just getting beaten down and down…"
    show pov embarrassed at left
    show pri angry_talk at right
    pri "Detention. After school detention."
    show pov shocked at left
    show pri bored_talk at right
    pri "You’ll need to attend detention for the rest of the semester."
    show pov shocked_talk at left
    show pri bored at right
    pov "The whole semester?!"
    show pov confused at left
    show pri smirk_talk at right
    pri "Did you prefer I make it the whole year?"
    show pov smirk at left
    show pri angry_talk at right
    pri "Maybe I should make you write 10,000 lines."
    show pov smirk_talk at left
    show pri angry at right
    pov "No! No, the rest of the semester is good."
    pov "I’m sorry."
    show pov embarrassed at left
    show pri bored_talk at right
    pri "You best be."
    pri "You can start with today."
    show pri shocked_talk at right
    pri "Now, head to class before you give me more reasons to punish you."
    show pov embarrassed at left
    show pri bored at right
    pov "Yes, Ma’am…"

    ## Head to classroom and disable townmap so they HAVE to attend class.

    ## SCENE END

    $ main_story = 145
    $ townmap_enabled = 0

    jump lbl_schoolhallway1_day_setup
