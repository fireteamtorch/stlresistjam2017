label Day2Block:
    scene black
    with dissolve

    play music "jingle_dayTitleDenoise.wav" noloop

    #image top_text = ParameterizedText(text = "Week 1\n\nNew Faces", xalign=0.5, yalign=0.0, text_size = 80)

    #show text "Week 1\nNew Faces" at truecenter with text_size = 80
    show text "{size=90}Week 2{/size}" at Transform(xalign = 0.5, yalign = 0.45) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "{size=70}A Night to Remember{/size}" at Transform(xalign = 0.5, yalign = 0.55) as text2
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

    #play music "noir_v002_lpf_LOOPedit.wav"
    play music "lux_v001_lpf_LOOPedit.wav" fadein 1.0

    #show charles sit at Seat1

    "The door opens, and Charles comes in, waving a rolled up newspaper."

    show charles smile at Seat2
    with Dissolve(disFactor)

    charles "Extra, extra! Read all about it! Beloved local diner now open on Friday nights. According to reliable sources, the drinks there are out of this world."

    show charles explain at Seat5
    with Dissolve(disFactor)

    "Charles sits down with a wide grin."

    bartender "Thanks for setting up the ads."

    show charles sit lookRight at Seat5
    with Dissolve(disFactor)

    charles "Told you it wouldn't cost you much. Let me order... the same thing."

    bartender "Well done steak and broccoli?"

    show charles sit lookLeft at Seat5
    with Dissolve(disFactor)

    charles "And a whisky sour."

    show charles sit lookRight at Seat5
    with Dissolve(disFactor)

    "Charles pulls out a large notebook, and begins intermittently jotting things down."

    "The door opens, and a young woman in her early twenties enters the bar, wearing a large backpack."

    show claire sit at Seat2
    with Dissolve(disFactor)

    "Without saying a word, she sets up her laptop and starts typing rapidly, the crisp clicking drowning out all other conversations."
    
    "Upon seeing your smile, she softens her keystrokes, but maintains her pace."
    
    show claire look player at Seat2
    with Dissolve(disFactor)

    claire "Oh, do you guys have wifi?"
    
    bartender "Sure do."

    show  claire happy at Seat2
    with Dissolve(disFactor)

    claire "Awesome!  ...What's the password?"

    bartender "'Youhavetobuyadrink.'"

    show claire look left at Seat2
    with Dissolve(disFactor)

    claire "Oh... um, rum and coke?"

    bartender "All righty."

    #show claire look player at Seat2
    show claire look player at Seat2
    with Dissolve(disFactor)
    
    "Claire looks at you with her eyes wide as you make the drink."

    show  claire happy at Seat2
    with Dissolve(disFactor)
    
    claire "Sooo... what's the pass?"

    show claire look left at Seat2
    with Dissolve(disFactor)
    
    bartender "'Youhavetobuyadrink.'"

    show claire look player at Seat2
    with Dissolve(disFactor)
    
    claire "But I al-"

    bartender "All lowercase."

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
    
    "Claire continues to type while humming softly, occasionally sipping on her rum and coke."

    #scene black
    #with dissolve

    #"The rest of the evening was pretty empty."

    "After a while, a police officer in her early thirties enters, and upon seeing Charles, sits down next to him."

    show elysia sit lookLeft at Seat4
    show charles sit lookLeft at Seat5
    with Dissolve(disFactor)

    charles "Hey, Elysia."

    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    elysia "Charles."

    show  charles smile at Seat5
    with Dissolve(disFactor)

    "Charles turns to you with a smile."

    charles "See? Told you everyone reads the papers."

    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "Where's Jens?"

    show elysia sit lookRight at Seat4
    show charles sit lookLeft at Seat5
    with Dissolve(disFactor)

    charles "Eloped with his fiancé, probably to some tropical paradise."

    show elysia smile lookRight at Seat4
    with Dissolve(disFactor)

    elysia "Luckyyyyy."

    show  charles smile at Seat5
    charles "This is his sibling who's taking over for a few weeks."

    show elysia smile lookPlayer at Seat4
    with Dissolve(disFactor)

    elysia "Nice to meet ya. You from out of town?"

    show charles sit lookRight at Seat5
    bartender "Yeah, I worked as a bartender up in DC."

    show elysia smile lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "Cool, big city. They probably all drink fancy mixed drinks up there, huh? Probably with fancy names like The Presidential Special, or something like that."

    show elysia smile lookPlayer at Seat4
    with Dissolve(disFactor)

    bartender "That's not a bad name for a drink, to be honest. But people usually just order beer or just pick out drinks at random because they like the name."

    show claire happy player at Seat2
    with Dissolve(disFactor)

    "Claire signals that she would like another rum and coke, which you serve while maintaining conversation."

    stop music fadeout 2.0

    scene black
    with dissolve

    show text "Outside the bar, daylight fades away completely as evening turns to late night." at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_te
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    play music "noir_v002_lpf_LOOPedit.wav" fadein 1.0

    scene bgBarNight

    show bgCounterTop
    with dissolve

    #"Outside the bar, daylight fades away completely as evening turns to late night."

    show claire happy player at Seat2
    show charles sit at Seat5
    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    "Claire exits after leaving a generous tip."

    hide claire sit
    with Dissolve(disFactor)


    "One of the patrons who frequents the diner during the day, Braxton, sits down at the bar. Elysia and Charles are engaged in a political debate."

    show braxton sit lookRight at Seat1
    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    elysia "Charles, you realize every single person who runs for office promises to 'cut taxes,' right? It's all bullshit."

    show charles sit lookLeft at Seat5
    charles "All I'm saying is that we should keep an open mind."

    elysia "I just want to know your opinion."

    show charles sit lookRight at Seat5
    charles "I'm a journalist. I have no opinions."

    show elysia closed at Seat4
    with Dissolve(disFactor)

    elysia "..."

    show charles smile at Seat5
    charles "I mean, I have no biases."

    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    elysia "So what's your opinion...?"

    show braxton sit lookLeft at Seat2
    show elysia closed at Seat4
    show frank sit beer lookRight at Seat1
    show charles sit lookLeft at Seat5
    with Dissolve(disFactor)

    "Frank enters, and quickly orders a beer."

    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    elysia "I mean, what's up with the immigration policy? Deporting people doing jobs we wouldn't do."

    show frank sit beer lookRight at Seat1
    show braxton sit lookLeft at Seat2
    show charles sit lookLeft at Seat5
    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    frank "*whisper* Dey tookk our jerrrbbbbs."

    show frank smile beer at Seat1
    show braxton smile at Seat2
    show elysia closed at Seat4
    with Dissolve(disFactor)

    "Braxton chuckles and smiles at Frank."

    show braxton sit lookLeft at Seat2
    show charles explain at Seat5
    with Dissolve(disFactor)

    charles "I'm sure some people would."

    show elysia sit lookRight at Seat4
    show braxton sit lookRight at Seat2
    show frank sit lookRight at Seat1
    with Dissolve(disFactor)

    elysia "Who? Name one person we know."

    show charles sit lookRight at Seat5

    charles "Let's just wait and see. I'm sure it's not that bad."

    show elysia closed at Seat4

    "Elysia sighs but declines pressing the issue further."

    show frank sit lookRight at Seat1
    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    frank "How's work, Braxton?" 

    show  braxton sit lookLeft at Seat2
    show frank sit beer lookRight at Seat1
    with Dissolve(disFactor)

    braxton "Not bad. I'm still alive."

    show frank smile beer at Seat1
    with Dissolve(disFactor)

    frank "Barely."

    show frank sit beer lookRight at Seat1
    with Dissolve(disFactor)

    braxton "Not easy dealing with young kids all day."

    show frank drunk at Seat1
    with Dissolve(disFactor)

    frank "Doesn't get easier when they grow older, either."

    "Frank takes a long sip."

    show braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    frank "Out of the house and still give me headaches."

    show braxton sit lookRight at Seat2
    with Dissolve(disFactor)

    braxton "Try teaching the works of Shakespeare to kids in this day and age."

    show frank drunk at Seat1
    with Dissolve(disFactor)

    frank "That's literally the worst thing I've heard all day."

    show braxton smile lookLeft at Seat2
    show charles sit lookLeft at Seat5
    with Dissolve(disFactor)

    braxton "'Literally' literally? Legitimately zero things worse?"

    show braxton smile lookLeft at Seat2
    show frank drunk angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "Oh, stop."

    show frank drunk at Seat1
    show braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    "The two of them fall quiet as on the right side of the bar, Charles begins loudly describing his latest book idea."

    show elysia sit lookRight at Seat4
    show charles smile at Seat5
    with Dissolve(disFactor)

    charles "And that's when she discovered that the boy, who creepily stared at her all this time, isn't a normal boy!"

    show elysia smile lookRight at Seat4
    show charles sit lookLeft at Seat5
    with Dissolve(disFactor)

    elysia "Let me guess, he's a vampire?"

    show charles smile at Seat5
    charles "Yeah!"

    show frank drunk angry lookRight at Seat1
    show braxton sit lookRight at Seat2
    show charles explain at Seat5
    with Dissolve(disFactor)
    "All of the patrons turn to look at Charles."

    braxton "That's pretty much {i}Twilight{/i}... and literally the wors-"

    show frank smile beer at Seat1
    with Dissolve(disFactor)

    frank "'Literally' literally-?"

    show braxton angry at Seat2
    with Dissolve(disFactor)

    braxton "Stop."

    show frank beer smile at Seat1
    with Dissolve(disFactor)

    frank "*whisper* Team Jacob."

    show braxton sit lookLeft at Seat2
    show frank drunk at Seat1
    show elysia closed at Seat4
    show charles sit lookRight at Seat5
    with Dissolve(disFactor)

    elysia "Oh, God. Yeah, Charles, don't write that..."

    show charles explain at Seat5

    charles "But my story has a robot in it...  a robot..."

    show elysia sit lookRight at Seat4
    show frank drunk angry lookLeft at Seat1
    show charles sit lookLeft at Seat5
    with Dissolve(disFactor)

    frank "Hey! Lemme get another beer."

    show elysia sit lookLeft at Seat4
    show braxton sit lookPlayer at Seat2
    with Dissolve(disFactor)

    braxton "No, this is definitely the time to cut him off."

    show elysia sit lookLeft at Seat4

    bartender "Hmm..."

    menu:
        "'Fine, Frank, here's another beer.'":
            #show text "" at truecenter
            show frank beer smile at Seat1
            show elysia sit lookLeft at Seat4
            show braxton sit lookLeft at Seat2
            with Dissolve(disFactor)
            frank "That's right! Come to Papa!"
            #show text "Frank will remember this..." at truecenter
            #with dissolve
            #"This is the result of the user choosing choice 1"
        "'Nope, Frank, I'm going to cut you off.'":
            show frank drunk angry lookRight at Seat1
            show elysia sit lookLeft at Seat4
            show braxton sit lookLeft at Seat2
            with Dissolve(disFactor)
            frank "Aww, I haven't had THAT many drinks..."
            #show text "" at truecenter
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

    pause 0.2

    scene black
    with dissolve

    "Before you even realized it, it was closing time."


    stop music fadeout 1.0
    pause 1
    show text "{size=70}End of Day{/size}" at truecenter as text3
    with dissolve
    play music "jingle_endOfDayDenoise.wav" noloop
    pause 2
    hide text3
    with dissolve
    pause 1


    jump Day3Block

return