## Throwaway Chat ##
label lbl_how_can_i_help_you_0:
    show pov neutral_talk at left
    with dissolve
    show jan neutral at right
    call lbl_retailstore_counter_check
    with dissolve
    pov "Hey."
    show pov neutral at left
    show jan neutral_talk at right
    jan "Hi, how can I help you today?"

    jump lbl_how_can_i_help_you_1

## Menu
label lbl_how_can_i_help_you_1:
    show pov neutral_talk at left
    show jan neutral at right
    menu:
        "Electronics":
            show pov neutral at left
            show jan neutral_talk at right
            jan "Sure, right this way."

            jump lbl_retailstore_electronics_day

        "Clothes":
            show pov neutral at left
            show jan neutral_talk at right
            jan "Sure, they're just right this way."

            jump lbl_retailstore_clothing_day

        "Looking for... something":
            show pov neutral at left
            show jan neutral_talk at right
            jan "Not quite sure what you're looking for? Try this aisle."

            jump lbl_retailstore_misc_day

        "Spare boxes?" if sister_path == 29 and retailstore_spareboxes == 0:
            jump lbl_retailstore_day_janae_spareboxes

        "A job" if 16 <= main_story <= 21 and nextday_ajob == 0 and retailstore_ajob == 0:
            jump lbl_retailstore_day_janae_job

        "Fun in the back?": ## TEMP
            jump lbl_janae_plowed_over_boxes

        "Talk":
            jump lbl_retailstore_day_janae_convo

        "Nevermind.":
            show pov embarrassed_talk at left
            show jan neutral at right
            pov "Actually, nevermind. I don't really know why I'm here."
            show pov neutral at left
            show jan neutral_talk at right
            jan "No worries. Please come by anytime if you need anything."

            jump lbl_retailstore_day

label lbl_retailstore_day_janae_convo:
## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if gtime == 0:
        if date == 8 or date == 11 or date == 25 or date == 0:
            jump lbl_retailstore_day_janae_1
        elif date == 9 or date == 12 or date == 27:
            jump lbl_retailstore_day_janae_2
        elif date == 7 or date == 20 or date == 28:
            jump lbl_retailstore_day_janae_3
        elif date == 6 or date == 13 or date == 29:
            jump lbl_retailstore_day_janae_4
        elif date == 5 or date == 14 or date == 24:
            jump lbl_retailstore_day_janae_5
        elif date == 10 or date == 15 or date == 21:
            jump lbl_retailstore_day_janae_11
        elif date == 4 or date == 19 or date == 22:
            jump lbl_retailstore_day_janae_12
        elif date == 3 or date == 18 or date == 23:
            jump lbl_retailstore_day_janae_13
        elif date == 2 or date == 17 or date == 30:
            jump lbl_retailstore_day_janae_14
        elif date == 1 or date == 16 or date == 26:
            jump lbl_retailstore_day_janae_15
    elif gtime == 1:
        if date == 6 or date == 18 or date == 30 or date == 0:
            jump lbl_retailstore_day_janae_6
        elif date == 7 or date == 11 or date == 29:
            jump lbl_retailstore_day_janae_7
        elif date == 8 or date == 17 or date == 25:
            jump lbl_retailstore_day_janae_8
        elif date == 9 or date == 16 or date == 26:
            jump lbl_retailstore_day_janae_9
        elif date == 10 or date == 15 or date == 27:
            jump lbl_retailstore_day_janae_10
        elif date == 1 or date == 14 or date == 28:
            jump lbl_retailstore_day_janae_11
        elif date == 5 or date == 13 or date == 24:
            jump lbl_retailstore_day_janae_12
        elif date == 4 or date == 12 or date == 23:
            jump lbl_retailstore_day_janae_13
        elif date == 3 or date == 20 or date == 22:
            jump lbl_retailstore_day_janae_14
        elif date == 2 or date == 19 or date == 21:
            jump lbl_retailstore_day_janae_15

