## Throwaway Hazel Adult Store Day Conversation ##
label lbl_adultstore_day_hazel:
    ## Main Story
    ## Answers Around Town Sexworld
    if main_story <= 35 and insexworld == 1:
        show btn adultstore_day_hazelsexworld_idle
        $ renpy.pause(0.001)

        jump lbl_adultstore_day_hazel_sexworld
    ## Sister Side Story
    if sister_path == 17.5:
        jump lbl_sister_in_the_adultstore
    elif sister_path == 29:
        jump lbl_box_favour
    elif sister_path == 30:
        show btn adultstore_day_hazel_idle
        $ renpy.pause(0.001)

        if fursuitforboxjob_boxes >= 50:

            pov "{i}I already have [fursuitforboxjob_boxes]. I can build the fort now.{/i}"
            menu:
                "Talk":
                    hide btn adultstore_day_hazel_idle
                    jump lbl_adultstore_day_hazel_convo
                "Nevermind.":
                    jump lbl_adultstore_day
        menu:
            "Talk":
                hide btn adultstore_day_hazel_idle
                jump lbl_adultstore_day_hazel_convo
            "Mascot Job":
                jump lbl_fursuit_for_box_job
            "Nevermind.":
                jump lbl_adultstore_day
    ## NO EVENT
    else:
        show btn adultstore_day_hazel_idle
        menu:
            "A job" if 16 <= main_story <= 21 and nextday_ajob == 0 and adultstore_ajob == 0:
                hide btn adultstore_day_hazel_idle
                jump lbl_adultstore_day_hazel_ajob
            # "BDSM Gear" if main_story == 170 and not inventory.has_item(Items.bdsmgear):
            #     hide btn adultstore_day_hazel_idle
            #     jump lbl_adultstore_day_hazel_bdsmgear
            "Talk":
                hide btn adultstore_day_hazel_idle
                jump lbl_adultstore_day_hazel_convo
            "Relieve some stress?":
                hide btn adultstore_day_hazel_idle
                jump lbl_hazel_backroom_cowgirl
            "Nevermind.":
                jump lbl_adultstore_day

label lbl_adultstore_day_hazel_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 9 or date == 18 or date == 26 or date == 0:
            jump lbl_adultstore_day_hazel_1
        elif date == 10 or date == 19 or date == 27:
            jump lbl_adultstore_day_hazel_2
        elif date == 6 or date == 20 or date == 28:
            jump lbl_adultstore_day_hazel_3
        elif date == 7 or date == 13 or date == 29:
            jump lbl_adultstore_day_hazel_4
        elif date == 8 or date == 14 or date == 30:
            jump lbl_adultstore_day_hazel_5
        elif date == 1 or date == 15 or date == 22:
            jump lbl_adultstore_day_hazel_11
        elif date == 2 or date == 16 or date == 23:
            jump lbl_adultstore_day_hazel_12
        elif date == 3 or date == 17 or date == 24:
            jump lbl_adultstore_day_hazel_13
        elif date == 4 or date == 11 or date == 25:
            jump lbl_adultstore_day_hazel_14
        elif date == 5 or date == 12 or date == 21:
            jump lbl_adultstore_day_hazel_15
    elif gtime == 1:
        if date == 5 or date == 18 or date == 26 or date == 0:
            jump lbl_adultstore_day_hazel_6
        elif date == 4 or date == 19 or date == 29:
            jump lbl_adultstore_day_hazel_7
        elif date == 3 or date == 20 or date == 30:
            jump lbl_adultstore_day_hazel_8
        elif date == 2 or date == 14 or date == 28:
            jump lbl_adultstore_day_hazel_9
        elif date == 1 or date == 13 or date == 27:
            jump lbl_adultstore_day_hazel_10
        elif date == 8 or date == 12 or date == 23:
            jump lbl_adultstore_day_hazel_11
        elif date == 7 or date == 11 or date == 22:
            jump lbl_adultstore_day_hazel_12
        elif date == 6 or date == 17 or date == 21:
            jump lbl_adultstore_day_hazel_13
        elif date == 10 or date == 16 or date == 25:
            jump lbl_adultstore_day_hazel_14
        elif date == 9 or date == 15 or date == 24:
            jump lbl_adultstore_day_hazel_15

