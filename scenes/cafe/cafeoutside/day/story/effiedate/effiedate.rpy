## Effie Date ##
label lbl_effie_date:
    scene bg effiedate_2
    with fade
    eff "How's the milkshake? I hope it's good."
    show bg effiedate_1
    pov "It tastes really good! Thanks for that."
    show bg effiedate_4
    eff "No worries. Consider it a welcome gift, from me to you."
    scene bg effiedate_1
    pov "Why the double straw though?"
    show bg effiedate_6
    eff "Don't be so naive, [povname]."
    show bg effiedate_9
    $ renpy.pause ()
    show bg effiedate_4
    eff "Damn, I'm good."
    show bg effiedate_3
    pov "Haha, no doubt."
    show bg effiedate_2
    eff "So tell me, why did a big city guy like you move to a small town for?"
    show bg effiedate_1
    if winc == 0:
        pov "My [dadrole]'s job was relocated to here."
    else:
        pov "My dad's job was relocated to here."
    show bg effiedate_2
    eff "What does he do?"
    show bg effiedate_1
    pov "That, I honestly do not know. Some general office cubicle job, I guess. A white collar position. We don't really speak much of it - he's hardly home."
    show bg effiedate_2
    eff "I can understand that."
    show bg effiedate_1
    pov "What about you? What does your dad do, if you don't mind me asking."
    show bg effiedate_2
    eff "Well, that is hard to explain. I guess you could say he's a photographer, sort of."
    show bg effiedate_1
    pov "That's pretty cool. What about your mom? What does she do?"

    scene bg effiedate_2
    eff "I have no idea. My mom and dad got a divorce a few years back. I haven't seen or heard from her since."
    show bg effiedate_1
    pov "Oh my God. I'm really sorry to hear that."

    scene bg effiedate_2
    eff "It's alright, you don't need to be sorry. I'm over it. I've gotten used to taking care of myself."
    show bg effiedate_10
    pov "Doesn't your dad take care of you?"

    scene bg effiedate_8
    eff "With food and shelter, but he doesn't earn enough to put me through Uni or spoil me with stuff. That's why I'm working after classes."
    show bg effiedate_1
    pov "I guess that's part of life, isn't it? Is it hard having to study, then work, all the time?"

    scene bg effiedate_4
    eff "It is a bit, but it's good for me, I think. I'm the type of person that wants to keep myself occupied, and what better way than with university courses and work."
    show bg effiedate_1
    pov "Seems pretty stressful. I haven't gotten around to that stage of life yet."

    scene bg effiedate_6
    eff "Ehh, you get used to it. It's a routine."
    show bg effiedate_10
    pov "What about for fun? What do you do for fun?"

    scene bg effiedate_6
    eff "I get a high on sucking strangers dicks in public."
    show bg effiedate_5
    pov "W-What? Seriously?"

    scene bg effiedate_4
    eff "Dude, Jesus. I'm joking. You're so freakin' gullible, you know."
    show bg effiedate_5
    pov "If I had a dollar for every time I fall for your so-called jokes."

    scene bg effiedate_6
    eff "You'd have enough to pay me for a blowjob."
    show bg effiedate_5
    pov "What the hell, Eff-"

    scene bg effiedate_6
    eff "There's another dollar. Haha! Man, you're easy."
    show bg effiedate_5
    pov "I've only just met you, but you're already getting on my nerves."

    scene bg effiedate_6
    eff "Good. Get used to it."
    show bg effiedate_10
    pov "Looks like I don't have a choice."

    scene bg effiedate_4
    eff "As I said, it may seem stressful at first, but you'll get used to it."
    show bg effiedate_3
    pov "I'll drink to that."

    scene bg effiedate_9
    $ renpy.pause ()

    scene bg effiedate_10
    $ renpy.pause ()

    scene bg effiedate_5
    $ renpy.pause ()

    scene bg effiedate_6
    eff "Mark today as our first date together. We might want to remember it."
    show bg effiedate_5
    pov "Oh, it's a date now?"

    scene bg effiedate_6
    eff "Well... I did ask you to meet me here, and I did make this milkshake for us to share, so yeah, I'm going to call this a date."
    show bg effiedate_5
    pov "Hmm, you are quite different from other girls I've dated."

    scene bg effiedate_6
    eff "You've actually dated before?"
    show bg effiedate_3
    pov "Go to hell! Haha! But seriously, you're quite straightforward and... how should I say this? I don't mean it in a negative way, but aggressive, I guess?"

    scene bg effiedate_2
    eff "I know what you mean. Don't worry about it, I get that a lot. I guess it came from my independency."
    eff "I've learnt to take everything into my own hands and stopped relying on anyone. It's just a lot quicker and produces better results."

    scene bg effiedate_1
    pov "I'm sure you can't do EVERYTHING."
    show bg effiedate_2
    eff "You'd be surprised by my capabilities."

    scene bg effiedate_5
    pov "Surprise me, then."

    scene bg effiedate_10
    $ renpy.pause ()

    scene bg effiedate_6
    eff "Come meet me outside my house, after sunset. I'll make your night go off with a bang."

    menu:
        "You're not going to kill me, are you?":
            jump lbl_milkshake_kill_me
        "You're a professional fireworks operator?":
            jump lbl_milkshake_fireworks
        "We're going to have sex already?":
            jump lbl_milkshake_have_sex