## Morning Exclusive
label lbl_retailstore_day_janae_1:
    show pov confused_talk at left
    show jan confused at right
    pov "You guys open yet."
    show pov confused at left
    jan "..."
    show jan confused_talk at right
    jan "Look around, [povname]."
    jan "What do you think?"
    show pov embarrassed_talk at left
    show jan smirk at right
    pov "Hmmm... my psychic powers are telling me... 'yes'?"
    show pov neutral at left
    show jan smirk_talk at right
    jan "It's impressive because it's correct."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_2:
    show pov neutral_talk at left
    show jan neutral at right
    pov "Anything on special today?"
    show pov confused at left
    show jan neutral_talk at right
    jan "Plenty. We have a massive sale going on on fake plant in geometric glass pots."
    show pov confused_talk at left
    show jan neutral at right
    pov "I see the same ones every single time I shop here."
    show jan confused at right
    pov "At this rate, they're basically going to invade every basic-bitch's house."
    show pov shocked at left
    show jan confused_talk at right
    jan "Excuse me but I love those little geometric pot plants."
    show pov embarrassed_talk at left
    show jan smirk at right
    pov "I mean, you're the exception of course."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_3:
    show pov bored_talk at left
    show jan confused at right
    pov "Ugh, mornings. Do you have anything for that."
    show pov bored at left
    show jan confused_talk at right
    jan "Mornings? No, we're not a coffee shop, [povname]."
    show pov confused at left
    show jan neutral_talk at right
    jan "Although the toys section has some dancing dolls."
    jan "A little creepy but you can dance along to wake your body up."
    show pov bored_talk at left
    show jan smirk at right
    pov "You make it sound so tempting."
    show pov shocked at left
    show jan smirk_talk at right
    jan "Don't knock it until you try it. Just like my perverted uncle said."
    show pov embarrassed at left
    show jan embarrassed_talk at right
    jan "I'm joking. That was just a bit of dark humour."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_4:
    show pov neutral_talk at left
    show jan neutral at right
    pov "Nothing, just wanted a little ol' chat."
    pov "Did anything interesting last night?"
    show pov neutral at left
    show jan neutral_talk at right
    jan "Just had some drinks out with some friends. Nothing big."
    show pov shocked at left
    jan "What about you, [povname]?"
    show pov embarrassed_talk at left
    show jan confused at right
    pov "I uh- don't remember..."
    show pov sad_talk at left
    show jan smirk at right
    pov "... Jeez, I don't even remember what I had for breakfast today."
    show pov embarrassed at left
    show jan smirk_talk at right
    jan "Haha, I can relate, don't worry."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_5:
    show pov neutral_talk at left
    show jan neutral at right
    pov "Yeah, hey."
    show pov neutral at left
    show jan embarrassed_talk at right
    jan "Hey?"
    show pov neutral_talk at left
    show jan embarrassed at right
    pov "Oh, hi. How's it going?"
    show pov confused at left
    show jan confused_talk at right
    jan "Are you okay?"
    show pov confused_talk at left
    show jan confused at right
    pov "Yeah, why do you ask?"
    show pov confused at left
    show jan confused_talk at right
    jan "Because this conversation is totally confusing me."

    jump lbl_retailstore_day

## Afternoon Exclusive
label lbl_retailstore_day_janae_6:
    show pov neutral_talk at left
    show jan neutral at right
    pov "When do you get off?"
    show pov neutral at left
    show jan confused_talk at right
    jan "Late, closing time. Why?"
    show pov neutral_talk at left
    show jan confused at right
    pov "Just curious. Thought we could hang out later."
    show pov neutral at left
    show jan embarrassed_talk at right
    jan "Sorry, I have other places to be straight after."
    show pov embarrassed at left
    jan "Thank you though."
    show pov embarrassed_talk at left
    show jan neutral at right
    pov "Maybe next time then."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_7:
    show pov neutral_talk at left
    show jan neutral at right
    pov "Did you have lunch yet?"
    show pov neutral at left
    show jan neutral_talk at right
    jan "Yeah, just had my break about an hour ago."
    show jan sad_talk at right
    jan "A few more hours left to go, thank God."
    show jan confused_talk at right
    jan "Aren't you usually working around this time?"
    show pov neutral_talk at left
    show jan neutral at right
    pov "I'm a casual employee. It's more just whenever I feel."
    show pov neutral at left
    show jan smirk_talk at right
    jan "Right, gotcha."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_8:
    show pov confused_talk at left
    show jan confused at right
    pov "Does this job pay well?"
    show pov confused at left
    show jan neutral_talk at right
    jan "One could say it pays 'well enough', and another would say 'not enough at all'."
    jan "Really up to your lifestyle."
    show pov smirk_talk at left
    show jan confused at right
    pov "What if I want to be a billionaire?"
    show pov embarrassed at left
    show jan bored_talk at right
    jan "You... want to be a billionaire, and you're asking if this job pays well?"
    jan "I'd say pay attention in classes more."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_9:
    show pov neutral_talk at left
    show jan neutral at right
    pov "Can I get a friend's discount?"
    show pov bored at left
    show jan confused_talk at right
    jan "Sorry, we don't do that here."
    show pov smirk_talk at left
    show jan confused at right
    pov "Oh what a shame, I really wanted to buy something but I guess I'll just have to walk away."
    show pov confused at left
    show jan neutral_talk at right
    jan "Sorry to hear that, thanks for coming."
    show pov confused_talk at left
    show jan confused at right
    pov "You're not gonna stop me? You're losing a sale."
    show pov smirk at left
    show jan bored_talk at right
    jan "I'm a retail worker, not a car salesman."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_10:
    show pov confused_talk at left
    show jan neutral at right
    pov "Yeah, why is it that the mall plays the same song on a loop?"
    show pov confused at left
    show jan smirk_talk at right
    jan "Brain washing? Torture? Cheapscapes? Not know what a playlist is?"
    jan "Your guess is as good as mine."
    show pov confused_talk at left
    show jan neutral at right
    pov "Yeah, why is it that the mall plays the same song on a loop?"
    show pov confused at left
    show jan neutral_talk at right
    jan "Brain washing? Torture? Che-"
    show pov shocked at left
    show jan bored_talk at right
    jan "Yeah, it's definitely brain washing."

    jump lbl_retailstore_day