## Morning Exclusive
label lbl_adultstore_day_hazel_1:
    show pov neutral_talk at left
    with dissolve
    show haz neutral at right
    call lbl_adultstore_counter_check
    with dissolve

    pov "Morning, Hazel. How's business?"
    show pov neutral at left
    show haz embarrassed_talk at right
    haz "Business is boomin'. Well, boomin' in a kid's fireworks display kind of way."
    show pov embarrassed_talk at left
    show haz neutral at right
    pov "I guess that's... good?"
    show pov neutral at left
    show haz smirk_talk at right
    haz "I mean, can't complain. We've had worst days."
    show pov neutral_talk at left
    show haz confused at right
    pov "The day sex toys go out of style is the day we evolve into genatal-less beings."
    show pov neutral at left
    show haz smirk_talk at right
    haz "Amen to that, honey."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_2:
    show pov neutral_talk at left
    with dissolve
    show haz neutral at right
    call lbl_adultstore_counter_check
    with dissolve
    pov "Morning, Hazel. Sleep soundly last night?"
    show pov neutral at left
    show haz neutral_talk at right
    haz "Always do, baby."
    show haz smirk_talk at right
    haz "Can't catch some Z's without flicking the bees' knees."
    show pov embarrassed at left
    haz "If you know what I mean."
    show pov embarrassed_talk at left
    show haz confused at right
    pov "I've uh- never visualized it in that way. Thank you."
    show pov bored at left
    show haz confused_talk at right
    haz "Is that not a common saying?"

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_3:
    show pov smirk_talk at left
    with dissolve
    show haz neutral at right
    call lbl_adultstore_counter_check
    with dissolve
    pov "Hey, Hazel. What's the word of the day?"
    show pov confused at left
    show haz neutral_talk at right
    haz "Aglet."
    show pov confused_talk at left
    show haz neutral at right
    pov "Aglet?"
    show pov confused at left
    show haz neutral_talk at right
    haz "Yeah, it's that plastic-y bit at the end of your shoelace."
    show pov smirk_talk at left
    show haz smirk at right
    pov "Hmm... aglet. I'll remember that."
    show pov neutral at left
    show haz smirk_talk at right
    haz "I'll make sure you remember that. Fo' motherfuckin' sho'."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_4:
    show pov neutral at left
    with dissolve
    show haz neutral_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "Hey, [povname]. What can I do for you this morning?"
    show pov neutral_talk at left
    show haz neutral at right
    pov "Just wanted to stop by and check out the merchandise."
    show pov neutral at left
    show haz neutral_talk at right
    haz "Anything catch your eye?"
    show pov neutral_talk at left
    show haz smirk at right
    pov "They all do!"
    show pov confused at left
    show haz smirk_talk at right
    haz "Are you going to take them all?"
    show pov embarrassed_talk at left
    show haz smirk at right
    pov "Erm... you know I'm not rich, right?"

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_5:
    show pov confused at left
    with dissolve
    show haz neutral_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "Morning, sunshine. Apparently there was a gang fight going on last night?"
    show pov confused_talk at left
    show haz confused at right
    pov "Again?"
    show pov confused at left
    show haz confused_talk at right
    haz "That's what I heard from Hitomi next door."
    show pov smirk at left
    show haz bored_talk at right
    haz "For all I know, she's just trying to scare me in some way."
    show pov smirk_talk at left
    show haz bored at right
    pov "Are you scared?"
    show pov smirk at left
    show haz smirk_talk at right
    haz "Bitch, the only {i}REAL{/i} gang war around here are tits fighting for territory."

    jump lbl_adultstore_day

