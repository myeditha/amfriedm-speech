# FLEX

## Introduction

Welcome! We have all had interactions with certain people in our lives who have highly distinct speech patterns, people who we can immediately identify based off of the content of their messages alone. With the help of amfriedm-speech I present a machine-based model that replicates exactly that! Practical Uses? I dunno. Research Value? Probably 0. Value in Flex dollars? Over 9000. And that's what counts.

## Setup

You'll need to download your own copies of conversations with the flexman for this to work. In order to do so,

1. Go to m.facebook.com/messages
2. Go to a conversation with the desired flex
3. Paste the following code to load all messages from the beginning of your conversation history:

    `setInterval(function () {
    document.getElementById('see_older')
    .getElementsByClassName('content')[0].click();
    }, 500);`

4. Once you have reached the beginning of your conversation history, right click and click 'Save As', and save it the directory that scrapemsgs.py is in. 

Once this is done, run scrapemsgs.py to generate a csv file of all messages and necessary information.

In the future, you will be able to then run createmodel.py to create a model, and usemodel.py to use the classifier. For now, you still have real life flexes that you could be chatting with, so get on with it!

