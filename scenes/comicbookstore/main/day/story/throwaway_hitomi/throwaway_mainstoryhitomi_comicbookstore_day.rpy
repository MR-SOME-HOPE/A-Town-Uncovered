## Hitomi Main Story Throwaway Conversations Comic Book Store ##
default comicbookstore_ajob = 0

## A Job
label lbl_comicbookstore_day_hitomi_ajob:
    show pov neutral_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    #call lbl_retailstore_counter_check
    pov "Hey, Hitomi."
    show pov neutral at left
    show hit neutral_talk at right
    hit "Hey, [povname]. Can I help you with anything?"
    show pov embarrassed_talk at left
    show hit embarrassed at right
    pov "I was actually wondering if you have a job opening here."
    show pov neutral_talk at left
    pov "Maybe I can help out with stuff."
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "Sorry to say but we're not really hiring."
    show pov confused at left
    hit "I can pretty much handle everything on my own and my granddad handles the behind the scenes side of the business."
    show pov confused_talk at left
    show hit neutral at right
    pov "What about the off-days where you're not available to take care of the store?"
    show pov confused at left
    show hit neutral_talk at right
    hit "The boys in the back are pretty much here every day and they've agreed to look after their 'second home' when I'm not around."
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "Hm, I guess that's a fair trade."
    show pov confused at left
    show hit confused_talk at right
    hit "Have you tried asking next door?"
    if adultstore_ajob == 0:
        show pov confused_talk at left
        show hit neutral at right
        pov "The adult store? I have not."
        show pov embarrassed at left
        show hit embarrassed_talk at right
        hit "Worth a try if you're desperate for one."
        show pov embarrassed_talk at left
        show hit neutral at right
        pov "I'll consider it... Thanks."
    else:
        show pov embarrassed_talk at left
        show hit embarrassed at right
        pov "Hazel? Yeah, I did. No luck."
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "Ah well, sorry I couldn't give you any better."
        show pov neutral_talk at left
        show hit neutral at right
        pov "I'll keep looking. Thanks, Hitomi."

    $ comicbookstore_ajob = 1

    jump lbl_comicbookstore_day_setup

## Buukakki Followers Are Everywhere - Hitomi
label lbl_buukakki_followers_are_everywhere_hitomi:
    ## SPRITE START NO BG NEEDED
    show pov confused_talk at left
    show hit shocked at right
    with dissolve
    pov "Hey, Hitomi."
    show pov confused at left
    show hit neutral_talk at right
    hit "Hey, [povname]. What can I find for ya?"
    show pov neutral_talk at left
    show hit confused at right
    pov "Nothing, except some answers."
    show pov shocked at left
    show hit smirk_talk at right
    hit "Alright, what questions do you have for me?"
    show pov smirk_talk at left
    show hit confused at right
    pov "Have you received one of these Master Buukakki flyers."
    show pov embarrassed at left
    show hit shocked_talk at right
    hit "Ughhh- of course. They came in the store and wouldn’t leave me alone until I took one for myself and a few to hand out to our customers."
    show hit bored_talk at right
    hit "Which between you and me, I ain’t doing. I threw them straight into the trash."
    show pov shocked at left
    show hit smirk_talk at right
    hit "What do I look like, an idiot? Miss me with that cult bullshit."
    show pov neutral_talk at left
    show hit neutral at right
    pov "Good call."
    show pov neutral at left
    show hit shocked_talk at right
    hit "But now they’re right outside on the streets shoving flyers in people’s flyers and trying to recruit people into whatever club, religion, cult, I don’t know."
    show hit smirk_talk at right
    hit "It’s kinda scaring of my regulars."
    show hit shocked_talk at right
    hit "They already have enough social anxiety, they don’t wanna be dealing with these overly-smiley freaks."
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "I can try and scare them away but-"
    show pov confused at left
    show hit neutral_talk at right
    hit "I already tried. They won’t budge, they pretend you don’t exist."
    show hit bored_talk at right
    hit "Fuckers."
    show pov bored_talk at left
    show hit bored at right
    pov "Well, alright. Thanks for talking to me about this."
    show pov neutral at left
    show hit embarrassed at right
    hit "Stay safe out there, don’t trust these losers one bit."

    $ buukakkifollowers_hitomi = 1

    call lbl_buukakki_followers_are_everywhere_check

    jump lbl_comicbookstore_day_setup
