label lbl_meet_cole:
    #GeeSeki Note: Think of Doug Judy from Brooklyn 99." A cool, sleezy, everybody’s friend kind of dude."
    #He’s also a wanna-be entrepreneur and businessman at heart." Wanting to sell people on crazy money-making schemes and what not, of course for the benefit of both of them."

    #-You walk along the hallway when you are suddenly grabbed by the shoulder by a stranger-
    show pov bored at left
    with dissolve
    show col neutral_talk at right
    with dissolve
    col "Hey man, how's it going!"
    show pov neutral_talk at left
    show col neutral at right
    pov "Woah! Uh… Hey there."
    show pov confused at left
    show col neutral_talk at right
    col "Man of few words, eh? I like it!"
    col "Heard all about the new kid in town, so I decided to do you a favour and introduce myself."
    show pov confused at left
    show col smirk_talk at right
    col "Name’s Cole: The men know me as ‘The Man’ and the ladies know me as the guy they think about every time they splooge."
    col "I am the man that can get you what you need and the man who knows everybody, so you can consider me your new best friend."
    show pov confused_talk at left
    show col angry at right
    pov "Are you trying to sell me something?"
    show pov confused at left
    show col angry_talk at right
    col "Ooft, that stings!"
    col "Why you have to burst a brother’s mood like that?"
    show pov sad at left
    show col bored_talk at right
    col "It ain’t wise to go around the new town being a downer like that, you know?"
    col "That’s poor people skills."
    show pov embarrassed_talk at left
    show col neutral at right
    pov "S-Sorry."
    show pov confused at left
    show col neutral_talk at right
    col "Nah, It’s cool man!"
    col "Just messing with ya."
    show pov neutral at left
    show col smirk_talk at right
    col "How you liking the town so far?"
    show pov neutral_talk at left
    show col smirk at right
    pov "It’s nice. Quite the peaceful little place."
    show pov neutral at left
    show col neutral_talk at right
    col "That’s good to hear, man!"
    show pov embarrassed at left
    show col smirk_talk at right
    col "Not a lot to do - but we got some of the finest ladies around!"
    col "Seriously, man. You play your cards right, and I guarantee you’ll soon be swimming in some of the finest cooch you have ever slid in."
    show pov embarrassed_talk at left
    show col smirk at right
    pov "That's… good to hear, I guess?"
    show pov neutral at left
    show col smirk_talk at right
    col "Aww, come on, man! No need to be shy!"
    show pov embarrassed at left
    show col neutral_talk at right
    col "Look, what’s your name?"
    show pov neutral at left
    col "Listen to me: all rambling, without even asking a brother for his name first."
    show pov neutral_talk at left
    show col neutral at right
    pov "Heh, It’s cool."
    pov "I’m [povname]."
    show pov neutral at left
    show col neutral_talk at right
    col "[povname]! Welcome to our little corner of paradise!"
    show pov confused at left
    col "As a welcoming gift, have some free product!"
    #-Cole hands you a small paper bag-
    show pov shocked_talk at left
    show col shocked at right
    pov "Are you giving me drugs?!"
    show pov confused at left
    show col shocked_talk at right
    col "What?!"
    show pov shocked at left
    show col bored_talk at right
    col "No! No, you want to speak to Jack for that."
    show pov bored at left
    show col neutral_talk at right
    col "That -you have in your hands- is some of my merch."
    col "I am a bit of a salesman, you see."
    show pov confused at left
    show col smirk_talk at right
    col "Any particular oddity you need? For the right price, I can get it for you - and won’t even ask any questions!"
    show pov bored_talk at left
    show col neutral at right
    pov "So you WERE trying to sell me something earlier?"
    show pov bored at left
    show col neutral_talk at right
    col "Hehe, brother’s gotta do what a brother’s gotta do."
    col "I have a family to feed."
    show pov confused at left
    show col smirk_talk at right
    col "They’re gerbils, but still, family."
    show pov neutral at left
    show col neutral_talk at right
    col "But you’re cool, so no reason why give the whole script, you know?"
    col "Honesty with potential clients is the best policy, and all."
    show pov neutral_talk at left
    show col neutral at right
    pov "I guess so…"
    pov "So this is your full time job?"
    show pov bored at left
    show col neutral_talk at right
    col "I am an entrepreneur on the rise, my friend! If there is a way to make profit off it, I am in!"
    col "Plus, it’s a great way to stay connected to the people, you know?"
    show pov bored_talk at left
    show col neutral at right
    pov "Quite the people person, huh?"
    show pov neutral at left
    show col neutral_talk at right
    col "You know it!"
    show pov confused at left
    show col neutral_talk at right
    col "People tend to be real friendly to the guy who got them that embarrassing thing they have been saving for months for; but are too afraid to buy themselves."
    col "Especially if it makes me not give others, said embarrassing details."
    show pov confused_talk at left
    show col neutral at right
    pov "I’ll… be sure to remember that, then."
    show pov neutral at left
    show col neutral_talk at right
    col "See? You are already getting adjusted to the way things work here!"
    col "I am certain we are going to get along just fine!"
    #-Cole’s phone rings-
    show pov bored at left
    show col bored_talk at right
    col "Oh, gotta go."
    col "A guy’s expensive sex doll arrived and he is getting antsy on delivery."
    show pov confused at left
    show col neutral_talk at right
    col "Catch you on the flip side, brother!"
    show pov confused_talk at left
    show col neutral at right
    pov "Y-Yeah, you too!"
    hide col
    #-Cole leaves-
    show pov confused at left
    pov "…"
    show pov confused_talk at left
    pov "Did he say sex doll?"
    $ cole_path = 1
    $ add_contact("Cole")
    pause 0.2
    jump lbl_schoolcafeteria_day_setup
