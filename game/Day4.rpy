label Day4Block:

    scene black
    with dissolve

    play music "jingle_dayTitleDenoise.wav" noloop

    show text "Week 4" at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "The calm after the storm" at Transform(xalign = 0.5, yalign = 0.53) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    scene bgBarDay
    show bgCounterTop
    with dissolve

    #play music "noir_v002_lpf_LOOPedit.wav"
    play music "lux_v001_lpf_LOOPedit.wav" fadein 1.0


    "You expect a quiet day after what happened last week. Maybe they won't show up..."

    "Charles and Elysia are the first ones to arrive, still debating as they place their orders."

    show charles sit at Seat3
    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)
    charles "Mine's super different though! In my book they are called Zones, and there are thousands of them."

    show elysia smile lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "With robots in them."

    show charles smile at Seat3
    with Dissolve(disFactor)
    charles "Indeed."

    "Claire and Braxton enter, and listen in on Charles's passionate defense of his new idea."

    show braxton sit lookRight at Seat2
    show claire sit at Seat5
    show elysia closed  at Seat4
    show charles explain at Seat3
    with Dissolve(disFactor)

    charles "And the children fighting to the death thing is only a small part of the book."

    show frank sit beer at Seat1
    show elysia sit lookLeft at Seat4
    show charles sit lookLeft at Seat3
    with Dissolve(disFactor)

    "The door opens, and a small crowd of young men enter. Behind them, Frank walks in and shakes raindrops off his hat."

    "This is turning out to be an unusually busy night, with a rowdy group of male college students sitting themselves down at one of the diner tables."

    show braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    braxton "Is it raining?"

    show frank sit beer lookRight at Seat1
    with Dissolve(disFactor)

    frank "Drizzling."

    show elysia closed at Seat4
    with Dissolve(disFactor)

    elysia "Shit. Makes patrols way more tedious... But that's not for another few hours."

    show elysia sit lookLeft at Seat4
    show frank smile beer at Seat1
    with Dissolve(disFactor)

    frank "Better get the drinking started then."

    show frank sit lookRight at Seat1
    show braxton smile at Seat2
    with Dissolve(disFactor)

    braxton "You offering to buy, Frank?"

    show frank smile beer at Seat1
    with Dissolve(disFactor)

    frank "Nah."

    show braxton smile lookRight at Seat2
    show claire sit lookLeft at Seat5
    show charles sit lookRight at Seat3
    with Dissolve(disFactor)

    claire "I can buy everyone a round."

    show claire sit lookPlayer at Seat5
    show frank sit beer lookPlayer at Seat1
    with Dissolve(disFactor)


    "Frank looks over at you, and shakes his head."

    show frank sit lookRight at Seat1
    show claire sit lookLeft at Seat5
    show charles sit lookLeft at Seat3
    with Dissolve(disFactor)

    frank "Nah, we can get our own drinks."

    show claire angry up at Seat5
    with Dissolve(disFactor)

    "Claire sighs, but says nothing."

    show claire sit at Seat5
    show elysia smile lookPlayer at Seat4
    show charles smile at Seat3
    with Dissolve(disFactor)

    elysia "So Charles wants to write a book where children in different areas fight to the death."

    show frank smile beer at Seat1
    show elysia smile lookLeft at Seat4
    show braxton smile lookPlayer at Seat2
    with Dissolve(disFactor)

    frank "{i}Battle Royale{/i}."

    show frank smile beer lookRight at Seat1
    show elysia smile lookPlayer at Seat4
    show braxton smile lookRight at Seat2
    with Dissolve(disFactor)

    elysia "Or {i}The Hunger Games{/i}."

    show frank smile beer at Seat1
    with Dissolve(disFactor)

    frank "{i}Battle Royale{/i}'s better: grittier, better commentary. A lot more teenagers but less angst. It's pretty good."

    show charles sit lookLeft at Seat3
    show frank sit beer lookRight at Seat1
    show charles sit lookLeft at Seat3
    with Dissolve(disFactor)

    charles "Frank, how do you know so much?"

    show frank smile beer at Seat1
    with Dissolve(disFactor)

    frank "Audiobooks, nothing better to do on cross-state deliveries."

    #show frank sit beer at Seat1
    show claire sit lookLeft at Seat5
    show braxton sit lookLeft at Seat2
    show frank sit beer lookRight at Seat1
    show elysia sit lookLeft at Seat4
    show charles sit lookRight at Seat3
    with Dissolve(disFactor)

    "One of the people sitting at a diner table approaches the bar to get another beer."
    "The drunk young man tries to get Claire's attention, but she shakes her head and declines to make small talk."
    
    show braxton sit lookRight at Seat2
    show claire angry up at Seat5
    show charles sad at Seat3
    with Dissolve(disFactor)

    "He grabs the beer and returns to his table, cursing under his breath as he walks away."

    show braxton sit lookLeft at Seat2
    show claire sit at Seat5
    show frank angry lookRight at Seat1 behind bgCounterTop
    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)
   
    "Everyone at the bar glares over angrily, and Frank starts to get up."

    hide frank angry lookRight
    show frank angry lookRight at Seat1
    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "Frank, don't do it."

    show braxton sit lookRight at Seat2 behind bgCounterTop
    with Dissolve(disFactor)

    "Braxton starts to get up."

    hide braxton sit lookRight
    show braxton sit lookRight at Seat2
    with Dissolve(disFactor)

    frank "Just want to teach that boy some manners."

    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    elysia "Frank!"

    show frank angry lookLeft at Seat1
    show elysia closed at Seat4
    with Dissolve(disFactor)

    frank "WHAT?!? With words!"

    show frank angry lookRight at Seat1 behind bgCounterTop
    show braxton sit lookRight at Seat2 behind bgCounterTop
    with Dissolve(disFactor)

    "Frank and Braxton continue to get up."

    show elysia sit lookLeft at Seat4
    show charles sit lookLeft at Seat3
    with Dissolve(disFactor)

    elysia "And why are you getting up?"

    "Braxton shrugs."

    braxton "He mentioned teaching. I take teaching very seriously."

    elysia "Goddamn it, Braxton, don't encourage him. Seriously, Frank, I don't want to have to break up a bar fight."
    elysia "The moment one of them says something, you're gonna throw punches."

    "Frank and Braxton look over at you, and turn to find Elysia glaring at them."

    show frank angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "What?! Can't a man go to the bathroom?"

    show frank angry lookRight at Seat1
    show braxton sit lookPlayer at Seat2
    with Dissolve(disFactor)

    "Braxton shrugs again."

    hide braxton sit 
    hide frank angry 
    with Dissolve(disFactor)

    "Frank and Braxton leave to go to the bathroom."

    elysia "Probably complaining their asses off in there."

    bartender "I can ask those guys to leave."

    show claire happy player at Seat5
    show charles smile at Seat3
    with Dissolve(disFactor)

    claire "It's all right... It's safe here, everyone's got my back."

    show claire sit at Seat5
    show charles sit lookRight at Seat3
    with Dissolve(disFactor)

    "During quiet moments, you can hear faint sounds of Frank complaining through the bathroom door. Charles takes the chance to share more of his story ideas."

    play music "noir_v002_lpf_LOOPedit.wav" fadein 1.0

    "The duo returns after a few minutes."

    show frank sit beer lookRight at Seat1
    show braxton sit lookLeft at Seat2
    show charles sit lookLeft at Seat3
    show claire sit lookLeft at Seat5
    with Dissolve(disFactor)

    elysia "You boys got it all out of your system?"

    frank "Yep, emptied my bladder."

    show claire angry up at Seat5
    with Dissolve(disFactor)

    claire "That's super gross, Dad."

    show charles teased at Seat3
    with Dissolve(disFactor)

    charles "Jesus, Frank."

    show claire sit at Seat5
    with Dissolve(disFactor)

    "Frank chugs his beer then asks for more."

    show charles sit lookLeft at Seat3
    with Dissolve(disFactor)

    braxton "So... what's new, Charles?"
    
    show claire sit lookLeft at Seat5
    with Dissolve(disFactor)

    show charles sad at Seat3
    charles "Riots, protests... a lot of stuff happening all around the country."

    show claire sit at Seat5
    with Dissolve(disFactor)

    "Everyone ponders Charles's words quietly for a few moments."

    show claire sit at Seat5
    with Dissolve(disFactor)

    claire "..."

    show braxton sit lookPlayer at Seat2
    with Dissolve(disFactor)

    braxton "..."

    show frank sit beer lookLeft at Seat1
    with Dissolve(disFactor)

    frank "..."

    show elysia closed at Seat4 
    with Dissolve(disFactor)

    elysia "..."

    show frank drunk at Seat1
    show braxton sit lookRight at Seat2
    show charles sit lookRight at Seat3
    show elysia sit lookRight at Seat4
    show claire sit lookLeft at Seat5
    with Dissolve(disFactor)

    claire "So, do you know any books or films?"

    show elysia sit lookLeft at Seat4
    show charles smile at Seat3
    with Dissolve(disFactor)

    charles "I'm well-educated in the literary and cinematic arts."

    bartender "Like... name a movie you like."

    show charles explain at Seat3
    with Dissolve(disFactor)

    charles "{i}Theodore Rex{/i}."

    show braxton sit lookPlayer at Seat2
    show charles sit lookLeft at Seat3
    with Dissolve(disFactor)

    braxton "I've never even heard of that one."

    show braxton sit lookLeft at Seat2
    show frank drunk angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "I saw it once. Whoopi Goldberg's in it. She's a robot cop who's hunting down a dinosaur killer."

    show frank drunk at Seat1
    show claire sit lookPlayer at Seat5
    with Dissolve(disFactor)

    claire "That... can't be a movie, right? Those are just words put together."

    show claire sit lookLeft at Seat5
    show charles explain at Seat3
    with Dissolve(disFactor)

    charles "I'll have you know it's one of the greatest pieces of cinematic history known to man."

    show claire sit at Seat5
    show frank drunk angry lookRight at Seat1
    with Dissolve(disFactor)

    frank "It's crap."

    show frank drunk at Seat1
    show charles teased at Seat3
    with Dissolve(disFactor)

    charles "Frank!"

    show frank drunk angry lookLeft at Seat1
    with Dissolve(disFactor)

    frank "Total crap."

    show frank drunk at Seat1
    show charles sad at Seat3
    with Dissolve(disFactor)

    charles "I can't believe this. Everyone's ganging up against me."

    bartender "Nobody's against you, Charles."

    show braxton smile lookRight at Seat2 
    show charles teased at Seat3
    with Dissolve(disFactor)

    braxton "I kind of am."

    show claire sit lookLeft at Seat5
    with Dissolve(disFactor)

    claire "Wait! Dad, tell me more about this movie."

    show frank drunk at Seat1
    show braxton sit lookLeft at Seat2
    with Dissolve(disFactor)

    frank "Uh... let me think it over."

    show frank drunk at Seat1
    show charles sit lookLeft at Seat3
    with Dissolve(disFactor)

    "Frank pauses to take a swig."

    show frank drunk at Seat1
    show braxton sit lookLeft at Seat2
    show elysia sit lookLeft at Seat4
    with Dissolve(disFactor)

    frank "It's like a movie about dinosaur racism? And Whoopi's partner is a dinosaur that eats too many cookies. He makes this machine to fling cookies at him."

    show braxton sit lookRight at Seat2
    show charles smile at Seat3
    with Dissolve(disFactor)

    charles "And that was hilarious! And had a great message about tolerance!"

    "Claire Googles 'Theodore Rex'."

    show claire happy at Seat5
    show charles sit lookRight at Seat3
    with Dissolve(disFactor)

    claire "Oh my God, this is a real movie."

    show claire sit at Seat5
    show braxton sit lookRight at Seat2
    show elysia sit lookRight at Seat4
    with Dissolve(disFactor)

    braxton "Let me see that... Ho-ly cow."

    show claire happy at Seat5
    with Dissolve(disFactor)

    claire "Wait, I found a trailer."

    show elysia smile lookRight at Seat4half behind bgCounterTop
    show charles smile at Seat4 behind elysia
    show braxton smile lookRight at Seat3half behind charles
    with Dissolve(disFactor)

    "Everyone bunches together to stare at Claire's computer screen except Frank, who continues drinking."

    charles "Now doesn't that look fantastic?"

    "Everyone is silent except Frank, who continues drinking."
    
    charles "Guys? Guys...? Come on, guys?"


    scene black
    with dissolve

    stop music fadeout 1.0
    pause 1
    show text "End of Day" at truecenter as text3
    with dissolve
    play music "jingle_endOfDayDenoise.wav" noloop
    pause 2
    hide text3
    with dissolve
    pause 3

    jump Day5Block

return