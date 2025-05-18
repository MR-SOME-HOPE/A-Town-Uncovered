label lbl_framed:
    scene bg principaloffice_day
    with fade
    ##"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    ##$ mc_opened_locker = True # TEMP TEST
    if not mc_opened_locker:
        show pov embarrassed_talk at left
        with dissolve
        show pri bored at right
        with dissolve
        pov "You wanted to see me, Director Lashley?"
        show pov embarrassed at left
        show pri bored_talk at right
        pri "Please take a seat, [povname]."
        show pov confused_talk at left
        show pri bored at right
        pov "Uhh… Okay?"

        ##-The Mc takes a seat and we move to the usual view of Lashley in her desk-
        scene bg framed_no_mag_bored_talk with fade

        pri "Do you understand why I called you here?"
        scene bg framed_no_mag_bored
        pov "No, not really."
        scene bg framed_no_mag_angry
        pov "But it's a good thing you did! I was about to come get you. Someone broke into my locker and-"
        scene bg framed_no_mag_angry_talk
        pri "Let me stop you right there, [povname]."
        scene bg framed_no_mag_bored_talk
        pri "Before you continue, I should inform you about something that came to my attention this morning."
        scene bg framed_no_mag_bored
        pov "Uh, alright…"
        pov "Is everything okay?"
        scene bg framed_no_mag_bored_talk
        pri "No, no it sadly is not."
        pri "It has come to my attention that you are apparently hoarding prohibited items within university premises."
        scene bg framed_no_mag_angry_talk
        pri "Primarily pornography."
        scene bg framed_no_mag_angry
        pov "WHAT?!"
        pov "Who told you that?!"
        pov "That's nothing but an absolute lie!"
        scene bg framed_no_mag_confused_talk
        pri "Is it? And what are we going to find if we open up your locker?"
        scene bg framed_no_mag_confused
        pov "I don't know, and that's the problem!"
        scene bg framed_no_mag_shocked
        pov "Someone broke into it early in the morning and put something in there!"
        pov "I even have a witness who saw the whole thing!"
        scene bg framed_no_mag_confused_talk
        pri "And you find them a reliable source?"
        scene bg framed_no_mag_confused
        pov "Why else would she have stopped me from opening the locker, in the first place?!"
        pov "C'mon, Director Lashley, you gotta believe me!"
        pov "I don't even know if there is actually anything in my locker, to begin with!"
        scene bg framed_no_mag_smirk_talk
        pri "{i}*giggle*{/i}"

    elif mc_opened_locker:
        show pov embarrassed at left
        with dissolve
        show pri angry_talk at right
        with dissolve
        pri "Sit down, [povname]..."
        show pov sad at left
        show pri angry at right
        pov "…"

        ##-you sit down which turns to the usual viewpoint of Lashley at her desk-
        scene bg framed_no_mag_angry with fade
        pov "Director Lashley, you have to believe me. None of that stuff is-"
        scene bg framed_no_mag_angry_talk
        pri "You'll have a chance to explain yourself soon, young man."
        scene bg framed_no_mag_bored_talk
        pri "First of all, you are going to listen to a variety of rumors that have reached my ear, that have relation to your current predicament."
        scene bg framed_no_mag_bored
        pov "Such as?"
        scene bg framed_no_mag_shocked_talk
        pri "Well, for starters, the fact of you were hoarding pornography was one of the first things that reached my ears."
        pri "Along with you buying in bulk and masturbating in the bathrooms."
        scene bg framed_no_mag_shocked
        pov "WHAT?!"
        pov "Those are all nothing but lies!"
        scene bg framed_no_mag_confused
        pov "You have to believe me, I do nothing of that sort of stuff!"
        pov "Much less, on university property!"
        scene bg framed_no_mag_confused_talk
        pri "Several people have come forward with this, [povname], I can't just ignore it completely."
        scene bg framed_no_mag_confused
        pov "I'm being set up!"
        pov "Who told you this stuff, they can't be a trusted source!"
        pov "Ask anyone who knows me; they can confirm my innocence!"
        scene bg framed_no_mag_smirk_talk
        pri "Pfft!"
        scene bg framed_no_mag_smirk
        pov "What?"
        scene bg framed_no_mag_smirk_talk
        pri "{i}*giggle*{/i}"

    scene bg framed_no_mag_smirk
    pov "Uh… What's so funny?"
    scene bg framed_no_mag_smirk_talk
    pri "I'm sorry, [povname]. I couldn't help myself."
    scene bg framed_no_mag_embarrassed_talk
    pri "I just wanted to see how you looked when confronted with such accusations."
    scene bg framed_no_mag_neutral_talk
    pri "It will help me determine whenever you are telling me the truth."
    pov "Wait, so all of that was a joke?!"
    scene bg framed_no_mag_sad_talk
    pri "Well, not really."
    scene bg framed_no_mag_bored_talk
    pri "I did came upon those rumors and accusations about you, however, they came from my usual line of delinquents in detention and their friends."
    pri "So, I knew right away not to trust anything they were saying."
    scene bg framed_no_mag_bored
    pov "So, I’m not in trouble? Why all of the theatrics, then?"
    scene bg framed_no_mag_neutral_talk
    pri "Like I said, [povname]: I wanted to see what your reaction would be if faced against false accusations."
    pri "It will help me judge your reaction if you are ever accused of something again."
    scene bg framed_no_mag_neutral
    pov "That’s… rather crafty of you, isn’t it?"
    scene bg framed_no_mag_smirk_talk
    pri "I do apologize for my methods, but I do what I do for the good of my students."
    scene bg framed_no_mag_bored_talk
    pri "But at the very least, you are in the clear, as I know full well who tried to frame you."
    scene bg framed_no_mag_bored
    pov "You do?"
    scene bg framed_no_mag_neutral_talk
    pri "Believe it or not, we do have cameras."
    pri "That, along with Zariah’s statement, has you completely off the hook."
    scene bg framed_no_mag_neutral
    pov "Thank God. My [mumrole] would have killed me if she heard I was involved in something like this."
    scene bg framed_no_mag_shocked
    pov "…Hang on, if you knew of my innocence and know who tried to frame me, what was the point of making a whole show of it?"
    scene bg framed_no_mag_bored_talk
    pri "To keep you safe from this repeating again."
    scene bg framed_no_mag_bored
    pov "What do you mean?"
    scene bg framed_no_mag_neutral_talk
    pri "I told you back at the cafeteria, remember?"
    scene bg framed_no_mag_bored_talk
    pri "Being seen around the administrator can bring a lot of attention to your person."
    pri "Top that with the fact you are the new kid, and it was bound for something like this to happen."
    pri "Just gave those knuckleheads an additional reason to go after you, other than playing a prank on the newbie."
    scene bg framed_no_mag_bored
    pov "Huh, so all of that was-?"
    scene bg framed_no_mag_smirk_talk
    pri "Just a way to prevent others from calling you the “Director’s Golden Boy” and then them picking on you because of it."
    scene bg framed_no_mag_smirk
    pov "Oh… Well, thanks for that. I guess?"
    scene bg framed_no_mag_neutral_talk
    pri "Don’t thank me just yet."
    scene bg framed_no_mag_sad_talk
    pri "Regrettably, we are going to have to play along, in order to keep appearances."
    scene bg framed_no_mag_sad
    pov "What does that mean?"
    scene bg framed_no_mag_sad_talk
    pri "I’m going to have to give you “Detention” in order to prevent any further pranks."
    scene bg framed_no_mag_sad
    pov "You are going to give me detention for something I didn’t even do?!"
    scene bg framed_no_mag_shocked_talk
    pri "Of course not. That would be downright ridiculous and unfair."
    scene bg framed_no_mag_sad_talk
    pri "Plus, sending you to detention is just going to get you mixed up with the wrong crowd who tried to frame you in the first place."
    scene bg framed_no_mag_neutral_talk
    pri "No, instead of that, you are going to go through one of my “Special” punishments."
    scene bg framed_no_mag_neutral
    pov "Special in what way, exactly?"
    scene bg framed_no_mag_neutral_talk
    pri "Remember how I had students in detention, sometimes aid the janitor? Well, instead of that, you are going to be meeting me here for some “Assistant Duties”."
    scene bg framed_no_mag_embarrassed_talk
    pri "Just pop in here from time to time and we can mark it as you helping me with paperwork and stuff."
    pri "A rumor here and a rumor there and people will think I am just keeping an eye on the new student to ensure they don’t waver from the good path."
    scene bg framed_no_mag_embarrassed
    pov "Am I actually going to do work?"
    scene bg framed_no_mag_sad_talk
    pri "I cannot force a student to do so without a viable reason, so for the moment, no. But there may be times where I need a hand when it comes to university paperwork and stuff. And I would more than appreciate your help."
    scene bg framed_no_mag_neutral_talk
    pri "Other than that, just come in and have a chat with me to kill time, from time to time, in order to keep appearances."
    scene bg framed_no_mag_confused
    pov "Alright… But why are you doing this, in the first place?"
    pov "Wouldn’t it be easier to assume I did all of those things, and just send me to detention to avoid the hassle, or just present the evidence to the guy who framed me and punish him instead?"
    scene bg framed_no_mag_bored_talk
    pri "While I assure you that I’m taking the appropriate methods of punishment on the student who framed you, I also want you to know that; yes, it would be far easier to just ignore the problem and assume you are guilty."
    scene bg framed_no_mag_bored
    pov "Then why-?"
    scene bg framed_no_mag_neutral_talk
    pri "Because you are my student, [povname]."
    pri "You are my student, so if I have it in my hands to help you when you need it, then it’s my duty as an educator to jump into action."
    scene bg framed_no_mag_shocked_talk
    pri "I told you before: the previous administrator was an embarrassment to everything an administrator represents."
    scene bg framed_no_mag_angry_talk
    pri "Caring only for the funds he could embezzle and the girls he could try and take advantage of."
    pri "Never once helping a student even lift a book that had fallen from their hands."
    pri "I’ve worked hard in order to erase that man’s legacy from this institution. And if I want to be everything that monster was not, then I have to set the example and be the first to reach out when a student is in need."
    scene bg framed_no_mag_confused_talk
    pri "Galatians 6:10 and James 4:17."
    pri "Those two are reasons enough for me to do what I do, but I’ll admit, there is another reason."
    scene bg framed_no_mag_embarrassed
    pov "Another reason?"
    scene bg framed_no_mag_smirk_talk
    pri "{i}*Giggle*{/i} I really like your company, [povname]."
    scene bg framed_no_mag_neutral_talk
    pri "You come to me without any fear or reservations. Without some secret agenda to butter up yourself with me; for better grades or a letter of recommendation."
    scene bg framed_no_mag_embarrassed_talk
    pri "You just… I don’t know. There is something about you that just… Just intrigues me in some way that I can’t explain."
    pri "It’s like I could talk away the day with you."
    scene bg framed_no_mag_shocked_talk
    pri "Even if the few times we have held a conversation, it is mostly me doing the talking."
    pri "So, let’s call it me being a little selfish and wanting to relish on that a bit more."
    pri "I would hate to lose those conversations just because some dunderheads make your life impossible because you are on good terms with the administrator."
    scene bg framed_no_mag_shocked
    pov "Wow…"
    pov "I-I don’t know what to say…"
    scene bg framed_no_mag_neutral_talk
    pri "Just say “Thanks” and head to class for now."
    scene bg framed_no_mag_embarrassed_talk
    pri "Wait a few days before coming back here. I’ll lay the groundwork to the rumors of your punishment, and make it believable."
    scene bg framed_no_mag_embarrassed
    pov "R-Right… Thank you, Director Lashley, really."
    scene bg framed_no_mag_embarrassed_talk
    pri "Don’t mention it. See you soon, [povname], Don’t be a stranger now!"
    scene bg framed_no_mag_embarrassed
    pov "I won’t. You can count on it."
    pov "See you later."
    pov "Oh! Before I go, what am I supposed to do with-"
    scene bg framed_no_mag_shocked_talk
    pri "I already told the janitors to get all of that smut out of your locker and throw it away - no need for you to worry about it."
    scene bg framed_no_mag_shocked
    pov "Right. Thanks again!"


    ## "The Mc leaves the room, Lashley keeps smiling for a moment then sighs"
    scene bg framed_no_mag_neutral_talk with fade
    pri "{i}*Sigh*{/i}"
    scene bg framed_no_mag_embarrassed
    pri "…"
    scene bg framed_no_mag_embarrassed_talk
    pri "I’m… Just making sure my student is alright…"
    pri "No other reason besides that, right?"
    scene bg framed_no_mag_confused
    $ renpy.pause(1.5)
    scene bg framed_no_mag_look_mag
    pri "…"
    scene bg framed_no_mag_reach_mag with dissolve




    ## "She takes out the magazine from before and stares at the front cover" ################ CG ART NEEDED
    scene bg framed_with_mag_look_down with dissolve
    pri "{i}I… I just want to see him more often…{/i}"
    pri "{i}Nothing bad with that, right?{/i}"
    pri "…"
    scene bg framed_with_mag_hold_mag_horny with dissolve
    pri "{i}Right..?{/i}"

    $ townmap_enabled = 1
    $ gtime = 1
    $ principallashley_path = 5.5

    jump lbl_schoolhallway2_day_setup
