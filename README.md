# YOLOPv2-Project
Use of YOLOPv2 network to make warning system for driver if he's to close to one of the lanes or other cars. Also showing approximation of relative speed of other cars in relation to us.

We(me and my colleague) used YOLOPv2 from this repo(check them out for model): https://github.com/CAIC-AD/YOLOPv2

We added functions to choose lane points from inference, filter them, approximate lines and show them on screen. 
Also we made easy(maybe not too accurate) estimation of distance from pixels.
Using those we can find center point of our lane on given pixel height and assuming that camera is in the middle of front window we can check how far from lane center we're headed.

You can see results here: https://youtu.be/Ms7LKPPRQp0 and https://youtu.be/xK1RWM9cPjM
