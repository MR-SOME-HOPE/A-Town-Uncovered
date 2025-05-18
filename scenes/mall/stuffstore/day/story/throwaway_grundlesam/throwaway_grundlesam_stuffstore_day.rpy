## Throwaway Grundle Sam Stuff Store Room Day Conversation ##
label lbl_stuffstore_day_grundlesam:
    ## Main Story
    ## Answers Around Town Sexworld
    if main_story <= 35 and insexworld == 1:
        jump lbl_stuffstore_day_grundlesam_sexworld
    ## Investigations
    elif main_story == 84:
        jump lbl_investigations_grundlesam
    # ## Buukakki Followers Are Everywhere
    # elif main_story == 151:
    #     jump lbl_buukakki_followers_are_everywhere_grundlesam
    ## Side Story
    if grundlesam_path == 0:
        jump lbl_stuffstore_day_grundlesam_0
    ## NO EVENT
    else:
        show pov embarrassed at left
        with dissolve
        show sam neutral_talk at right
        with dissolve
        call lbl_stuffstore_counter_check
        sam "OooH! Hi again, ma good sir! Hehehe~"

        jump lbl_stuffstore_day_grundlesam_menu

label lbl_stuffstore_day_grundlesam_convo:
## 1 - 3 is morning exclusive
## 4 - 6 is afternoon exclusive
## 7 - 10 is interchangeable
    if gtime == 0:
        if date == 6 or date == 11 or date == 22 or date == 0 or date == 4:
            jump lbl_stuffstore_day_grundlesam_1
        elif date == 7 or date == 18 or date == 21 or date == 27 or date == 3:
            jump lbl_stuffstore_day_grundlesam_2
        elif date == 10 or date == 17 or date == 23 or date == 29 or date == 14:
            jump lbl_stuffstore_day_grundlesam_3
        elif date == 8 or date == 20 or date == 24 or date == 30:
            jump lbl_stuffstore_day_grundlesam_7
        elif date == 9 or date == 16 or date == 26 or date == 13:
            jump lbl_stuffstore_day_grundlesam_8
        elif date == 1 or date == 19 or date == 25 or date == 5:
            jump lbl_stuffstore_day_grundlesam_9
        elif date == 2 or date == 15 or date == 28 or date == 12:
            jump lbl_stuffstore_day_grundlesam_10

    elif gtime == 1:
        if date == 2 or date == 19 or date == 22 or date == 0 or date == 10:
            jump lbl_stuffstore_day_grundlesam_4
        elif date == 1 or date == 18 or date == 30 or date == 7 or date == 15:
            jump lbl_stuffstore_day_grundlesam_5
        elif date == 4 or date == 20 or date == 28 or date == 16 or date == 27:
            jump lbl_stuffstore_day_grundlesam_6
        elif date == 3 or date == 11 or date == 23 or date == 29:
            jump lbl_stuffstore_day_grundlesam_7
        elif date == 6 or date == 12 or date == 24 or date == 26:
            jump lbl_stuffstore_day_grundlesam_8
        elif date == 5 or date == 13 or date == 21 or date == 17:
            jump lbl_stuffstore_day_grundlesam_9
        elif date == 9 or date == 14 or date == 25 or date == 8:
            jump lbl_stuffstore_day_grundlesam_10