## Interchangeable
label lbl_retailstore_day_janae_11:
    show pov neutral_talk at left
    show jan neutral at right
    pov "Yes, I'm looking for someone."
    show pov neutral at left
    show jan neutral_talk at right
    jan "I may be able to help. What do they look like?"
    show pov smirk_talk at left
    show jan confused at right
    pov "Tall, handsome, foreign-looking, charming as heckers."
    show pov confused at left
    show jan bored_talk at right
    jan "{i}*Sigh*{/i} Once again, [povname]-"
    show pov embarrassed at left
    jan "I have not seen Geoff Silverbloom here."
    show pov embarrassed at left
    show jan smirk at right
    pov "Damnit. I really want his autograph."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_12:
    show pov neutral_talk at left
    show jan neutral at right
    pov "Just wanted to say hi, see how things are with you."
    show pov neutral at left
    show jan confused_talk at right
    jan "Oh, y'know. Work's work."
    show jan embarrassed_talk at right
    jan "Not much to talk about in retail other than complain about customers."
    show pov embarrassed at left
    show jan bored_talk at right
    jan "Like seriously, why are people so frikkin' mean to service workers."
    show pov shocked at left
    show jan angry_talk at right
    jan "I am a human being too!"
    show pov embarrassed_talk at left
    show jan angry at right
    pov "I feel you, Janae. Hang in there, baby."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_13:
    show pov confused_talk at left
    show jan neutral at right
    pov "How come I've never seen you ordering from Ice Cream'py?"
    show pov smirk at left
    show jan neutral_talk at right
    jan "Not really my thing. I like to watch my figure."
    show jan confused_talk at right
    jan "Everything goes straight to my butt and thighs."
    show pov smirk_talk at left
    show jan confused at right
    pov "I see."
    show pov shocked at left
    show jan bored_talk at right
    jan "... So you agree? That my butt is big."
    show pov embarrassed at left
    show jan bored at right
    pov "... N-no comment."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_14:
    show pov confused_talk at left
    show jan confused at right
    pov "Yeah, what's up with Grundle Sam?"
    pov "That weirdo with the cheesy tuxedo shirt next door."
    show pov smirk at left
    show jan confused_talk at right
    jan "Yeah, I don't know. He tried to talk to me but I kinda kept my distance."
    show pov shocked at left
    show jan embarrassed_talk at right
    jan "Usually I'm nice but his eyes seem to be popping out of his skull more than normal."
    show pov neutral_talk at left
    show jan smirk at right
    pov "I've noticed that! I'm glad it wasn't just me."

    jump lbl_retailstore_day

label lbl_retailstore_day_janae_15:
    show pov smirk_talk at left
    show jan confused at right
    pov "Hey, just wondering if you have access to the PA system."
    show pov smirk at left
    show jan confused_talk at right
    jan "Yeah, why?"
    show pov smirk_talk at left
    show jan confused at right
    pov "I lost my friend and his phone's dead. Hoping you can help me out."
    show pov smirk at left
    show jan confused_talk at right
    jan "What's his name?"
    show pov smirk at left
    show jan bored at right
    pov "Last name McCrack-"
    show pov embarrassed at left
    show jan bored_talk at right
    jan "I'm gonna stop you there and I'm gonna stop talking to you now."

    jump lbl_retailstore_day
