## The Natural Spring
label lbl__the_natural_spring_hscene_revisit:
    scene thenaturalspring_hscene2
    with fade

    ## They continue playing with each other until they all cum in the spring
    $ renpy.pause()
    
    menu:
        "Cum":
            pass
        "Continue":
            jump lbl__the_natural_spring_hscene_revisit

    scene bg thenaturalspring_2_5
    with vpunch
    $ renpy.pause()
    pov "{i}*Pants*{/i}"
    pov "Thanks, girls."
    pov "I feel- totally relaxed now."

    mum "Good to hear, honey."

    sis "I'm not ready to leave yet."

    scene black
    with fade
    $ renpy.pause()

    jump lbl_vrheadset_character_selection

image thenaturalspring_hscene1:
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_1.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_3.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_4.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.4
    repeat

image thenaturalspring_hscene2:
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_1.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_3.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_4.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.25
    repeat
