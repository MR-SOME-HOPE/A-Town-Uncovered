## Fun Ride Home From Camp
label lbl_fun_ride_home_from_camp:
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
    jump lbl_fun_ride_home_from_camp_end

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

label lbl_fun_ride_home_from_camp_end:
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
    
    $ mumsiscamp_path = 15

    # "Dev Note" "Thank you for enjoying this family trip. Please let us know what kind of adventure these 3 should go on next!"

    scene bg myhousefront_day
    with fade

    jump lbl_myhousefront_day_setup