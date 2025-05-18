## Operation Get The Flyers Back
default operation_lockpick_tries = 0
default operation_lockpick_unlocktry = 0
default operation_lockpick_flyerplace = "bin"
default operation_lockpick_search = "null"

label lbl_operation_get_the_flyers_back:
    scene bg schoolhallway2_day

    "Commence operation: get the flyers back?"
    menu:
        "Yes":
            if operation_flyer == "lockpick":
                jump lbl_operation_get_the_flyers_back_lockpick
            else:
                jump lbl_operation_get_the_flyers_back_distract
        "No":
            jump lbl_schoolhallway2_day

label lbl_operation_get_the_flyers_back_lockpick:
    scene black
    with fade
    $ renpy.pause()
    "After waiting for Lashley to head downstairs…"

    scene bg schoolhallway2_day
    with fade

    if skill_luc >= 15:
        $ operation_lockpick_unlocktry = renpy.random.randint(1,60) #95% chance
    elif skill_luc >= 10:
        $ operation_lockpick_unlocktry = renpy.random.randint(1,12) #75% chance
    elif skill_luc >= 5:
        $ operation_lockpick_unlocktry = renpy.random.randint(1,6) #50% chance
    else:
        $ operation_lockpick_unlocktry = renpy.random.randint(1,4) #25% chance

    ## SPRITES
    show pov embarrassed_talk at left
    show eff embarrassed at right
    with dissolve
    pov "Alright, is everyone in their places?"
    show pov shocked at left
    show eff neutral_talk at right
    eff "Yeah, Jacob and Cole are downstairs chatting up the dean."
    show pov confused at left
    show eff shocked_talk at right
    eff "..."
    show eff neutral_talk at right
    eff "Edward’s giving the okay signal."
    show pov neutral at left
    show eff smirk_talk at right
    eff "Do your thing, [povname]."
    show pov neutral_talk at left
    show eff smirk at right
    pov "Alright- here goes nothing."

    ## MC starts picking the lock. Based on his luck will depend on whether he gets it in time or not.
    ## CG
    scene bg operationgettheflyersback_1
    with fade
    $ renpy.pause()

    if operation_lockpick_unlocktry >= 4:
        jump lbl_operation_get_the_flyers_back_lockpick_unlocksuccess
    else:
        jump lbl_operation_get_the_flyers_back_lockpick_unlockfail

label lbl_operation_get_the_flyers_back_lockpick_unlockfail:
    ## CG
    pov "Mmmm...."
    pov "This- this is harder than I thought-"
    pov "..."
    pov "{i}Fuck- I messed up.{/i}"

    eff "Dude? How's it goooooing?!"

    pov "Shhh!"
    pov "..."
    pov "{i}Dammit, I have to start all over again-{/i}"

    eff "Abort, abort-"
    eff "Edward’s giving the stop signal."
    eff "Quick, disperse."

    pov "{i}Fuck- we’ll have to try again another day.{/i}"
    pov "{i}I might need some better LUCK next time.{/i}"

label lbl_operation_get_the_flyers_back_lockpick_unlocksuccess:
    ## CG
    pov "I got it!"
    pov "Quick, get in before anyone else sees."

    jump lbl_operation_get_the_flyers_back_lockpick_search

label lbl_operation_get_the_flyers_back_lockpick_search:
    ## In the office
    scene bg principaloffice_day
    with fade

    ## NO SPRITE NEEDED
    pov "I actually need you at the door watching out for Edward’s signals while I look."

    eff "No problemo, check all the places."

    ## You look around for the flyers. You luck will depend on how many tries you have to search the 5 different places; side bookshelf, desk, bin, trophy cabinet, back bookshelf.

    menu:
        "Check desk":
            $ operation_lockpick_search = "desk"
        "Check bin":
            $ operation_lockpick_search = "bin"
        "Check back bookcase":
            $ operation_lockpick_search = "backbookcase"
        "Check side bookcase":
            $ operation_lockpick_search = "sidebookcase"
        "Check trophy cabinet":
            $ operation_lockpick_search = "trophy"

    if operation_lockpick_flyerplace == operation_lockpick_search:
        jump lbl_operation_get_the_flyers_back_lockpick_searchsuccess
    else:
        $ operation_lockpick_tries -= 1
        if operation_lockpick_tries <= 0:
            jump lbl_operation_get_the_flyers_back_lockpick_searchfail
        else:
            pov "{i}Nope. Not here.{/i}"
            if operation_lockpick_tries == 1:
                pov "{i}Based on my luck, I have [operation_lockpick_tries] try left.{/i}"
            else:
                pov "{i}Based on my luck, I have [operation_lockpick_tries] tries left.{/i}"

            jump lbl_operation_get_the_flyers_back_lockpick_search

