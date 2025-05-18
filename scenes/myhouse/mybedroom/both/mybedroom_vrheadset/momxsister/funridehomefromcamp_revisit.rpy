## Fun Ride Home From Camp
label lbl_fun_ride_home_from_camp_revisit:
    scene black
    with fade
    $ renpy.pause()
    "In the long car ride home..."

    scene img_funridehomefromcamp_1
    with fade
    $ renpy.pause()
    show img_funridehomefromcamp_2
    $ renpy.pause()
    show img_funridehomefromcamp_3
    $ renpy.pause()
    jump lbl_fun_ride_home_from_camp_revisit_end

image img_funridehomefromcamp_1:
    "bg funridehomefromcamp_1"
    pause 0.3
    "bg funridehomefromcamp_2"
    pause 0.1
    "bg funridehomefromcamp_3"
    pause 0.1
    "bg funridehomefromcamp_4"
    pause 0.2
    "bg funridehomefromcamp_2"
    pause 0.2
    repeat

image img_funridehomefromcamp_2:
    "bg funridehomefromcamp_1"
    pause 0.3
    "bg funridehomefromcamp_3"
    pause 0.1
    "bg funridehomefromcamp_4"
    pause 0.2
    "bg funridehomefromcamp_2"
    pause 0.2
    repeat

image img_funridehomefromcamp_3:
    "bg funridehomefromcamp_1"
    pause 0.2
    "bg funridehomefromcamp_3"
    pause 0.1
    "bg funridehomefromcamp_2"
    pause 0.2
    repeat

label lbl_fun_ride_home_from_camp_revisit_end:
    scene black
    with fade
    $ renpy.pause()
    
    if winc == 0:
        mum "We're almost home guys, finish up!"
        "Both" "We're cumming, [missus]!"
    else:
        mum "We're almost home kids, finish up!"
        "Both" "We're cumming, mom!"

    $ renpy.pause()
    
    jump lbl_vrheadset_character_selection