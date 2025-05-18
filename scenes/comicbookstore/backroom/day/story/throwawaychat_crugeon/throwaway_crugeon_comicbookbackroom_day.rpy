## Throwaway Crugeon Comic Book Back Room Day Conversation ##
label lbl_comicbookbackroom_day_crugeon:
    show btn_comicbookbackroom_day_crugeon_idle2
    show btn_comicbookbackroom_day_davendithas_idle2
    show btn_comicbookbackroom_day_lordkev_idle2
    $ renpy.pause(0.001)
    hide btn_comicbookbackroom_day_crugeon_idle2
    jump lbl_comicbookbackroom_day_crugeon_convo

label lbl_comicbookbackroom_day_crugeon_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 4 or date == 18 or date == 22 or date == 31:
            jump lbl_comicbookbackroom_day_crugeon_1
        elif date == 7 or date == 11 or date == 30:
            jump lbl_comicbookbackroom_day_crugeon_2
        elif date == 8 or date == 17 or date == 23:
            jump lbl_comicbookbackroom_day_crugeon_3
        elif date == 10 or date == 12 or date == 29:
            jump lbl_comicbookbackroom_day_crugeon_4
        elif date == 9 or date == 16 or date == 26:
            jump lbl_comicbookbackroom_day_crugeon_5
        elif date == 2 or date == 19 or date == 25:
            jump lbl_comicbookbackroom_day_crugeon_11
        elif date == 1 or date == 14 or date == 28:
            jump lbl_comicbookbackroom_day_crugeon_12
        elif date == 3 or date == 15 or date == 27:
            jump lbl_comicbookbackroom_day_crugeon_13
        elif date == 5 or date == 13 or date == 24:
            jump lbl_comicbookbackroom_day_crugeon_14
        elif date == 6 or date == 20 or date == 21:
            jump lbl_comicbookbackroom_day_crugeon_15
    elif gtime == 1:
        if date == 4 or date == 13 or date == 23 or date == 31:
            jump lbl_comicbookbackroom_day_crugeon_6
        elif date == 1 or date == 18 or date == 30:
            jump lbl_comicbookbackroom_day_crugeon_7
        elif date == 2 or date == 20 or date == 28:
            jump lbl_comicbookbackroom_day_crugeon_8
        elif date == 3 or date == 11 or date == 24:
            jump lbl_comicbookbackroom_day_crugeon_9
        elif date == 6 or date == 15 or date == 22:
            jump lbl_comicbookbackroom_day_crugeon_10
        elif date == 9 or date == 19 or date == 21:
            jump lbl_comicbookbackroom_day_crugeon_11
        elif date == 5 or date == 14 or date == 25:
            jump lbl_comicbookbackroom_day_crugeon_12
        elif date == 7 or date == 16 or date == 26:
            jump lbl_comicbookbackroom_day_crugeon_13
        elif date == 8 or date == 17 or date == 27:
            jump lbl_comicbookbackroom_day_crugeon_14
        elif date == 10 or date == 12 or date == 29:
            jump lbl_comicbookbackroom_day_crugeon_15

