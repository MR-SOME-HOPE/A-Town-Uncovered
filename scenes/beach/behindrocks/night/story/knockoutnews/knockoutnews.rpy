label lbl_knockout_news:
    #[Beach behind the rocks, morning - “Knockout News”  - main_story =108]

    # Summary: -Mc arrives at the beach past the rocks, he starts looking for Jacob and Effie
    # when he suddenly receives a phone call from Edward, who is beyond panicked
    # over what he’s found. As Mc is attempting to calm Edward down and figure out
    # what he has to tell him that has him so scare, a shadowy figure (Jacob)
    # approaches the mc from behind the rocks and as soon as Edward is able to
    # tell the Mc what he wants to say, he is knocked out by the figure before
    # being dragged away and his phone taken away from the sand as Edward screams
    # for him-

    #-MC arrives at the beach past the rocks point-
    scene bg knockoutnews_sky
    with fade
    $ renpy.pause(0.5)

    show povbody knockoutnews_sky_nophone
    show eyes knockoutnews_sky_up
    show povexpression knockoutnews_sky_confused
    with dissolve
    $ renpy.pause(0.5)
    show povexpression knockoutnews_sky_confused_talk
    pov "Jacob? Effie? Are you guys here yet?"
    show eyes knockoutnews_sky_right
    show povexpression knockoutnews_sky_bored_talk
    pov "…"
    show eyes knockoutnews_sky_down
    pov "Huh, seems like I’m early…"
    show eyes knockoutnews_sky_up
    show povexpression knockoutnews_sky_confused_talk
    pov "That’s weird, considering Jacob was apparently already on his way here when he woke me up with his call…"
    pov "Maybe he went to the comic book shop while waiting for Effie? I should probably call him or-"

    #-Mc’s Phone starts to ring-
    show eyes knockoutnews_sky_down
    show povexpression knockoutnews_sky_bored_talk
    pov "Huh, speak of the devil…"

    show povbody knockoutnews_sky_withphone with dissolve
    show eyes knockoutnews_sky_right
    #-Mc picks up the phone-
    $ renpy.pause(0.5)

    show povexpression knockoutnews_sky_bored_talk
    pov "Hey, Jaco-"
    show eyes knockoutnews_sky_up
    show povexpression knockoutnews_sky_shocked
    edw "[povname]!" with hpunch
    show eyes knockoutnews_sky_right
    show povexpression knockoutnews_sky_shocked_talk
    pov "Gah! Edward!"
    show povexpression knockoutnews_sky_angry_talk
    pov "Jesus Christ, what’s with everyone calling me today just to yell in my ear?!"
    show povexpression knockoutnews_sky_angry
    edw "I’m sorry but that’s really not important right now! I need you to come to my house RIGHT THE FUCK NOW!"
    show eyes knockoutnews_sky_down
    show povexpression knockoutnews_sky_confused_talk
    pov "What? Why?"
    pov "Did something happen to the recordings?!"

    #-A shadowy figure comes out from the rocks behind the Mc in the distance-
    show povexpression knockoutnews_sky_confused
    edw "No, dude. The problem is what the recordings captured!"
    edw "Where are you right now?"
    show eyes knockoutnews_sky_right
    show povexpression knockoutnews_sky_confused_talk
    pov "Uhh… I’m at the private spot at the beach past the rocks."
    show eyes knockoutnews_sky_up
    show povexpression knockoutnews_sky_embarrassed_talk
    pov "I agreed with Jacob and Effie that I would meet them here in the morning and-"

    #-The figure gets closer-
    show jacshadow knockoutnews_sky_1 behind povbody with dissolve
    show eyes knockoutnews_sky_right
    show povexpression knockoutnews_sky_confused
    edw "NO!"
    edw "NO NO NO NO NO, DUDE! STAY THE FUCK AWAY FROM THE WATER!"
    show eyes knockoutnews_sky_down
    show povexpression knockoutnews_sky_bored
    edw "THE PARK! THE BEACH! FUCK, MAYBE EVEN YOUR OWN BATHTUB! I DON’T KNOW ANYMORE!"
    show povexpression knockoutnews_sky_bored_talk
    pov "Edward, slow down a little! I can barely understand you!"

    #-The figure gets even closer-
    show jacshadow knockoutnews_sky_2 with dissolve
    show eyes knockoutnews_sky_up
    show povexpression knockoutnews_sky_bored
    edw "JESUS CHRIST, DUDE. ARE YOU GOING TO ACT LIKE YOU DON’T KNOW WHAT I’M TALKING ABOUT?!"
    show eyes knockoutnews_sky_down
    show povexpression knockoutnews_sky_confused
    edw "YOU WERE RIGHT, DUDE! YOU WERE FUCKING RIGHT! THERE IS SOMETHING IN THE LAKE OF THE PARK!"
    show povexpression knockoutnews_sky_shocked_talk
    pov "What?!"

    #-The figures get even closer, now standing right behind the MC-
    show jacshadow knockoutnews_sky_3 with dissolve
    show povexpression knockoutnews_sky_confused
    edw "THEY ARE IN THE WATER, DUDE!"
    edw "THEY ARE COMING OUT OF THE GODDAMNED WATER!"
    show povexpression knockoutnews_sky_confused_talk
    pov "W-Wait… YOU MEAN THAT THEY CROSSED OVER HERE?!"

    #-The shadowy figure knocks out the Mc by hitting him on the backside of the
    # head with a large object and the Mc falls unconscious face first into the sand.
    # Here have a shot of the back of the Mc’s head or hand on one side of the
    # scene while on the other side is his phone resting on the sand after it fell-
    scene bg knockoutnews_sand with hpunch
    scene bg knockoutnews_sand_povbody1_eyesopen with fade
    with vpunch
    $ renpy.pause(0.5)
    scene bg knockoutnews_sand_povbody1_eyesclosing with dissolve
    scene bg knockoutnews_sand_povbody1_eyesclosed with dissolve
    $ renpy.pause(1.0)


    edw "[povname]?"
    edw "DUDE?!"
    edw "WHAT WAS THAT SOUND? ARE YOU OKAY?!"


    #-The Mc’s body starts to be dragged away from the scene-
    with hpunch
    scene bg knockoutnews_sand_povbody2_eyesclosed with dissolve
    edw "OH JESUS, OH JESUS, OH FUCK!"
    edw "DUDE, PLEASE SAY SOMETHING, FOR THE LOVE OF GOD!"

    #-The rest of the Mc is dragged out of the shot-
    with hpunch
    scene bg knockoutnews_sand_povbody2_eyesclosed with dissolve
    $ renpy.pause(2.0)
    with hpunch
    scene bg knockoutnews_sand_povbody3_eyesclosed with dissolve
    $ renpy.pause(2.0)
    with hpunch
    scene bg knockoutnews_sand_povbody4_eyesclosed with dissolve
    $ renpy.pause(2.0)
    with hpunch
    scene bg knockoutnews_sand_povbody5_eyesclosed with dissolve
    $ renpy.pause(2.0)
    with hpunch
    scene bg knockoutnews_sand_povbody6_eyesclosed with dissolve
    $ renpy.pause(2.0)
    with hpunch
    scene bg knockoutnews_sand_povbody7_eyesclosed with dissolve
    $ renpy.pause(2.0)
    with hpunch
    scene bg knockoutnews_sand_povbody8_eyesclosed with dissolve
    $ renpy.pause(2.0)
    with hpunch
    scene bg knockoutnews_sand with dissolve
    $ renpy.pause(2.0)


    edw "WHAT DO I DO, WHAT DO I DO?!"
    edw "THIS IS WAY MORE THAN WHAT I SIGNED UP FOR, DUDE!"
    window hide dissolve
    #-The figure returns and stands next to the phone before bending over to pick it up and the scene fades to black-
    #=SCENE ENDS=

    scene black with fade
    $ renpy.pause()

    $ main_story = 109

    jump lbl_headache_awakening
