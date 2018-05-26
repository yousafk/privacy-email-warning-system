# Privacy Email Warning System
If you've watched Silicon Valley Season 5, then you've seen Gilfoyle's Bitcoin Warning Alert System which blasts "You Suffer" by Napalm Death. You can [watch it here.](https://www.youtube.com/watch?v=uS1KcjkWdoU)

**In light of so many privacy emails from companies as a result of EU's new General Data Protection Regulation (GDPR),** I created a warning system that works with my Gmail to blast "You Suffer" by Napalm Death **everytime I receive a new privacy update email.** 

# Installation
**Allow less secure access to Gmail**
Directions here: [Google Support](https://support.google.com/accounts/answer/6010255?hl=en)

**Install the dependencies** 
`pip install -r requirements.txt`

**Run it in the background**

    exec -a warning-sys python3 main.py &

**Stopping**

    pfkill -f warning-sys
    
**Enjoy!**
