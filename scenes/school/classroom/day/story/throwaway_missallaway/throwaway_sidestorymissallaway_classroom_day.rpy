## Miss Allaway Side Story Throwaway Conversations Classroom ##
label lbl_classroom_day_missallaway_16:
    show pov bored at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis bored_talk at right
    with dissolve
    mis "Sit down, [povname]. Class is about to start."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_17:
    show pov embarrassed at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis angry_talk at right
    with dissolve
    mis "Don't forget detention during lunch, [povname]. Don't you dare skip out on it."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_18:
    show pov confused at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis embarrassed_talk at right
    with dissolve
    mis "Sorry, [povname] but I'm busy at the moment. I- I don't want to talk."

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_19:
    show pov sad at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis angry_talk at right
    with dissolve
    mis "Didn't I tell you to leave me alone?"
    pov "{i}I'll just be a good boy and study, impress her that way.{/i}"
    $ renpy.notify("New Objective: Max out your Intelligence")

    jump lbl_classroom_day

label lbl_classroom_day_missallaway_20:
    show pov shocked at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis angry_talk at right
    with dissolve
    mis "Don't- talk to me right now."
    show pov smirk at left
    show mis sad_talk at right
    mis "I shouldn't have let you sit with me during lunch."
    show pov smirk_talk at left
    show mis shocked at right
    pov "I can see you blushing."

    jump lbl_classroom_day

## Miss Allaway Movie Date
label lbl_classroom_day_missallaway_moviedate:
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral at right
    with dissolve
    pov "Hey, Miss. I heard of a really cool movie that came out recently?"
    show pov neutral at left
    show mis confused_talk at right
    mis "What is it?"
    show pov smirk_talk at left
    show mis neutral at right
    pov "Come with me tonight and you'll find out."
    show pov smirk at left
    show mis neutral_talk at right
    mis "Oh, that's sweet. Sure, I'll see you there later."
    mis "I could really use a break and unwind a little."
    if allawaybedroomsex_sneakherin == 1:
        $ allawaybedroomsex_sneakherin = 0
        mis "Didn't you already ask me over to your house today?"
        pov "Yeah, I know. But I heard the news of this movie and I figured it was something you might enjoy."
        mis "We'll forget about meeting up at your house for 'lunch', then."
        pov "Plus, cuddling up with you is the end goal in either situation so it's a win-win for me."
        mis "Well, aren't you a sweet talker?"
        mis "Okay, if you are that enthusiastic about it, how can I refuse?"
        mis "You do know quite well how to show me a good time, after all."
        pov "You bring out the best in me."
        mis "Alright, stop it before you get me all red in public!"

    scene black
    with fade
    $ renpy.pause(1.5)
    "At the cinema..."
    stop music fadeout 2.0
    $ moviedate = 3
    $ gtime = 2

    jump lbl_cinema_night_setup

## Ask Allaway to Come Visit
label lbl_classroom_day_missallaway_come_visit:
    show pov smirk_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis neutral at right
    with dissolve
    pov "Hey, Miss. Do you have lunch plans?"
    show pov neutral at left
    show mis neutral_talk at right
    mis "Same as any other day. Just going to be sitting alone at the cafeteria."
    show pov smirk_talk at left
    show mis confused at right
    pov "Why don't we head over to my place for something more..."
    show pov smirk at left
    mis "..."
    show pov smirk_talk at left
    show mis embarrassed at right
    pov "Spicy?"
    show pov smirk at left
    show mis embarrassed_talk at right
    mis "Hmmm, I do like spicy..."
    mis "Hot- and spicy- and... sweet... and savoury..."
    show pov embarrassed at left
    show mis bored_talk at right
    mis "And throbbing..."
    show pov smirk_talk at left
    show mis shocked at right
    pov "I'll take that as a 'yes'?"
    show pov neutral at left
    show mis embarrassed_talk at right
    mis "I'll see what I can do."
    mis "{i}*Whisper*{/i} How about I meet you there, I can't really be seen walking home with you."
    show pov smirk_talk at left
    show mis smirk at right
    pov "I'll go um... pre-heat the oven then."
    show pov smirk at left
    show mis smirk_talk at right
    mis "I can't wait."

    $ allawaybedroomsex_sneakherin = 1

    jump lbl_classroom_day_setup

## Allaway Come Visit Fail
label lbl_classroom_day_missallaway_come_visit_fail:
    show pov neutral_talk at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis angry at right
    with dissolve
    pov "Hi-"
    show pov shocked at left
    show mis angry_talk at right
    mis "No."
    show pov confused_talk at left
    show mis angry at right
    pov "Wh-"
    show pov shocked at left
    show mis angry_talk at right
    mis "Nope."
    show pov shocked_talk at left
    show mis angry at right
    pov "Uh-"
    show pov shocked at left
    show mis angry_talk at right
    mis "Incorrect-"
    show pov angry_talk at left
    show mis angry at right
    pov "What's going on?"
    show pov shocked at left
    show mis angry_talk at right
    mis "Where were you?"
    show pov confused_talk at left
    show mis angry at right
    pov "What? When?"
    show pov shocked at left
    show mis angry_talk at right
    mis "You-!"
    show mis angry at right
    mis "..."
    show pov shocked at left
    show mis angry_talk at right
    mis "{i}*Whisper*{/i} I thought we were meeting up at your place..?"
    show mis angry at right
    pov "..."
    show pov embarrassed_talk at left
    pov "Oh- right..."
    show pov sad at left
    show mis angry_talk at right
    mis "I was there, and I waited for you like an idiot."
    mis "What the actual f- heck?"
    mis "I was craving too, for some hardcore-"
    show mis angry at right
    mis "Mm..."
    show mis bored_talk at right
    mis "I can't even look at you right now."
    show pov sad_talk at left
    show mis bored at right
    pov "I'm sorry..."
    show pov sad at left
    show mis bored_talk at right
    mis "Just, don't bother me today."
    show mis bored at right
    pov "..."
    show mis bored_talk at right
    mis "Goodbyeeeee."
    if missallaway_points >= 2:
        $ missallaway_points -= 2
    else:
        $ missallaway_points = 0
    $ renpy.notify("Relationship with Miss Allaway Decreased by 2")

    $ allawaybedroomsex_sneakherin = 3

    jump lbl_classroom_day_setup

## Allaway Come Visit Don't Talk To Me
label lbl_classroom_day_missallaway_come_visit_donttalktome:
    show pov sad at left
    with dissolve
    hide btn_classroom_day_missallaway_idle2
    show mis bored_talk at right
    with dissolve
    mis "Don't talk to me."
    show mis bored at right
    pov "..."

    jump lbl_classroom_day_setup
