## Edward Side Story Throwaway Conversations Schoolyard ##

## Headset Mod
# label lbl_schoolyard_day_edward_headsetmod:
#     "*VR headset modification placeholder*"
#     show pov confused at left
#     with dissolve
#     hide btn schoolyard_day_edward_idle
#     show edw neutral_talk at right
#     with dissolve
#     edw "Give me that!"
#     $ inventory.drop(Items.vrheadset)
#     show pov angry_talk at left
#     show edw bored at right
#     pov "Hey what are you doing!?"
#     show pov confused at left
#     show edw neutral_talk at right
#     edw "Don't worry you'll thank me in a minute!"
#     show pov confused_talk at left
#     show edw neutral at right
#     pov "Okay..."
#     scene black
#     with fade
#     "A few minutes later."
#     scene bg schoolyard_day
#     with fade
#     show pov confused at left
#     with dissolve
#     show edw neutral_talk at right
#     with dissolve
#     $ inventory.add(Items.vrheadsetmod)
#     $ vrheadset_chest = 1
#     edw "There all done!"
#     show pov confused_talk at left
#     show edw neutral at right
#     pov "What exactly did you do to my very expensive VR kit?"
#     show pov confused at left
#     show edw neutral_talk at right
#     edw "Oh now it will interface directly with your mind to help you vividly remember things you experienced in the past!"
#     show pov neutral at left
#     show edw smirk_talk at right
#     edw "Particularly the most sexual exciting moments of your existence!"
#     show pov confused_talk at left
#     show edw neutral at right
#     pov "I don't know how but, uh thanks I guess..."
#     show pov confused at left
#     show edw smirk_talk at right
#     edw "Oh you'll be thanking me a lot more than that after you actually try it!"
#     show pov confused_talk at left
#     show edw neutral at right
#     pov "Sure... I'll talk you later."
#     hide pov
#     show edw smirk_talk at right
#     edw "Oh you'll see once you put it on..."
#     hide edw
#     with fade
#     jump lbl_schoolyard_day