## Afternoon Exclusive
label lbl_adultstore_day_hazel_6:
    show pov confused at left
    with dissolve
    show haz smirk_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "Hey, [povname]. Getting ready for a date?"
    show pov embarrassed_talk at left
    show haz smirk at right
    pov "Why... do you ask?"
    show pov smirk_talk at left
    pov "Do I look extra spiffy today?"
    show pov confused at left
    show haz neutral_talk at right
    haz "Hm, no. I assumed you're looking for a new sex toy for a date is all."
    show pov confused_talk at left
    show haz embarrassed at right
    pov "Is- is that a thing?"
    show pov smirk at left
    show haz embarrassed_talk at right
    haz "Look, man. I tried a new sales approach, it didn't pan out. Let it go."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_7:
    show pov neutral at left
    with dissolve
    show haz smirk_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "Good afternoon, sir. How may I be of assitance?"
    show pov smirk_talk at left
    show haz embarrassed at right
    pov "Oooh, how high-class. I'm just perusing your exquisite inventory of fine and risque goods."
    show pov smirk at left
    show haz embarrassed_talk at right
    haz "Geez, [povname]. Can you sound even more-"
    show pov smirk_talk at left
    show haz confused at right
    pov "Sexy? I figured you'd be fond of my black-tie vernacular."
    show pov smirk at left
    show haz bored_talk at right
    haz "You're giving me a headache. Go back to being stupidly cute, like a puppy with 3 legs."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_8:
    show pov smirk at left
    with dissolve
    show haz smirk_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "Hey, sugar. Looking for something... or someone?"
    show pov smirk_talk at left
    show haz neutral at right
    pov "Why not both? Do you have a... Miss Sally?"
    show pov confused at left
    show haz confused_talk at right
    haz "The blow up doll? No, sorry. Out of stock."
    show pov embarrassed_talk at left
    show haz confused at right
    pov "That's alright, I'm in the market for a Tanaka-chan."
    show pov shocked at left
    show haz neutral_talk at right
    haz "Also sold out. But we do have a Mr Hump-and-Dump, pre-owned though."
    show pov embarrassed_talk at left
    show haz smirk at right
    pov "I'll... keep looking."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_9:
    show pov neutral_talk at left
    with dissolve
    show haz neutral at right
    call lbl_adultstore_counter_check
    with dissolve
    pov "Afternoon, Hazel. Wondering if you have an item in stock."
    show pov neutral at left
    show haz neutral_talk at right
    haz "Whatcha' lookin' for, baby?"
    show pov smirk_talk at left
    show haz embarrassed at right
    pov "Cock flavoured condoms."
    show pov embarrassed at left
    show haz embarrassed_talk at right
    haz "Oooh, damn. I actually do have some in stock but they're expired."
    show pov confused at left
    show haz confused_talk at right
    haz "The taste probably turned from cock to grape."
    show pov neutral_talk at left
    show haz neutral at right
    pov "I hear you. Nothing off-putting than playing tricks on your tastebuds."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_10:
    show pov confused_talk at left
    with dissolve
    show haz neutral at right
    call lbl_adultstore_counter_check
    with dissolve
    pov "Hey, Hazel. What time are you closing?"
    show pov neutral at left
    show haz neutral_talk at right
    haz "In a few hours."
    show pov smirk_talk at left
    show haz confused at right
    pov "Same time everyday?"
    show pov smirk at left
    show haz confused_talk at right
    haz "Yeeeeeep."
    show pov shocked at left
    show haz angry_talk at right
    haz "Why? Are you planning a robbery or something? Because, [povname], that shit ain't funny."
    show pov embarrassed_talk at left
    show haz confused at right
    pov "I- I was honestly just curious. Don't worry about me."

    jump lbl_adultstore_day