## Morning Exclusive
label lbl_comicbookbackroom_day_crugeon_1:

    show pov neutral at left
    with dissolve
    show cru neutral_talk at right
    with dissolve
    cru "Morning, [povname]."
    show pov neutral_talk at left
    show cru neutral at right
    pov "Morning to you, dude."
    show pov confused_talk at left
    show cru shocked at right
    pov "Say, why don't I ever see you at school?"
    show pov confused at left
    show cru confused_talk at right
    cru "Why don't I see {i}you{/i} at school?"
    show pov confused_talk at left
    show cru embarrassed at right
    pov "I- uh- huh?"

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_2:

    show pov confused at left
    with dissolve
    show cru neutral_talk at right
    with dissolve
    cru "Good morning, nice day today, isn't it?"
    show pov confused_talk at left
    show cru embarrassed at right
    pov "It's dark in here and the windows are boarded up."
    show pov bored at left
    show cru embarrassed_talk at right
    cru "Yeah, but the sun is peaking through the doorway."
    show pov bored_talk at left
    show cru embarrassed at right
    pov "Oh yeah, all that vitamin D."
    show pov confused at left
    show cru smirk_talk at right
    cru "Hope we get some vitamin D, if you know what I mean."
    show pov bored at left
    show cru shocked_talk at right
    cru "Wait- that didn't come out right."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_3:

    show pov neutral at left
    with dissolve
    show cru neutral_talk at right
    with dissolve
    cru "Hey, [povname]."
    show pov neutral_talk at left
    show cru neutral at right
    pov "Hi, Crug. What's new in this morning's agenda?"
    show pov neutral at left
    show cru neutral_talk at right
    cru "Nothing new, just keeping watch for foes to battle."
    show pov smirk_talk at left
    show cru neutral at right
    pov "You mean, me?"
    show pov embarrassed at left
    show cru neutral_talk at right
    cru "Yeah! You wanna play."
    show pov embarrassed_talk at left
    show cru neutral at right
    pov "Maybe... in a bit... maybe."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_4:

    show pov neutral_talk at left
    with dissolve
    show cru neutral at right
    with dissolve
    pov "Morning, bro."
    show pov bored at left
    show cru neutral_talk at right
    cru "Hi, ma dudey"
    show pov bored_talk at left
    show cru confused at right
    pov "Yeah, don't call me, 'dudey'."
    show pov confused at left
    show cru confused_talk at right
    cru "Isn't that the hip thing nowadays?"
    show pov confused_talk at left
    show cru embarrassed at right
    pov "In what world?"
    show pov confused at left
    show cru embarrassed_talk at right
    cru "I guess the thug life didn't choose me."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_5:

    show pov neutral_talk at left
    with dissolve
    show cru shocked at right
    with dissolve
    pov "Morning. Meet any girls last night?"
    show pov neutral at left
    show cru embarrassed_talk at right
    cru "Last night? What did you think I was doing last night?"
    show pov neutral_talk at left
    show cru embarrassed at right
    pov "I'm being hopeful and optimistic for you."
    show pov shocked at left
    show cru smirk_talk at right
    cru "I did go out and party actually."
    show pov shocked_talk at left
    show cru embarrassed at right
    pov "Really?"
    show pov bored at left
    show cru embarrassed_talk at right
    cru "It was a family thing..."

    jump lbl_comicbookbackroom_day

## Afternoon Exclusive
label lbl_comicbookbackroom_day_crugeon_6:

    show pov neutral_talk at left
    with dissolve
    show cru neutral at right
    with dissolve
    pov "Afternoon, my good sir."
    show pov neutral at left
    show cru neutral_talk at right
    cru "Howdy, partner."
    show pov neutral_talk at left
    show cru neutral at right
    pov "G'day, mate."
    show pov neutral at left
    show cru neutral_talk at right
    cru "Pleasant greetings."
    show pov neutral_talk at left
    show cru neutral at right
    pov "Bye!"
    show pov neutral at left
    show cru sad_talk at right
    cru "H- oh... okay."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_7:

    show pov smirk_talk at left
    with dissolve
    show cru confused at right
    with dissolve
    pov "The party is here, where's all the girls?."
    show pov neutral at left
    show cru embarrassed_talk at right
    cru "That's a joke right?"
    show pov smirk_talk at left
    show cru embarrassed at right
    pov "Bingo."
    show pov neutral at left
    show cru embarrassed_talk at right
    cru "Don't know whether to laugh or cry."
    show pov smirk_talk at left
    show cru embarrassed at right
    pov "Hahaha, me neither."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_8:

    show pov confused_talk at left
    with dissolve
    show cru neutral at right
    with dissolve
    pov "I always see you just sitting there."
    pov "Doesn't it get boring?"
    show pov confused at left
    show cru smirk_talk at right
    cru "It would be if I was surrounded by friends."
    show pov smirk_talk at left
    show cru embarrassed at right
    pov "Sounds like a tagline for a children's show."
    show pov neutral at left
    show cru embarrassed_talk at right
    cru "It sounded cooler in my head."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_9:

    show pov confused_talk at left
    with dissolve
    show cru confused at right
    with dissolve
    pov "Yo, ever get Dave there to talk?"
    show pov confused at left
    show cru confused_talk at right
    cru "I've been around him for so long that I can't tell if he did or not."
    show pov neutral at left
    show cru neutral_talk at right
    cru "I like to imagine he sounds like Morgan Meefran."
    show pov neutral_talk at left
    show cru neutral at right
    pov "I like to imagine he sounds like Mr Bene."
    show pov neutral at left
    show cru smirk_talk at right
    cru "Or Kashira."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_10:

    show pov neutral at left
    with dissolve
    show cru neutral_talk at right
    with dissolve
    cru "Good to see you again, [povname]."
    show pov confused at left
    show cru smirk_talk at right
    cru "Ready to lose to me again?"
    show pov angry_talk at left
    show cru shocked at right
    pov "Is that a threat? Because you know I can beat the shit out of you."
    show pov angry at left
    show cru sad_talk at right
    cru "I- I- I'm sorry, I didn'-"
    show pov smirk_talk at left
    show cru bored at right
    pov "Chill, I'm joking. No need to freak."

    jump lbl_comicbookbackroom_day

