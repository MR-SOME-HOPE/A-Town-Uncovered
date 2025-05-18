## Hitomi Side Story Throwaway Conversations Comic Book Store ##
default comicbookstore_spareboxes = 0

## Spare Boxes
label lbl_comicbookstore_day_hitomi_spareboxes:
    show pov neutral_talk at left
    with dissolve
    show hit neutral at right
    with dissolve
    pov "Hey, Hitomi!"
    show pov smirk_talk at left
    show hit confused at right
    pov "Just wonder if you have any spare boxes that I can use."
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "Sorry but all our boxes are filled with stuff and we're actually on the look out for more."
    show hit sad_talk at right
    hit "Everything is going digital nowadays so it's rare to find people actually wanting to buy and keep physical copies."
    show hit smirk_talk at right
    hit "Thank God for the collectors and the enthusiasts though."
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "Damn... well, good luck with the store, Hitomi. Thanks for the help."
    show pov neutral at left
    show hit neutral_talk at right
    hit "Anytime, [povname]."

    $ comicbookstore_spareboxes = 1

    jump lbl_comicbookstore_day_setup
