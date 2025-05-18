label lbl_distractions:
    ##[Lashley’s Office Second Floor, After School– “Distractions” – misslashley_path = 25]

    #-Mc knocks the door to Lashley's office after classes the same day of the previous scene-
    scene bg distractions
    show eyes distractions_down
    show charexpression distractions_bored
    with fade
    pov "Director Lash-"
    show charexpression distractions_bored_talk
    pri "Just come in, [povname]. Come in and sit down…"
    show charexpression distractions_bored
    pov "..."
    pov "Alright…"

    #-Mc sits on the chair as Lashley keeps working, ignoring him with an upset look on her face-
    #(maybe have some transitions of her working on some paperwork to emphasize the silence between them?)

    show charexpression distractions_confused
    pov "…"
    pov "So…"
    show charexpression distractions_confused_talk
    pri "Looking forward to this party of yours?"
    show charexpression distractions_bored
    pov "It’s not a party and don’t tell me you are upset over it."
    show charexpression distractions_confused_talk
    pri "Upset?"
    show charexpression distractions_smirk_talk
    pri "Who is upset?"
    show charexpression distractions_nasty_talk
    pri "Why would I be upset?"
    show eyes distractions_up
    show charexpression distractions_smirk_talk
    pri "It’s not like I just stumbled into you planning to woo your way into some out of town life guard’s swimsuit!"
    show eyes distractions_down
    show charexpression distractions_bored
    pov "Okay, there are a lot of things wrong with that sentence!"
    show charexpression distractions_smirk
    pov "First of all, I never even agreed to be a part of Jacob’s plan!"
    show charexpression distractions_bored_talk
    pri "I know what I heard, [povname]!"
    show eyes distractions_up
    show charexpression distractions_smirk_talk
    pri "And I heard it all loud and clear!"
    show eyes distractions_down
    show charexpression distractions_shocked
    pov "Wait, were you spying on me?!"
    show charexpression distractions_shocked_talk
    pri "I-I-"
    show charexpression distractions_smirk_talk
    pri "O-Of course not!"
    show charexpression distractions_interested_talk
    pri "I just so happened to be heading to your locker to talk to you when I stumbled into the conversation!"
    show charexpression distractions_confused_talk
    pov "So you were eavesdropping on me then, how is that any better?!"
    show eyes distractions_up
    show charexpression distractions_shocked_talk
    pri "I wasn’t eavesdropping either!"
    show eyes distractions_down
    show charexpression distractions_angry_talk
    pri "And don’t try to shift the blame here, I’m the one mad at you!"
    show charexpression distractions_bored
    pov "I haven’t done anything!"
    show eyes distractions_up
    show charexpression distractions_confused
    pov "You are the one who lied to me about rumors still going around about the whole porn thing!"
    show charexpression distractions_confused_talk
    pri "J-Just because it’s not the case in your social circle doesn’t mean that it’s true for everyone else!"
    show eyes distractions_down
    show charexpression distractions_bored
    pov "And just because you heard Jacob adding me to his plans doesn’t mean I agree to be a part of them!"
    show charexpression distractions_bored_talk
    pri "That’s-..."
    show charexpression distractions_embarrassed_talk
    pri "W-Well…"
    pri "B-But I…"
    show eyes distractions_up
    show charexpression distractions_bored_talk
    pri "…"
    show eyes distractions_down
    show charexpression distractions_bored
    pov "…"
    pov "{i}*Sigh*{/i}"
    show charexpression distractions_embarrassed
    pov "Alright, Alright. Yelling at each other isn’t going to solve anything."
    show eyes distractions_up
    pov "Let’s call a break to the whole argument and cool off a bit, okay?"
    show eyes distractions_down
    show charexpression distractions_bored_talk
    pri "…"
    pri "Alright, that sounds reasonable enough…"

    #-The Mc and Lashley share a moment of silence, both of them clearly uncomfortable of the whole situation and waiting for the other to say something-

    show charexpression distractions_bored
    pov "…"
    show charexpression distractions_sad_talk
    pri "…"

    #-The following line occurs in the Mc’s head-

    show charexpression distractions_bored
    pov "{i}Oh boy, this is going to take a while, isn’t it?{/i}"
    with fade

    #(have a quick fade to black and back to indicate the passage of time)

    show charexpression distractions_confused
    pov "It’s been 2 hours and she is still not saying anything!"
    show charexpression distractions_bored
    pov "Should I try saying something first?"


    menu distraction_menu:
        "Try changing the subject":
            #-If “Try changing the subject” was picked-
            #(This option loops and leads back to the choice tree)

            show charexpression distractions_shocked
            pov "So…"
            show charexpression distractions_bored
            pov "Um…"
            show eyes distractions_up
            show charexpression distractions_confused
            pov "How’s Jesus lately and all?"
            show charexpression distractions_confused_talk
            pri "What?"
            show charexpression distractions_confused
            pov "First thing that came to mind, I’m sorry."
            show eyes distractions_down
            show charexpression distractions_smirk_talk
            pri "He’s alright I suppose?"
            show charexpression distractions_interested_talk
            pri "He still died for our sins and all that, so…"
            show eyes distractions_up
            show charexpression distractions_bored_talk
            pri "You know…"
            show eyes distractions_down
            show charexpression distractions_bored
            pov "Right, right…"
            pov "Well, could have been worse right?"
            show charexpression distractions_bored_talk
            pri "Well, only if you can imagine worse things than being crucified and poked with a spear simply for spreading your beliefs of love and peace and then white washed by future caucasian generations who exploit your image for their own toxic interpretation of your words."
            show eyes distractions_up
            pri "Then yeah. Could have been worse…"
            show eyes distractions_down
            show charexpression distractions_bored
            pov "Alright, I’m not even gonna attempt getting near that whole landmine there, I’ll shut up now…"
            show charexpression distractions_bored_talk
            pri "Thank you."

            #-Mc and Lashley go back to the awkward silence-

            #-In the Mc’s head-

            show charexpression distractions_confused
            pov "{i}I… Should probably try something else…{/i}"
            show charexpression distractions_bored
            pov "{i}Don’t think we are ready to ignore the elephant in the room just yet…{/i}"
            #-The end of this choice returns you back to the choice tree-
            #=CHOICE END=
            jump distraction_menu
        "Man up and apologize first":
            #-If “Man up and apologize” was picked-
            #+2 Lashley RP.
            $ add_points("principallashley_points",2)
            show eyes distractions_up
            show charexpression distractions_confused
            pov "Sigh."
            show charexpression distractions_bored
            pov "Look, I still don’t think I did anything wrong, but it’s clear it means enough for you to be this upset about it."
            show charexpression distractions_smirk
            pov "And though I feel like I have a solid argument and am upset, I really just want to put it between us already and move on."
            show eyes distractions_down
            pov "Not because I don’t validate your anger or anything like that, but because I like it better when we are friendly with each other."
            show eyes distractions_up
            show charexpression distractions_interested
            pov "So, If nothing else, I’ll be the bigger man and let you know that I’m sorry."
            show eyes distractions_down
            show charexpression distractions_interested_talk
            pri "…"
            show charexpression distractions_smirk_talk
            pri "Wow…"
            show charexpression distractions_shocked_talk
            pri "I, uh…"
            show eyes distractions_up
            show charexpression distractions_interested_talk
            pri "I honestly didn’t expect you to apologize."
            show eyes distractions_down
            show charexpression distractions_bored_talk
            pri "I figured we would be arguing for a while longer and have a whole make up arc or something."
            show eyes distractions_up
            pri "That’s what I thought normally happens in situations like this."
            show charexpression distractions_bored
            pov "Yeah, friendships and relationships really aren’t like those novels."
            show charexpression distractions_interested
            pov "In reality it’s more than expected for the guy to apologize regardless if he did something wrong or not."
            show eyes distractions_down
            show charexpression distractions_embarrassed_talk
            pri "I’ll keep it in mind for the future then."
            show eyes distractions_up
            show charexpression distractions_interested_talk
            pri "Thanks for apologizing."
            show charexpression distractions_interested
            pov "Yeah, no problem."
            show eyes distractions_down
            show charexpression distractions_confused
            pov "Well, don’t you want to say something as well so we are back on even terms?"
            show eyes distractions_up
            show charexpression distractions_confused_talk
            pri "Before that, can I ask you something?"
            show charexpression distractions_confused
            pov "Sure, what is it?"
            #=CHOICE END=
            #-This choice unlike the previous one continues the dialogue as normal-
        "Edge her to apologize first":
            #-If “Edge her to apologize first” was picked-
            #-1 Lashley RP.
            $ subtract_points("principallashley_points",1)
            show eyes distractions_down
            show charexpression distractions_confused
            pov "So…"
            pov "Is there something you want to say to me?"
            show charexpression distractions_bored
            pri "I have plenty in mind, you’ll have to be more specific…"
            show charexpression distractions_confused
            pov "Well, I just figured I was owed something like an… apology, maybe?"
            show eyes distractions_up
            show charexpression distractions_confused_talk
            pri "Oh, and just exactly what for, if I may ask?"
            show eyes distractions_down
            show charexpression distractions_bored_talk
            pri "I have a little difficulty seeing just why I owe you one, so enlighten me."
            show charexpression distractions_confused

            #-The following line occurs in the Mc’s head-
            show charexpression distractions_bored
            pov "{i}Oh boy, here we go.{/i}"

            #-Back to regular dialogue
            show eyes distractions_up
            show charexpression distractions_bored
            pov "W-Well, for starters, how about the whole “People still spreading rumors behind your back” whole deal?"
            show eyes distractions_down
            show charexpression distractions_bored_talk
            pri "Again, just because your friend group isn’t doesn’t mean other people aren’t doing just that!"
            show charexpression distractions_smirk_talk
            pri "I told you before that everything I’m trying to do is lend you a hand here and keep nasty rumors off you."
            show eyes distractions_up
            show charexpression distractions_angry_talk
            pri "What, am I supposed to apologize for looking after you and taking an interest in your well being now?!"
            show charexpression distractions_confused
            pov "That’s not at all what I meant and you know it!"
            show eyes distractions_down
            show charexpression distractions_confused_talk
            pri "Well, you seem to be rather difficult to understand all of a sudden, [povname]!"
            show eyes distractions_up
            show charexpression distractions_interested_talk
            pri "But then again, I supposed that’s to be expected now that I know you are “that” type of guy who is more than eager to follow up on your male friends plans to “chase some tail” as you kids call it!"
            show eyes distractions_down
            show charexpression distractions_interested
            pov "I do not like what you are insinuating with that phrase and I told you before that just because Jacob wants to include me in his plans, doesn’t mean I agree to join him in them!"
            show eyes distractions_up
            show charexpression distractions_smirk_talk
            pri "Alright, let’s suppose that’s true, care answering a question then?"
            show charexpression distractions_smirk
            pov "If it gets us closer to solving all of this then I don’t really have a choice, do I?"
            show charexpression distractions_bored_talk
            pri "No, you really don’t."
            show eyes distractions_down
            show charexpression distractions_bored
            pov "Alright then, shoot."
            #=CHOICE END=
            #=END=

    ######
    #-Lashley proceeds to look at the Mc with an inquisitive look-

    show eyes distractions_up
    show charexpression distractions_bored
    pri "Will you be going, then?"
    show eyes distractions_down
    show charexpression distractions_bored
    pov "What do you mean?"
    show charexpression distractions_bored_talk
    pri "To this party of yours. Will you be attending then?"
    show eyes distractions_up
    show charexpression distractions_confused
    pov "It’s not a party and is that really what you wanted to ask me?"
    show charexpression distractions_smirk
    pov "Whether I’m going or not?"
    show eyes distractions_down
    show charexpression distractions_bored
    pri "Just answer the question, [povname]."
    show charexpression distractions_smirk
    pov "Well, I think so, yeah."
    show charexpression distractions_shocked
    pov "But not for the reasons you think."
    show eyes distractions_up
    show charexpression distractions_bored_talk
    pri "Please elaborate."
    show charexpression distractions_bored
    pov "Well, I got invited and Zariah wants me to take a listen to her new EP, what’s the problem?"
    show eyes distractions_down
    show charexpression distractions_smirk
    pov "It’s not like I have anything else planned for this weekend and it sounds like a fun time."
    show charexpression distractions_smirk_talk
    pri "You sure that’s a wise decision?"
    show eyes distractions_up
    show charexpression distractions_confused
    pov "What’s wrong with wanting to hang out with my friends?"
    show eyes distractions_down
    show charexpression distractions_bored_talk
    pri "The fact you may be heading there for the wrong reasons..."
    show charexpression distractions_smirk
    pov "Are you still asking whether or not I’m going to fool around with those lifeguards?"
    show charexpression distractions_bored_talk
    pri "Well, you haven’t really given out an answer."
    show eyes distractions_up
    show charexpression distractions_embarrassed_talk
    pri "And after what we did in the car last time, I…"
    show eyes distractions_down
    pri "Well, I think I’m entitled to a straight answer from you."
    show charexpression distractions_bored
    pov "Oh… So that’s what this was about…"
    show charexpression distractions_bored_talk
    pri "Took you long enough to realize..."
    show charexpression distractions_smirk_talk
    pov "Lashley, I just want to go out and have some fun with my friends for a while."
    show eyes distractions_up
    show charexpression distractions_bored
    pov "Just some drinks, some snacks, checking out Zariah’s new EP and maybe dancing a little."
    pov "I really doubt my night is going to be more than just that."
    show eyes distractions_down
    show charexpression distractions_bored_talk
    pri "You don’t know that."
    pri "You young men can’t control your hormones after all.."
    show eyes distractions_up
    show charexpression distractions_confused
    pov "Well… How about I give you my word on this?"
    show charexpression distractions_confused_talk
    pri "How do I know you aren’t going to break your promise?"
    show charexpression distractions_bored
    pov "Because you know me, Lashley."
    show eyes distractions_down
    show charexpression distractions_confused
    pov "I would never do anything to hurt you or that you explicitly tell me that bothers you or that you are absolutely not ok with."
    show eyes distractions_up
    show charexpression distractions_embarrassed
    pov "I’ve been there when you needed me and I’ve gone out of my way for you."
    show eyes distractions_down
    pov "Isn’t that worth you putting in a bit of little faith on me?"
    show charexpression distractions_bored_talk
    pri "…"
    show eyes distractions_up
    show charexpression distractions_embarrassed
    pov "If it bothers you that much, I promise I won’t lay a finger on one of those lifeguards."
    show eyes distractions_down
    pov "I’ll be a quiet little wallflower and just focus on having fun with my friends and keeping my junk in my pants."
    show charexpression distractions_confused
    pov "Does that work for you?"

    #Lashley -grumble- I still don’t like the idea…

    show charexpression distractions_bored
    pov "Ok, tell you what. I can probably sneak out earlier from the party if I come up with a good excuse and if you are free we could go and spend the rest of the night somewhere else."
    show eyes distractions_up
    show charexpression distractions_confused
    pov "Just you and me for as long as you want."
    pov "Not sure what we could do, but I’ll think of something."
    show eyes distractions_down
    show charexpression distractions_bored
    pov "Would you like that?"
    show charexpression distractions_bored_talk
    pri "…"
    show eyes distractions_up
    show charexpression distractions_confused_talk
    pri "Sigh. I guess so…"
    show charexpression distractions_bored_talk
    pri "Alright, [povname]."
    pri "I trust you and I know you’ll keep your word on this."
    show charexpression distractions_embarrassed_talk
    pri "I know I shouldn’t doubt you, but I just get worried..."
    show eyes distractions_down
    show charexpression distractions_embarrassed
    pov "Hey, it’s alright."
    show eyes distractions_up
    pov "I appreciate that you get worried about me."
    show charexpression distractions_embarrassed_talk
    pri "And I appreciate that you are willing to control yourself for me."
    show charexpression distractions_interested
    pov "You are the better prize after all."
    show charexpression distractions_smirk_talk
    pri "Oh, please."
    show charexpression distractions_interested_talk
    pri "I’m sure you would rather mess around with those fit lifeguards rather than with boring old me."
    show eyes distractions_down
    show charexpression distractions_interested
    pov "Don’t say that, we had fun messing around last time, right?"
    pov "I treasure what we have."
    show eyes distractions_up
    show charexpression distractions_embarrassed_talk
    pri "Oh, you do?"
    show charexpression distractions_smirk_talk
    pri "Perhaps you are willing to… demonstrate your affection a bit then?"
    show charexpression distractions_smirk
    pov "Depends on how you want me to demonstrate it."
    show eyes distractions_down
    show charexpression distractions_smirk_talk
    pri "Well, I’ve been feeling the heat coming back again and I really don’t feel like getting some more wine."
    show eyes distractions_up
    pri "Is there some way you can help out with that?"
    show charexpression distractions_interested
    pov "I can think of a couple of things, though you are quite cute when you are tipsy, you know?"
    show charexpression distractions_shocked_talk
    pri "I can’t believe you just said that!"
    show charexpression distractions_embarrassed
    pov "You left yourself open there."
    show charexpression distractions_smirk_talk
    pri "Well, aren’t you a little Mr. Smarty Pants?"
    show eyes distractions_down
    show charexpression distractions_nasty_talk
    pri "We’ll see if you are so smug once I get my hands on you."
    show charexpression distractions_smirk
    pov "Eager today, huh?"
    show charexpression distractions_smirk_talk
    pri "Are you going to tell me you aren’t?"
    show eyes distractions_up
    show charexpression distractions_interested
    pov "You know the answer to that, but does this mean we are cool then?"
    show eyes distractions_down
    show charexpression distractions_smirk_talk
    pri "Yes, [povname]. We are “cool” as you say."
    pri "I’m just being overly needy and I know you are not one to break your promises."
    show eyes distractions_up
    show charexpression distractions_interested_talk
    pri "So… How about we washed all of this away with a little bit of… Extra counseling?"
    show charexpression distractions_smirk
    pov "I like that idea."
    show charexpression distractions_smirk_talk
    pri "Good boy, lock the door beforehand though, will you?"
    show charexpression distractions_interested_talk
    pri "This time, we are moving at my speed."
    show eyes distractions_down
    show charexpression distractions_smirk_talk
    pri "I was hoping this time we could-"

    #-Cue a sudden knock on the door-
    show eyes distractions_up
    show charexpression distractions_shocked
    coa "Hey, boss?"
    show charexpression distractions_bored
    coa "The repairmen came over to take a look at your a/c unit, they're waiting for you outside."
    show eyes distractions_down
    show charexpression distractions_angry_talk
    pri "Oh for the love of-"
    pri "I swear I have the worst luck lately..."
    show eyes distractions_up
    show charexpression distractions_bored_talk
    pri "Yes, thank you, I’ll be right there!"
    show eyes distractions_down
    show charexpression distractions_bored
    pov "Duty calls?"
    show eyes distractions_up
    show charexpression distractions_bored_talk
    pri "I just hope they at least are able to repair the unit, we were just getting to the good part…"
    show charexpression distractions_embarrassed
    pov "There’s always next time."
    pov "You know I like to stop by often."
    show charexpression distractions_neutral_talk
    pri "I just hope you are ready for next time since I’ll be all pent up till then."
    show charexpression distractions_smirk_talk
    pri "Better get those fingers warmed up for then, young man."
    show charexpression distractions_smirk
    pov "You bet!"
    show eyes distractions_down
    show charexpression distractions_interested
    pov "I’m glad we could work most of this out, though I still have some questions as to the whole rumors thing."
    show eyes distractions_up
    show charexpression distractions_interested_talk
    pri "We can talk about it at a later date, ok?"
    show charexpression distractions_embarrassed_talk
    pri "One problem at a time."
    pri "A lady is entitled to a few secrets, doesn’t she?"
    show charexpression distractions_interested_talk
    pri "I promise I’ll explain it all later and it will make sense in hindsight."
    show eyes distractions_down
    show charexpression distractions_neutral
    pov "If you say so?"
    show eyes distractions_up
    show charexpression distractions_interested_talk
    pri "I’m putting my trust in you here, so you better keep your promise, ok?"
    show charexpression distractions_interested
    pov "I know that."
    show charexpression distractions_neutral
    pov "Don’t worry, I won’t let you down."
    pov "See you soon."

    #-Mc leaves the room-

    show charexpression distractions_smirk_talk
    pri "Of course, [povname]. I trust you…"

    #-Lashley’s eyes and expression turn sour-

    show charexpression distractions_confused_talk
    pri "It’s all those distractions around you that I don’t trust…"
    show eyes distractions_down
    show charexpression distractions_nasty_talk
    pri "Seems like we are going to have to play a little rougher now."
    show eyes distractions_up
    show charexpression distractions_smirk_talk
    pri "All’s fair in love and war, right?"
    show charexpression distractions_interested_talk
    pri "No matter, true love always wins in the end!"
    show charexpression distractions_smirk_talk
    pri "Even if you have to step on a couple of heads to get there..."

    $ townmap_enabled = 1

    $ principallashley_path = 19.5

    jump lbl_schoolhallway2_day_setup
