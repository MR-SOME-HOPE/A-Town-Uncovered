## Followers of Master Buukakki
label lbl_followers_of_master_buukakki:
    ## CG SCENE
    ## At the mall on your journey to buy the gifts for Davendithas, you stumble
    # upon a bunch of "friendly" faces handing out flyers.
    scene bg followersofmasterbuukakki_1
    with hpunch
    "Distributor" "Here you, a flyer for you. Join the Followers of Master Buukakki!"

    ## You get a flyer shoved into you.

    # It’s an invitation to join ‘The Followers of Master Buukakki

    # On the other side is an unfinished map.
    show bg followersofmasterbuukakki_2
    pov "{i}What the hell is this?{/i}"
    pov "{i}Who’s Master Buukakki…{/i}"
    pov "{i}I’ll just keep this in my pocket for now.{/i}"
    show bg followersofmasterbuukakki_3
    pov "..."
    pov "...."
    pov "{i}Weirdos.{/i}"

    $ main_story = 147

    jump lbl_mall_day_setup
