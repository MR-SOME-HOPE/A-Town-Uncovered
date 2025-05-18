label lbl_natural_urges:
    scene bg schoolhallway2_day
    if gtime == 0:
        show btn schoolhallway2_day_luna_idle
    $ renpy.pause(0.001)
    ###if principallashley_path == 6 and gtime == 1
    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    default mc_told_lashley_about_liking_a_girl = False
    ##-Scenes starts a few days after the previous scene, The Mc enters her office to find Lashley flustered and fidgeting-
    image bg naturalurges_massage_anim = Animation(
    "//scenes/school/principaloffice/day/story/naturalurges/assets/bg_naturalurges_massage1.jpg", 0.8,
    "//scenes/school/principaloffice/day/story/naturalurges/assets/bg_naturalurges_massage2.jpg", 0.8,
    "//scenes/school/principaloffice/day/story/naturalurges/assets/bg_naturalurges_massage3.jpg", 0.8
    )


    scene bg framed_no_mag_embarrassed with fade
    pov "Director Lashley?"
    scene bg framed_no_mag_shocked_talk
    pri "W-What?"
    scene bg framed_no_mag_embarrassed_talk
    pri "[povname]. Hi!"
    scene bg framed_no_mag_sad_talk
    pri "You caught me a bit ill, as I’m sure you can see."
    scene bg framed_no_mag_shocked
    pri "{i}No! Not now! Anytime but now!{/i}"
    scene bg framed_no_mag_angry
    pov "Everything okay?"
    scene bg framed_no_mag_embarrassed_talk
    pri "Y-Yeah! Just uh… Allergies and stuff like that. Happens from time to time."
    scene bg framed_no_mag_embarrassed
    pri "{i}Okay. Don't panic, Lashley! Act natural!{/i}"
    scene bg framed_no_mag_confused
    pov "Should I come back some other time?"
    scene bg framed_no_mag_shocked_talk
    pri "No!"
    scene bg framed_no_mag_sad_talk
    pri "P-Please, sit down. I’ve been looking forward to the next time we would be able to chat."
    scene bg framed_no_mag_embarrassed
    pov "Are you sure, I mean, you are all red and-"
    scene bg framed_no_mag_embarrassed_talk
    pri "D-Don’t make me beg now."
    scene bg framed_no_mag_embarrassed
    pov "Uhh… Okay…"

    ##-The Mc sits down, now its move obvious something is definitely going on with Lashley, clear signs of her being under something"
    scene bg framed_no_mag_confused
    pov "Are you sure you are feeling okay? Should I call the nurse or something?"
    scene bg framed_no_mag_embarrassed_talk
    pri "It’s alright, really!"
    scene bg framed_no_mag_sad_talk
    pri "Remember how I told you that I used to get sick often when I was younger?"
    pri "This is basically it. Nothing to be worried about."
    scene bg framed_no_mag_embarrassed
    pov "If you say so…"
    pov "So… What should we talk abou-"
    scene bg framed_no_mag_shocked_talk
    pri "You are friends with a lot of girls, right?"
    scene bg framed_no_mag_shocked
    pov "What?"
    scene bg framed_no_mag_confused
    pri "{i}Did I just ask that?!{/i}"# (thoughts):
    scene bg framed_no_mag_embarrassed_talk
    pri "I-I uh, figured I’ve done all the talking lately, so I wanted to start asking you questions and get to know you for a change."
    scene bg framed_no_mag_confused_talk
    pri "I-Is that wrong?"
    scene bg framed_no_mag_confused
    pov "Uh, no! Not at all, it just wasn’t the type of question I was expecting."
    pov "I suppose I do. I have some guy friends too."
    scene bg framed_no_mag_embarrassed_talk
    pri "I-I know that. It’s just that I mainly see you around girls, lately."
    scene bg framed_no_mag_embarrassed
    pov "Well, I… can’t really deny that."
    scene bg framed_no_mag_confused_talk
    pri "Are you... Close with them?"
    scene bg framed_no_mag_shocked
    pri "{i}Lashley, that is none of your business!{/i}" #(thoughts):
    scene bg framed_no_mag_sad
    pov "I guess?"
    scene bg framed_no_mag_confused
    pov "Define close."
    scene bg framed_no_mag_sad_talk
    pri "Well… Do you, present any particular feelings or desires for any of them?"
    scene bg framed_no_mag_sad
    pov "Uh…"
    scene bg framed_no_mag_sad_talk
    pri "Any… longing for a particular girl in your life?"
    scene bg framed_no_mag_sad
    pov "Are you asking me if I like any of them?"
    scene bg framed_no_mag_confused_talk
    pri "Well… Do you?"
    scene bg framed_no_mag_confused

    menu any_particular_girl:
        "Yes, I do.":
            $ mc_told_lashley_about_liking_a_girl = True
            scene bg framed_no_mag_confused
            pov "Bit embarrassing to come out and say it, but yeah. I think I do."
            pri "{i}W-What?{/i}"#(thoughts):
            scene bg framed_no_mag_sad_talk
            pri "Oh…"
            scene bg framed_no_mag_bored_talk
            pri "That’s… Great…"
            scene bg framed_no_mag_confused
            pov "Everything okay?"
            scene bg framed_no_mag_confused_talk
            pri "Yeah… Please, go on. Tell me more about this… girl…"
            pri "Someone in your close friends group?"
            scene bg framed_no_mag_confused
            pov "I… Don’t really feel comfortable just going out and saying it, you know?"
            scene bg framed_no_mag_shocked_talk
            pri "I assure you, it’s fine!"
            scene bg framed_no_mag_embarrassed_talk
            pri "I’m not about to just go and spread rumors about it or anything."
            scene bg framed_no_mag_embarrassed
            pov "I-I know that, it's just… I’d rather talk about something else, for now…"
            scene bg framed_no_mag_confused
            pov "Didn’t really come prepared for all the love talk, you know?"
            scene bg framed_no_mag_sad_talk
            pri "I see… Well, I-I guess I can respect that…"
            scene bg framed_no_mag_sad

        "Not really.":
            scene bg framed_no_mag_embarrassed
            pov "Sorry to disappoint you, but I don’t really have any special feelings for anyone right now."
            scene bg framed_no_mag_neutral
            pri "{i}Why am I a bit relieved to hear that?{/i}"#(thoughts):
            scene bg framed_no_mag_neutral_talk
            pri "R-Really, not a single person?"
            scene bg framed_no_mag_neutral
            pov "Really."
            pov "I guess I haven’t put much of a focus on that."
            scene bg framed_no_mag_embarrassed_talk
            pri "And what about… casual encounters?"
            pri "Do you fancy more of that kind of interaction?"
            scene bg framed_no_mag_embarrassed
            pov "Now that's a bit too personal for the first few questions, isn’t it?"
            scene bg framed_no_mag_shocked_talk
            pri "I don’t mean any harm by it!"
            scene bg framed_no_mag_confused
            pov "I-I know that, but mind if we talk about something else, first?"
            pov "You know, build up to it?"
            scene bg framed_no_mag_neutral_talk
            pri "T-That’s fair enough."

        "Why the interest?":
            scene bg framed_no_mag_shocked
            pov "That’s a rather sudden question, why such a big interest?"
            scene bg framed_no_mag_shocked_talk
            pri "N-No reason!"
            pri "I-I-It was just the first thing that came to mind, really!"
            scene bg framed_no_mag_confused_talk
            pri "You are no stranger to asking personal questions right off the bat, right?"
            scene bg framed_no_mag_confused
            pov "I… Suppose I’m also guilty of that, aren’t I?"
            pov "Sorry, I just wasn’t expecting that right off the bat, you know?"
            pov "I’m usually the one asking the questions."
            scene bg framed_no_mag_confused_talk
            pri "It’s alright, I totally get it! B-But you still haven’t answered my question."
            scene bg framed_no_mag_confused
            jump any_particular_girl

    scene bg framed_no_mag_sad_talk
    pri "I-I apologize."
    pri "I really don’t get the chance to talk to anyone, outside of a work related scenario, so I guess I’m a bit awkward when it comes to my social skills."
    scene bg framed_no_mag_sad
    pov "It’s alright, the question caught me off guard mostly."
    pov "Also, are you sure you are feeling alright?"
    scene bg framed_no_mag_shocked_talk
    pri "A-A hundred percent!"
    scene bg framed_no_mag_confused_talk
    pri "Why do you ask?"
    scene bg framed_no_mag_confused
    pov "Well, the fact that you have a stutter and are stuttering every few sentences, is one."
    scene bg framed_no_mag_embarrassed
    pov "The fact you are all red in the face is another."
    pov "And the fact you look nervous as a dog in the fireworks show is another."
    scene bg framed_no_mag_sad
    pri "{i}He knows something’s up with me!{/i}"#(thoughts):
    scene bg framed_no_mag_embarrassed_talk
    pri "O-Oh, you noticed those…"
    scene bg framed_no_mag_sad_talk
    pri "Like I told you, [povname]: this is an illness I’ve had since I was young."
    pri "My body heats up, my back tends to ache and I get really jumpy out of a sudden."
    pri "Don’t worry about it."
    scene bg framed_no_mag_sad
    pov "Sounds rough. Do you take any medication?"
    scene bg framed_no_mag_bored_talk
    pri "U-Used to. Nowadays I try to go for more natural remedies."
    pri "It’s mainly just annoying when it happens, so n-no use getting my body hooked up in pills when it’s not something serious."
    scene bg framed_no_mag_bored
    pov "I guess I see the point…"
    pov "Well, is there anything I can do?"
    scene bg framed_no_mag_neutral_talk
    pri "You are so thoughtful, [povname]."
    pri "B-But I’m fine, really!"
    pri "Just have to bear through it until my body calms down."
    scene bg framed_no_mag_neutral
    pov "Well..."
    scene bg framed_no_mag_confused
    pov "This may be a little forward of me."
    scene bg framed_no_mag_shocked
    pov "But maybe I could massage your back, where it aches?"
    scene bg framed_no_mag_shocked_talk
    pri "M-Massage?!"
    scene bg framed_no_mag_shocked
    pov "Yeah, [sister] often forces me to help with her back pains."
    pov "It’s something I’ve gotten used to doing, really. I don’t mind giving you a hand."
    scene bg framed_no_mag_shocked_talk
    pri "T-There is really no need, I-!"
    scene bg framed_no_mag_shocked
    pov "I insist."
    scene bg framed_no_mag_embarrassed_talk
    pri "Um…"
    pri "Okay…"

    ##-The Mc moves and positions himself behind Lashley-
    scene bg framed_no_mag_embarrassed
    pov "Okay, I’m going to start with your shoulders and work my way down, okay?"
    scene bg framed_no_mag_embarrassed_talk
    pri "O-Okay."
    scene bg framed_no_mag_confused
    pri "{i}Why am I letting him do this?!{/i}"#(thoughts):
    scene bg framed_no_mag_embarrassed
    pov "Let me know if I’m being too rough with you, okay?"
    scene bg framed_no_mag_embarrassed_talk
    pri "S-Sure thing. Thanks for doing this, I know it can’t be the most fun thing to-"


    ##-The Mc places his hands on Lashley’s shoulders making her face redden-"
    scene black
    with fade

    pri "-Eep!"
    scene bg naturalurges_massage1
    show eyes distractions_up
    show charexpression distractions_embarrassed_talk
    with dissolve

    show charexpression distractions_shocked_talk
    pri "-Eep!" with vpunch
    show charexpression distractions_shocked
    pov "Woah, 'you alright? I haven’t even applied any pressure yet."
    show charexpression distractions_confused
    show eyes naturalurges_back
    with dissolve

    show charexpression distractions_confused_talk
    pri "Y-Yeah!"
    pri "All fine, everything’s fine!"
    show charexpression distractions_embarrassed
    pov "You sure? I-"
    show charexpression distractions_embarrassed_talk
    pri "It’s fine, [povname]! Please continue…"
    show charexpression distractions_embarrassed
    pri "{i}Oh my God, Oh my God, Oh my God!{/i}"#(thoughts):
    pri "{i}Why do I want him to touch me so bad?!{/i}"#(thoughts):
    pri "{i}What is wrong with me?!{/i}"#(thoughts):
    pov "Okay…"
    show bg naturalurges_massage_anim
    ##-The Mc places his hands on Lashley’s shoulders and starts applying pleasure."


    show charexpression distractions_embarrassed_talk
    pri "{i}*Moan*{/i}"
    show charexpression distractions_shocked_talk
    pri "Eep! I’m so sorry!"
    show charexpression distractions_embarrassed
    pri "{i}Did I just moan, with him just touching me?!{/i}"#(thoughts):
    pov "Director Lashley, it’s fine."
    pov "Relax a little. You are meant to enjoy this."
    pov "Does it feel good?"
    show charexpression distractions_embarrassed_talk
    pri "Y-Yes…"
    show charexpression distractions_embarrassed
    pri "{i}It’s amazing...{/i}"#(thoughts):
    show charexpression distractions_shocked
    pov "Good, I’m going to apply some more pressure, okay?"
    pov "Tell me if I’m going too far."
    show charexpression distractions_embarrassed_talk
    pri "O-Okay…"
    show charexpression distractions_embarrassed
    pov "Here I go, let's do it slowly."

    ##-The Mc applies more pressure making Lashley’s head arch back-
    show charexpression distractions_embarrassed_talk
    pri "{i}*Moan*{/i}"
    show charexpression distractions_embarrassed
    pov "You have a lot of knots over here."
    pov "It’s like handling a piece of steel!"
    show charexpression distractions_embarrassed_talk
    pri "I-I do have a lot of work on my shoulders…"
    show charexpression distractions_embarrassed
    pov "I can see that, lets go a little lower and work on your back, alright?"
    show charexpression distractions_embarrassed_talk
    pri "Y-Yes…"
    show charexpression distractions_shocked_talk
    pri "{i}*Moan*{/i} [povname], I…"

    menu:
        "Talk Seductively (requires 5 charisma) (disabled)"if skill_cha < 5:
            pass
        "Talk Seductively (requires 5 charisma)"if skill_cha >= 5:
            $ skill_cha -= 5
            $ renpy.notify("You used 5 Charisma Points")
            $ renpy.pause(1.0)

            $ add_points("principallashley_points",2)

            show charexpression distractions_shocked
            pov "Do you like that?"
            show charexpression distractions_shocked_talk
            pri "H-Huh?"
            show charexpression distractions_embarrassed
            pov "Does it feel good when I rub your body like this?"
            show charexpression distractions_embarrassed_talk
            pri "I-I…"
            show charexpression distractions_embarrassed
            pri "{i}H-He is too close! My heart is leaping out of my chest!{/i}"#(thoughts):
            show charexpression distractions_confused
            pov "Well?"
            show charexpression distractions_embarrassed
            pov "Do you like it?"
            pov "Want me to go a little… Harder?"
            show charexpression distractions_shocked_talk
            pri "{i}AHHHHHH!{/i}"#(thoughts):
            show charexpression distractions_embarrassed_talk
            pri "Y-Yes, please..."
            show charexpression distractions_shocked
            pov "Oh, you like it harder, then?"
            show charexpression distractions_embarrassed_talk
            pri "T-That’s not what I-!"
            show charexpression distractions_embarrassed
            pov "I’m just teasing you, relax."
            pov "You do have a lot of knots back here."
            pov "Do you have back pains often?"

        "Work on her some more (use strength)":
            $ add_points("principallashley_points",1)
            show charexpression distractions_embarrassed
            pov "It’s okay."
            show charexpression distractions_neutral
            pov "Just relax and let me work your back."
            show charexpression distractions_shocked
            pov "Okay, I’m going a little bit harder on here."
            pov "Ready?"
            show charexpression distractions_embarrassed_talk
            pri "I-I think-"

            ##-The Mc starts kneading Lashley’s shoulder harder, with varying results depending on his strength stat-

            if 0 <= skill_str <= 5:
                show charexpression distractions_embarrassed_talk
                pri "Mmm…?"
                show charexpression distractions_confused_talk
                pri "A-are you… doing anything different?"
                show charexpression distractions_embarrassed
                pov "Trying, these knots are like working with a rock!"
                pov "Do you get back pains often?"

            elif 6 <= skill_str <= 13:
                $ skill_str -= 6
                $ renpy.notify("You used 6 Strength Points")
                $ renpy.pause(1.0)
                $ add_points("principallashley_points",1)
                show charexpression distractions_shocked_talk
                pri "{i}*Moan*{/i}"
                show charexpression distractions_embarrassed_talk
                pri "T-That feels really nice, [povname]."
                show charexpression distractions_embarrassed
                pri "{i}My lord, I could feel his hands all over me forever…{/i}"#(thoughts):
                show charexpression distractions_shocked
                pri "{i}W-Wait… What am I thinking?!{/i}"#(thoughts):
                pri "{i}He is my student for God's sake!{/i}"#(thoughts):
                show charexpression distractions_embarrassed
                pov "I’m glad to hear that."
                pov "You have quite a lot of knots back here."
                pov "Do you happen to get back pains a lot?"

            elif 14 <= skill_str <= 20:
                $ skill_str -= 14
                $ renpy.notify("You used 14 Strength Points")
                $ renpy.pause(1.0)
                $ add_points("principallashley_points",3)
                pri "{i}*Moan*{/i}"
                show charexpression distractions_embarrassed_talk
                pri "{i}*Moan*!{/i}"
                show charexpression distractions_shocked_talk
                pri "O-Oh, Sweet Lord, [povname]!"
                show charexpression distractions_embarrassed_talk
                pri "T-This feels… Incredible!"
                show charexpression distractions_embarrassed
                pri "{i}I’m like putty in his expert hands!{/i}"#(thoughts):
                show charexpression distractions_shocked
                pri "{i}W-Why do I love this so much?!{/i}"#(thoughts):
                pri "{i}It’s like my mind is going blank!{/i}"#(thoughts):
                show charexpression distractions_neutral
                pov "I’m glad to hear you are liking it."
                pov "You have a lot of knots back here but nothing I can’t work with."
                show charexpression distractions_embarrassed
                pov "Do you happen to get a lot of back pains really often?"

    show charexpression distractions_embarrassed_talk
    pri "Y-Yeah…"
    pri "I have a lot of… Um…"
    show charexpression distractions_confused_talk
    pri "Frontal weight…"
    show charexpression distractions_confused
    pri "{i}Did I really just call it that?!{/i}"#(thoughts):
    show charexpression distractions_shocked
    pri "{i}What if he thinks I'm too heavy?!{/i}"#(thoughts):
    pri "{i}And why do I suddenly care so much about what he thinks of me?!{/i}"#(thoughts):
    show charexpression distractions_confused
    pov "Can't imagine what it's like."
    show charexpression distractions_shocked
    pov "Well, if a backrub from time to time helps you out, I don't mind doing it again."
    show charexpression distractions_confused_talk
    pri "R-Really?"
    show charexpression distractions_confused
    pov "Yeah, if you'll let me that is."
    show charexpression distractions_bored
    pri "{i}Say no, say no, say no!{/i}"#(thoughts):
    show charexpression distractions_embarrassed_talk
    pri "U-Um… Alright… I-I'll keep it mind…"
    show charexpression distractions_sad
    pri "{i}Why can't I say no to him?!{/i}"#(thoughts):
    show charexpression distractions_shocked
    pov "Well, just a minutes more and we should be done here."
    show charexpression distractions_embarrassed
    pov "Let's not set loose your back too much at once."
    show charexpression distractions_neutral_talk
    pri "A-Alright…"
    show charexpression distractions_embarrassed
    pov "Sorry if I made you uncomfortable."
    show charexpression distractions_shocked_talk
    pri "N-Not at all!"
    show charexpression distractions_neutral_talk
    pri "Thank you, [povname], my back does feel a bit better."
    show charexpression distractions_neutral
    pov "That’s good to hear."
    pov "So, how about you, Director Lashley?"
    show charexpression distractions_neutral_talk
    pri "What about me?"
    show charexpression distractions_confused
    pov "Well, you did ask if I was interested in anyone."
    show charexpression distractions_shocked
    pov "How about you?"
    show charexpression distractions_embarrassed_talk
    pri "U-Umm, I-"
    show charexpression distractions_embarrassed
    pov "Only fair, right?"
    show charexpression distractions_confused_talk
    pri "Y-Yes, I suppose..."
    show charexpression distractions_embarrassed
    pri "{i}See where you get us with your questions?!{/i}"#(thoughts):
    show charexpression distractions_embarrassed_talk
    pri "Well… To be honest with you, [povname]."
    pri "I-I find myself rather… Conflicted, when it come to that topic."
    show charexpression distractions_confused
    pov "What do you mean?"
    show charexpression distractions_confused_talk
    pri "I don’t really have much experience in the topic."
    show charexpression distractions_sad_talk
    pri "Growing up, my father was very protective and kept me from dating."
    pri "In all honesty, I didn’t really had much interest on the topic but…"
    show charexpression distractions_sad
    pov "But?"
    show charexpression distractions_embarrassed_talk
    pri "I recently found myself with some… Strange feelings for someone and I don’t know how to react."
    show charexpression distractions_confused
    pov "What exactly do you feel?"
    show charexpression distractions_bored_talk
    pri "I-It’s hard to describe…"
    show charexpression distractions_shocked
    pov "Is it a crush?"
    show charexpression distractions_shocked_talk
    pri "H-Huh?!"
    show charexpression distractions_confused
    pov "I mean, it’s pretty common."
    pov "You meet someone new, click with them and suddenly there is this rush of emotions on you."
    show charexpression distractions_confused_talk
    pri "I-Is that so?"
    show charexpression distractions_confused
    pov "Nothing wrong with that."
    show charexpression distractions_shocked
    pov "The heart wants what it wants and all of that."
    show charexpression distractions_embarrassed
    pov "I think it’s nice for you to have these feelings, you just don’t know how to deal with them, due to your upbringing."
    show charexpression distractions_bored_talk
    pri "Y-Yeah, I figured as much…"
    show charexpression distractions_embarrassed_talk
    pri "A-And… Do you have a crush right now?"
    show charexpression distractions_confused
    pov "I suppose I opened the door for that one, huh?"
    pov "Well…"

    menu:
        "Be Mysterious.":
            show charexpression distractions_shocked
            pov "Who knows?"
            show charexpression distractions_shocked_talk
            pri "Eh?!"
            show charexpression distractions_confused
            pov "Where’s the fun in just giving you the answer straight?"
            show charexpression distractions_bored_talk
            pri "B-But I thought…"
            pov "I know, I know."
            show charexpression distractions_bored
            pov "I know, I know."
            show charexpression distractions_confused
            pov "Well, I guess I can say this."
            show charexpression distractions_shocked
            pov "I happen to have my eye on a certain older woman lately."
            show charexpression distractions_shocked_talk
            pri "You do?"
            show charexpression distractions_shocked
            pov "She is really kind, hardworking and cares about the people around her."
            pov "A truly self made woman that rises to any challenge and isn’t afraid to voice her opinion."
            show charexpression distractions_confused
            pov "Nothing more attractive than that, at least in my eyes."
            show charexpression distractions_bored_talk
            pri "Oh, she sounds… Lovely..."
            show charexpression distractions_bored
            pov "She really is, a bit socially awkward but that only makes her cuter."
            show charexpression distractions_embarrassed_talk
            pri "How nice…"
            show charexpression distractions_confused
            pri "{i}I’m as self made woman too… Am I also attractive in his eyes?{/i}"#(thoughts):
            show charexpression distractions_shocked
            pov "Her blonde hair looks really good on her and she has the most beautiful pair of blue eyes I have ever seen."
            show charexpression distractions_confused
            pri "{i}So he likes blondes with blue eyes? Maybe I…{/i}"#(thoughts):
            pov "And she makes the cutests noises when I massage her back."
            show charexpression distractions_shocked
            pri "Wha-?!"
            show charexpression distractions_confused
            pov "Hehehe, sorry."
            pov "Was that too obvious?"
            show charexpression distractions_shocked_talk
            pri "I-I-"
            show charexpression distractions_shocked
            pov "Let’s leave it at that."
            pov "I know I can’t really pursue her, after all."
            show charexpression distractions_shocked_talk
            pri "T-Thats…"
            show charexpression distractions_shocked
            pov "But know I’m saying the truth."
            pov "I wouldn’t lie about something like this."

        "Be Direct.":
            show charexpression distractions_confused
            pov "Yeah, it is a bit embarrassing to admit, but I think you are really attractive."
            show charexpression distractions_shocked_talk
            pri "H-HUH?!"
            pri "[povname]. T-that’s!"
            show charexpression distractions_shocked
            pov "I know it isn’t appropriate for me to say it outloud."
            show charexpression distractions_embarrassed
            pov "But you were willing to be honest with me, so how can I not do the same?"
            show charexpression distractions_embarrassed_talk
            pri "B-But I…"
            show charexpression distractions_shocked
            pov "I’m not expecting you to like me back or anything. But I do want to assure you that you have nothing to worry about."
            pov "You are a great catch!"
            pov "You are kind, smart and a hard working woman willing to give her all for what she believes in."
            show charexpression distractions_confused
            pov "Whoever caught your interest is a really lucky person to have caught your eye."
            pov "You are definitely a 10 in my book."
            show charexpression distractions_embarrassed
            pri "{i}I think I’m going to faint!{/i}"#(thoughts):
            show charexpression distractions_embarrassed_talk
            pri "T-Thank you, thats…"
            show charexpression distractions_shocked
            pov "You don’t have to say anything."
            pov "Sorry if I made you uncomfortable."
            show charexpression distractions_embarrassed
            pov "But at least it got you blushing!"
            pov "You look really cute with those red cheeks on your face."

    ##-Lashley stands up, clearly in a panic as she heads for the door."

    scene bg naturalurges_lashley_stands with vpunch
    $ renpy.pause(0.01,hard=True)
    show bg naturalurges_lashley_standing
    pri "I-I-I’m sorry, [povname], but I just remembered I have to-"
    pri "I-I have too…"
    pri "{i}Come up with something!{/i}"#(thoughts):
    pri "W-Wash my hair!"
    pri "{i}Come up with something better!{/i}"#(thoughts):
    pov "Oh, that’s quite alright. I should be going as well."
    pri "D-Don’t let me keep you, then!"

    scene bg principaloffice_day
    with fade
    show pov smirk_talk at left
    with dissolve
    show pri embarrassed at right
    with dissolve
    #scene black with fade

    ##-The Mc walks out and is standing on the other side of the door with Lashley holding it open-
    pov "I had fun today, Director Lashley, I hope the massage helped you with the stress a little bit."
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "It did! Definitely did! Best massage I have ever gotten in my life. Now, if you’ll excuse me-"
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "Just one more thing, Director Lashley."
    show pov smirk at left
    show pri embarrassed at right
    pri "{i}Dear God, please have mercy on me!{/i}"#(thoughts):
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "Y-Yes?"
    show pov smirk_talk at left
    show pri confused at right
    pov "I realize this may come off as rude, but I can’t really help being curious about it."
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "What is it?"
    show pov smirk_talk at left
    show pri shocked at right
    pov "Are you not wearing a bra today?"
    show pov smirk at left
    show pri shocked_talk at right
    pri "S-Sorry, duty calls!"
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "P-Please come back some other time!"

    $ principallashley_path = 6.9

    jump lbl_schoolhallway2_day_setup
