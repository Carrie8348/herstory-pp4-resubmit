## Herstory
[LiveSite Here](http://herstory.herokuapp.com/)
<hr>

### Make sure our voices are heard

<hr>

<img src="static/site_image/head.png" width="500" />

<hr>

![mockup](/documentations/pics/mockup.png)

# Table of Content
1. [Introduction](#Introduction)
2. [Wireframes](#Wireframes)
3. [Goal](#Goal)
4. [UX](#UX)
5. [Features](#Features)
6. [Information Architecture](#Information-Architecture)
7. [Existing Features](#Existing-Features)
8. [Future Features](#Future-Features)
9. [SEO Implementation](#SEO-Implementation)
10. [Social Links](#Social-Links)
11. [Bugs](#Bugs)
12. [Used](#Used)
13. [Testing](#Testing)
14. [Deployment](#Deployment)
15. [Local Environment](#Local-Environment)
16. [Acknowledgement](#Acknowledgement)
17. [Disclaimer](#Disclaimer)
18. [Special Thanks](#Special-Thanks)



## Introduction

Women are as complicated as men. 

For many, many centuries, we have tried to tell our stories. Yet, in history, we did not have many audiences. Even lots of women themselves would not believe we do have stories to tell. 

But until recent years, through a series of feminist movements, for example, #metoo, women have started to say no to things they don't want to do, and we use all different ways to memorize our journeys, raise our voices, and ensure our stories are heard.

Herstory is a website that introduces meaningful documentaries about women, hoping to inspire audiences, and brings many thoughts, stories, and ideas to them. 

We want to build an excellent community for documentary lovers and those interested in feminist history. 

## Wireframes

1. Homepage
![wireframe](/documentations/wireframes/wf-01.png)
2. Movie Detail Page
![wireframe](/documentations/wireframes/wf-02.png)
3. Profile Page
![wireframe](/documentations/wireframes/wf-03.png)
4. Add Review Page
![wireframe](/documentations/wireframes/wf-04.png)
5. Edit Review Page
![wireframe](/documentations/wireframes/wf-05.png)
6. Watchlist Page
![wireframe](/documentations/wireframes/wf-06.png)


## Goal
- Build a good platform for users to find documentaries they might be interested in. 
- Provide high-quality content for target users.- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- Excellent UX keeps users on the site exploring more content and exchanging ideas by leaving reviews and adding movies to their watchlists.- [node.js] - evented I/O for the backend

## UX

### Ideal User

The ideal user for this site is:

- English speaking.
- Users who are interested in feminist history and documentaries.

Visitors to this website are searching for:

- Documentaries.
- Exploring stories to be inspired.

Why our site?

- We have an excellent taste collection of documentaries about women and feminist histories.
- A good community for users to exchange ideas and topics.
- Easy to navigate.


### User Stories

1. Users can view the movies list on the home page.
2. Users can view the movie details.
3. Login Users can add the movie to their watchlist.
4. Login Users can remove the film from their watchlist.
5. Login Users can add reviews on the film.
6. Login Users can edit or remove reviews on the movies
7. Users can see other people???s reviews of the film.
8. Login users can see how many likes of the movie and can like the movie too.
9. Users can sign up, log in, and log out.
10. Users can create a profile.
11. User can edit their profiles.
12. Super users can add the movie to the movie list in the admin panel.


## Features

Each page features a responsive navigation bar with a conventional placing of the logo (top left), the Account, and Watchlist (only for login users) on the right top corner. On small screens, the Account and Watchlist (only for login users) are on the right side of the logo.

Each page features a footer on the bottom, with our social media link displayed.

##### Topnav on the page

- Topnav on big screen without watchlist (not logged-in)
![topnav](/documentations/pics/topnav_without_login_big.png)

- Topnav on big screen with wishlist (logged-in)
![topnav](/documentations/pics/topnav_login_big.png)

- Topnav on small screen without watchlist (not logged-in)
![topnav](/documentations/pics/topnav_without_login_small.png)

- Topnav on small screen with watchlist

![topnav](/documentations/pics/topnav_login_small.png)

- Footer on big screen
![footer](/documentations/pics/footer-big.png)

- Footer on small screen
 
![footer](/documentations/pics/footer-small.jpeg)


#### Home Page
The Homepage displays the all movies on the site. 

There is a header pic displays, that's my drawing, and meaning all women in all races have lots stories to tell. Here is a place for every women.

There are movie image, title , director , lead actors displays . User can click on any of them to be redirected to the related movie detail page. 

It is responsive. On the larger screen, the products list 4 in a row, in the middle to large, 3 in a row, minor to middle screen, and 2 in a row, and lastly, it lists only 1 in a row. And the page when it onlys shows two movies side by side, the topnav will also be the same as the mobile position.

- Homepage on big screen
![homepage](/documentations/pics/homepage-big.png)

- Homepage on smaller screen
![homepage](/documentations/pics/homepage-smaller.png)

- Homepage on even smaller screen
![homepage](/documentations/pics/homepage-even-smaller.png)

- Homepage on the smallest screen, such as mobile

![homepage](/documentations/pics/homepage-small.jpeg)


#### Movie Detail Page
This page shows specific movie information to the user, with a movie picture showing, and title, directors, actors, release date, country and summary display. 

Users can click the button on the page to add a movie to the watchlist. 

Login users can click the like button under the movie summary.Login users can see how many likes this movie has got.

Users can go back to the home page by clicking the button.

Users can see the reviews has been left for the movie. But only login users can click the "Add Review" button to add a review to the specific movie. Without logging in, users are offer a choice of "Sign in" so they can leave review too.

- Movie Detail Page on big screen
![movie_detail](/documentations/pics/movie_detail_big.png)

- Movie Detail Page on small screen

![movie_detail](/documentations/pics/movie_detail_small.jpeg)

- Add to Watchlist button (same on big and small screen)

![watchlist_button](/documentations/pics/add_to_watchlist_button.png)

- Movie Likes  (same on big and small screen)

![movie_likes](/documentations/pics/likes.png)

- Go Back Button (same on big and small screen)

![go_back](/documentations/pics/go_back.png)

- Add Reviews Button (same on big and small screen)

![add_reviews_button](/documentations/pics/add_reviews.png)

- Reviews showing on the page (same on big and small screen)
![add_reviews_button](/documentations/pics/reviews_display.png)


#### Add / Edit Review Page
These two pages are almost identical, but only for different purpose, one is for user to add review to the movie, one is for user to edit the existing review.

- Add Review Page on big screen
![add_reviews](/documentations/pics/add_review_page_big.png)

- Add Review Page on small screen

![add_reviews](/documentations/pics/add_review_page_small.jpeg)

- Edit Review Page on big screen
![edit_reviews](/documentations/pics/edit_review_big.png)

- Edit Review Page on small screen

![edit_reviews](/documentations/pics/edit_review_small.jpeg)

#### Sign up/Log in/Log out Page
These pages contains function for user to register, log in and log out.

User needs to click on the "Account" icon on the topnav to find their options.

- Not logged in user's option in dropdown menu

![account_icon](/documentations/pics/account_icon_dropdown_menu_without_logged_in.png)

- Logged in user's option in dropdown menu

![account_icon](/documentations/pics/account_icon_dropdown_menu_logged_in.png)

Register: User clicks on the "Account" icon on the topnav, to have a dropdown menu, and choose "Register" to sign up to the website. 

- Sign Up page on big screen
![register](/documentations/pics/sign-up-big.png)

- Sign Up page on small screen

![register](/documentations/pics/sign-up-small.jpeg)

Log in: User clicks on the "Account" icon on the topnav, to have a dropdown menu, and choose "Log in" if he/she already has an account. 

- Log in page on big screen
![log_in](/documentations/pics/log-in-big.png)

- Log in page on small screen

![log_in](/documentations/pics/log-in-small.jpeg)

Log out: Login User clicks on the "Account" icon on the topnav, to have a dropdown menu ,and choose "Log out".

- Sign out page on big screen
![sign_out](/documentations/pics/sign-out-big.png)

- Sign out page on small screen

![sign_out](/documentations/pics/sign-out-small.jpeg)



#### Profile Page
This page contains user information with a form, so the users can update their info by clicking the button at the bottom of the form when needed.

- Profile page on big screen
![profile](/documentations/pics/profile_big.png)

- Profile page on small screen

![profile](/documentations/pics/profile_small.jpeg)


#### Watchlist Page
This page contains login user's choices of movie. They add the movie from the movie detail page to this watchlist. And it shows the movie image, title and director name. Login user can click the image or movie title to be redirected to the movie detail page.

Login user can remove the movie from the watchlist. 

When there is nothing in the watchlist, there will be a sentence on the page: "There is nothing on your watchlist"

- Watchlist page (with saved movie) on big screen
![watchlist](/documentations/pics/watchlist_big.png)

- Watchlist page (with saved movie) on small screen

![watchlist](/documentations/pics/watchlist_small.jpeg)


- Empty Watchlist page on big screen
![watchlist](/documentations/pics/empty_watchlist_big.png)

- Empty Watchlist page on small screen

![watchlist](/documentations/pics/empty_watchlist_small.jpeg)

## Information Architecture
### Database Modelling

#### Movie App:

| Model Name | Models | Model Type |
| ------ | ------ |------ |
| Movie | title |CharField |
| Movie | director |CharField |
| Movie | lead_actor |CharField|
| Movie | country |CharField |
| Movie | updated_on |DateTimeField |
| Movie | summary  |TextField |
| Movie |featured_image  |CloudinaryField |
| Movie |released_on |CharField|
| Movie |status  |IntegerField |
| Movie |likes  |ManyToManyField |

#### Review App:

| Model Name | Models | Model Type |
| ------ | ------ |------ |
| Reviews| title |CharField |
| Reviews | movie |ForeignKey |
| Reviews | created_on |DateTimeField|
| Reviews | body |TextField |
| Reviews| posted_by |ForeignKey/UserModel |

#### Wishlist App:
| Model Name | Models | Model Type |
| ------ | ------ |------ |
| Watchlist |user  |OneToOneField |
| Watchlist | movies |ManyToManyField |
|WatchlistItem |movie  |ForeignKey |
| WatchlistItem |watchlist  |ForeignKey|

#### Profiles App:
| Model Name | Models | Model Type |
| ------ | ------ |------ |
| Profiles | User|OneToOneField/ UserModel |
| Profiles |phone_number  |CharField |
| Profiles | street_address1  |CharField |
| Profiles | street_address2 |CharField |
| Profiles |town_or_city  |CharField |
| Profiles |county  |CharField |
| Profiles | postcode  |CharField |
| Profiles |country  |CountryField |
|Profiles |email  |EmailField |
| Profiles |birthday  |DateField |


## Existing Features
- Header Logo - It exists on every page. Clicking the logo returns to the home page.
- Topnav icons Accounts exists on every page. Login user can click on it and have a dropdown menu with options "My profile" and "Log out". User not logging in can have options in the dropdown menu "Register" and "Log in".
- Footer - It exists on every page and allows all users to navigate to the site's social media accounts quickly. It also shows the copyright at the bottom.
- Review Form -  This will enable users to make reviews of the products.
- Watchlist - This allows users to add movies they want to see in the future.


## Future Features
- User Profile Picture - Users can upload their picture to the profile, which will show on the review comment when they do reviews. 
- Emoji - Users can use emojis when they leave reviews in the review area.
- A Forum - Users can add posts to start their topics and interact with other login users.
- Rating - For login users to quickly rate the movie without leaving a review.

## SEO Implementation

I have used the following meta to implement my SEO words:
 ```sh
<meta name="description" content="HerStory, documentaries about women theme-color=bg-white">
```
 ```sh
 <meta name="keywords" content="women, woman, documentary, feminist, female">
```

## Social Links

#### Facebook
It is the most common platform to interact with site users to start a campaign. Right now, no such Facebook page is created, but it is an idea for future events coming, so this could be useful.

#### Instagram
Another great platform is Instagram. Facebook is for the first generation of internet users, and Instagram targets younger generations. So far, there is an Instagram icon linking to my personal IG account. In the future, hopefully, we will create an account and showcase our documentary collections to millions of potential customers out there.


#### Linked-In
There is a link to my linked-in account URL for business growth potential. It is an authentic platform for people interested in this site or potential suppliers to build up open and honest business possibilities. 


## Bugs

- Watchlist Error: There was no showing on this page after I added the movie to the list. But it shows in the database. 
- Solution: After many, many times checking my models and view, I found this minor typo issue that calls "movie" "Movie," which caused the problem. Therefore it was solved.

<hr>

- Heroku App  Error:  I have deployed the project on the Heroku app with no problem, but when I click "open app" on Heroku, it shows the " --tail" error.

- Solution: Tutor Christine Kelley helped me with this one as I am still unfamiliar with spotting issues with Heroku logs. She discovered that the "all auth" wasn't appropriately added to the "Requirement.txt" file. Therefore I use the command "pip3 freeze > requirements.txt" to solve it. It works!

<hr>

- Another was the Heroku displaying issue: When I could successfully open the app from the Heroku site, the logo and header pic was not showing correctly on the page, the links were turning blue, and the display of movies was wrong.

- Solution: Since the previously mentioned "all auth" error caused the deploying issue, I added the "DISABLE_COLLECTSTATIC" back in the config vars in the Heroku settings. And the "Debug=True" by the time tutor Christine Kelley suggested I change it to "False" and delete the "DISABLE_COLLECTSTATIC."  Then it works!

<hr>

- HTML validator issue: I have created a separated file for the mobile-top-header html, which exists in the project level templages foler - includes folder. And this caused an issue in the W3C validator, becuase it doesn't start with <ol> or <ul>

- Solution: I tried added it in the file and it passed the validation, but it displays wrong on the mobile then. Therefore I ignore it.


## Used

- This project uses HTML and CSS programming languages.

- Bootstrap
  1. The project uses Bootstrap 4 to structure the website and make the website responsive quickly and simply.
  2. The project also uses BootstrapCDN to provide icons from FontAwesome.

- Django:
  1. The project uses Django MTV (models, templates, and views) to make front-end and back-end functions with each other.

- Google Fonts : The project uses Google Fonts to style the website fonts.

- jQuery: The project uses jQuery to reference Javascript needed for the responsive navbar.

- Crispy Forms: It is for the forms to interact with the database.

- Cloudinary: It is used to store static and media files.

- Git: To commit to our GitPod terminal and push to GitHub.

- GitHub: To keep the project after pushing.

- Heroku: To deploy the project.

- Keynote: Draw my wireframes. 

- Canva: Design my logo.

- Procreate: Draw the header picture on the home page.


## Testing
Testing information can be found in separate [Testing.md File](/testing.md)

## Deployment
#### Heroku

This project deploys on Heroku.

1. Add requirements.txt by using the command in the terminal: 
```sh
 pip3 freeze --local > requirements.txt
```
2. Git adds and commits the changes.
3. Create or log in to a Heroku account.
4. Create a Heroku app.
5. On the Resources page, search and add Heroku Postgres.
6. Add Database URL and Secret key both in Heroku and local.
7. Add gunicorn to the project.
8. Allow Heroku as ALLOWED_HOSTS in the settings of the project.
9. Add and commit the changes to the code and push them to GitHub.
10. Deploy page in Heroku, choose "GitHub" as the "deployment method, "connect to GitHub, and select related repo. 
11. Choose "Automatic Deploys".
12. Choose "Enable automatic deploys" or choose "Deploy branch" and manually deploy.
13. Click "Deploy branch."
14. If successful, it shows a message "The app was successfully deployed.".
15. "View" when it is done.
16. If not successful, read the log and spot the issue. 
17. Fix issue and deploy again until successful.

## Local Environment
- Use Gitpod's built-in virtual environment feature.
- Create env.py contains the duplicate keys that exist in the Heroku Config vars:
  1. Database URL
  2. Secret Key
  3. Cloudinary
- To also start a requirement.txt file with the command :
```sh
 pip3 freeze --local > requirements.txt
```

### Static and Media Files
```sh
 STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

```
```sh
MEDIA_URL = '/django-summernote/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## Acknowledgement
1. I have collected some ideas for the footer code from the W3C school website. 
2. I have collected the movie posters and descriptions from douban.com.
3. I have used my previous pp5 project, "Handy Thoughts" as my basic layout for this resubmit project.

## Disclaimer
The content of this website is for educational purposes only.


## Special Thanks
This is the second time I have worked on PP4. I certainly know a lot more after the studies and the work on project 5.  

I must thank all the tutors, Ger Tobin, Christine Kelley, and Kevin Loughrey. Even this time around, I knew more, but I still got caught up in things I was not capable of. Your help and advice are very much appreciated. And the encouragements, I wish we'd cheered with wine haha.

And to the assessment result last time. It was very fair. I didn't do enough CRUD and failed. It pushed me to face it and work harder. And I am much more confident now.