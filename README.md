# Brenda Guijarro Tinoco #
## Art E-commerce ##

 
## UX ##

Project Goals:
 * Create an interactive , attractive and responsive art online shop
 * Create a functional e-commerce for an Oil paintings artist.
 
 
### Design Process ###


Provide a powerfull e-commerce for an artist which will assist to  attract more clients, possible commisions and 
open up to the professional artistic world.
To sketch the frontend part of the project I have used Blasamiq wireframes: 

   <img src="static/wireframes/wf1.png" alt="wireframe1" width="400" height="400"/>
   <img src="static/wireframes/wf2.png" alt="wireframe2" width="400" height="400"/> 
   <img src="static/wireframes/wf3.png" alt="wireframe3" width="400" height="400"/>  
   <img src="static/wireframes/wf4.png" alt="wireframe4" width="400" height="400"/>
   <img src="static/wireframes/wf5.png" alt="wireframe5" width="400" height="400"/>
   <img src="static/wireframes/wf6.png" alt="wireframe6" width="400" height="400"/>
   <img src="static/wireframes/wf7.png" alt="wireframe7" width="400" height="400"/> 
    
   
## General Features ##

The site counts with three different product pages: Canvas, prints, and All products which combines both. 
On all three pages, you can sort the products by price from low to high.
The Prints have the option to choose size because they all can be made in A5, A4, and A3. 
In the future I will add a fourth product page will it contain a large variety of accessories and possibly some clothing.
It also counts with a shopping bag and checkout functionality. 
If a client desires to sign up to track its orders through BGT art shop exists the possibility to register and save your payment, shipping details, and no less important order history.
However, is not required to be registered to place orders or turn into Brenda's art lover. 
The layout of the product pages is been designed using Bootstrap card elements and helped me a lot to create this 'art gallery' vibe that fits the most for this site. 
The carousel also makes an impression and visibly impacts the user,
advertising past commissions or expositions. 


## SuperUser Features ##
All superusers have access to the CRUD functionality (Only site Admins):

1. C - Create: Allowed to submitt their own recipes to share with the community of users.
2. R - Read: Full access to all recipes and info about Thermomix.
3. U - Uptade: Update or change only the recipies that have been submitted under their user_id.
4. D - Delete: Delete only the recipies that have been submitted under their user_id.


Technologies Used:
 1. HTML5 : Used to create the form and the content of the web site.
 2.	CSS3 : Used to style the HTML
 3. Bootstrap Frameworks: Used some components, Header and card layout and Caroussel. 
    Also used the grid system to make the website responsive for all size devices.
 4. JavaScript: For interactivity.
 5. JQuery : The project uses JQuery to simplify DOM manipulation.
 4. Gitpod and Github : to write , test and deploy my code. 
 5. Heroku : to Deploy my project and store sensible data variables.
 6. Python3, Flask and Json
 7. Django
 8. AWS (Amazon Web Services)
 9. Stripe : to handle payments and webhooks
 10. SQLite3 and Postgres
 11. Installed few liabraries :
    asgiref==3.3.4
    boto3==1.17.91
    botocore==1.20.91
    dj-database-url==0.5.0
    Django==3.2.3
    django-allauth==0.41.0
    django-countries==7.2.1
    django-crispy-forms==1.11.2
    django-storages==1.11.1
    gunicorn==20.1.0
    jmespath==0.10.0
    oauthlib==3.1.0
    Pillow==8.2.0
    psycopg2-binary==2.8.6
    python3-openid==3.2.0
    pytz==2021.1
    requests-oauthlib==1.3.0
    s3transfer==0.4.2
    sqlparse==0.4.1
    stripe==2.57.0

Features to implement :

I wanted to add an accesories page 

## Testing ##

I have Validated the code using: 
 * HTML   [HTML-Validator](https://validator.w3.org/#validate_by_input) - No errors found.
 * CSS    [CSS-Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - No errors found.
 * JS     [JS -Validator](https://jshint.com/) - No errors found.
 * Python [Python-Validator](http://pep8online.com/checkresult) - No errors found.


Tested the website in different browsers:    
* Chrome
* Edge
* Mozilla Firefox 
* Safary
    
I have also used the Inspect tool from Google Chrome to testt the responsiveness of the website in different size devices and 
manually tested in iPhone 6, 7 Plus, 8, xs, 12 pro, MacBook Pro 15", Asus VivoBook 14.5", HP Envy 21" , Ipad 3 and Ipad Pro 5.


* Navbar from medium and small devices converts into a dropdown menu. 
* The card containers from Materialize that have been used to organize the layout of the sign in and log in;
  from medium to small  screen sizes, the number of columns used per card is larger in a way it only shows one card at
  a time. Same with the input forms for editing and uploading recipes, and carousel and collapsible for the Home or Recipes page.
* Footer is responsive in all devices. 


## Deployment ## 

This project was entirely built in Gitpod and deployed in Heroku and GitHub. 

Deployment steps:

1. Log in into my GitHub. 
2. Go to my repositories.
3. choose the repository called 4rdMilestoneProject.
4. Settings.
5. Select Master branch.
6. Validate selection.
7. The ulr of the website is displayed.

You can see the website [GitHub](https://SaraSanchezz.github.io/4MilestoneProject/)
                        [Heroku](https://brendas-shop.herokuapp.com/)

Steps to run the code locally:

1. Open GitHub.
2. Select desired repository.
3. Click on clone or download.
4. Start your IDE.
5. Open the terminal.
6. Type git clone followed by the code of the repository at the terminal.

## Credits ## 


### Content ###
- The content of the page is been written by me and at the projects page is been copied from the projects structure and requirements, from the module materials.
- There are some parts of the code taken from Bootstrap componenents and after have been adjusted and modified it 
 to my web needs as for example:
    - [Navbar](https://materializecss.com/navbar.html)
    - [Collapsible](https://materializecss.com/collapsible.html)
    - [Carousel](https://materializecss.com/carousel.html)
    - [Card-structure](https://materializecss.com/cards.html)
    - [Footer](https://materializecss.com/footer.html)

### Media ### 
- The Hero image from the Website is been taken from [Unsplash](https://unsplash.com/)
- The Thermomix images are been taken from the internet, as there is not good pictures on free libraries, 
that is one of the reasons I have linked them on the project through the external link.
-[Image 1](https://stackoverflow.com/)
-[Image 2](https://stackoverflow.com/)
-[Image 3](https://stackoverflow.com/)
-[Image 4 ](https://stackoverflow.com/)

### Acknowledgements ### 

- [W3Schools.com](https://www.w3schools.com/).
- [MDB](https://mdbootstrap.com/).
- [Thermomix.co.uk](https://www.vorwerk.co.uk/shop/thermomix/thermomix-tm6/p/62149)
- [Cookidoo](https://cookidoo.co.uk/foundation/en-GB)
- [Materialize](https://materializecss.com/about.html)
- [Stackoverflow](https://stackoverflow.com/).
- Slack Community. 
- All the tutors who had assisted me during the process, the were all helpful and extremelly kind.
