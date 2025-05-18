label lbl_meet_hazel:
    #GeeSeki Note: Uni-aged chick that works at the sex shop."
    #She’s semi-social media famous, having about 60k followers on Instagram (or whatever the ATU version of that is called)."."." *currently looking* Instantgram."
    #She’s always on her phone doing social media work to grow her brand but to a point where she’s rude to people talking to her." She’s got a pretty ghetto speech pattern and mannerisms."
    #Although can be introduced by Sister in Sister’s side story, introduce her as if the player hasn’t gotten to that part yet."
    show pov neutral at left
    with dissolve
    show haz neutral_talk at right
    call lbl_adultstore_counter_check
    with dissolve

    idk "Hey, sweetie. How can I help you?"
    show pov embarrassed_talk at left
    show haz neutral at right
    pov "Hi, I’m just… perusing."
    show pov embarrassed at left
    show haz smirk_talk at right
    idk "First time in a sex store?"
    show pov embarrassed_talk at left
    show haz neutral at right
    pov "O-oh! Is that what this is? Hehehe…"
    pov "Of course I’ve been in a sex store before, what makes you think I haven’t?"
    show pov embarrassed at left
    show haz smirk_talk at right
    idk "You’re blushing."
    show pov embarrassed at left
    show haz confused_talk at right
    idk "Are you sure you should be in here? How old are you?"
    show pov embarrassed_talk at left
    show haz neutral at right
    pov "Old enough."
    show pov embarrassed at left
    show haz neutral_talk at right
    idk "I’ll take your word on it, but if anyone gets in trouble about this, it’s definitely you."
    show pov embarrassed_talk at left
    show haz confused at right
    pov "I’d be worried if I was underaged but I’m not so therefore I’m not worried."
    show pov embarrassed at left
    show haz confused_talk at right
    idk "You’re a weird one, aren’t you?"
    idk "I haven’t seen you around before."
    show pov neutral_talk at left
    show haz neutral at right
    pov "Yeah, we just moved in not too long ago. A friend of mine invited me to the comic book store and I was just curious as to what this place was."
    show pov embarrassed_talk at left
    show haz smirk at right
    pov "The front doesn’t really give anything away."
    show pov embarrassed at left
    show haz smirk_talk at right
    idk "One could say that but another would say that the front gives more than enough hints away."
    show pov confused at left
    show haz neutral_talk at right
    haz "I’m Hazel, if you don’t recognize me."
    show pov confused_talk at left
    show haz neutral at right
    pov "I’m [povname]."
    pov "Should I recognize you?"
    show pov confused at left
    show haz neutral_talk at right
    haz "Well, I highly doubt you would but I’ve had rare occasions of people knowing who I was."
    show pov neutral_talk at left
    show haz neutral at right
    pov "Are you- famous?"
    show pov smirk at left
    show haz smirk_talk at right
    haz "Only if you think 60,000 followers on Instantgram is considered ‘famous’."
    show pov embarrassed at left
    show haz angry_talk at right
    haz "Don’t answer that."
    show pov neutral_talk at left
    show haz neutral at right
    pov "Whoa, hey, that’s not all bad. I know thousands of girls who would kill for 10,000 followers."
    show pov sad_talk at left
    show haz sad at right
    pov "Knowing the internet and social media, I wouldn’t be surprised if someone actually would kill for 10,000 followers."
    show pov neutral at left
    show haz bored_talk at right
    haz "We’re not at that stage of desperate yet, almost though, give it another 5 years."
    show pov embarrassed_talk at left
    show haz neutral at right
    pov "Anyway, I gotta head out. Nice chatting with you, Hazel."
    show pov neutral at left
    show haz neutral_talk at right
    haz "Ditto, [povname]. Hope to see you around often, honey."
    haz "And I’m not saying that because I want you to buy something."
    show pov smirk at left
    show haz smirk_talk at right
    haz "Okay- maybe a little."
    show pov embarrassed at left
    show haz embarrassed_talk at right
    haz "That came out wrong."
    show pov neutral at left
    show haz neutral_talk at right
    haz "Bye!"
    $ hazel_path = 1
    $ add_contact("Hazel")
    pause 0.1
    jump lbl_adultstore_day_setup
