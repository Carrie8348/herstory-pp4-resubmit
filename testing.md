# Testing.md

- Test User Stories
- Manual Testing
- Validations
- Lighthouse
- Browser Validation
- User Testing

<hr>

## Test User Stories

1. Users can view the movies list on the home page.
   - Users can check the movies on the homepage with or without logging in. 
2. Users can view the movie details.
   - The movie images and movie titles on the homepage can be clicked and redirect the user to the specific movie detail page. Then user will see the movie detail such as movie title, director names, lead actors name, movie released date, country, and summary. 
3. Login Users can add the movie to their watchlist.
   - Login users on movie detail page, can see a button "Add to Watchlist", when this button is clicked, the movie will be added to user's watchlist.
4. Login Users can remove the film from their watchlist.
   - Login users can see the Watchlist icon on the topnav. When they click this icon, they will be redirected to the watchlist page. 
   - If there is movie saved, they will see the movie title, image and direcor information in it. The movie image and title are links to this movie detail page.
   - With a button "Remove from Watchlist" under, user can click it and remove the movie from the watchlist as wish. 
   - If there is no movies saved, then there will have a sentence showed "There is nothing on your watchlist".
5. Login Users can add reviews on the film.
   - Login users can find a button "Add Reviews" on the movie detail page, under the summaries. 
   - Not login user will see a button of "Sign In".
   - Login users click the button "Add Reviews" will be redirected to "add_review" page. And then they can fill out the form and click the button under.
   - The added review will shown under the movie's review section. Everyone can see it. But only the review's author can see two links "edit" and "delete" to interact with this review.
6. Login Users can edit or remove reviews on the movies.
   - Login users can edit their own reviews by click on the link under their review. Then they will be redirected to the "edit_review" page. They can revise the review content and hit the button below.
   - If login users click on the "delete" link, then the review will be deleted. 
7. Users can see other people’s reviews of the film.
   - All reviews of the movies are showing on the movie detail page.
8. Login users can see how many likes of the movie and can like the movie too.
   - There is a button under the movie summary on the movie detail page. Login user can see it and click on it to add likes to it. And there is number of likes showing next to this button.
9. Users can sign up, log in, and log out.
   - Users can click on the Account icon on the topnav, when it's in "not logged in" status, the dropdown menu contains two options "Register" and "Log in". 
   - Users choose "Register" will be redirected to this "sign up" page. They can fill out the form and click the button. When it's done, they will be redirected to a page with instruction that they will receive an email to verify their email address. Users receive email and click on the links, then the email address gets verified. The registration is done. 
   - Users choose "Sign In" will be redirected to "sign in" page. They can use their username and password to log in.
   - Under the logged-in status, users can click on the topnav "Account" icon to have two options showing in the dropdown menu, "My profile" and "Log out".
   - Users choose "Log out" will be redirected to the "sign out" page, there will have a question displays asking if user do want to sign out. Users can click the button and complete signing out.
10. Users can create a profile.
    -  Under the logged-in status, users can click on the topnav "Account" icon to have two options showing in the dropdown menu, "My profile" and "Log out".
    - Users choose "My profile" will be redirected to the "profile" page. There is a form on the page, users can fill out the form to create this profile, once they click the button below, the data will be saved to the databse.
11. User can edit their profiles.
    - On profile pages, user can change information in the form, click the button below, update the data in the database.
12. Super users can add the movie to the movie list in the admin panel.
    - Superusers can log in from the admin panel, and choose "movie", and then "add movie", to add movies to the database, which will be shown on the homepage and movie detail page.

<hr>

## Manual Testing


#### Header 

Topnav

- Expectation: Display on every page. There are logo, account icon displays, and watchlist displays on a login user's screen.
- Test: Visit every page on different sizes of screens. 
- Result: Worked as expected.

- Topnav on big screen without watchlist (not logged-in)
![topnav](/documentations/pics/topnav_without_login_big.png)

- Topnav on big screen with wishlist (logged-in)
![topnav](/documentations/pics/topnav_login_big.png)

- Topnav on small screen without watchlist (not logged-in)
![topnav](/documentations/pics/topnav_without_login_small.png)

- Topnav on small screen with watchlist

![topnav](/documentations/pics/topnav_login_small.png)

