
label Day1Block:
    scene black
    with dissolve

    play music "jingle_dayTitleDenoise.wav" noloop

    #image top_text = ParameterizedText(text = "Week 1\n\nNew Faces", xalign=0.5, yalign=0.0, text_size = 80)

    #show text "Week 1\nNew Faces" at truecenter with text_size = 80
    show text "{size=90}Week 1{/size}" at Transform(xalign = 0.5, yalign = 0.45) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "{size=70}New Faces{/size}" at Transform(xalign = 0.5, yalign = 0.55) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    #show charles sit at Seat1
    #show claire sit at Seat4
    #show frank sit at Seat2
    scene bgBarDay

    show bgCounterTop
    with dissolve

    #play music "noir_test_v001_lowpassEQ.mp3"
    #play music "noir_v002_lpf_LOOPedit.wav"
    play music "lux_v001_lpf_LOOPedit.wav" fadein 1.0

    "Well, Jens did it again..."
    "Went off somewhere fun and made you be the responsible one."
    bartender "Oh well, might as well put my skills to use."
    "..."   
    "......"
    "Hmmm... maybe you should've told someone the diner's now open Friday nights too..."
    bartender "I guess I'll leave the lights on, see if anyone comes by..."
    "..."
    "A few hours pass..."

    scene black
    with dissolve

    show text "Late night..." at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_te
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    scene bgBarNight

    show bgCounterTop
    with dissolve

    play music "noir_v002_lpf_LOOPedit.wav" fadein 1.0

    #show charles sit at Center(xcenter = Seat2.xcenter,ycenter = (Seat2.ycenter))
    #show charles sit at Seat2

    show frank sit beer lookLeft at Seat1
    with Dissolve(disFactor)

    "A middle-aged man walks in and looks at his watch. He shakes the minor look of confusion off of his face, then rubs his belly before walking over."

    show frank sit beer lookRight at Seat2
    with Dissolve(disFactor)
    frank "*Slurp*"

    bartender "Hey there. What can I get ya?"

    show frank sit beer lookPlayer at Seat2
    with Dissolve(disFactor)
    frank "Oh, you got a menu?"
    bartender "Just what's on the wall."

    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)
    "Frank squints his eyes to read the wall."

    show frank sit beer lookPlayer at Seat2
    with Dissolve(disFactor)
    frank "Hamburger and fries, and-"

    show frank sit at Seat2
    with Dissolve(disFactor)
    "Frank tucks the can of beer in his hand into his pocket."

    frank "Sorry, probably ain't suppose to have my own. Lemme get one of them beers."

    bartender "Got a favorite brand?"

    frank "Naw, whatever's cheap. Just none of that 'light beer' stuff."

    show frank sit beer lookRight at Seat2
    with Dissolve(disFactor)
    "Frank quickly finishes his own can when he thinks you're not looking."

    show frank sit at Seat2
    with Dissolve(disFactor)
    "You serve him a can of Sub beer."

    bartender "Here you go, Sub Lime."

    frank "Oh dear!"

    show frank looking anim at Seat2
    "Frank shifts uncomfortably at the mention of lime. You can tell he's too polite to send the drink back, and so, averting your gaze, he hesitantly moves to open it."
    
    bartender "Just messing, it's just regular old beer."

    show frank smile beer at Seat2
    with Dissolve(disFactor)
    frank "HA! Thank god."

    show frank sit at Seat2
    with Dissolve(disFactor)
    "Frank takes a closer look at the label and sighs in relief, within seconds, he empties the whole can into his mouth."

    show frank smile at Seat2
    with Dissolve(disFactor)
    frank "Nice and cold. Lemme get another."

    show frank smile beer at Seat2
    with Dissolve(disFactor)
    "You pass him a fresh can."

    show frank sit beer lookPlayer at Seat2
    with Dissolve(disFactor)
    "The door opens, and a young man in his late twenties enters the bar."

    show frank sit beer lookRight at Seat2
    show charles smile at Seat1
    with Dissolve(disFactor)

    charles "You open?"

    bartender "Come on in, the grill's still running."

    show charles sit at Seat1
    with Dissolve(disFactor)

    charles "Oh, cool."

    show charles sit lookLeft at Seat4
    with Dissolve(disFactor)
    "Charles ponders his surroundings, and chooses to sit down on the empty side of the bar."

    show charles sit lookRight at Seat4

    charles "Open late, huh?"

    "Charles studies the wall intensely."

    show charles sit lookRight at Seat4

    charles "Oh... do you have steak?"

    "You nod."

    bartender "How'd you like it done?"

    show frank angry lookRight at Seat2
    show charles smile at Seat4
    with Dissolve(disFactor)
    charles "Well done, with some a side of... do you have kale?"

    show frank angry lookLeft at Seat2
    with Dissolve(disFactor)
    "Off to the side, Frank almost chokes on his beer."

    show frank angry lookRight at Seat2
    with Dissolve(disFactor)
    bartender "Sorry, broccoli's closest we got."

    show frank sit beer lookRight at Seat2
    show charles sit lookLeft at Seat4
    with Dissolve(disFactor)
    charles "That'd work."

    "Half an hour goes by..."

    show frank drunk at Seat2
    with Dissolve(disFactor)
    "Frank's face turns cherry red, and he finally slows his pace."

    frank "So, um, did you buy the place from Jens? It never used to be open this late."

    bartender "Oh no, Jens is my brother. He asked me to take over for him for a while so he can go travel with his fiancé."
    
    bartender "I figured, why not put his liquor license to use, and try to open up the bar on Friday nights."
    
    show frank smile beer at Seat2
    with Dissolve(disFactor)
    "Frank nods appreciatively while sipping on cold beer."

    show frank drunk at Seat2
    with Dissolve(disFactor)
    frank "Yeah... I do see the resemblance. Well, good for Jens."

    show charles smile at Seat4

    "Charles perks up at the sound of conversation."

    show charles sit lookLeft at Seat4

    charles "No wonder, I was on my way home after meeting a super important deadline, and saw this place open. I thought I got lost or something."

    show frank drunk angry lookRight at Seat2
    show charles smile at Seat4
    with Dissolve(disFactor)
    "Charles looks at you with an excited smile that screams 'Please ask what I do for a living.'"

    show frank drunk at Seat2
    with Dissolve(disFactor)
    bartender "Well, I'll bite. What kind of deadline?"

    show frank drunk angry lookLeft at Seat2
    with Dissolve(disFactor)
    "Somehow, his eyes light up even more."

    show frank drunk at Seat2
    show charles explain at Seat4
    with Dissolve(disFactor)
    charles "I'm a reporter for the local paper."

    bartender "Journalist, huh?"

    show charles sit lookRight at Seat4
    charles "Yeah, normally, the workload isn't all that bad. But you know... elections coming up."

    show frank drunk angry lookRight at Seat2
    show charles sit lookLeft at Seat4
    with Dissolve(disFactor)
    "Charles look around to gauge people's reactions before continuing. Frank is too drunk to care."

    show frank drunk at Seat2
    show charles sit lookRight at Seat4
    with Dissolve(disFactor)
    charles "I'll bring an extra copy of the paper with me next time."

    bartender "You don't have to."

    show charles explain at Seat4

    charles "Oh, you should consider running an ad in the papers, it's pretty cheap and I can get you a deal."

    show charles sit lookLeft at Seat4
    bartender "I'm just trying this out for now."

    charles "No worries, it'll cost you almost nothing, and you only need to run it for a day or two. The town's small, so everyone reads the paper here."
    
    show charles explain at Seat4

    "Charles hands you a business card."

    show charles smile at Seat4

    charles "Call me after Tuesday and I'll give you a quote."

    bartender "Thanks."

    show charles sit lookRight at Seat4

    "After that brief exchange, Charles seems to get lost in thought, while Frank continues to nurse the beer in his hand."

    scene black
    with dissolve
    "The rest of the night proves uneventful. After the patrons leave, you close up shop."
    
    bartender "All in all, not bad for the first day."



    stop music fadeout 1.0
    pause 1
    show text "{size=70}End of Day{/size}" at truecenter as text3
    with dissolve
    play music "jingle_endOfDayDenoise.wav" noloop
    pause 2
    hide text3
    with dissolve
    pause 1



    jump Day2Block

return