## Interchangable
label lbl_adultstore_day_hazel_11:
    show pov neutral_talk at left
    with dissolve
    show haz neutral at right
    call lbl_adultstore_counter_check
    with dissolve
    pov "Hello, hello, hello! How's the store?"
    show pov neutral at left
    show haz smirk_talk at right
    haz "Hasn't burnt down yet so I still have a job!"
    show pov smirk_talk at left
    show haz neutral at right
    pov "Always looking at the brightside of life."
    show pov confused at left
    show haz smirk_talk at right
    haz "When you work at a sex store, you see enough of the dark side."
    show pov confused_talk at left
    show haz confused at right
    pov "I feel like there's a sexual innuendo somewhere in there, I just can't really pin point what it is."
    show pov confused at left
    show haz confused_talk at right
    haz "Why do you think I'm always spouting sexual innuendos? I'm not that close yet."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_12:
    show pov neutral at left
    with dissolve
    show haz neutral_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "What's up, hot stuff? Any plans for later?"
    show pov smirk_talk at left
    show haz neutral at right
    pov "Nothing set in stone yet. Do you wanna do something together?"
    show pov smirk at left
    show haz smirk_talk at right
    haz "Not tonight, I might just crash at my pad and give the ol' bean a beating."
    show haz embarrassed_talk at right
    haz "I've been pretty stressed lately."
    show pov smirk_talk at left
    show haz smirk at right
    pov "Need a hand with that? No need to return the favour."
    show pov embarrassed at left
    show haz smirk_talk at right
    haz "Kind of you to offer but it's really just a girls night in."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_13:
    show pov confused_talk at left
    with dissolve
    show haz confused at right
    call lbl_adultstore_counter_check
    with dissolve
    pov "Gosh, why is it so cold in here."
    show pov confused at left
    show haz embarrassed_talk at right
    haz "Is it? I felt pretty hot so I turned the aircon on."
    show pov sad_talk at left
    show haz confused at right
    pov "I feel like I'm going to catch a cold in here."
    show pov confused at left
    show haz embarrassed_talk at right
    haz "Really? I feel like all the products in here makes customers hot and bothered, so it sort of compensates."
    show pov shocked at left
    show haz confused_talk at right
    haz "Are my nipples poking too much?"
    show pov embarrassed_talk at left
    show haz neutral at right
    pov "I can't really see them properly. You're all good."
    show pov embarrassed at left
    show haz smirk_talk at right
    haz "I can definitely feel them but I ain't complainin'."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_14:
    show pov shocked at left
    with dissolve
    show haz angry_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "Frikkin dickin' pickle-lickin' asshole!"
    show pov embarrassed_talk at left
    show haz angry at right
    pov "Hey, you okay there?"
    show pov shocked at left
    show haz angry_talk at right
    haz "No! This asshole is using my pics to catfish this other dickle pickin' asshole licker."
    show pov angry_talk at left
    show haz angry at right
    pov "That's fucked up. You should report them."
    show pov angry at left
    show haz angry_talk at right
    haz "I did! These low-lives have no lives."
    show pov angry_talk at left
    show haz angry at right
    pov "Yeah, fuck those guys. They're literally worst than Hitler."

    jump lbl_adultstore_day

label lbl_adultstore_day_hazel_15:
    show pov neutral at left
    with dissolve
    show haz neutral_talk at right
    call lbl_adultstore_counter_check
    with dissolve
    haz "Are you on Instantgram?"
    show pov neutral_talk at left
    show haz embarrassed at right
    pov "I do have an account but I don't use it often, why?"
    show pov smirk at left
    show haz embarrassed_talk at right
    haz "Just curious. I wanted to know what your handle was so I could follow you."
    show pov embarrassed_talk at left
    show haz embarrassed at right
    pov "Don't bother with me, my feed is near empty and boring."
    show pov embarrassed at left
    show haz embarrassed_talk at right
    haz "If you say so. No point following me then, haha."
    haz "I'll go back to totally doing actual work."

    jump lbl_adultstore_day
