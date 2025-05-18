## Throwaway Alanna Mall Day Conversation ##
label lbl_mall_day_alanna:

    ## Main Story
    ## Before Looking for a Job
    if main_story <= 15:
        show btn mall_day_icecreamstore_idle
        pov "{i}It's Ice Cream'py.{/i}"
        pov "{i}I'm not really in the mood for some icecream.{/i}"
        jump lbl_mall_day_setup
    ## Answers Around Town Sexworld
    elif main_story <= 40 and insexworld == 1:
        jump lbl_mall_day_alanna_sexworld
    ## Investigations
    elif main_story == 84:
        jump lbl_investigations_alanna
    # ## Buukakki Followers Are Everywhere
    # elif main_story == 151:
    #     jump lbl_buukakki_followers_are_everywhere_alanna
    ## NO EVENT
    else:
        jump lbl_mall_day_alanna_menu

## Menu
label lbl_mall_day_alanna_menu:
    show btn mall_day_icecreamstore_idle
    menu:
        "A job" if 16 <= main_story <= 21:
            if nextday_ajob == 0:
                jump lbl_a_job
            elif nextday_ajob == 1:
                jump lbl_a_job_2
        "Work" if main_story >= 22:
            jump lbl_working_at_icecreampy
        "Buy a tub of icecream" if mum_path == 12 and not (inventory.has_item(Items.icecream1) or inventory.has_item(Items.icecream2) or inventory.has_item(Items.icecream3) or inventory.has_item(Items.icecream4)):
            jump lbl_cheermomup_icecream
        "Spare Boxes?" if sister_path == 29 and mall_spareboxes == 0:
            jump lbl_mall_day_alanna_spareboxes
        "Talk" if main_story >= 22:
            jump lbl_mall_day_alanna_convo
        "Nevermind":
            jump lbl_mall_day

label lbl_mall_day_alanna_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 10 or date == 16 or date == 26 or date == 0:
            jump lbl_mall_day_alanna_1
        elif date == 7 or date == 11 or date == 27:
            jump lbl_mall_day_alanna_2
        elif date == 6 or date == 12 or date == 30:
            jump lbl_mall_day_alanna_3
        elif date == 5 or date == 13 or date == 29:
            jump lbl_mall_day_alanna_4
        elif date == 4 or date == 14 or date == 28:
            jump lbl_mall_day_alanna_5
        elif date == 3 or date == 15 or date == 25:
            jump lbl_mall_day_alanna_11
        elif date == 2 or date == 20 or date == 24:
            jump lbl_mall_day_alanna_12
        elif date == 1 or date == 19 or date == 21:
            jump lbl_mall_day_alanna_13
        elif date == 9 or date == 18 or date == 22:
            jump lbl_mall_day_alanna_14
        elif date == 8 or date == 17 or date == 23:
            jump lbl_mall_day_alanna_15
    elif gtime == 1:
        if date == 10 or date == 16 or date == 28 or date == 0:
            jump lbl_mall_day_alanna_6
        elif date == 9 or date == 11 or date == 27:
            jump lbl_mall_day_alanna_7
        elif date == 8 or date == 17 or date == 26:
            jump lbl_mall_day_alanna_8
        elif date == 7 or date == 12 or date == 25:
            jump lbl_mall_day_alanna_9
        elif date == 6 or date == 18 or date == 24:
            jump lbl_mall_day_alanna_10
        elif date == 5 or date == 13 or date == 23:
            jump lbl_mall_day_alanna_11
        elif date == 4 or date == 19 or date == 22:
            jump lbl_mall_day_alanna_12
        elif date == 3 or date == 14 or date == 21:
            jump lbl_mall_day_alanna_13
        elif date == 2 or date == 20 or date == 29:
            jump lbl_mall_day_alanna_14
        elif date == 1 or date == 15 or date == 30:
            jump lbl_mall_day_alanna_15

## Morning Exclusive
label lbl_mall_day_alanna_1:
    show pov neutral_talk at left
    with dissolve
    show ala bored at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Morning, Alanna."
    pov "You're up bright and early."
    show pov neutral at left
    show ala bored_talk at right
    ala "So are you."
    show pov smirk_talk at left
    show ala bored at right
    pov "Hmm, touche. My body clock just decided that I should be awake and about."
    show pov embarrassed at left
    show ala bored_talk at right
    ala "That's a great story, [povname]."
    show pov embarrassed_talk at left
    show ala bored at right
    pov "I see you're still not in the mood. I'll leave you to it."

    jump lbl_mall_day