#######################################################
## Snap Back to Virtual Reality
label lbl_snap_back_to_virtual_reality:
    #[School yard, Morning- “Snap back to Virtual Reality”  - edward_vr_path=1]

    #-Mc approaches Edward in the school’s yard-
    show pov confused_talk at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw neutral at right
    with dissolve
    pov "Hey Edward."
    show pov confused at left
    show edw embarrassed_talk at right
    edw "Hey, [povname], what’s up?"
    show pov confused_talk at left
    show edw embarrassed at right
    pov "Hey, I wanted to ask since you seem like the type of guy who would be into it."
    pov "Do you know much about virtual reality?"
    show pov embarrassed at left
    show edw confused_talk at right
    edw "Uh, do I know much about virtual reality?"
    show pov confused at left
    show edw smirk_talk at right
    edw "Dude, I love the virtual reality scene!"
    show pov shocked at left
    show edw neutral_talk at right
    edw "Do you realize how many years videogame nerds and technology enthusiasts have spent perfecting and idealizing the technology of interacting with a 3d space with a computer?"
    edw "It’s been a thing ever since home computers were a thing, dude and nowadays it's super easy to get into!"
    show pov neutral at left
    show edw smirk_talk at right
    edw "I’ve actually been working on something regarding virtual reality for quite a while now too."
    show edw confused_talk at right
    edw "Why do you ask though?"
    show pov shocked_talk at left
    show edw confused at right
    pov "OH. Well, I’ve always been interested a bit in virtual reality and I see the headset they are offering at the mall from time to time when I head over there but I wanted to hear your recommendations."
    show pov embarrassed at left
    show edw shocked_talk at right
    edw "Oh, well…"
    edw "This is a bit embarrassing after all I just said about vr but I don’t actually have a vr headset."
    show pov confused_talk at left
    show edw embarrassed at right
    pov "Really?"
    pov "That’s surprising considering your job for the technology behind it."
    show pov confused at left
    show edw smirk_talk at right
    edw "Well, I just can’t seem to fit it within my budget to have one of those."
    edw "Don’t get me wrong, I totally could if I really wanted to and quality vr headsets are becoming more affordable."
    show pov embarrassed at left
    show edw embarrassed_talk at right
    edw "But my budget is already stretched thin as it is with my monthly spending of equipment, materials and power tools for my projects."
    edw "So I had to decide whether to fork out the cash for a headset I probably won’t use much after a while due to my projects, or the material and equipment I need to keep working on the projects that would inevitably take my time off the headset."
    show pov smirk_talk at left
    show edw smirk at right
    pov "So a no-win situation for you and vr, huh?"
    show pov smirk at left
    show edw smirk_talk at right
    edw "At least until I don’t also have to juggle my work time with school work time anymore."
    edw "Until then I’ll have to put my VR related project on the backburner along with my cat crossbow and stealth attack helicopter projects."
    show pov embarrassed_talk at left
    show edw neutral at right
    pov "I’m… not even gonna ask about those last two."
    show pov confused_talk at left
    pov "But what was your VR project about?"
    show pov confused at left
    show edw neutral_talk at right
    edw "It’s an attachment to a VR headset that allows you to enter a sort of lucid dream state when you are conscious."
    show edw confused_talk at right
    edw "In theory, it could be used for you to relive through some of your own memories in semi real time!"
    show pov neutral_talk at left
    show edw embarrassed at right
    pov "That sounds like an amazing project! Why aren’t you more excited about it?"
    show pov confused at left
    show edw embarrassed_talk at right
    edw "I mean, its cool and all but until I can properly test it with some actual hardware it’s really only as good as the paper it was printed on, you know?"
    edw "Though to be fair, I always use heavy duty classic three ring binders and the fancy gloss printing paper for all of my project blueprints."
    show pov shocked at left
    show edw confused_talk at right
    edw "The one that costs an extra few bucks at the print shop."
    show pov shocked_talk at left
    show edw confused at right
    pov "Oooh, very fancy indeed, then."
    show pov shocked at left
    show edw confused_talk at right
    edw "Yeah, some of my assignments for class aren’t even as well presented."
    show pov shocked_talk at left
    show edw smirk at right
    pov "No kidding."
    show pov neutral_talk at left
    show edw confused at right
    pov "Back on topic though, how sure are you that this sort of thing could even work?"
    show pov confused at left
    show edw smirk_talk at right
    edw "Dude, who do you think you are talking to?"
    edw "If I planned it out, then I can make it work."
    show pov shocked at left
    show edw shocked_talk at right
    edw "Still though, even the headset at the mall is 900 bucks, so that would be a big dent in my monthly spending budget."
    show pov smirk at left
    show edw bored_talk at right
    edw "So unless I hit a dead end on all of my current projects or hit a creative block for a while, I ain’t gonna look into a headset for myself in a while."
    show edw smirk_talk at right
    edw "Why spend it all on just one project when you can instead divide your assets and tackle multiple projects at a time?"
    show pov confused_talk at left
    show edw smirk at right
    pov "I… guess I see your logic on it?"
    show pov neutral at left
    show edw neutral_talk at right
    edw "Good!"
    show pov embarrassed at left
    show edw smirk_talk at right
    edw "Now, since you are interested in my projects, how about I show you the one I’m currently working on?"
    show pov smirk_talk at left
    show edw smirk at right
    pov "As long as there isn’t a chance it explodes on me."
    show pov shocked at left
    show edw confused_talk at right
    edw "…"
    show pov embarrassed_talk at left
    show edw bored at right
    pov "…"
    show pov shocked at left
    show edw bored_talk at right
    edw "…"
    edw "I’ll see you later, then."
    show pov embarrassed_talk at left
    show edw bored at right
    pov "Yeah, see you, dude…"
    $ edward_vr_path = 2

    #=SCENE END=
    hide edw
    with fade
    jump lbl_schoolyard_day

