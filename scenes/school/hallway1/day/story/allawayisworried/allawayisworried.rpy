## Allaway is Worried
label lbl_allaway_is_worried:
    scene bg schoolhallway1_dayempty
    with fade

    if missallaway_points <= 6:
        show pov confused at left
        with dissolve
        show mis sad_talk at right
        with dissolve
        mis "[povname], you understand that my role as a teacher is to guide you and be a person you can talk to in case you have a problem, correct?"
        show pov embarrassed_talk at left
        show mis sad at right
        pov "Uhh… Yeah?"
        pov "I suppose?"
        show pov confused at left
        show mis embarrassed_talk at right
        mis "And you know that you are welcome to talk to me about any trouble you may have at home or during class hours, correct?"
        show pov confused_talk at left
        show mis neutral at right
        pov "I think so?"
        show pov confused at left
        show mis neutral_talk at right
        mis "Great."
        show pov shocked at left
        show mis bored_talk at right
        mis "In that case, is there anything you would like to tell me?"
        show pov confused_talk at left
        show mis bored at right
        pov "Not particularly, no."
        show pov confused at left
        show mis bored_talk at right
        mis "Okay, I am going to be more direct about this."
        show mis confused_talk at right
        mis "Are you feeling okay. Like actually okay-okay and not yeah-whatever-just-okay-okay?"
        show pov sad at left
        mis "I hope you don't take this the wrong way but you're looking a little pale, and very- how do I put this..?"
        show pov shocked at left
        mis "Like the government is after you."
        show pov embarrassed_talk at left
        show mis confused at right
        pov "I’ve been getting that a lot today."
        pov "Didn’t expect to get singled out by my teacher, however."
        show pov bored at left
        show mis sad_talk at right
        mis "I apologize, [povname]."
        show mis confused_talk at right
        mis "But as you know, we were instructed to keep an eye on you due to the whole 'park incident' and the possibility of you getting harmed in any way."
        show mis embarrassed_talk at right
        mis "So when I saw you in this state, I needed to ask."
        show pov bored_talk at left
        show mis embarrassed at right
        pov "No, no. It’s okay."
        pov "I get what you're doing, Miss."
        show pov sad at left
        show mis confused_talk at right
        mis "So, is there any particular reason you are like this today?"
        show mis confused at right
        pov "..."
        show pov confused_talk at left
        show mis confused at right
        pov "Bad dreams… I guess is the right word for it."
        show pov confused at left
        show mis confused_talk at right
        mis "Bad dreams?"
        show pov angry_talk at left
        show mis shocked at right
        pov "Well, a lot is going on, Miss Allaway."
        show pov bored_talk at left
        show mis sad at right
        pov "It takes a toll on a guy."
        pov "It'll take a toll on anyone."
        show pov sad at left
        pov "…"
        show pov sad_talk at left
        pov "Don't blame me for being anxious 24/7."
        pov "I just wondered why didn’t they take me instead, I was already deemed an easy victim."
        pov "I can’t help but to feel sort of guilty over what happened…"
        pov "Like, I was meant to be the one taken, you know?"
        show pov sad at left
        show mis sad_talk at right
        mis "What happened was a tragedy, there is no denying that."
        show pov sad at left
        show mis sad_talk at right
        mis "But even if it was you the one who got taken, things wouldn’t be any different now would they?"
        show mis angry_talk at right
        mis "There would still be a kidnapper on the loose, the town still got vandalized and there is still a family worried sick for their missing loved ones."
        show mis sad_talk at right
        mis "You can’t blame yourself for that."
        show mis sad at right
        pov "…"
        show pov sad at left
        mis "…"
        show mis embarrassed_talk at right
        mis "If it helps…"
        mis "I’m glad it wasn’t you who was taken."
        show pov embarrassed at left
        show mis sad_talk at right
        mis "Don’t get me wrong, I wish nobody had gotten kidnapped in the first place."
        show pov embarrassed at left
        show mis sad_talk at right
        mis "But it would have been really sad to walk into the classroom every day and find your seat empty."
        mis "I’m sure Effie, Jacob and all of your friends and family would feel the same."
        mis "You are becoming a part of the town, so it would hurt us if you were to just disappear."
        show pov embarrassed at left
        show mis sad at right
        pov "…"
        show pov embarrassed_talk at left
        show mis sad at right
        pov "Thank you, Miss Allaway."
        show pov embarrassed_talk at left
        show mis sad at right
        pov "I guess I really needed to hear that…"
        show pov embarrassed at left
        show mis neutral_talk at right
        mis "Of course, [povname]."
        show pov neutral at left
        show mis neutral_talk at right
        mis "Now, I know this is sudden. But I need you to go to Director Lashley’s office."
        show pov confused at left
        show mis neutral_talk at right
        mis "She has requested to meet with you, likely to ask you similar things I did."
        show mis confused_talk at right
        mis "I would normally write a report for her or inform her verbally, but she was very insistent that she wanted to speak to you face to face."
        show pov confused_talk at left
        show mis confused at right
        pov "Oh, okay."
        show pov confused_talk at left
        show mis confused at right
        pov "Am I not going to have to write the essay you asked for, then?"
        show pov confused
        show mis bored_talk at right
        mis "If your chat with the administator ends early, then I do expect you to come back and finish the assignment."
        mis "However, if first period ends while you are there, then you’ll be excused."
        mis "Move along now. Don’t keep the administator waiting."
        show mis bored
        show pov embarrassed_talk at left
        pov "Sure thing."
        show pov neutral_talk at left
        pov "Thanks again, Miss Allaway."
        show pov neutral
        show mis neutral_talk at right
        mis "It was my pleasure, [povname]."
        show mis bored_talk at right
        mis "Now get going!"
        mis "Don’t waste time."

    else:
        show pov confused at left
        with dissolve
        show mis sad_talk at right
        with dissolve
        mis "What’s wrong, [povname]?"
        show pov confused_talk
        pov "W-What are you-?"
        show pov confused
        show mis angry_talk
        mis "Save the coy bullshit, alright?"
        show mis confused_talk
        mis "I came into that classroom after a stressful night, hoping to be done with the lesson soon, so I could find a moment to talk to the love of my life. And instead I find him looking half dead and like he is about to pass out or have a heart attack."
        show mis confused
        show pov smirk_talk
        pov "I’m the love of your life?"
        show pov smirk
        show mis angry_talk
        mis "Don’t you dare change the subject!"
        show pov confused
        mis "I want you to put yourself in my shoes and imagine walking in, to me, looking like that."
        mis "Would you get as worried as I am right now?"
        mis "Would you ask the same things I am asking you right now?"
        mis "Would you tell me to cut the bullshit and tell me to give you a straight answer?"
        show mis sad_talk
        mis "I know when something is wrong with you, [povname]."
        show mis neutral_talk
        mis "You wouldn’t let me deal with things all alone back then. Well, you better believe I am not letting you do the same now!"
        show mis neutral
        pov "…"
        show mis sad_talk
        mis "[povname], please…"
        show mis sad
        show pov sad
        pov "..."
        show pov sad_talk
        pov "Bad dreams… I guess, is the right word for it."
        show pov sad
        show mis confused_talk
        mis "What do you mean?"
        show mis confused
        show pov sad_talk
        pov "Well, a lot is going on, Allaway..."
        pov "That, and the whole stress of being drugged and a kidnapper on the loose, takes a toll on a guy."
        show pov sad
        pov "…"
        show pov sad_talk
        pov "I… I keep thinking it should have been me, you know?"
        show pov sad
        show mis angry_talk
        mis "Don’t be stupid, [povname]."
        show pov shocked
        mis "How can you say that?"
        show mis angry
        show pov shocked_talk
        pov "I can’t help it."
        pov "I mean, I was practically a sitting duck out there!"
        show mis sad
        show pov sad_talk
        pov "I just wondered why didn’t they take me instead."
        pov "I can’t help but to feel sort of guilty over what happened…"
        pov "Like, I was meant to be the one taken, you know?"
        show pov sad
        show mis sad_talk
        mis "What happened was a tragedy."
        mis "But even if you were the one who got taken, things wouldn’t be any different, now, would they?"
        mis "There would still be a kidnapper on the loose, the town still be vandalized and there would still be families worried sick for their missing loved ones."
        mis "You can’t blame yourself for that."
        pov "…"
        show pov shocked
        show mis neutral_talk at center with dissolve#TEMP
        #-Allaway gets closer to you and hugs you tightly-
        mis "[povname], you are my world…"
        show pov confused
        show mis sad_talk
        mis "If something were to happen to you, I…"
        mis "I don’t think I would be able to take it!"
        show pov sad
        mis "Don’t get me wrong, I wish nobody had gotten kidnapped in the first place."
        mis "But if I had to come in to that classroom and find your seat empty every day…"
        mis "If I had to sit by my phone, hoping and praying for any news that they found you…"
        mis "I would die on the inside."

        #-She kisses you softly, making it quick in order to not be caught by any passerby-

        mis "I’m sure Effie, Jacob and all of your friends and family would miss you."
        mis "But If I lost you, I would lose my reason to live!"
        mis "You became such an important part of my life that… I simply cannot see a future without you..."
        show mis sad
        show pov bored
        pov "…"
        show pov bored_talk
        pov "Thank you, Miss Allaway."
        pov "I guess I really needed to hear that…"
        show pov bored
        show mis bored_talk
        mis "I love you, [povname]."
        show mis smirk_talk
        mis "And you are forbidden to disappear, understood?"
        show mis smirk
        show pov smirk_talk
        pov "Heh, Understood."
        pov "I love you too."
        show pov smirk
        show mis bored_talk
        mis "Good! Now before you make me cry, I need you to go to Director Lashley’s office."
        mis "She has requested to meet with you."
        show mis bored
        show pov confused_talk
        pov "For what?"
        show pov confused
        show mis bored_talk
        mis "Probably to give you a personal evaluation."
        mis "You were drugged after all, so she probably wants to make sure you are handling the stress of it properly."
        show mis confused_talk
        mis "I told her I would do it, but she was very insistent on doing it herself."
        show mis confused
        show pov confused_talk
        pov "Oh, okay."
        pov "Am I not going to have to write the essay you asked for, then?"
        show pov confused
        show mis smirk_talk
        mis "Yes, but I do expect you to take me out to the movies as a way of paying it back to me, got it?"
        show mis smirk
        show pov smirk_talk
        pov "My pleasure."
        show pov smirk
        show mis bored_talk
        mis "Good! I’ve been dying to spend some time with my boyfriend, so you better make it a good date."
        show mis neutral_talk
        mis "Move along now. Don’t keep the administator waiting."
        show mis neutral
        show pov neutral_talk
        pov "Sure thing."
        pov "Thanks again, Allaway."
        show pov neutral
        show mis bored_talk
        mis "I love you, you big idiot."
        mis "Now get going!"
        mis "Don’t make the administator wait."

    $ main_story = 73

    $ townmap_enabled = 0

    jump lbl_schoolhallway1_day_setup
