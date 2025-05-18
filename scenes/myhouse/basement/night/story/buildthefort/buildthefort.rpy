## Build the Fort ##
label lbl_build_the_fort:

    scene bg mybasement_lightsonmessy
    with fade
    show pov confused_talk at left
    with dissolve
    show sis neutral at right
    with dissolve
    pov "Okay, I'm here. What's the plan of action?"
    show pov confused at left
    show sis neutral_talk at right
    sis "Well, what I was thinking was to have a sort of twin-tower front and simply build the fort around it."
    show pov confused_talk at left
    show sis neutral at right
    pov "Hmm, we'll see what we can pull off, there's not a lot of space down here."
    show pov confused at left
    show sis neutral_talk at right
    sis "I'll head upstairs and see if I can find some miscellaneous things to help radicalize this fort."
    show pov bored_talk at left
    show sis confused at right
    pov "I don't think that's what that word means."
    show pov confused at left
    show sis confused_talk at right
    sis "Doesn't miscellaneous mean, ‘unspecified entities' or something like that?"
    show pov confused_talk at left
    show sis confused at right
    pov "No, radicalize."
    show pov bored at left
    show sis confused_talk at right
    sis "Yeah, ‘to make radical', duh."
    show sis bored_talk at right
    sis "I might as well look for a thesaurus for you while I'm up there."
    show pov confused_talk at left
    show sis neutral at right
    pov "Whatever, you go look for stuff and I'll work out the general shape of it."
    show pov neutral at left
    show sis neutral_talk at right
    sis "Awesome. Can't wait to see the final result."

    scene bg buildafort_1
    with fade
    $ renpy.pause(2,hard=True)
    show bg buildafort_2
    with fade
    $ renpy.pause(2,hard=True)
    show bg buildafort_3
    with fade
    $ renpy.pause(2,hard=True)
    show bg buildafort_4
    with fade
    $ renpy.pause(2,hard=True)
    show bg buildafort_5
    with fade
    $ renpy.pause(2,hard=True)

    scene black
    with fade
    $ renpy.pause()

    scene bg buildafort_6
    with fade
    pov "There."
    pov "It's done."
    pov "It's complete."
    pov "It's-"
    sis "I love it."
    sis "Gosh golly, fuckity fuck, I love it so much."
    pov "..."
    pov "Are you cry-"
    sis "Shhh. You mustn't speak."
    sis "Just breathe it in."
    pov "..."
    pov "{i}*Inhale*{/i}"
    show bg buildafort_7
    $ renpy.pause(0.1,hard=True)
    show bg buildafort_8
    pov "{i}*cough cough*{/i} Fuck-"
    pov "{i}*gasp* *cough cough*{/i}"
    pov "{i}*gulp*{/i} Yuck..."
    pov "Dust."
    sis "..."
    sis "You just looove ruining moments like this, don't you?"
    pov "I didn't mean t- you told me to brea-"
    sis "Shut up. Let's climb inside."
    $ sister_path = 11
    $ townmap_enabled = 1

    jump lbl_under_cardboard_stars
