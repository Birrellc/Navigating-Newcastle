# TESTING

This project has been tested throughout with the use of preview, DevTools, manual testing and also the website was deployed on Heroku pages very early in development with an automatic deploy feature enabled for every commit made which allowed me to test live deployments very early in the development cycle.

---

## HTML

- For HTML testing I ran my code through [W3C HTML Validator](https://validator.w3.org) by URI validation using my [Deployed Live Site](https://validator.w3.org).
- I received no errors for my HTML as shown in the Image below.
- In order to be extra thorough i actually tested the link for each page although the image only shows the main site test everything came back with 0 errors.

![HTML VALIDATION TEST](../testing/test-images/html-test-img.png)

---

## CSS

- For CSS testing i first [Auto Prefixer CSS](https://autoprefixer.github.io) to make sure my CSS has all the correct vendor prefixes.
- The commit showing these changes being implemented can be found [Here](https://github.com/Birrellc/Navigating-Newcastle/commit/fc256d091fc00856bba4dce0a80f9b0ad88e076a)
- I then proceeded to run my code through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and received no errors as shown in the image below.
- I also then applied a red border to all my elements to check for any overflow issues & there are none.

![CSS VALIDATION TEST](../testing/test-images/css-test-img.png)

---

## jQuery / JavaScript

- Due to my project being more focused on creating a CRUD application I found I did not need to use as much JavaScript for this process to chose to keep it to a minimum to allow more time to focus on the core concepts of the project.
- For JavaScript validation I ran my code through [JsHint](https://jshint.com/) and recieved no errors or warnings as show in the image below.

![JS VALIDATION TEST](../testing/test-images/jshint-test-img.png)

---

## Python

- For Python testing I ran my code through [Extends Class Python Tester](https://extendsclass.com/python-tester.html).
- I ran through all 3 of my .py files: app.py, forms.py and decorators.py of which i recieved no errors for any of them as show below.

#### app.py

![app.py VALIDATION TEST](../testing/test-images/app-test-img.png)

#### forms.py

![forms.py VALIDATION TEST](../testing/test-images/forms-test-img.png)

#### decorators.py

![decorators VALIDATION TEST](../testing/test-images/decorators-test-img.png)

---

## Responsive Testing

- I used 3 different methods for my responsive testing which were: [DevTools](https://developer.chrome.com/docs/devtools/), [Am I Responsive](http://ami.responsivedesign.is/) & [Responsivley App](https://responsively.app/)
- First off throughout the project i used [DevTools](https://developer.chrome.com/docs/devtools/) to keep an eye out for any responsive errors and continued throughout the whole development process.
- Nearing to the end of the process i used [Am I Responsive](http://ami.responsivedesign.is/) to create the snapshot below showing how the project looks on various devices.

#### Am I Responsive

![Am I Responsive](../testing/test-images/nn-amiresponsive.png)

- After using Am i Responsive i decided to use [Responsivley App](https://responsively.app/) to view my website with multiple device sizes at once where i noticed an issue where there was a spacing below my footer when using that app but when i looked at the same resolutions in devtools i found no spacing so decided to leave it here. Example shown below

#### Responsively

![Am I Responsive](../testing/test-images/responsively.gif)

Full list of tested resolutions with [DevTools](https://developer.chrome.com/docs/devtools/) & [Responsivley App](https://responsively.app/):

1. iPhone 5/5se 320px
2. iPhone X 375px
3. Pixel 2 411px
4. iPhone 6/7/8 Plus 414px
5. Ipad 768px
6. Nexus 10 800px
7. Generic Laptop 1280px
8. MacBook Air 1440px
9. Desktop 1920px

---