## Menu
label lbl_stuffstore_day_grundlesam_menu:
    menu:
        "Talk":
            jump lbl_stuffstore_day_grundlesam_convo
        "Trade Totems":
            show pov neutral at left
            show sam neutral_talk at right
            sam "Let's trade, my good sir."
            jump lbl_stuffstoremenu_wolf
        "Ask about...":
            menu:
                "Totem Animals":
                    sam "The Wolf Totem gives you Charisma benefits."
                    sam "The Owl Totem gives you Intelligence benefits."
                    sam "The Rabbit Totem gives you Luck benefits."
                    sam "The Elk Totem gives you Stamina benefits."
                    sam "And the Bear Totem gives you Strength benefits."
                    sam "Hehehe~ {i}*snort*{/i}"

                    jump lbl_stuffstore_day_grundlesam_menu
                "Totem Materials":
                    sam "Hehehe~ Alright, to keep things simple. Let's pretend we're in a game, okay? {i}*snort*{/i}"
                    sam "The Wooden Material gives you +1 Points every night."
                    sam "The Bronze Material gives you +2 Points every night."
                    sam "The Silver Material gives you +3 Points every night."
                    sam "The Gold Material gives you +4 Points every night."
                    sam "The Meteor Rock Material gives you +5 Points every night."
                    sam "Hehehe~ {i}*snort*{/i}"
                    sam "And just to add, Animal Totems and Add-ons of the same benefit stack points. Hehehe~"

                    jump lbl_stuffstore_day_grundlesam_menu
                "Totem Add-ons":
                    sam "The Scarf add-on gives you Charisma benefits."
                    sam "The Monocle add-on gives you Intelligence benefits."
                    sam "The Four Leaf Clover add-on gives you Luck benefits."
                    sam "The Sweat Drop add-on gives you Stamina benefits."
                    sam "And the Belt add-on gives you Strength benefits."
                    sam "Hehehe~ {i}*snort*{/i}"
                    sam "And just to add, Animal Totems and Add-ons of the same benefit stack points. Hehehe~"

                    jump lbl_stuffstore_day_grundlesam_menu
        "Spare Boxes?" if sister_path == 29 and stuffstore_spareboxes == 0:
            jump lbl_stuffstore_spare_boxes
        "A job" if 16 <= main_story <= 21 and nextday_ajob == 0 and stuffstore_ajob == 0:
            jump lbl_stuffstore_day_grundlesam_ajob
        "Nevermind.":
            hide pov embarrassed
            with dissolve
            show sam embarrassed at right
            sam "..."
            show sam embarrassed_talk at right
            sam "Nice talking to you, ma good sir."

            jump lbl_stuffstore_day

## Morning Exclusive
label lbl_stuffstore_day_grundlesam_1:
    show pov embarrassed at left
    show sam neutral_talk at right
    sam "Morning! What can I do you for, ma good sir?"
    show pov embarrassed_talk at left
    show sam neutral at right
    pov "Hi, I just uh.. I was bored so I came here to see what's up."
    show pov embarrassed at left
    show sam smirk_talk at right
    sam "The usual, everything's good or as good as it can be."
    show pov shocked at left
    sam "Hehehehehe~"
    show pov confused at left
    show sam smirk_talk at right
    sam "What about you?"
    show pov bored_talk at left
    show sam embarrassed at right
    pov "As I said, just bored."

    jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_2:
    show pov neutral at left
    show sam neutral_talk at right
    sam "Good morning, ma good sir!"
    show pov embarrassed at left
    show sam smirk_talk at right
    sam "Decided to trade in some totems?"
    show pov embarrassed_talk at left
    show sam neutral at right
    pov "Morning. And maybe. We'll see."
    show pov neutral_talk at left
    show sam shocked at right
    pov "I just sorta stopped by to check out the cool knick-knacks."
    show pov embarrassed at left
    show sam shocked_talk at right
    sam "Y- you think my knick-knacks are cool?"
    show pov embarrassed_talk at left
    show sam shocked at right
    pov "Quite."
    show pov embarrassed at left
    show sam neutral_talk at right
    sam "Hehehehehe~ Thank you, ma good sir!"

    jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_3:
    show pov neutral_talk at left
    show sam neutral at right
    pov "Good morning, Grundle Sam."
    show pov confused_talk at left
    show sam confused at right
    pov "Is- 'Grundle' really part of your name?"
    show pov smirk_talk at left
    show sam embarrassed at right
    pov "Is that a first name? Is Sam your second or last name?"
    show pov confused_talk at left
    pov "I have a lot of questions."
    show pov confused at left
    sam "..."
    show pov bored at left
    show sam embarrassed_talk at right
    sam "Please leave your inquiries in the suggestion box on your way out, ma good sir."

    jump lbl_stuffstore_day

