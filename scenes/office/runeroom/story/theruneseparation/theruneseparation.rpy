## The Rune Separation
label lbl_the_rune_separation:
    scene black
    with fade

    xin "C'mon, El!"

    elo "*Grr* I'm- pulling!"
    scene bg theruneseparation_1
    with fade

    xin "PULL! ARRGHH!"

    elo "AAAGGH!!"

    show bg theruneseparation_2

    dad "AAAARRGHHH!!!"

    swdad "FUCCKING PULL!!!!!"

    dad "AAAAAAARRGHHH!"

    show bg theruneseparation_3

    swdad "FUUUCCCKKK!!!!"

    xin "*GRUNTSSS*"

    show bg theruneseparation_4

    dad "HEEAAVEE!"

    elo "PULL!!!"

    show bg theruneseparation_3
    $ renpy.pause(2,hard=True)
    show bg theruneseparation_5
    with hpunch

    dad "IT'S MOVING!"

    elo "IT MOVED!!"

    xin "DON'T FUCKING STOP!"

    show bg theruneseparation_5
    with hpunch
    $ renpy.pause(1,hard=True)

    show bg theruneseparation_6

    pov "Oh my God..."

    pri "What's happening...?"
    pri "Can anyone see anything?!"

    show bg theruneseparation_4
    with hpunch
    $ renpy.pause(2,hard=True)
    show bg theruneseparation_5
    $ renpy.pause(2,hard=True)
    show bg theruneseparation_7
    with hpunch
    
    elo "Jesus- d- don't stop..."

    dad "This-"

    swdad "This is it..."

    xin "*Pants* Eureka."

    show bg theruneseparation_8
    with hpunch
    "*BOOOOOMM CRAAASSHHH SHAATTERERRR*"

    pri "FUUCCKK!!!"

    pov "HOLY SHIT!"

    show bg theruneseparation_9
    with dissolve
    $ renpy.pause(2,hard=True)
    show bg theruneseparation_10
    $ renpy.pause()

    pri "Is everyone, okay?"

    eff "Y-yueah... was- was that a black hole?"

    show bg theruneseparation_11
    "Girl" "Help! MOM! HEEELP!"

    show bg theruneseparation_12
    with dissolve
    "*Vvvrrrnggg...*"

    "Girl" "*Pants*"

    show bg theruneseparation_13
    $ renpy.pause(0.5,hard=True)
    show bg theruneseparation_13
    $ renpy.pause(0.5,hard=True)
    scene black

    $ main_story = 132

    scene black
    with fade
    $ renpy.pause()

    jump lbl_apocalypse_aftermath
