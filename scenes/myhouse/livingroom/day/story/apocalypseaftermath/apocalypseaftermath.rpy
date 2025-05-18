## Apocalypse Aftermath
label lbl_apocalypse_aftermath:
    scene bg apocalypseaftermath_1
    with fade

    news "Today marks exactly one month since the devastating explosion at The Robot Company, also known as TRC."
    news "The tragic event, which claimed the lives of two people—TRC’s CEO Eloise Lashley and one of its employees, Henry Smith—left a deep impact on our community." 
    show bg apocalypseaftermath_2
    news "Smith, a father and hardworking man, and Lashley, a visionary leader, will both be remembered for their contributions to this town."
    news "The explosion not only caused loss of life but also triggered a shockwave that damaged several nearby buildings. "
    news "The tremor was felt throughout the town, but in the wake of the disaster, our community rallied together for a swift cleanup. "
    news "Today, the recovery process has been completed, and the town has returned to normal."

    show bg apocalypseaftermath_1
    news "And in another major development, TRC has officially reopened its doors for business."
    news "Despite the tragedy and the damage caused, the company is once again operational, with a new leadership team stepping in to steer the way forward." 
    news "This reopening is a significant milestone, as it symbolizes both recovery and resilience."

    news "We’ll continue to monitor the progress of TRC in the coming weeks. "
    news "For now, the focus remains on rebuilding and honoring those we lost."

    news "Thank you for tuning in. Stay with us for more on this story and other updates."

    scene black
    with fade

    $ main_story = 133

    jump lbl_the_aftermath_at_home
