## Buukakki Followers Are Everywhere
default buukakkifollowers_flyer = 0
default buukakkifollowers_grundlesam = 0
default buukakkifollowers_alanna = 0
default buukakkifollowers_violette = 0
default buukakkifollowers_hitomi = 0

label lbl_buukakki_followers_are_everywhere:
    scene bg mall_day
    with fade
    show pov confused_talk at left
    with dissolve
    pov "Hey! Can I get one of those."
    show pov confused at left
    "Distributor" "Sure! Here ya go. Do you got any questions or queries, please don’t hesitate to talk to use about it."
    show pov embarrassed_talk at left
    pov "Thanks, I-"

    ## CG of back of the flyer with no map

    pov "Wait- there’s no map."
    pov "Excuse me but wasn’t there a map on here before?"
    pov "I was actually wondering where it was supposed to lead us because the previous flyer I had included a map but I was confused as to where that location was."

    "Distributor" " Oh- well, you see. There was an error in the printing process and that section was messed up for a whole number of our flyers."
    "Distributor" " If you are really interested in it, we’d be happy to discuss it more in depth with you and sign you up!"

    ## In thought

    pov "{i}I think that’s a cover up. There’s no way the printing manage to fuck up in that way..{/i}"
    pov "{i}I really don’t wanna have to sign up with these bozos.{/i}"
    pov "{i}I’ll skip for now but I may need to play along later on.{/i}"

    ## Back to speech
    show pov confused_talk at left
    with dissolve
    pov "No, thanks. I would like to… mull it over some more first."
    show pov shocked_talk at left
    "Distributor" " Of course! Don’t be a stranger, we have many members around the town and we’ll be more than happy to talk with you."
    show pov bored_talk at left
    pov "{i}Great- I hope the others are able to get flyers with maps on them...{/i}"

    $ buukakkifollowers_flyer = 1

    call lbl_buukakki_followers_are_everywhere_check

    scene bg mall_day
    with fade

    jump lbl_mall_day_setup

label lbl_buukakki_followers_are_everywhere_check:
    if buukakkifollowers_flyer == 1 and buukakkifollowers_grundlesam == 1 and buukakkifollowers_alanna == 1:
        if buukakkifollowers_violette == 1 and buukakkifollowers_hitomi == 1:
            $ main_story = 152
        else:
            pass
    else:
        pass

    return
