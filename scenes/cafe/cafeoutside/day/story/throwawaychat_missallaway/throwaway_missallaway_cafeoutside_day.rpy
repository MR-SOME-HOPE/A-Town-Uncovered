## Throwaway Miss Allaway Cafe Day Conversation ##
label lbl_cafeoutside_day_missallaway:
    show btn cafeoutside_day_missallaway_idle
    if main_story == 84:
        pov "{i}I've already talked to her.{/i}"
        jump lbl_cafeoutside_day
## Main Story Conversation
    #if main_story == 33:
    #    jump lbl_cafeoutside_daysexworld_missallaway_1
    menu:
        "Talk":
            jump lbl_cafeoutside_day_missallaway_convo
        "Give Gift" if selecteditem != None:
            jump lbl_missallaway_giftgiving
        "Nevermind":
            jump lbl_cafeoutside_day

label lbl_cafeoutside_day_missallaway_convo:
## 1 - 4 is morning exclusive
## 5 - 8 is afternoon exclusive
## 9 - 11 is the weekend morning exclusive (cafe)
## 12 - 15 is interchangeable
    if gtime == 0:
        if date == 1 or date == 20 or date == 26 or date == 31:
            jump lbl_cafeoutside_day_missallaway_9
        elif date == 2 or date == 16 or date == 27:
            jump lbl_cafeoutside_day_missallaway_10
        elif date == 5 or date == 13 or date == 28:
            jump lbl_cafeoutside_day_missallaway_11
        elif date == 6 or date == 17 or date == 29:
            jump lbl_town_day_missallaway_12
        elif date == 9 or date == 18 or date == 30:
            jump lbl_town_day_missallaway_13
        elif date == 10 or date == 12 or date == 25:
            jump lbl_town_day_missallaway_14
        elif date == 7 or date == 14 or date == 21:
            jump lbl_town_day_missallaway_15
        elif date == 8 or date == 15 or date == 22:
            jump lbl_cafeoutside_day_missallaway_9
        elif date == 4 or date == 11 or date == 23:
            jump lbl_cafeoutside_day_missallaway_10
        elif date == 3 or date == 19 or date == 24:
            jump lbl_cafeoutside_day_missallaway_11

## Weekend Morning
label lbl_cafeoutside_day_missallaway_9:
    show pov neutral_talk at left
    with dissolve
    show misc neutral at right
    hide btn cafeoutside_day_missallaway_idle
    with dissolve
    pov "Hey, Miss. Enjoying the coffee aroma?"
    show pov neutral at left
    show misc neutral_talk at right
    mis "Just being here makes me relaxed and.."
    show misc shocked_talk at right
    mis "{i}*yawn*{/i}"
    show misc embarrassed_talk at right
    mis "Oh gosh, sorry about that. It's the coffee."
    show pov smirk_talk at left
    show misc neutral at right
    pov "Isn't that the opposite of what it's supposed to do to you?"
    show pov neutral at left
    show misc neutral_talk at right
    mis "My body is most likely 35 percent water, 35 percent coffee."
    show pov neutral at left
    show misc neutral_talk at right
    mis "So much so that I skipped the whole energy spike and went straight to the drop."

    jump lbl_cafeoutside_day

label lbl_cafeoutside_day_missallaway_10:
    show pov neutral_talk at left
    with dissolve
    show misc neutral at right
    hide btn cafeoutside_day_missallaway_idle
    with dissolve
    pov "Good morning, Miss. Good to see you here."
    show pov neutral at left
    show misc neutral_talk at right
    mis "Likewise, [povname]. You should try today's special."
    show pov neutral_talk at left
    show misc smirk at right
    pov "What is it?"
    show pov confused at left
    show misc smirk_talk at right
    mis "Coffee cake."
    show pov bored_talk at left
    show misc confused at right
    pov "Isn't that always the special?"
    show pov smirk at left
    show misc confused_talk at right
    mis "... Coffee cake is never NOT special."

    jump lbl_cafeoutside_day

label lbl_cafeoutside_day_missallaway_11:
    show pov neutral at left
    with dissolve
    show misc neutral_talk at right
    hide btn cafeoutside_day_missallaway_idle
    with dissolve
    mis "Hey! [povname]! How are you?"
    show pov neutral_talk at left
    show misc neutral at right
    pov "I'm well. Yourself?"
    show pov neutral at left
    show misc smirk_talk at right
    mis "Never better."
    show pov neutral_talk at left
    show misc smirk at right
    pov "What got you in such a good mood?"
    show pov neutral at left
    show misc smirk_talk at right
    mis "I'm a woman of simple desires. I see pastries, I smile."
    show pov smirk_talk at left
    show misc shocked at right
    pov "Are you calling me a pastry?"
    show pov smirk at left
    show misc smirk_talk at right
    mis "Ha! You're funny."

    jump lbl_cafeoutside_day