label lbl_mall_day_alanna_2:
    show pov smirk_talk at left
    with dissolve
    show ala bored at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Good morning, Ice Cream'py."
    show pov smirk at left
    show ala bored_talk at right
    ala "The store can't greet you. But I'm here."
    show pov neutral_talk at left
    show ala bored at right
    pov "What's new with you?"
    show pov neutral at left
    show ala bored_talk at right
    ala "Nothing."
    show pov embarrassed at left
    show ala bored_talk at right
    ala "My life literally consists of sleeping, eating, and working here."
    show pov embarrassed_talk at left
    show ala bored at right
    pov "Don't think of this as a dead-end job."
    show pov embarrassed at left
    show ala bored_talk at right
    ala "I don't. Just a really long path of nothing-ness."

    jump lbl_mall_day

label lbl_mall_day_alanna_3:
    show pov neutral at left
    with dissolve
    show ala bored_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "{i}*Sigh*{/i} Morning."
    show pov smirk_talk at left
    show ala bored at right
    pov "Aren't you happy to see me?"
    show pov neutral at left
    show ala embarrassed_talk at right
    ala "Aha, sorry. I'm just tired, as usual."
    show pov neutral_talk at left
    show ala embarrassed at right
    pov "Why don't you get a shot of caffeine in your system."
    show pov confused at left
    show ala confused_talk at right
    ala "Not a fan of coffee or energy drinks."
    show pov smirk at left
    show ala bored_talk at right
    ala "So I'm pretty much screwed forever."

    jump lbl_mall_day

label lbl_mall_day_alanna_4:
    show pov neutral at left
    with dissolve
    show ala confused_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "Hey, [povname]."
    show pov confused at left
    ala "Did you hear what happened last night?"
    show pov confused_talk at left
    show ala confused at right
    pov "What happened?"
    show pov shocked at left
    show ala neutral_talk at right
    ala "Someone got trapped inside the mall."
    show pov smirk_talk at left
    show ala neutral at right
    pov "Again?"
    show pov neutral at left
    show ala confused_talk at right
    ala "Yeah, one of those idiots who was doing the '24 hour challenge'."
    show ala smirk_talk at right
    ala "I heard his camera battery died a few minutes into the night."
    show pov smirk at left
    show ala bored_talk at right
    ala "So that was a waste of life."

    jump lbl_mall_day

label lbl_mall_day_alanna_5:
    show pov neutral at left
    with dissolve
    show ala bored_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "Good morning, sir. How can I-"
    show pov bored at left
    ala "Oh, it's you."
    show pov bored_talk at left
    show ala bored at right
    pov "Ahem- I'm still a potential customer."
    show pov neutral at left
    show ala bored_talk at right
    ala "What do you want then?"
    show pov embarrassed_talk at left
    show ala bored at right
    pov "Oh, nothing. Don't really buy anything at the moment."
    show pov embarrassed at left
    show ala bored_talk at right
    ala "Yeah, I figured. Don't get my hopes up like that again."
    show pov bored at left
    ala "You're killing me."

    jump lbl_mall_day

## Afternoon Exclusive
label lbl_mall_day_alanna_6:
    show pov smirk_talk at left
    with dissolve
    show ala bored at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Yo yo yo, Alanna-yo."
    show pov smirk at left
    show ala bored_talk at right
    ala "Hi."
    show pov smirk_talk at left
    show ala bored at right
    pov "What's freezy-freezy-frizzle, ma' pink and white nizzle drizzle?"
    show pov smirk at left
    show ala bored_talk at right
    ala "Can you shut up, please."
    show pov embarrassed at left
    ala "I'm having nth thoughts about you."
    show pov embarrassed_talk at left
    show ala bored at right
    pov "'nth' thoughts?"
    show pov embarrassed at left
    show ala bored_talk at right
    ala "I lost count of how many times I've made an assumption of you."

    jump lbl_mall_day

label lbl_mall_day_alanna_7:
    show pov neutral_talk at left
    with dissolve
    show ala bored at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Hey, Alanna."
    show pov confused_talk at left
    show ala confused at right
    pov "Why is the aicon blasting hard today?"
    show pov confused at left
    show ala confused_talk at right
    ala "No idea, I couldn't tell."
    show pov confused at left
    show ala bored_talk at right
    ala "Standing behind this counter is pretty much the coldest part of the mall."
    show pov bored_talk at left
    show ala bored at right
    pov "Well, it's damn cold."
    show pov bored at left
    show ala bored_talk at right
    ala "Well, damn, [povname]. Go complain to God himself, I'm sure he'll be happy to listen."

    jump lbl_mall_day

label lbl_mall_day_alanna_8:
    show pov angry_talk at left
    with dissolve
    show ala confused at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Why does the goddamn music loop in this mall?"
    show pov angry at left
    show ala confused_talk at right
    ala "What music?"
    show pov confused at left
    show ala confused at right
    ala "..."
    show ala shocked_talk at right
    ala "Oh! {i}That{/i} music."
    show pov embarrassed at left
    show ala embarrassed_talk at right
    ala "I've been here for so long, my brain totally decided to ignore its existence."
    show ala confused_talk at right
    ala "That is so strange that I'm hearing it now..."

    jump lbl_mall_day

