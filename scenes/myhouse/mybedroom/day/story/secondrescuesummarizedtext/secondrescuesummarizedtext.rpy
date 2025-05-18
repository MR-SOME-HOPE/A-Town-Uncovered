## Second Rescue Summarized Text
label lbl_second_rescue_summarized_text:
    # The next morning, you get a text from Edward telling you to meet up at the hideout, Effie is there and there’s things that need discussing.
    scene bg secondrescuesummarizedtext_1
    with fade

    edw "Dude, meet up at HQ. Effie and Jacob are here too."
    edw "Did you sleep well?"
    edw "Sorry, Jacob sent that."


    $ main_story = 140.1

    jump lbl_mybedroom_day_setup
