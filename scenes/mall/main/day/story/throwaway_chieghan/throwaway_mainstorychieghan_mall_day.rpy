## Chieghan Main Story Throwaway Conversations Mall ##

## Sex Around Town Chieghan Mall
label lbl_mall_day_chieghan_sexworld:
    if sexaroundtownchieghan == 0:
        show pov embarrassed_talk at left
        with dissolve
        hide btn_schoolbathroom_day_chieghansexworld_idle2
        show chisw neutral at right
        with dissolve
        pov "Heeeey... Chieghan..."
        show chisw confused at right
        pov "What's the special ocassion?"
        show pov embarrassed at left
        show chisw neutral_talk at right
        chi "We just like bubble tea."
        show pov sad_talk at left
        show chisw smirk at right
        pov "No, I mean. Why is everyone around town having sex in public?"
        show pov embarrassed at left
        show chisw neutral_talk at right
        chi "Ahahaha! You're so funny, [povname]!"
        show pov confused at left
        show chisw smirk_talk at right
        chi "You say such weird things."
        show chisw neutral at right
        chi "..."
        show pov confused_talk at left
        show chisw confused at right
        pov "What's so funny?"
        show pov bored at left
        show chisw neutral_talk at right
        chi "You are, [povname]-ssi."
        show pov confused at left
        show chisw embarrassed_talk at right
        chi "I enjoy our talking."
        show pov embarrassed at left
        chi "You are nice to me when other people are being assholes."
        chi "I have good friends like Meghan and Teghan, so I am very lucky."
        show pov embarrassed_talk at left
        show chisw confused at right
        pov "This conversation went a totally different direction."
        show pov confused at left
        show chisw confused_talk at right
        chi "What is 'direction'?"
        show pov confused_talk at left
        show chisw confused at right
        pov "It's like- a way?"
        show pov embarrassed at left
        show chisw confused_talk at right
        chi "Away...?"
        show chisw smirk_talk at right
        chi "So it's like, I say to the mean bitches, 'go direc-tion?'"
        show pov embarrassed_talk at left
        show chisw confused at right
        pov "Um... no, nevermind. I'll go ask someone else."
        show pov embarrassed at left
        show chisw neutral_talk at right
        chi "I am so confused. Bye, [povname]-ssi."

        $ sexaroundtownchieghan = 1

        jump lbl_mall_day

    else:
        show pov embarrassed at left
        with dissolve
        hide btn_mall_day_chieghansexworld_idle2
        show chisw neutral_talk at right
        with dissolve
        chi "Hi, [povname]."
        show chisw confused_talk at right
        chi "You're sweating a lot. Get some water."
        show pov embarrassed_talk at left
        show chisw confused at right
        pov "Yeah, I will, it's just uh- there's a lot to take in."
        show pov bored at left
        show chisw confused_talk at right
        chi "Yeah, you need to definitely take in a lot of water."

        jump lbl_mall_day
