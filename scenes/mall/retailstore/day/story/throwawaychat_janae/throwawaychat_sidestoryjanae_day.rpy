## Janae Main Story Throwaway Conversations Retail Store ##

## Spare Boxes
label lbl_retailstore_day_janae_spareboxes:
    default retailstore_spareboxes = 0
    show pov confused_talk at left
    show jan confused at right
    pov "I'm wondering if you have some spare boxes that I can use, Janae."
    show pov confused at left
    show jan embarrassed_talk at right
    jan "Oh, sorry..."
    jan "I can't help you there, [povname]. It's store policy to reuse all functioning boxes for our inventory."
    show pov confused_talk at left
    show jan confused at right
    pov "Not even a few boxes?"
    show pov bored at left
    show jan confused_talk at right
    jan "Sorry, [povname]. The manager's pretty strict about it."
    show jan bored_talk at right
    jan "They're all about the environment, y'know."
    show pov embarrassed_talk at left
    show jan embarrassed at right
    pov "{i}*Sigh*{/i} Alright, thanks anyway, Janae."
    show pov embarrassed at left
    show jan embarrassed_talk at right
    jan "Hope too see you around soon."
    
    $ retailstore_spareboxes = 1

    jump lbl_retailstore_day_setup