label lbl_vr_buds:
    #[School yard, Morning- “VR Buds”  - edward_vr_path=2]

    #-Following scene happens after buying the VR headset from the mall for 500 bucks and interacting with Edward about Virtual Reality again-
    show pov smirk_talk at left
    show edw confused at right
    with dissolve
    pov "Hey, Edward, guess what!"
    show pov bored at left
    show edw smirk_talk at right
    edw "You found out about the simulation?"
    show pov bored_talk at left
    show edw smirk at right
    pov "No, I actually bought-"
    show pov shocked_talk at left
    pov "Wait, what about a simulation?"
    show pov shocked at left
    show edw shocked_talk at right
    edw "Nothing! Nothing, who said anything about a simulation?"
    show pov confused_talk at left
    show edw bored at right
    pov "But you just-"
    show pov confused at left
    show edw bored_talk at right
    edw "I have no memory of such a thing."
    show pov embarrassed at left
    show edw neutral_talk at right
    edw "What did you buy, [povname]?"
    show pov embarrassed_talk at left
    show edw shocked at right
    pov "I… I bought a VR headset."
    show pov embarrassed at left
    show edw shocked_talk at right
    edw "What?!"
    show pov neutral at left
    show edw neutral_talk at right
    edw "Dude that is awesome!"
    show pov neutral_talk at left
    show edw neutral at right
    pov "Yeah, I wanted to show it to you as soon as I got it!"
    show pov embarrassed_talk at left
    pov "Do you think you can give it the memory attachment thingie you were talking about last time?"
    show pov embarrassed at left
    show edw confused_talk at right
    edw "Wait, you want me to test my project on your headset?"
    show pov embarrassed_talk at left
    show edw confused at right
    pov "Yeah, I was on the fence about it at first but the idea of being able to look back into my memories in real time like you said sounds pretty awesome so I want to see it for myself!"
    show pov confused at left
    show edw confused_talk at right
    edw "Aren’t you worried I might break it?"
    show pov embarrassed at left
    show edw smirk_talk at right
    edw "I know this things are expensive man…"
    show pov embarrassed_talk at left
    show edw embarrassed at right
    pov "Well, I wouldn’t ask this of just anybody and who better out there to fix something broken than you, dude?"

    #(+1 Edward RP)
    $ add_points("edward_points",2)
    show pov neutral at left
    show edw embarrassed_talk at right
    edw "Aww, man. You are gonna make me tear up now."
    edw "Well, I have been more anxious about the project ever since we talked about it and honestly, from the way I am, it was a matter of time before I bought one just to scratch my inventor's itch."
    show pov neutral_talk at left
    show edw neutral at right
    pov "So, will you do it?"
    show pov embarrassed at left
    show edw bored_talk at right
    edw "Hmmm…"
    show pov shocked at left
    show edw bored_talk at right
    edw "Eh, what the hell?"
    show edw smirk_talk at right
    edw "If things don’t go as plan I can at least increase your headset’s resolution and storage capacity."
    edw "I can even do it in a way your warranty wouldn’t be void if something were to happen to it!"
    show pov neutral_talk at left
    show edw neutral at right
    pov "Awesome, can’t wait to test it out!"
    show pov neutral at left
    show edw neutral_talk at right
    edw "Neither do I, dude!"
    edw "I’ll have it ready in a couple of days; once I install it, test it and fine tune it to have everything working properly."
    show edw smirk_talk at right
    edw "I’ll get to work on it right away!"
    show pov neutral_talk at left
    show edw neutral at right
    pov "Alright, let me know when I can pick it up then."
    show pov embarrassed at left
    show edw smirk_talk at right
    edw "Sure thing, thanks for the opportunity, [povname]."
    edw "I won’t forget it."
    show pov neutral_talk at left
    show edw neutral at right
    pov "My pleasure, dude."
    show pov neutral at left
    show edw smirk_talk at right
    edw "Alright, I’ll get going with this, talk to you later!"
    show pov neutral_talk at left
    show edw neutral at right
    pov "Sure thing!"

    $ edward_vr_path = 3
    $ inventory.drop(Items.vrheadset)

    hide edw
    with fade
    jump lbl_schoolyard_day

    #-After this scene, the Virtual Reality topic becomes unavailable for 2 days while Edward works on the headset-

    #=SCENE END=