label lbl_operation_get_the_flyers_back_lockpick_searchfail:
    ## If fail, you have to leave the office and try again another time.
    ## NO SPRITES NEEDED

    eff "Abort!"
    eff "Quick, [povname]. We gotta get out of here."

    pov "Fuck."
    pov "So unlucky… where the hell did she put it?"

    scene bg schoolhallway2_day
    with fade

    jump lbl_schoolhallway2_day_setup

label lbl_operation_get_the_flyers_back_lockpick_searchsuccess:
    ## If successful, you take the flyers that includes the maps.
    ## NO SPRITES NEEDED

    pov "I found it!"
    pov "Let’s get the fuck outta here."

    eff "I’ll signal back to Edward that we got it."
    eff "Disperse and we’ll meet back at the hideout."

    ## You exit the office and everything goes back to normal.

    scene bg schoolhallway2_day
    with fade

    $ main_story = 155

    jump lbl_schoolhallway2_day_setup

label lbl_operation_get_the_flyers_back_distract:
    scene black
    with fade
    $ renpy.pause()
    "After waiting for Lashley to head downstairs…"

    scene bg schoolhallway1_day
    with fade
    ## SPRITES

    show pov neutral_talk at left
    with dissolve
    pov "Uh- hey! Dean Lashley."

    menu:
        "I have a question for you.":
            show pov embarrassed_talk at left
            show pri neutral at Position(xpos=1200)
            show col neutral at Position(xpos=1700)
            with dissolve
            pov "I have a question for you."
            show pov embarrassed at left
            show pri neutral_talk at Position(xpos=1200)
            pri "What can I help you with, [povname]?"
            show pov embarrassed_talk at left
            show pri neutral at Position(xpos=1200)
            pov "Well- you see- uhhhhh…"
            show pov shocked_talk at left
            pov "Shoot-"
            show pov embarrassed_talk at left
            pov "I completely forgot what I was gonna ask…"
            show pov bored_talk at left
            pov "Mmmmmm"
            pov "It’s-"
            show pov shocked_talk at left
            pov "It’s on the tip of my tongue-"
            pov "Give me a sec-"
            show pov bored at left
            hide pri
            show col smirk at Position(xpos=1700)
            with dissolve
            col "…"
            show pov embarrassed_talk at left
            pov "Well, y’know-"
            show col confused at Position(xpos=1700)
            pov "No, that wasn’t it…"
            show pov embarrassed at left
            show col smirk at Position(xpos=1700)
            pri "I’m sure you’ll remember it later, find me in my office when you do."

        "Do you have the time with you?":
            show pov embarrassed_talk at left
            show pri confused at Position(xpos=1200)
            show col neutral at Position(xpos=1700)
            pov "Do you have the time with you?"
            show pov embarrassed at left
            show pri smirk_talk at Position(xpos=1200)
            show col shocked at Position(xpos=1700)
            pri "It’s 9:08am"
            show pov embarrassed_talk at left
            show pri bored at Position(xpos=1200)
            pov "Thanks."
            show col embarrassed_talk at Position(xpos=1700)
            col "Wait-!"
            show pov embarrassed at left
            show col confused_talk at Position(xpos=1700)
            col "9:08?"
            show col shocked_talk at Position(xpos=1700)
            col "Dang, I’m late for class."
            show pov neutral at left
            show pri bored_talk at Position(xpos=1200)
            show col shocked at Position(xpos=1700)
            pri "Yes, you guys are."
            show pri smirk_talk at Position(xpos=1200)
            pri "Hurry along before I have to send you to the dean’s office."
            show pri neutral_talk at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pri "Hahaha, that’s a joke. I’m the dean."
            show pov confused at left
            pri "I have a busy itinerary already."
            show pov embarrassed at left
            show pri neutral_talk at Position(xpos=1200)
            pri "Chow, kids, and God bless."

        "There’s something going on outside.":
            show pov confused_talk at left
            show pri confused at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pov "There’s something going on outside."
            show pov confused at left
            show pri confused_talk at Position(xpos=1200)
            pri "What’s going on outside?"
            show pov embarrassed_talk at left
            show pri confused at Position(xpos=1200)
            show col bored at Position(xpos=1700)
            pov "U-uhhhh."
            pov "Military recruiters!"
            show pov embarrassed at left
            show pri smirk_talk at Position(xpos=1200)
            pri "Are there now?"
            show pov embarrassed_talk at left
            show pri confused at Position(xpos=1200)
            pov "Yeah, they’re trying to get me to sign up."
            pov "They’re really pushy about it too."
            show pov embarrassed at left
            show pri confused_talk at Position(xpos=1200)
            pri "Remember, [povname]. You always have the power to say no."
            pri "If the military isn’t meant for you, then God wouldn’t have forced it onto you."
            show pri neutral_talk at Position(xpos=1200)
            pri "Trust the Lord."
            show pov bored at left
            show pri neutral at Position(xpos=1200)
            show col smirk_talk at Position(xpos=1700)
            col "See! That’s what I was telling him."
            show pri neutral_talk at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pri "Listen to Cole, [povname]. He’s a smart kid."
            show pov embarrassed at left
            show pri bored_talk at Position(xpos=1200)
            pri "Anyway, I gotta go."

    show pov shocked_talk at left
    show col embarrassed at Position(xpos=1700)
    pov "WAIT!"
    show pov shocked at left
    show pri shocked_talk at Position(xpos=1200)
    pri "Good heavens!"
    show pov confused at left
    show pri confused_talk at Position(xpos=1200)
    pri "What?"
    show pov embarrassed_talk at left
    show pri confused at Position(xpos=1200)
    show col bored at Position(xpos=1700)
    pov "Uhhh-"

    menu:
        "How’s work?":
            show pov neutral_talk at left
            show pri neutral at Position(xpos=1200)
            show col bored at Position(xpos=1700)
            pov "How’s work?"
            pov "You must be busy today, yeah?"
            show pov neutral at left
            show pri embarrassed_talk at Position(xpos=1200)
            pri "I actually am pretty busy, you’re right."
            pri "There’s no rest for poor, ol’ me."
            show pri embarrassed at Position(xpos=1200)
            show col neutral_talk at Position(xpos=1700)
            col "And you’re doing such a great job at it."
            show pri shocked at Position(xpos=1200)
            show col smirk_talk at Position(xpos=1700)
            col "Everytime I come here, I feel inspired and motivated to learn because of you."
            show pri smirk_talk at Position(xpos=1200)
            show col neutral at Position(xpos=1700)
            pri "That’s such a nice thing to hear, Cole. Thank you for saying that."
            show pov neutral at left
            show pri neutral_talk at Position(xpos=1200)
            pri "Let’s start the day off strong, shall we?"
            pri "I’ll see you two later."

        "Cole has something to confess.":
            show pov shocked_talk at left
            show pri neutral at Position(xpos=1200)
            show col confused_talk at Position(xpos=1700)
            pov "Cole has something to confess."
            show pov embarrassed at left
            show col confused_talk at Position(xpos=1700)
            col "Me?"
            show pri neutral_talk at Position(xpos=1200)
            show col confused at Position(xpos=1700)
            pri "What is it, Cole?"
            show pov embarrassed at left
            show pri neutral at Position(xpos=1200)
            show col embarrassed_talk at Position(xpos=1700)
            col "Oh- uh. I was just-"
            show pov smirk at left
            show col shocked_talk at Position(xpos=1700)
            col "Well, [povname] here."
            show pov shocked at left
            show pri shocked at Position(xpos=1200)
            show col smirk_talk at Position(xpos=1700)
            col "Has a crush on you!"
            show pov shocked_talk at left
            show pri confused at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pov "Cole?!"
            show pov embarrassed_talk at left
            show pri bored at Position(xpos=1200)
            pov "N-no nono… that’s not-"
            show pov shocked_talk at left
            pov "Cole."
            show pov embarrassed at left
            show col angry_talk at Position(xpos=1700)
            col "Don’t throw me under the bus like that."
            show pri bored_talk at Position(xpos=1200)
            show col embarrassed at Position(xpos=1700)
            pri "If you don’t mind you two, I have things to do. I don’t have time for your boy-talk shenanigans."
            show pov shocked at left
            pri "And I hope you two ARE joking, that would be very inappropriate, [povname]."

        "Did you catch the new webslinger-man movie?":
            show pov shocked_talk at left
            show pri confused at Position(xpos=1200)
            show col neutral at Position(xpos=1700)
            pov "Did you catch the new webslinger-man movie?"
            show pov shocked at left
            show pri embarrassed_talk at Position(xpos=1200)
            pri "I have not. Did you catch it over the weekend?"
            show pov smirk_talk at left
            show pri confused at Position(xpos=1200)
            pov "I did! It is one of the best movies I’ve ever seen and you should definitely go see it too!"
            show pov smirk at left
            show col smirk_talk at Position(xpos=1700)
            col "I can get you discounted tickets, call it a perk for being such an awesome dean."
            show pri neutral_talk at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pri "My, that sounds lovely. Unfortunately I don’t have much time to go to the cinemas nowadays."
            show pov shocked at left
            show pri embarrassed_talk at Position(xpos=1200)
            show col confused at Position(xpos=1700)
            pri "But I appreciate the offer and recommendation."
            show pov bored at left
            show pri neutral_talk at Position(xpos=1200)
            show col bored at Position(xpos=1700)
            pri "Now, if you’ll excuse me.."

    show pov shocked_talk at left
    show pri confused at Position(xpos=1200)
    show col embarrassed at Position(xpos=1700)
    pov "WAIT-"
    show pov shocked_talk at left
    show pri bored_talk at Position(xpos=1200)
    pri "What is it now, [povname]. Last thing, and anything else, you can inquire with me some other time."
    show pov embarrassed_talk at left
    show pri confused at Position(xpos=1200)
    pov "Errmm-"

    menu:
        "What’s that sweet smell?":
            show pov neutral_talk at left
            show pri shocked at Position(xpos=1200)
            show col bored at Position(xpos=1700)
            pov "What’s that sweet smell?"
            show pov embarrassed_talk at left
            pov "Is it a new perfume you’re wearing?"
            show pov neutral at left
            show pri smirk_talk at Position(xpos=1200)
            pri "Oh- well, yes actually. It’s new. I bought it just last week."
            show pov neutral_talk at left
            show pri neutral at Position(xpos=1200)
            pov "It smells terrific."
            show pov neutral at left
            show pri embarrassed_talk at Position(xpos=1200)
            pri "Why, thank you."
            show pri confused_talk at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pri "It’s a bit unusual for a student to be mentioning it but I can’t say it can be helped if I was the one that put it on."
            show pri shocked at Position(xpos=1200)
            show col smirk_talk at Position(xpos=1700)
            col "It’s definitely your scent."
            show pri embarrassed at Position(xpos=1200)
            show col shocked_talk at Position(xpos=1700)
            col "Oh- I didn’t mean it that way."
            show pov neutral at left
            show col neutral_talk at Position(xpos=1700)
            col "You know what I mean."
            show pri neutral_talk at Position(xpos=1200)
            show col neutral at Position(xpos=1700)
            pri "Thank you, you two."
            show pov embarrassed at left
            show col embarrassed at Position(xpos=1700)
            pri "And if that’s it then I’ll be off."

        "What’s for lunch at the cafeteria today?":
            show pov confused_talk at left
            show pri shocked at Position(xpos=1200)
            show col embarrassed at Position(xpos=1700)
            pov "What’s for lunch at the cafeteria today?"
            show pov confused at left
            show pri embarrassed_talk at Position(xpos=1200)
            pri "I’m not sure. I’m sure you’ll find out sooner or later."
            show pov shocked_talk at left
            show pri shocked at Position(xpos=1200)
            show col confused at Position(xpos=1700)
            pov "Oh- but- I really need to know now because…"
            show pov confused_talk at left
            show pri confused at Position(xpos=1200)
            pov "I have-"
            show pov shocked_talk at left
            show pri shocked at Position(xpos=1200)
            pov "Allergies!"
            show pov embarrassed_talk at left
            pov "And I would really like to know if I should get food somewhere else or not."
            show pov embarrassed at left
            show pri embarrassed_talk at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pri "Well, you can probably head to the cafeteria now and ask about it if it worries you that much."
            show pri bored_talk at Position(xpos=1200)
            pri "Do it between classes though."
            show pov bored at left
            pri "Now if you’ll excuse me."

        "I lost my USB the other day.":
            show pov shocked_talk at left
            show pri confused at Position(xpos=1200)
            show col neutral at Position(xpos=1700)
            pov "I lost my USB the other day."
            show pov shocked at left
            show pri neutral_talk at Position(xpos=1200)
            pri "You should check out the lost and found."
            show pov embarrassed at left
            show col smirk_talk at Position(xpos=1700)
            col "It’s not there, trust me."
            show pov confused at left
            show pri shocked_talk at Position(xpos=1200)
            pri "Oh- well, I can’t help you there, [povname]. You should really take care of your things more carefully."
            show pov embarrassed at left
            show pri bored_talk at Position(xpos=1200)
            pri "It’s not the school’s responsibility to look after your things for you."
            pri "You should know better."
            show pov bored_talk at left
            show pri bored at Position(xpos=1200)
            show col smirk at Position(xpos=1700)
            pov "Yeah, right. Sorry."
            show pri neutral_talk at Position(xpos=1200)
            pri "Now, if you’ll excuse me."

    show pov bored_talk at left
    show pri confused at Position(xpos=1200)
    show col neutral at Position(xpos=1700)
    pov "Oh- but-"
    show pov confused at left
    show pri embarrassed_talk at Position(xpos=1200)
    pri "Talk to me about it later, [povname]."
    show pri neutral_talk at Position(xpos=1200)
    pri "I’m sorry but I’m really busy right now. I don’t have all morning for small talk."
    show pov embarrassed at left
    show pri smirk_talk at Position(xpos=1200)
    show col bored at Position(xpos=1700)
    pri "Thank you and God bless the both of you."

    ## Lashley leaves the scene.
    show pov confused at left
    hide pri
    show col shocked_talk at Position(xpos=1700)
    with dissolve
    col "Oh- Jacob’s given the okay signal."
    show col smirk_talk at Position(xpos=1700)
    col "We’re good, they got it."
    show pov bored at left
    show col neutral_talk at Position(xpos=1700)
    col "Good job, [povname]."
    col "It wasn’t the cleanest method but it got the job done."
    show pov embarrassed_talk at left
    show col neutral at Position(xpos=1700)
    pov "Thanks for backing me up."
    show pov embarrassed at left
    show col smirk_talk at Position(xpos=1700)
    col "I was just enjoying the shitshow to be honest."
    show pov smirk_talk at left
    show col smirk at Position(xpos=1700)
    pov "Pfft. Whatever."
    show pov neutral at left
    show col neutral at Position(xpos=1700)
    pov "Let’s meet up at the hideout later like we agreed."
    show pov neutral at left
    show col smirk_talk at Position(xpos=1700)
    col "Gotcha, peace dude. Good job."

    scene black
    with fade
    scene bg schoolhallway1_day
    with fade

    $ main_story = 155

    jump lbl_schoolhallway1_day_setup