## Interchangable
label lbl_comicbookbackroom_day_crugeon_11:

    show pov bored_talk at left
    with dissolve
    show cru confused at right
    with dissolve
    pov "Hey, Crug. What else do you do here for fun?"
    show pov shocked at left
    show cru confused_talk at right
    cru "Other than play with our dicks?"
    show pov shocked_talk at left
    show cru confused at right
    pov "Wa- wait wait. Hold the phone."
    show pov confused_talk at left
    pov "What did you say?"
    show pov shocked at left
    show cru confused_talk at right
    cru "I said, 'other than play with our decks'."
    show pov embarrassed_talk at left
    show cru confused at right
    pov "Y-yeah... that's what I thought you said."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_12:

    show pov confused_talk at left
    with dissolve
    show cru confused at right
    with dissolve
    pov "Hey dude, does anyone else come back here?"
    show pov confused at left
    show cru confused_talk at right
    cru "Other than us, you, Jacob, and Hitomi?"
    cru "Not really."
    show pov confused_talk at left
    show cru embarrassed at right
    pov "Wouldn't it be nice to have more members?"
    show pov embarrassed at left
    show cru embarrassed_talk at right
    cru "I sort of like the exclusivity, it makes me feel important."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_13:

    show pov neutral at left
    with dissolve
    show cru neutral_talk at right
    with dissolve
    cru "[povname]! Good to see you here!"
    show pov neutral_talk at left
    show cru neutral at right
    pov "Good to be here, I think."
    pov "What's been happening?"
    show pov neutral at left
    show cru neutral_talk at right
    cru "Funny you ask."
    show pov embarrassed at left
    show cru neutral_talk at right
    cru "Yesterday, I accidentally ate some really nasty-"
    show pov embarrassed_talk at left
    show cru bored at right
    pov "So... same old nerd club, aye?"

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_14:

    show pov bored at left
    with dissolve
    show cru neutral_talk at right
    with dissolve
    cru "Hi, [povname]. You wanna play?"
    show pov neutral_talk at left
    show cru shocked at right
    pov "Not right now, just wanted to chat."
    show pov embarrassed at left
    show cru shocked_talk at right
    cru "You mean with me?"
    show pov embarrassed_talk at left
    show cru neutral at right
    pov "Uh- I guess?"
    show pov shocked at left
    show cru neutral_talk at right
    cru "{i}*Giggty giggty*{/i}"
    show pov embarrassed_talk at left
    show cru embarrassed at right
    pov "... Well, I'll see you later."

    jump lbl_comicbookbackroom_day

label lbl_comicbookbackroom_day_crugeon_15:

    show pov neutral at left
    with dissolve
    show cru neutral_talk at right
    with dissolve
    cru "Hi, [povname]. What brings you around here?"
    show pov neutral_talk at left
    show cru neutral at right
    pov "Oh, you know, the people, the cards."
    show pov confused_talk at left
    show cru embarrassed at right
    pov "...The funky smell."
    show pov confused at left
    show cru embarrassed_talk at right
    cru "Oh, the smell? Well, you see, about that..."
    show pov bored_talk at left
    show cru embarrassed at right
    pov "I'll stop you right there. I don't wanna know."

    jump lbl_comicbookbackroom_day
