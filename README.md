Website
=======

Code for my personal website.

The website is written in python/Flask for dynamically loading pages.

The CSS and JavaScript is handled using Bootstrap v3.

The colour selection was made using www.lavishbootstrap.com and one of their images.

Self-written code uses regular expressions to find the latest Astronomy Picture of the Day (APOD) and place that as the home page picture. If this fails, then it will show a picture of Naples and Versuvius in the background. Also, it will randomly pick between APOD and Naples every time someone loads the home page, where the probability of having one image or the other is always 50/50.
