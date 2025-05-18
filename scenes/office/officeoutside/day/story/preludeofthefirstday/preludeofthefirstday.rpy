#[Outside The Robotics Company offices, after school - “Prelude of the first day"  - main_story =90]

#-Scenes is available once the player has talked to Edward in school and headed into the office area-

#-If the player tries to head any other place or let time pass by napping or talking to someone, a message telling them to head to work will appear-


#-Mc shows into frame once the player clicks the building for the first time-
label lbl_prelude_of_the_first_day:
    scene bg townmap_day
    scene bg officeoutside_day with fade
    pov "Well, this is the place…"
    pov "Is this plain building really holding such an important company?"
    pov "I figured they'd be way bigger if anything."
    pov "Now where's that old man-"

    #-Dad appears into scene as the Mc says this-
    show pov bored at left
    with dissolve
    dad "Wasting energy waiting for your disrespectful ass."
    show pov shocked_talk at left
    show dad bored at right
    with dissolve
    pov "Gah! Where the hell did you come from?!"
    show pov shocked at left
    show dad bored_talk at right
    dad "Doesn't matter. You are late."
    show pov angry_talk at left
    show dad bored at right
    pov "I got here as soon as class ended!"
    show pov confused_talk at left
    pov "Need I remind you I have to walk here?"
    show pov angry at left
    show dad bored_talk at right
    dad "You should learn to manage your time better to get here on time."
    show pov confused_talk at left
    show dad smirk at right
    pov "What, were you expecting me to teleport here or something?"
    show pov confused at left
    show dad smirk_talk at right
    dad "Right now I expect you to lose that attitude of yours and keep your mouth shut."
    show pov bored at left
    show dad bored_talk at right
    dad "Once we go in you are going to have to fill some documents at the front desk with the receptionists and then the HR representative will come for you."
    show pov shocked_talk at left
    show dad shocked at right
    pov "You aren't even showing me around yourself?"
    show pov confused at left
    show dad shocked_talk at right
    dad "That's not my department and neither am I interested in wasting my day like that when I have work to do."
    show pov smirk_talk at left
    show dad confused at right
    pov "I'll be sure to count my blessings then."
    show pov bored at left
    show dad angry_talk at right
    dad "Watch it, mister."
    show dad shocked_talk at right
    dad "Just because I am not around to keep you in check doesn't mean you are off the hook."
    show pov shocked at left
    show dad angry_talk at right
    dad "These walls have ears and if I find out you are causing trouble that will reflect on me and cause trouble on my performance, there will be hell to pay."
    show pov bored at left
    show dad confused_talk at right
    dad "Do you understand me?"
    show pov bored_talk at left
    show dad confused at right
    pov "Yeah, yeah, yeah. You are big and scary."
    show dad bored at right
    pov "Can we get this over please?"
    show pov bored at left
    show dad bored_talk at right
    dad "Hmph, very well."
    show pov shocked at left
    show dad smirk_talk at right
    dad "But come in after me, the less people know we are related the better."
    show pov smirk_talk at left
    show dad bored at right
    pov "Funny, I was thinking the same thing."

    #-Dad glares at the mc one more time-
    show pov smirk at left
    show dad bored at right
    dad "…"
    show pov confused at left
    show dad bored_talk at right
    dad "Whatever…"
    show pov angry at left
    show dad angry_talk at right
    dad "Fucking punks these days…"

    #-Dad leaves the scene-
    hide dad
    with dissolve
    show pov angry_talk at left
    pov "Shit mustache prick…"
    show pov bored_talk at left
    pov "Sigh…"
    show pov embarrassed_talk at left
    pov "Well, here goes nothing."

    #=SCENE END=
    $ main_story = 91
    $ townmap_enabled = 0
    jump lbl_officeoutside_day
