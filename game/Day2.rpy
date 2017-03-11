label Day2Block:
    scene black
    with dissolve

    play music "tempDayTitleShortestDeNoise.mp3" noloop

    #image top_text = ParameterizedText(text = "Week 1\n\nNew Faces", xalign=0.5, yalign=0.0, text_size = 80)

    #show text "Week 1\nNew Faces" at truecenter with text_size = 80
    show text "Week 2" at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "A night to remember" at Transform(xalign = 0.5, yalign = 0.53) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    scene bgBarDay
    #with dissolve
    #scene bgBarNight

    show bgCounterTop
    with dissolve

    play music "noir_v002_lpf_LOOPedit.wav"

    #show charles sit at Seat1

    "The door opens, and Charles comes in, waving a rolled up newspaper."

    show charles sit at Seat2

    charles "Extra extra, read all about it. Beloved local diner now open on Friday nights. According to reliable sources, the drinks there are out of this world."

    show charles sit at Seat5

    "Charles sits down with a wide grin."

    bartender "Thanks for setting up the ads."

    charles "Told you it wouldn't cost you much. Let me order... the same thing."

    bartender "Well done steak and broccoli?"

    charles "And a whiskysour."

    "Charles pulls out a large notebook, and began intermittently jotting things down."


    "The door opens, and a young woman in her early 20's enters the bar, a large backpack behind her back."

    show claire sit at Seat2
    with Dissolve(disFactor)

    "Without saying a word, she setup her laptop and starts typing rapidly, the crisp clicking drowning out all other conversations. Upon seeing your smile, she softens her keystrokes, but maintains her pace."
    
    show claire look player at Seat2
    with Dissolve(disFactor)

    claire "Oh, do you guys have Wifi?"
    
    bartender "Sure do."

    show  claire happy at Seat2
    with Dissolve(disFactor)

    claire "Awesome!  ...What's the password?"

    bartender "Youhavetobuyadrink."

    show claire look left at Seat2
    with Dissolve(disFactor)

    claire "Oh... erm Rum and Coke?"

    bartender "Alrighty."

    #show claire look player at Seat2
    show claire look player at Seat2
    with Dissolve(disFactor)
    
    "Claire looks at you with her eyes wide as you make the drink."

    show  claire happy at Seat2
    with Dissolve(disFactor)
    
    claire "Sooo... what's the pass?"

    show claire look left at Seat2
    with Dissolve(disFactor)
    
    bartender "Youhavetobuyadrink."

    show claire look player at Seat2
    with Dissolve(disFactor)
    
    claire "but I al-"

    bartender "All lower case."

    show  claire happy at Seat2
    with Dissolve(disFactor)
    
    claire "Oh...  ohhhh."

    show claire sit at Seat2
    with Dissolve(disFactor)
    
    "Claire makes a clicking noise of acknowledgement."

    show claire happy player at Seat2
    with Dissolve(disFactor)
    
    claire "ICWhatUDidThar."

    show  claire happy at Seat2
    with Dissolve(disFactor)
    
    "Claire continues to type while humming softly, occasionally sipping on her Rum and Coke."

    #scene black
    #with dissolve

    #"The rest of the evening was pretty empty."

    "After a while, a police officer in her early 30s enters, and upon seeing Charles, sits down next to him."

    show elysia sit at Seat4

    charles "Hey Elysia."

    elysia "Charles."

    "Charles turns to you with a smile."

    charles "See? Told you everyone reads the papers."

    elysia "Where's Jens?"

    charles "Eloped with his fiance probably to some tropical paradise."

    elysia "Luckyyyyy."

    charles "This is his cousin who's taking over for a few weeks."

    elysia "Nice to meet ya. You from out of town?"

    bartender "Yeah, I worked as a bartender up in DC."

    elysia "Cool, big city. They probably all drink fancy mixed drinks up there huh? Probably with fancy names like The Presidential Special, or something like that."

    bartender "That's not a bad name for a drink to be honest. But people usually just order beer or just pick out drinks at random because they like the name."

    "Claire signals that she would like another Rum and Coke, which you serves while maintaining conversation."

    "Outside the bar, daylight fades away completely as evening turns to night."

    "Claire exits after leaving a generous tip."

    hide claire sit
    with Dissolve(disFactor)


    "One of the patrons, Braxton, that frequents the diner during the day sits down at the bar, while Elysia and Charles engaged in a political debate."

    show braxton sit lookRight at Seat1
    with Dissolve(disFactor)

    elysia "Charles, you realize every single person who runs for office promises to 'cut taxes' right? It's all bullshit."

    charles "All I'm saying, is that we should keep an open-mind."

    elysia "I just want to know your opinion."

    charles "I'm a journalist, I have no opinions."

    elysia "..."

    charles "I mean I have no biases."

    elysia "So what's your opinion..."

    show braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    show frank sit at Seat1
    with Dissolve(disFactor)

    "Frank enters, and quickly orders a beer."

    elysia "I mean what's up with the immigration policy. Deporting people doing jobs we wouldn't do."

    frank "*Whisper* Dey tookk our jerrrbbbbs."

    show braxton smile at Seat2
    with Dissolve(disFactor)

    "Braxton chuckles and smiles at Frank."

    show braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    charles "I'm sure some people would."

    elysia "Who? Name one person we know."

    charles "Let's just wait and see, I'm sure it's not that bad."

    "Elysia sighs but declined pressing the issue further."

    show frank sit lookRight at Seat1
    with Dissolve(disFactor)

    frank "How's work Braxton?" 

    show  braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    braxton "Not bad. I'm still alive."

    frank "Barely."

    braxton "Not easy dealing with young kids all day."

    frank "Doesn't get easier when they grow older either."

    "Frank takes a long sip."

    show braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    frank "Out of the house and still give me headaches."

    show braxton sit lookRight at Seat2
    with Dissolve(disFactor)

    braxton "Try teaching the works of Shakespeare to kids in this day and age."

    frank "That's literally the worst thing I've heard all day."

    braxton " 'Literally' literally? Legitimately zero things worse?"

    show frank drunk angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "Oh stop."

    show frank drunk at Seat1
    with Dissolve(disFactor)

    "The two of them fell quiet as on the right side of the bar, Charles begins loudly describing his latest book idea."

    charles "And that's when she discovered that the boy who creepily stared at her all this time, isn't a normal boy!"

    elysia "Let me guess, he's a vampire?"

    charles "Yeah!"

    show  frank drunk angry lookRight at Seat1
    show  braxton sit lookRight at Seat2
    with Dissolve(disFactor)
    "All the patrons turns to look at Charles."

    braxton "That's pretty much Twilight... and literally the wors-"

    show  frank smile beer at Seat1
    with Dissolve(disFactor)

    frank " 'Literally' Literally?-"

    show  braxton angry at Seat2
    with Dissolve(disFactor)

    braxton "Stop."

    show frank beer smile at Seat1
    with Dissolve(disFactor)

    frank "*Whisper* Team Jacob."

    show braxton sit lookLeft at Seat2
    show frank drunk at Seat1
    with Dissolve(disFactor)

    elysia "Oh god. Yeah, Charles don't write that..."

    charles "But my story has a robot in it...  a robot..."

    show  frank drunk angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "Hey! Lemme get another beer."

    show  braxton sit lookPlayer at Seat2
    with Dissolve(disFactor)

    braxton "No, this is definitely the time to cut him off."

    bartender "Hmm..."

    menu:
        "'Fine Frank, here's another beer'":
            show text "" at truecenter
            show frank beer smile at Seat1
            with Dissolve(disFactor)
            frank "That's right! Come to papa!"
            #show text "Frank will remember this..." at truecenter
            #with dissolve
            #"This is the result of the user choosing choice 1"
        "'Nope Frank, I'm going to cut you off'":
            show frank drunk angry lookRight at Seat1
            with Dissolve(disFactor)
            frank "Aww, I've not had THAT many drinks..."
            show text "" at truecenter
            #"This is the result of the user choosing the second choice."
    show text "Frank will remember this..." at truecenter
    with dissolve
    
    pause 1.5
    
    frank "No I won't..."
    
    hide text "Frank will remember this..." at truecenter
    with Dissolve(0.2)

    show text "Or maybe not..."
    with dissolve

    pause 1.5

    hide text "Or maybe not..."
    with Dissolve(0.2)

    "Before you even realized it, it was closing time."

return