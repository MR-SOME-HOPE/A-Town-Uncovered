## Grundle Sam Side Story Throwaway Conversations Stuff Store ##
default stuffstore_spareboxes = 0

## Spare Boxes
label lbl_stuffstore_spare_boxes:
    show pov confused_talk at left
    show sam confused at right
    pov "Hey, I was wondering if you have any spare boxes that I can have."
    show pov confused at left
    show sam embarrassed_talk at right
    sam "Sorry, ma good sir."
    sam "I rarely have a need for a box let alone boxes {i}**snort*{/i}."
    show pov embarrassed at left
    show sam smirk_talk at right
    sam "A lot of my stuff would only need to be stored when I relocate my business. Hehehe~"
    show pov embarrassed_talk at left
    show sam neutral at right
    pov "Heh, alright then. Thanks, anyway."
    show pov confused at left
    show sam smirk_talk at right
    sam "Do you want to buy a-"
    show pov bored_talk at left
    show sam embarrassed at right
    pov "No- not right now, maybe later."

    $ stuffstore_spareboxes = 1

    jump lbl_stuffstore_day_setup