label lbl_milkshake_kill_me:
    if effie_points <= 9:
        $ effie_points += 1
    else:
        $ effie_points = 10
    $ renpy.notify("Your relationship with Effie has increased")

    scene bg effiedate_5
    pov "You're not going to kill me, are you?"
    show bg effiedate_6
    eff "After I'm done with you, you'll be glad I killed you. Hehe."

    scene bg effiedate_7
    pov "I'm just going to assume you're joking, and laugh it off."
    eff "..."
    show bg effiedate_8
    eff "Don't wear white. Blood stains badly."

    scene bg effiedate_7
    eff "..."

    jump lbl_milkshake_for_two_end

label lbl_milkshake_fireworks:
    if effie_points <= 9:
        $ effie_points += 1
    else:
        $ effie_points = 10
    $ renpy.notify("Your relationship with Effie has increased")

    scene bg effiedate_1
    pov "You're a professional fireworks operator?"
    show bg effiedate_2
    eff "And a stunt driver."

    scene bg effiedate_1
    pov "Don't tell me you're also a black belt."
    show bg effiedate_6
    eff "Black belt in 3 different martial arts."

    scene bg effiedate_5
    pov "Only 3 different martial arts?"
    show bg effiedate_4
    eff "Go easy on me; I only started 2 years ago."

    jump lbl_milkshake_for_two_end

label lbl_milkshake_have_sex:
    if effie_points >= 1:
        $ effie_points -= 1
    else:
        $ effie_points = 0
    $ renpy.notify("Your relationship with Effie has decreased")

    scene bg effiedate_7
    pov "We're going to have sex already?"
    show bg effiedate_8
    eff "Wow, I don't think you know where to draw the line, do you?"
    eff "If we were to hook up, could you at least have some decency with it, and not act like a dick, with brainless body attached?"

    scene bg effiedate_7
    pov "I thought you were bold and straightforward."
    show bg effiedate_8
    eff "There's a line, [povname]. Learn when not to cross that line."

    jump lbl_milkshake_for_two_end

label lbl_milkshake_for_two_end:

    scene bg effiedate_10
    $ renpy.pause ()

    scene bg effiedate_2
    eff "Anyhoo, I've got to get back to work. Enjoy the rest of the milkshake for me, okay?"
    eff "I'll see you later. My house is just at the end of this street, you can't miss it."
    show bg effiedate_3
    pov "I'll see you then."
    $ main_story = 11
    $ townmap_enabled = 1
    $ renpy.notify("New Objective: Meet Effie Outside her House at night")
    if gtime == 0:
        $ gtime = 1

    jump lbl_cafeoutside_day_setup
