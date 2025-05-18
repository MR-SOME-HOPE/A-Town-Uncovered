## Breaking News
label lbl_breaking_news:
    scene bg mylivingroom_day
    with fade
    show pov neutral at left
    with dissolve
    show sis neutral at Position(xpos=1300)
    with dissolve
    show mum bored_talk at right
    with dissolve

    mum "Remember to come straight from university unless you’re working today, young man."
    show pov sad at left
    mum "I have some chores you have left to do as punishment."
    show pov sad_talk at left
    show sis neutral at Position(xpos=1300)
    show mum neutral at right
    if winc == 0:
        pov "Yes, [missus]."
    else:
        pov "Yes, Mom."
    show pov neutral at left
    show sis neutral_talk at Position(xpos=1300)
    show mum neutral at right
    sis "If you do stop by Ice Cream’py, can you get me a tub of vanila? "
    sis "I’ll pay it back to you."
    show pov neutral_talk at left
    show sis neutral at Position(xpos=1300)
    show mum neutral at right
    pov "Yeah, sure thing."
    pov "I better get going."
    pov "See ya!"
    show pov embarrassed at left
    show sis bored at Position(xpos=1300)
    show mum neutral_talk at right
    mum "Have a nice day, sweetiecakes. I love you!"
    show pov embarrassed at left
    show sis smirk_talk at Position(xpos=1300)
    show mum embarrassed at right
    sis "Make sure to keep your pants on!"
    sis "Don’t make it a habit."
    show pov embarrassed_talk at left
    show sis smirk at Position(xpos=1300)
    show mum neutral at right
    pov "Tch- yeah, alright."
    hide pov embarrassed_talk
    hide sis smirk
    news "{i}*On TV* This just in-{/i}"
    show mum confused at right
    mum "Hmm..?"

    ## CG Scene Start
    ## bg breakingnews_x
    scene bg breakingnews
    with fade
    news "{i}The breaking and entering of a house in the suburbs has our little town in a panic.{/i}"
    news "{i}Police believe that this is tied to other numerous vandalistic incidents around town-.{/i}"

    $ main_story = 52

    $ townmap_enabled = 1

    jump lbl_stumbling_upon_the_crime
