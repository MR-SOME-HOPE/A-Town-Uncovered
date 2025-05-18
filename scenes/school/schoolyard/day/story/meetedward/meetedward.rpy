label lbl_meet_edward:
    #GeeSeki Note: Think of Data from the Goonies, but not fresh off the boat."
    #A real smarty-pants, inventor kinda guy."
    #Think of other popular inventors in pop culture, Robin Williams in flubber, detective gadget, that’s literally all I can think of atm."
    show btn schoolyard_day_edward_idle
    $ renpy.pause(0.001)

    #-you approach a timid looking dude looking into a device-
    show pov shocked at left
    with dissolve
    hide btn schoolyard_day_edward_idle
    show edw shocked_talk at right
    with dissolve
    edw "Woah, stay right where you are!"
    edw "Don’t move a muscle!"
    show pov confused_talk at left
    show edw confused at right
    pov "W-What?"
    show pov confused at left
    show edw neutral_talk at right
    edw "Relax, I need you to stay still for a moment while the analyzer does its job, ok?"
    edw "I am detecting some very high readings off from you."
    show pov confused_talk at left
    show edw confused at right
    pov "Readings? What Kind of readings?"
    show pov confused at left
    show edw neutral_talk at right
    edw "I am not sure, I haven’t figured out what this device reads to begin with but it’s going off the charts with you!"
    show pov smirk_talk at left
    show edw neutral at right
    pov "You built a scanner that you are not even sure what it scans?"
    pov "What could be scanning off me?"
    show pov bored at left
    show edw neutral_talk at right
    edw "Anything - from metal, to lies, to lethal doses of radiation."
    show pov confused_talk at left
    show edw bored at right
    pov "What was that last one?!"

    #-The device makes several noises before finally powering down-
    show pov confused at left
    show edw angry_talk at right
    edw "Ugh, worthless piece of junk!"
    show pov confused at left
    show edw neutral_talk at right
    edw "Well, whatever you are emitting, completely shatters anything I have pointed this thing onto."
    show pov confused_talk at left
    show edw angry at right
    pov "Do you always greet people by pointing random electronic goobers into their faces?"
    show pov bored at left
    show edw angry_talk at right
    edw "It’s not a goober; it's a gizmo."
    show pov bored_talk at left
    show edw bored at right
    pov "That doesn’t answer my question."
    show pov bored at left
    show edw bored_talk at right
    edw "Nor does it have to."
    edw "Anyway, you are the new kid, right?"
    show pov bored_talk at left
    show edw bored at right
    pov "Gee, what gave it away?"
    show pov sad at left
    show edw sad_talk at right
    edw "The fact you didn’t immediately; turn me away, call me a creep, told me to scram, or punched me in the face."
    show pov embarrassed_talk at left
    show edw neutral at right
    pov "I definitely wasn’t planning to."
    show pov neutral at left
    show edw neutral_talk at right
    edw "I like you!"
    edw "Edward’s the name - and building Gizmo’s is my game!"
    show pov neutral_talk at left
    show edw neutral at right
    pov "I’m [povname]. Nice to meet you."
    pov "So you build stuff?"
    show pov neutral at left
    show edw neutral_talk at right
    edw "Yep! From R/C cars with 4k hd cameras you can control from a smartphone, to installing solar panels in your roof - or even programming the clock in an old vcr."
    edw "If it’s got buttons, moving parts, cables, chips, or electronics; I am all over it."
    show pov smirk_talk at left
    show edw smirk at right
    pov "Do I want to imagine what you do with those R/C cameras?"
    show pov smirk at left
    show edw smirk_talk at right
    edw "Hey, I am an inventor and visionary; not a saint."
    show pov smirk_talk at left
    show edw neutral at right
    pov "Fair enough, I guess."
    show pov confused_talk at left
    show edw neutral at right
    pov "So what exactly does that ‘gizmo’ of yours do?"
    show pov confused at left
    show edw confused_talk at right
    edw "I told you, man: beats me."
    edw "Originally I designed it to be a toaster; but then it started reading things, so I made it into a scanner."
    show pov bored_talk at left
    show edw bored at right
    pov "Seems like the natural course of events, yes."
    show pov confused at left
    show edw sad_talk at right
    edw "Anyway, the thing fried -reading whatever it is you are transmitting- so I better go repair it now."
    edw "You don’t have any magnets, metals, or lethal amounts of plutonium on you, right?"
    show pov bored_talk at left
    show edw neutral at right
    pov "Not that I know of."
    show pov confused at left
    show edw neutral_talk at right
    edw "Good! That’s three things off the list of candidates."
    edw "Talk to you later, [povname]!"
    show pov neutral_talk at left
    show edw neutral at right
    pov "Uh, yeah! See you later, Edward…"

    #-Edward Leaves-
    hide edw
    show pov confused at left
    pov "…"
    show pov confused_talk at left
    pov "What just happened?"
    $ edward_path = 1
    $ add_contact("Edward")
    pause 0.2
    jump lbl_schoolyard_day_setup