label lbl_mall_day_alanna_9:
    show pov neutral at left
    with dissolve
    show ala bored_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "Hey, you here for work?"
    show pov smirk_talk at left
    show ala bored at right
    pov "You wish, I'm just passing by."
    show pov smirk at left
    show ala bored_talk at right
    ala "I wish a lot of things."
    show pov confused at left
    show ala bored_talk at right
    ala "For example, I wish I wasn't so deep in student debt that it physical hurts my asshole."
    show pov smirk_talk at left
    show ala bored at right
    pov "Life fucks us all, am I right."
    show pov embarrassed at left
    show ala bored_talk at right
    ala "Yeah, thanks for disecting that joke for us."

    jump lbl_mall_day

label lbl_mall_day_alanna_10:
    show pov confused at left
    with dissolve
    show ala confused_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "Do you like ice cream, [povname]."
    show pov confused_talk at left
    show ala confused at right
    pov "... You mean like right now?"
    show pov confused at left
    show ala embarrassed_talk at right
    ala "Just in general."
    show pov smirk_talk at left
    show ala smirk at right
    pov "I mean, yeah, it's cool."
    show pov embarrassed at left
    ala "..."
    show ala neutral_talk at right
    ala "Cool."
    ala "We make such a great comedic duo."

    jump lbl_mall_day

## Interchangeable
label lbl_mall_day_alanna_11:
    show pov neutral_talk at left
    with dissolve
    show ala bored at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Hey, Alanna."
    show pov confused_talk at left
    show ala confused at right
    pov "Why do I sense a subtle lingering scent of- fish?"
    show pov confused at left
    show ala confused_talk at right
    ala "You smell fish? I smell cheese."
    show pov confused_talk at left
    show ala confused at right
    pov "Maybe it's both..?"
    show pov confused at left
    show ala bored_talk at right
    ala "Fish-cheese."
    show pov smirk_talk at left
    show ala bored at right
    pov "I think it's more of cheese-fish."

    jump lbl_mall_day

label lbl_mall_day_alanna_12:
    show pov smirk_talk at left
    with dissolve
    show ala confused at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Man, Alanna. You must have an immune-system of a goddess."
    pov "How do you not get sick and take the day off?"
    show pov shocked at left
    show ala bored_talk at right
    ala "My diet consists of cold and flu pills."
    show pov embarrassed_talk at left
    show ala bored at right
    pov "That's a joke right."
    show pov embarrassed at left
    show ala bored at right
    ala "..."
    show pov bored at left
    show ala bored_talk at right
    ala "Do you really have to ask that?"

    jump lbl_mall_day

label lbl_mall_day_alanna_13:
    show pov confused at left
    with dissolve
    show ala confused_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "[povname], [povname], [povname]."
    show pov confused_talk at left
    show ala confused at right
    pov "What's up with the tone?"
    show pov bored at left
    show ala bored_talk at right
    ala "{i}*Sigh*{/i} [povname], [povname], [povname]."
    show pov bored_talk at left
    show ala bored at right
    pov "Alanna, alanna, alanna."
    show pov confused at left
    show ala confused_talk at right
    ala "It's such a shame that you don't even notice it."
    show ala confused at right
    pov "..."
    show pov confused_talk at left
    show ala smirk at right
    pov "Notice what?"

    jump lbl_mall_day

label lbl_mall_day_alanna_14:
    show pov confused at left
    with dissolve
    show ala bored_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    ala "Man, I really feel like quitting."
    show pov confused_talk at left
    show ala bored at right
    pov "Then why don't you?"
    show pov confused at left
    show ala bored_talk at right
    ala "Because being employed is better than nothing."
    show pov embarrassed_talk at left
    show ala bored at right
    pov "Here here."
    show pov smirk_talk at left
    pov "I'll drink to that."
    show pov neutral at left
    show ala bored_talk at right
    ala "Ughh, I really need a drink, now that you mention it."

    jump lbl_mall_day

label lbl_mall_day_alanna_15:
    show pov smirk_talk at left
    with dissolve
    show ala bored at right
    call lbl_icecreampy_counter_check
    with dissolve
    pov "Hey, can I get a raise?"
    show pov confused at left
    show ala confused_talk at right
    ala "No."
    show pov confused_talk at left
    show ala confused at right
    pov "Why not?"
    show pov confused at left
    show ala confused_talk at right
    ala "Because I'm not your boss."
    show pov confused_talk at left
    show ala confused at right
    pov "Where and who {i}is{/i} my boss?"
    show pov bored at left
    show ala smirk_talk at right
    ala "Do you know- the muffin man?"

    jump lbl_mall_day