Logo
- Expectation: When the user clicks the logo, they will be redirected to the homepage. 
- Test: Try every page on the big screen. When I click on the logo, the page gets redirected to the home page. 
- Result: Worked as expected.

The logo:

<img src="static/site_image/logo.png" width="100" />

Account
- Expectation:  This icon shows on every page. On big screens, it shows text under it that says "Accounts," but no text on smaller screens. It is a dropdown menu. When the user clicks this icon, there are options for the login user to view their profile and log out. For not login users, there are options for logging in and registering. The users will be redirected to the pages according to what they clicked on in the menu. 
- Test: Try on both big and small screens, log in or not log in.
- Result: Worked as expected.

- Not logged in user's option in dropdown menu

![account_icon](/documentations/pics/account_icon_dropdown_menu_without_logged_in.png)

- Logged in user's option in dropdown menu

![account_icon](/documentations/pics/account_icon_dropdown_menu_logged_in.png)



Watchlist icon
- Expectation:  This icon shows only appears when the user is logged in. It is linked to the user's watchlist page. Like the Account icon, there is a text under the icon it says "Watchlist" on the big screen, not on small screens.
- Test: Try on both big and small screens, log in or not log in.
- Result: Worked as expected.

- Watchlist icon on big screen

![watchlist](/documentations/pics/watchlist_icon_big.png)

- Watchlist icon on small screen

![watchlist](/documentations/pics/watchlist_icon_small.png)


Homepage Body
- Expectation: With a responsive header picture on the page under the topnav. There is a welcome message shown under the picture. Then the main content of this page is the movie lists, which display all the movies in the database. In each card of the movie, there is a movie image, title, director name, and lead actor's name displayed. Users can click on the image and movie title to be redirected to the movie detail page.
- Test: Try on both big and small screens.
- Result: Worked as expected.

- Homepage on big screen
![homepage](/documentations/pics/homepage-big.png)

- Homepage on smaller screen
![homepage](/documentations/pics/homepage-smaller.png)

- Homepage on even smaller screen
![homepage](/documentations/pics/homepage-even-smaller.png)

- Homepage on the smallest screen, such as mobile

![homepage](/documentations/pics/homepage-small.jpeg)


Footer
- Expectation:  It shows on every page. Stick to the bottom. There are three social account icons listed on top of the footer. Users can click on them and be redirected to those pages. The very last part is the copyright.
- Test: Try on both big and small screens and every page.
- Result: Worked as expected.

- Footer on big screen
![footer](/documentations/pics/footer-big.png)

- Footer on small screen
 
![footer](/documentations/pics/footer-small.jpeg)

Log In 
- Expectation: The user can click on the account icon on the top and choose "log in" from the dropdown menu. They will be redirected to the page. If the user has never signed up before, they can click the link on the text to be linked to a register page. If they already have an account,  they can enter their username and password, then log in. There is also a link to reset the password if they forget it.
- Test: Try on both big and small screens.
- Result: Worked as expected.

- Log in page on big screen
![log_in](/documentations/pics/log-in-big.png)

- Log in page on small screen

![log_in](/documentations/pics/log-in-small.jpeg)


Sign Out
- Expectation:  A login user can click on the account icon on the top and choose "sign out" from the dropdown menu. Then they will be redirected to the page with a question confirming the user's choice and a button to sign out eventually.
- Test: Try on both big and small screens.
- Result: Worked as expected.

- Sign out page on big screen
![sign_out](/documentations/pics/sign-out-big.png)

- Sign out page on small screen

![sign_out](/documentations/pics/sign-out-small.jpeg)


Register
- Expectation: The user can click the account icon on the top and choose "register" from the dropdown menu. They will be redirected to a page with signup forms. They must fill out their email address, user name, password, etc. Then they can click the button at the bottom or choose the login button to log in if they have an account. Once the user fills out the form to register, they will be redirected to a page showing message "Verify email address." They will receive an email with the link to verify the email address. Once they click the link, their email address is verified, then the registration is successful. They can log in with the details then.
- Test: Try on both big and small screens.
- Result: Worked as expected.

- Sign Up page on big screen
![register](/documentations/pics/sign-up-big.png)

- Sign Up page on small screen

![register](/documentations/pics/sign-up-small.jpeg)

