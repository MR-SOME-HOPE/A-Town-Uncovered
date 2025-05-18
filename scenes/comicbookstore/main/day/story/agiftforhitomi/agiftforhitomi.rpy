label lbl_a_gift_for_hitomi:
    #[Comic Book Store, Afternoon - “A gift for Hitomi”  - hitomi_path = 6]#5

    #-Before the next part of the side story can continue, MC has to cheer up Hitomi by handing her a gift after finding her still saddened by her recent failure-

    #-Mc approaches the counter of the comic book shop to find Hitomi still a down-
    show pov confused_talk at left
    show hit neutral at right
    with dissolve
    pov "Hey, Hitomi."
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "How's the webcomic going?"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Oh, hi [povname]..."
    hit "I've been trying to practice lately, but I'm still getting comments regarding the quality of the art."
    show pov embarrassed at left
    show hit confused_talk at right
    hit "I've been looking at a few tutorials and such online, but I'm still struggling with the basics…"
    show pov neutral_talk at left
    show hit confused at right
    pov "Well, you are just starting off, so it's natural to be struggling a bit to find your footing, right?"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "I guess…"
    show pov confused at left
    show hit shocked_talk at right
    hit "Though I'm getting people who are downright calling my art dog shit. And that's never fun to hear, even if I know I should just ignore 'em."
    show pov shocked at left
    show hit smirk_talk at right
    hit "Honestly, I don't really want to talk about the whole subject for a bit… or a while…"
    show pov embarrassed_talk at left
    show hit bored at right
    pov "I can imagine… Anything I can do to make you feel a little better?"
    show pov confused at left
    show hit bored_talk at right
    hit "Sweet of you to ask, but I don't think so…"
    show pov neutral_talk at left
    show hit shocked at right
    pov "Hmmm, gimme a sec, I'll come up with something - just you wait!"
    show pov shocked at left
    show hit confused_talk at right
    hit "W-Wait!"

    $ hitomi_path = 5.5

    jump lbl_comicbookstore_day

    #-SCENE TAKES A PAUSE HERE-

    #-The Player will have to go to the mall and get Hitomi a "Drawing Anatomy for the Struggling Artist" book in order to continue the scene-


label lbl_a_gift_for_hitomi_pt2:
    #-ONCE THE PLAYER RETURNS WITH THE BOOK ON THEIR INVENTORY-
    show pov neutral_talk at left
    show hit confused at right
    with dissolve
    pov "I'm back!"
    pov "And I managed to find something I think you are going to like~"
    show pov neutral at left
    show hit confused_talk at right
    hit "O-Oh?"
    hit "[povname], you didn't have to get me anything!"
    show pov embarrassed_talk at left
    show hit confused at right
    pov "Look, don't think about it too much. It's nothing, really!"
    show pov neutral_talk at left
    pov "Besides I already got it for you, and I'd feel really awkward if you asked me to return it, so here!"
    show pov confused at left
    show hit embarrassed_talk at right
    hit "Y-You really didn't have to…"
    show pov neutral at left
    show hit smirk_talk at right
    hit "B-But OK, since you already got it for me, then it would be rude to not receive it…"
    show pov neutral_talk at left
    show hit smirk at right
    pov "That's the spirit!"
    show pov shocked at left
    show hit embarrassed_talk at right
    hit "A book on anatomy?"
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "Well, yeah. Makes sense that if you are struggling with body proportions then you need to study anatomy, right?"
    show pov smirk_talk at left
    pov "Figured something like this could help you out in the long run."
    show pov smirk at left
    show hit embarrassed_talk at right
    hit "I…"
    show pov embarrassed at left
    show hit neutral_talk at right
    hit "This is really sweet of you, [povname]. Thank you so much!"
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "Don't mention it. Did it make you feel a little better?"
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "A-A lot, actually."
    show pov neutral at left
    show hit embarrassed at right
    pov "That's good enough for me, then. I wanna keep reading your webcomic, so hopefully with this it will help you keep going for a while!"
    show pov neutral at left
    show hit smirk_talk at right
    hit "It definitely will! I'll get to studying it right away!"
    show hit neutral_talk at right
    hit "Think you can come by later, once I've had time to practice with it?"
    show pov neutral_talk at left
    show hit smirk at right
    pov "Sure thing!"
    pov "I can't wait to see how you improve, with it!"
    show pov neutral at left
    show hit neutral_talk at right
    hit "Thank you so much, once again. You really didn't have to do this."
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "Don't sweat it, I'm happy to help."
    pov "I'll see you later, then!"
    show pov neutral at left
    show hit smirk_talk at right
    hit "Sure thing!"
    hit "Don't be a stranger!"

    #-After this scene, the player will have to wait 5 days for the next scene to take place-

    #=SCENE END=
    $ hitomi_path = 6

    $ inventory.drop(Items.drawinganatomy)

    jump lbl_comicbookstore_day