## Afternoon Exclusive
label lbl_stuffstore_day_grundlesam_4:
    show pov neutral at left
    show sam neutral_talk at right
    sam "Afternoon, ma good sir."
    show pov neutral_talk at left
    show sam shocked at right
    pov "Afternoon, ma better sir."
    show pov neutral at left
    show sam smirk_talk at right
    sam "Afternoon, ma best sir."
    show pov smirk_talk at left
    show sam smirk at right
    pov "Afternoon, ma better-than-best sir."
    show pov smirk at left
    sam "..."
    show pov confused at left
    show sam smirk_talk at right
    sam "Are you interested in-"
    show pov neutral_talk at left
    show sam bored at right
    pov "Thanks, I'll be going now."

    jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_5:
    show pov neutral_talk at left
    show sam neutral at right
    pov "Hey, Sam."
    pov "Nice day today, aye?"
    show pov embarrassed at left
    show sam smirk_talk at right
    sam "I wouldn't know, I haven't been out of my store in a while."
    show pov shocked at left
    sam "Hehehehe~"
    show pov embarrassed at left
    sam "Why do you think I'm so pale."
    show pov embarrassed_talk at left
    show sam confused at right
    pov "I thought it was all the incense."

    jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_6:
    show pov smirk_talk at left
    show sam neutral at right
    pov "Got anything new today, Sam?"
    show pov neutral at left
    show sam neutral_talk at right
    sam "Not a lot if anything at all, ma good sir."
    show sam embarrassed_talk at right
    sam "Trading totems don't exactly offer much opportunity to bring in new stock."
    show pov embarrassed_talk at left
    show sam confused at right
    pov "I'm not a business-man but I kne-"
    show pov shocked at left
    show sam smirk_talk at right
    sam "The dreamcatchers are pretty popular though."
    show pov embarrassed at left
    show sam embarrassed_talk at right
    sam "I should've invested more into those... Hehehe~"

    jump lbl_stuffstore_day

## Interchangeable
label lbl_stuffstore_day_grundlesam_7:
    show pov smirk_talk at left
    show sam confused at right
    pov "Hey, Sam. You close with anyone else at the mall?"
    show pov confused at left
    show sam embarrassed_talk at right
    sam "I've tried to introduce myself to some of my neighbours but-"
    show pov embarrassed at left
    show sam sad_talk at right
    sam "I guess they don't like me very much, ma good sir."
    show sam embarrassed_talk at right
    sam "Hehehe- hehe~ he... {i}*sniffs*{/i}"
    show pov shocked at left
    show sam sad at right
    pov "{i}Shit, I'm getting out of here before I have to deal with this.{/i}"
    show pov shocked at left
    show sam sad_talk at right
    sam "{i}*Sobs harder*{/i}"

    jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_8:
    show pov smirk_talk at left
    show sam neutral at right
    pov "Sam, the man. The good sir, for sure."
    show pov neutral at left
    show sam neutral_talk at right
    sam "Hello, ma good sir."
    show sam smirk_talk at right
    sam "You sound to be in a good mood, I can guarantee it's due to my new stock of mood rocks."
    show pov smirk_talk at left
    show sam smirk at right
    pov "Maybe it's just a coincidence."
    show pov confused at left
    show sam smirk_talk at right
    sam "Maybe it's not. How about you buy one and find out?"
    show pov smirk at left
    show sam bored at right
    pov "Maybe I'll get out of your hair and think about it."

    jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_9:
    show pov confused at left
    show sam neutral_talk at right
    sam "Hello, good to see you again, ma good sir. Hehehe~"
    show pov confused_talk at left
    show sam smirk at right
    pov "What's so funny?"
    show sam embarrassed at right
    pov "Is there something on my face?"
    show pov confused at left
    show sam neutral_talk at right
    sam "No, not at all. I just- I remember a lot of funny memories."
    sam "Hehehehe~"
    show pov smirk_talk at left
    show sam bored at right
    pov "Confusious says not to dwell on the past."
    show pov smirk at left
    sam "..."

    jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_10:
    show pov confused at left
    show sam smirk_talk at right
    sam "Hey, ma good sir. You here for some fortune telling."
    show pov neutral_talk at left
    show sam neutral at right
    pov "I wasn't originally but I can do for a little look into what's ahead."
    show pov neutral at left
    show sam bored at right
    sam "Hmmm...."
    show pov embarrassed at left
    sam "Hummmmmmm..."
    show pov confused at left
    show sam bored_talk at right
    sam "Oh yes, I can see it! I can see you!"
    show pov bored at left
    sam "Buying my whole stock of-"
    show pov bored_talk at left
    show sam shocked at right
    pov "Alright, I'm out. That was very insightful, Sam."

    jump lbl_stuffstore_day
