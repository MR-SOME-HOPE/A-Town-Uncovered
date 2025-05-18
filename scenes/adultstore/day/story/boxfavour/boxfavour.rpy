## Box Favour ##
label lbl_box_favour:
    default boxfavour_truth = 0

    scene bg adultstore_day
    show pov embarrassed_talk at left
    with dissolve
    show haz neutral at right
    with dissolve
    call lbl_adultstore_counter_check
    pov "Hey Hazel, are you busy?"
    show pov embarrassed at left
    show haz neutral_talk at right
    haz "Oh, hey."
    if hazel_points <= 1:
        show haz smirk_talk at right
        if winc == 1:
            haz "You're [sister]'s brother, right?"
        else:
            haz "You're [sister]'s [sisrole], right?"
        show haz embarrassed_talk at right
        haz "Uh..."
        haz "Sorry, I forgot your name..."
        show pov neutral_talk at left
        show haz neutral at right
        pov "It's [povname]."
        show pov neutral at left
        show haz neutral_talk at right
        haz "Right! That's it!"
    show pov shocked at left
    show haz confused_talk at right
    haz "Say, [povname], have you seen [sister]?"
    show pov embarrassed at left
    haz "We have some work piled up for her but she hasn't shown up in a while."
    haz "She isn't even answering her phone."
    show pov embarrassed_talk at left
    show haz confused at right
    pov "Yeah... About that..."

    menu:
        "Tell the truth":
            $ boxfavour_truth = 1
            show pov sad_talk at left
            show haz shocked at right
            pov "She is going through a very hard time right now so she is a bit disconnected from things."
            show pov embarrassed_talk at left
            show haz sad at right
            pov "It's actually something I'm trying to fix right now."
            show pov embarrassed at left
            show haz sad_talk at right
            haz "Damn..."
            show haz embarrassed_talk at right
            haz "Well, let me know if I can help in anyway."
            haz "[sister] is a good friend and a reliable part time employee so I want her to know I have her back."
            show pov embarrassed_talk at left
            show haz embarrassed at right
            pov "I'm sure she'll appreciate knowing that, Hazel."
        "Cover for [sister]":
            show pov sad_talk at left
            show haz shocked at right
            pov "She is very ill right now, we are not sure if it's food poisoning or an infection but she is in no condition to go out."
            show pov embarrassed_talk at left
            show haz confused at right
            pov "She actually send me here to tell you."
            show pov embarrassed at left
            show haz confused_talk at right
            haz "Should couldn't at least call or text me herself?"
            show pov embarrassed_talk at left
            show haz embarrassed at right
            pov "It's.. uh- really bad. Like she's pretty loopy and high on drugs most of the time."
            show pov embarrassed at left
            show haz embarrassed_talk at right
            haz "Yeah, I was afraid that would happen."
            show haz confused_talk at right
            haz "We ordered some very shoddy take-out last time and we both felt weird afterwards."
            show haz embarrassed_talk at right
            haz "Well, just tell her to try and get better soon."
            show haz confused_talk at right
            haz "I can't cover her forever, my hips hurt from doing both of our jobs."
            show pov shocked at left
            show haz confused_talk at right
            haz "So, was that all you came here for?"

    show pov embarrassed_talk at left
    show haz confused at right
    pov "Actually, there is something you could help us out with."
    pov "Do you have any spare boxes you could give me?"
    show pov embarrassed at left
    show haz confused_talk at right
    haz "What do you need them for?"
    show pov embarrassed_talk at left
    show haz confused at right
    pov "It's a really long story."
    show pov neutral at left
    show haz confused_talk at right
    haz "Well, I do think I have some in the back..."
    show pov confused at left
    haz "But..."
    show pov confused_talk at left
    show haz confused at right
    pov "But?"
    show pov sad at left
    show haz confused_talk at right
    haz "Well, I'm afraid I can't just give them to you, I need them to store some of the unsold inventory."
    show pov embarrassed_talk at left
    show haz bored at right
    pov "But you said you would be willing to help!"
    show pov embarrassed at left
    show haz bored_talk at right
    haz "Dude, chill your grill."
    show pov confused at left
    show haz smirk_talk at right
    haz "I am, but listen, this is a two way street. You feel?"
    show pov embarrassed at left
    haz "The ol' I scratch your back, you scratch mine?"
    show pov smirk_talk at left
    show haz smirk at right
    pov "Ohhh!"
    pov "I see where you're going with this."
    pov "Seems like it's only fair. A man's gotta do what a man's gotta do."
    show haz confused at right
    pov "What uh- when do you wanna-"
    show pov shocked at left
    show haz confused_talk at right
    haz "The store has not been selling well lately so I have them all filled with unsold stuff."
    show pov embarrassed_talk at left
    show haz confused at right
    pov "W- Wait... are we on the right page?"
    show pov shocked at left
    show haz confused_talk at right
    haz "I hope so? What- did you think I was gonna say?"
    show pov embarrassed_talk at left
    show haz confused at right
    pov "I- uh..."

    menu:
        "I thought you were hitting on me.":
            show pov embarrassed_talk at left
            show haz shocked at right
            pov "I thought you were hitting on me."
            if skill_luc >= 12:
                if hazel_points <= 9:
                    $ hazel_points += 1
                else:
                    $ hazel_points = 10
                $ skill_luc -= 6
                $ renpy.notify("You used 6 Luck Points\nYour relationship with Hazel has increased")
                show pov embarrassed at left
                show haz smirk_talk at right
                haz "Well, aren't you a presumtuous one."
                show pov shocked at left
                haz "And what if I was flirting a little? What of it?"
                show pov smirk_talk at left
                show haz smirk at right
                pov "Is that as yes?"
                show pov embarrassed at left
                show haz neutral_talk at right
                haz "Let's put a pin in that, hot cakes."
            else:
                show pov embarrassed at left
                show haz smirk_talk at right
                haz "Haha, that's cute [povname]. Aren't you just adorable."
                show pov bored at left
                haz "You haven't stopped blushing since the moment you walked into the store."
                show pov embarrassed at left
                show haz embarrassed_talk at right
                haz "Anyways, moving on from that awkward ordeal."
        "I thought you wanted to have a quickie.":
            show pov embarrassed_talk at left
            show haz shocked at right
            pov "I thought you wanted to have a quickie."
            if skill_luc >= 10 and skill_cha >= 10:
                if hazel_points <= 8:
                    $ hazel_points += 2
                else:
                    $ hazel_points = 10
                $ skill_luc -= 5
                $ skill_cha -= 5
                $ renpy.notify("You used 5 Luck Points\nYou used 5 Charisma Points\nYour relationship with Hazel has increased by 2")
                $ renpy.pause(1,hard=False)
                show pov embarrassed at left
                show haz shocked_talk at right
                haz "Straight forward and honest. Refreshing I guess."
                show haz smirk_talk at right
                haz "Maybe another time, hotshot."
            else:
                if hazel_points >= 1:
                    $ hazel_points -= 1
                else:
                    $ hazel_points = 0
                $ renpy.notify("Your relationship with Hazel has decreased by 1")
                show pov embarrassed at left
                show haz confused_talk at right
                haz "Whoooa there, boy. You ain't even left homebase let alone hit first base."
                show pov shocked at left
                haz "Maybe I should reconsider our deal."
                show pov shocked_talk at left
                show haz confused at right
                pov "No-! No. Sorry. I'm desperate for the boxes."
                haz "..."
        "Nothing...":
            show pov embarrassed_talk at left
            show haz confused at right
            pov "Nothing. Haha, just lost my train of thought and got confused."
            show pov embarrassed at left
            haz "Mmmmmm-hm."

    show pov embarrassed at left
    show haz confused_talk at right
    haz "Well okay, here's the deal."
    show pov confused at left
    haz "The central office decided to send us some extra products, new experimental stuff in hopes to increase sales again."
    show pov confused_talk at left
    show haz confused at right
    pov "This is a chain sex store?! I thought it was a-"
    show pov embarrassed_talk at left
    show haz bored at right
    pov "Mom and pops'..."
    show pov bored_talk at left
    pov "Just ignore me."
    show pov bored at left
    show haz confused_talk at right
    haz "Yeah, definitely."
    haz "Sex sells, therefore there has to be some corporate mentality added into the business side of things."
    show pov confused at left
    haz "Even amateur pornstars have a union nowadays."
    show pov sad at left
    haz "So until I find a way to get rid of all these products, I don't have any spare boxes to give you."
    show haz embarrassed_talk at right
    haz "Which is even harder than it sounds since sales have been getting increasingly lower these past few months."
    show haz sad_talk at right
    haz "If things continue like they are I'm afraid I may lose my job and the store might close down."
    show pov sad_talk at left
    show haz embarrassed at right
    pov "That sucks big time, Hazel. You would think that a store like this would be evergreen all year round."
    show pov confused at left
    show haz confused_talk at right
    haz "February and December are usually the peak months."
    show pov embarrassed at left
    show haz neutral_talk at right
    haz "Valentine's Day and Christmas. The time for family, and love."
    show haz sad_talk at right
    haz "But even so, it usually is never this bad. Either it's just a really bad month or more people are used to buying sex products anonymously online."
    show haz embarrassed_talk at right
    haz "To which I can understand whole heartedly. I would do that myself but what's the point when I come here everyday anyway."
    show pov confused_talk at left
    show haz smirk at right
    pov "Well, is there anyway I can help out in exchange for a few boxes? What do you have for me to do in mind?"
    show pov confused at left
    show haz smirk_talk at right
    haz "There is this one new thing that the central office is asking all their stores to add in with the new line of merchandise I was telling you about and I haven't had a chance to look for applicants yet."
    show haz confused_talk at right
    haz "But I really don't think you will be interested in it."
    haz "Not to mention I doubt you would be willing to do it."

    menu:
        "I don't like the sound of that.":
            show pov embarrassed_talk at left
            show haz neutral at right
            pov "I don't like the sound of that..."
            pov "That's too much foreshadowing for it to be anything good..."
            show pov sad at left
            show haz neutral_talk at right
            haz "Trust me, it isn't..."
        "Lay it on me.":
            show pov smirk_talk at left
            show haz shocked at right
            pov "Lay it on me, I'm ready."
            show pov embarrassed_talk at left
            show haz smirk at right
            pov "How bad can it be? Come on, tell me what it is."
            show pov embarrassed at left
            show haz smirk_talk at right
            haz "Trust me dude, it's bad..."
        "I'll do anything.":
            show pov sad_talk at left
            show haz confused at right
            pov "I'll do anything, Hazel. I'm desperate!"
            show haz smirk at right
            pov "Please, I'm up for anything if it means getting those boxes!"
            show pov embarrassed at left
            show haz smirk_talk at right
            haz "Alright, well, don't say I didn't warn you when you see it."

    scene bg boxfavour_1
    with dissolve

    menu:
        "Wow...":
            show bg boxfavour_2
            pov "Wow... it's-"
            pov "It's-"
            pov "Well..."
            show bg boxfavour_3
            haz "I know."
            haz "I doubt I'm going to find anyone willing to wear this thing for long, much less for what it pays."
            show bg boxfavour_2
            pov "W-what..?"
            pov "What are you talking about?"
            pov "It's a lovely costume of... of..."
            show bg boxfavour_4
            pov "What is this... thing?"
        "Stay Silent":
            pov "..."
            pov "...."
            pov "....."
            haz "Yeah, that has pretty much been the reaction of everyone who has seen the costume so far."
            show bg boxfavour_3
            pov "..."
        "Jesus H. Christ.":
            show bg boxfavour_5
            pov "Oh, God! Jesus Believe us! H. Christ Almighty."
            show bg boxfavour_6
            pov "Forgive me my sins but fucking shithole!"
            show bg boxfavour_3
            haz "I know."
            haz "I doubt I'm going to find anyone willing to wear this thing for long, much less for what it pays."
            show bg boxfavour_2
            pov "Is it... is it dead?"
            show bg boxfavour_4
            haz "Is it de- no... it's a costume."
        "What is it?":
            show bg boxfavour_5
            pov "What... is it?"
            show bg boxfavour_4
            pov "It smells horrendous."
            show bg boxfavour_2
            pov "Y'know, I knew I smelled something funky earlier. I just didn't wanna say anything."

    show bg boxfavour_7
    with hpunch
    haz "It's the new mascot for the new brand of toys and lubricants, I think it's a Japanese brand."
    show bg boxfavour_8
    pov "It's like something out of those art sites online that weird, horny tweens lurk on..."
    show bg boxfavour_9
    haz "Other stores have been using its image and products and they seem to have received an increase in sales, so our regional manager decided to try something more extreme, so..."
    show bg boxfavour_10
    haz "Now we are stuck with... this... thing? I don't even know what to call it."
    show bg boxfavour_8
    pov "Oh my God, are those-"
    pov "Padded hips?"
    pov "And a padded... chest?!"
    show bg boxfavour_7
    haz "They figured that a sex shop should obviously have a risque mascot. One that is curvy no matter who wears the suit."
    haz "It even comes with a small voice box with sultry lines and replies to some questions."
    show bg boxfavour_8
    pov "They've really gone all out on this, haven't they?"
    show bg boxfavour_11
    haz "Not exactly..."
    haz "There was a mess up with the manufacturing of this particular suit and well..."
    show bg boxfavour_12
    haz "I know what you're thinking, and no it's not Bruce Jennah."
    haz "It's tail is stitched on the front."
    pov "How did they fuck that up?"
    haz "Probably because whoever made this was paid less than a dollar and jumped off a building that very same day."
    pov "I don't feel bad about myself, thank you for that."

    menu:
        "I'll do it.":
            pov "I'll do it. For [sister]."
            pov "{i}Sigh{/i}"
            show bg boxfavour_8
            pov "If I don't get a fastpass to heaven or she refuses to give me one of her kidneys if I were to ever need one, I'm going to be very displeased."
            pov "So, Hazel. How are we going to do this?"
        "Stay silent":
            pov "..."
            haz "I understand, it's going to take a while for all this to process."
            haz "But do you smell something?"
            show bg boxfavour_10
            haz "Besides this nasty-ass suit?"
            show bg boxfavour_8
            pov "..."
            show bg boxfavour_7
            haz "Yes, that's right. It's the smell of desperation."
            show bg boxfavour_8
            pov "You'll have to forgive me, I just had a stroke."
            pov "Can you explain how this is going to work while my brain reboots?"
        "Everyday...":
            pov "Everyday we stray further away from God."
            haz "..."
            haz "That's the fighting spirit."
            pov "There has to be another way to help with sales!"
            pov "I said I would do anything but this?"
            pov "Any other option is better than than this."
            show bg boxfavour_11
            haz "Maybe so, but seeing as this is a new mandatory thing from the higher ups it's the only thing they want to see in action."
            show bg boxfavour_8
            pov "{i}*Sigh*{/i} So how will this work?"

    scene bg adultstore_day
    with dissolve
    show pov sad at left
    with dissolve
    show haz neutral_talk at right
    with dissolve
    call lbl_adultstore_counter_check
    haz "You wear this for a couple of shifts until I find a proper replacement and I pay you in any leftover boxes I have by the end of the day."
    haz "Depending on how many people you manage to get in, I'll add a few boxes in."
    show pov sad_talk at left
    show haz neutral at right
    pov "What if this doesn't work and I don't get any people in?"
    show pov shocked at left
    show haz embarrassed_talk at right
    haz "Look, if that happens. I'll throw in 2 boxes for your effort at the very least."
    show pov confused_talk at left
    show haz neutral at right
    pov "2 boxes, and I still have to go through the embarrassment of wearing this thing all day?"
    show pov confused at left
    show haz neutral_talk at right
    haz "Well, you know."
    show pov bored at left
    show haz smirk_talk at right
    haz "Tit for Tat, right?"
    show pov sad at left
    haz "You want boxes, then you better put on a good show."
    show pov bored_talk at left
    show haz smirk at right
    pov "Why does this suddenly feel like blackmail now?"
    show pov bored at left
    show haz smirk_talk at right
    haz "You see blackmail, I see opportunity."
    show pov sad at left
    show haz embarrassed_talk at right
    if winc == 1:
        haz "Look, if the store closes down, not only am I out of a job, but so is your sister and I doubt thats something that's going to help her get better."
    else:
        haz "Look, if the store closes down, not only am I out of a job, but so is your [sisrole] and I doubt thats something that's going to help her get better."
    show pov embarrassed at left
    show haz confused_talk at right
    haz "Which seriously though, if [sister] doesn't show up soon, she's definitely fired."
    haz "She did me a few favours and now I'm covering for her, but I can't cover her forever."
    show pov sad_talk at left
    show haz neutral at right
    pov "Le {i}*Sigh*{/i}"
    show pov embarrassed_talk at left
    show haz smirk at right
    pov "No guts, no glory. Am I right?"
    show pov bored at left
    show haz smirk_talk at right
    haz "Try making that sound cool in this fursuit, bud."
    show pov sad at left
    show haz neutral_talk at right
    haz "Let me know when you're ready."

    scene black
    $ sister_path = 30

    jump lbl_adultstore_day_setup
