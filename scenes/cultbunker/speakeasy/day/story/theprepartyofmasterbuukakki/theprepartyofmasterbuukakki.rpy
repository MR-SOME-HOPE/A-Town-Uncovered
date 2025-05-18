## The Pre-Party of Master Buukakki
label lbl_the_preparty_of_master_buukakki:
    ## Fade to when you guys enter the speakeasy area.

    scene black
    with fade
    $ renpy.pause()
    "Inside the cult bunker..."

    ## CG
    ## A waiter comes up to you and offers Cole a glass of champagne.
    scene bg theprepartyofmasterbuukakki_1
    with fade
    $ renpy.pause(1,hard=True)
    show bg theprepartyofmasterbuukakki_2
    with dissolve

    col "{i}*Sips*{/i}"
    col "…"
    col "Mmmm! Really citrusy, that’s different but actually really nice."
    col "Jacob, you should try some."

    jac "…"

    ## Jacob glances behind the bar to see a girl squirting into the glasses.
    show bg theprepartyofmasterbuukakki_3

    jac "Uhhh-"
    jac "I should keep my senses clear, maybe on the way out."

    ## Around the room are people in gear going at it casually but also mingling.

    ## A hand-bell rings which signals the time to head into the main hall.
    "{i}*Ding ding ding*{/i}"

    "Member #1" "Oh- that's the bell."

    "Member #2" "Let's head in quick, I want good seats."

    "Member #3" "I'm so close to cumming but the ceremony is about to start."

    ## Everyone heads in.
    scene black
    with fade
    $ renpy.pause()
    "Everyone heads into the hall and takes their seats..."

    ## SCENE ENDS

    $ main_story = 174

    jump lbl_places_everyone