- Verify email address email on big screen
![verify_email_address_email](/documentations/pics/confirm_email_big.png)

- Verify email address email on small screen

![verify_email_address_email](/documentations/pics/confirm_email_small.jpeg)


Movie

Movie Detail Page
- Expectation: When a user views a movie detail page, there will be an image of the movie on the top or a default image. Movie titles, director names, lead actors' names, release dates, countries, and movie summaries are displayed on the page. And there is an option of an "Add to Watchlist"  button for the login user. Under the summary, there is a like button for the login user. Besides the like button, there is a number showing the number of likes. Then the following line is one button, "Go back" Then, there is a horizontal line that keeps the review part in the lower section of the page. With the button "Write a review," the login user can be redirected to the add review page. For not login users, they will be redirected to the login page. If there are any reviews of the movie, they will be shown in this section too.
- Test: Try on both big and small screens.
- Result: Worked as expected.

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


Movie review page
- Expectation: Login users can write a movie review by clicking the button on the movie detail page. They will be redirected to this add review page and then leave their comments by clicking the button at the bottom. When the review is added to this movie detail page, it will be shown under the movie summary. And the user can also edit or remove the review by clicking on the links. The user can revise and re-send the review on the edit review page.
- Test: Try on both big and small screens.
- Result: Worked as expected.

- Add Review Page on big screen
![add_reviews](/documentations/pics/add_review_page_big.png)

- Add Review Page on small screen

![add_reviews](/documentations/pics/add_review_page_small.jpeg)

- Edit Review Page on big screen
![edit_reviews](/documentations/pics/edit_review_big.png)

- Edit Review Page on small screen

![edit_reviews](/documentations/pics/edit_review_small.jpeg)



Watchlist Page
- Expectation: Only login users can see this icon on the topnav and be redirected to this page. If there are added movies, it will show the watchlist item with a movie image, title, and director name. Then there is a button "Remove from wishlist" under these for the user to remove the item if they're no longer interested. If there is nothing on the watchlist, a message will show, "You have nothing on your watchlist."
- Test: Try on both big and small screens.
- Result: Worked as expected.

- Watchlist page (with saved movie) on big screen
![watchlist](/documentations/pics/watchlist_big.png)

- Watchlist page (with saved movie) on small screen

![watchlist](/documentations/pics/watchlist_small.jpeg)


- Empty Watchlist page on big screen
![watchlist](/documentations/pics/empty_watchlist_big.png)

- Empty Watchlist page on small screen

![watchlist](/documentations/pics/empty_watchlist_small.jpeg)

Profile Page
- Expectation: When the login user clicks the account icon on the header and chooses "My Profile," they will be redirected to this page. There will be a personal info form for users to update the delivery info if they need to. 
- Test: Try on both big and small screens.
- Result: Worked as expected.

- Profile page on big screen
![profile](/documentations/pics/profile_big.png)

- Profile page on small screen

![profile](/documentations/pics/profile_small.jpeg)

<hr>

## Validations
#### HTML
- The W3C Markup Validator service was used to validate the HTML.
- Most of HTML pages are tested and passed with no errors.
- The "mobile_top_header" html file in "templates - includes" folder, is showing error because there is no <ol> or <ul> starting the file. But if I added it, the whole mobile top nav get ruied. So I keep it this way.


#### CSS
- The W3C Markup Validator service was used to validate the CSS.
- All CSS files are tested and passed with no errors.

#### Python
- The PEP8 Python validator service was used to validate the python files.
- In the testing, the main errors are because lines are too long. I tried to make them shorter, but it passed the test but did not function right on the site anymore. Therefore I put #noqa at the end of the lines.

#### JavaScript
- I used https://jshint.com/ to test the JavaScript. The error appears, claims undefined variable "Stripe," but since this code was copied from Boutique Ado, and it is too vital for the site to work, I ignored it for the moment.

## Lighthouse Validation
The site has been tested with Lighthouse. Performance could be further improved by analyzing the file types of images. Also since I use a free subscription for the Heroku app it starts really slowly which can affect the performance score.
![Lighthouse-validator](/documentations/pics/lighthouse.png)

## Browser Validation
The site was tested on different browsers:
- Google Chrome
- Firefox
- Safari

## User testing
I have several family and friends view and tried the site, and they like the look of it and think it functions well and smoothly. 