label lbl_memories_of_a_virtual_reality:

    #[School yard, Morning- “Memories of a Virtual Reality”  - edward_vr_path=3]

    #-This scene is available 2 days after giving Edward your VR headset and picking the Virtual Reality topic again-
    show pov neutral at left
    show edw smirk_talk at right
    with dissolve
    edw "Ah, [povname]!"
    edw "Just the bro I wanted to see!"
    show pov shocked at left
    show edw neutral_talk at right
    edw "Here I’m handing you your new and improved VR headset back!"
    show pov neutral_talk at left
    show edw neutral at right
    pov "Nice!"
    pov "Did you manage to make your thingy work?"
    show pov embarrassed at left
    show edw smirk_talk at right
    edw "Oh, it was even better than I initially imagined!"
    edw "That being said, the technology still has a lot of room for improvement."
    show pov embarrassed_talk at left
    show edw smirk at right
    pov "What do you mean?"
    show pov confused at left
    show edw bored_talk at right
    edw "Well, the original plan was to be able to see a selected memory you put your mind on in detail."
    edw "But despite my tinkering with it, it seems the device itself is stuck in only being able to relieve certain types of memories."
    show pov shocked at left
    show edw embarrassed_talk at right
    edw "It seems like the headset only responds to memories where a large amount of dopamine was released into our brain."
    show pov embarrassed at left
    show edw smirk_talk at right
    edw "Memories of great excitement, joy or pleasure to be precise."
    show pov confused_talk at left
    show edw confused at right
    pov "Why does it do that?"
    show pov shocked at left
    show edw confused_talk at right
    edw "Well, The device scans your brain and latches onto the subtle dopamine release you get upon visualizing a good memory in your head."
    edw "Then by an extremely detailed and technical wording filled process I’ll spare you the details on, basically helps your brain further visualize that memory and let you live through it."
    show pov embarrassed_talk at left
    show edw smirk at right
    pov "That sounds like a great success if you managed to even work to that point."
    show pov confused at left
    show edw smirk_talk at right
    edw "Yeah, but the original design is supposed to let you pick what specific memory you want to relieve, not just the happy ones."
    edw "So until I can get it to work exactly the way I envisioned, it’s back to the drawing board for me."
    show edw neutral_talk at right
    edw "Still, it’s better than nothing and I figure you’d like to experience it by yourself so I brought back to you."
    show pov embarrassed_talk at left
    show edw neutral at right
    pov "Thanks a lot, man."
    pov "I’m sorry it wasn’t everything you wanted though."
    show pov embarrassed at left
    show edw neutral_talk at right
    edw "Eh, that’s alright."
    edw "Besides, at the end of the day, the journey is much more fun than the destination."
    show pov neutral at left
    show edw embarrassed_talk at right
    edw "Plus, you helped me make progress on one of the projects that has been collecting dust in my pending projects bookshelf for quite a while now so I consider that a victory."
    show pov neutral_talk at left
    show edw embarrassed at right
    pov "Well, I’m glad you see it that way."
    show pov embarrassed at left
    show edw shocked at right
    pov "Anyway, do I owe you anything for this?"
    show pov confused at left
    show edw shocked_talk at right
    edw "Nope!"
    edw "This modification is 100%% free of charge."
    show pov embarrassed at left
    show edw neutral_talk at right
    edw "You payed for the whole headset off your pocket and even gave me the opportunity to tinker with it without me even asking you."
    edw "So you get this for free."
    show pov shocked_talk at left
    show edw neutral at right
    pov "Wow, thanks a lot, dude!"
    show pov embarrassed at left
    show edw neutral_talk at right
    edw "Don’t mention it!"
    show pov confused at left
    show edw shocked_talk at right
    edw "Fair warning though, the headset is designed to work indoors in a cool temperature room."
    show edw embarrassed_talk at right
    edw "And using it standing up can be quite disorienting when reliving a memory."
    show pov neutral at left
    show edw neutral_talk at right
    edw "So for best results, turn on the air conditioning and lay down in your room while using it."
    show pov neutral_talk at left
    show edw neutral at right
    pov "Alright, I’ll keep it in mind."
    show pov neutral at left
    show edw neutral_talk at right
    edw "Once it’s on, just concentrate on the specific memory you want to relieve and let the thing do its magic."
    show pov smirk_talk at left
    show edw neutral at right
    pov "You got it, dude. Again, thanks a lot for this."
    show pov smirk at left
    show edw neutral_talk at right
    edw "Nah, man. Thank you for the opportunity."
    show pov confused_talk at left
    show edw neutral at right
    pov "Say, what memories did you relive?"
    show pov confused at left
    show edw embarrassed_talk at right
    edw "Well… Promise not to laugh?"
    show pov neutral_talk at left
    show edw embarrassed_talk at right
    pov "You got my word."
    show pov confused at left
    show edw embarrassed_talk at right
    edw "It’s a bit embarrassing to say it, but…"
    edw "I visualized my times with my grandpa when he first taught me how to use power tools."
    show pov embarrassed at left
    show edw neutral_talk at right
    edw "He is one of the reasons I am who I am today. And I miss him every day."
    show pov embarrassed_talk at left
    show edw neutral at right
    pov "Wow, that's… surprisingly sweet."
    pov "I’m sure he was an awesome grandpa."
    show pov embarrassed at left
    show edw neutral_talk at right
    edw "He really, really was…"
    edw "After that, I visualize the first time I saw a sex bot on display on a robotics convention!"
    show edw embarrassed_talk at right
    edw "I had just turned 18 and the design of that beautiful chrome minx shall forever live rent-free in my memory. And seeing her live again was an engineer’s wet dream for sure!"
    show pov neutral_talk at left
    show edw embarrassed at right
    pov "And the tender moment is gone - thanks for that."
    show pov neutral at left
    show edw embarrassed_talk at right
    edw "It was really special for me, OK?!"
    show edw neutral_talk at right
    edw "Anyway, let me know how you like it once you test it out."
    edw "I have to get back to my other projects."
    show pov neutral_talk at left
    show edw neutral at right
    pov "I sure will, dude. Thanks again!"
    show pov neutral at left
    show edw smirk_talk at right
    edw "Not a problem, dude. See you later."
    show pov smirk_talk at left
    show edw smirk at right
    pov "Later, Edward!"

    $ inventory.add(Items.vrheadsetmod)
    $ vrheadset_chest = 1
    $ edward_vr_path = 6
    $ inventory.add(Items.vrheadsetmod)
    $ vrheadset_chest = 1
    $ edward_vr_path = 6

    #=SCENE END=
    hide edw
    with fade
    jump lbl_schoolyard_day
