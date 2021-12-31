# Seeing Blindly
### Video Demo:  <URL HERE>
### Description: 
  - Seeing Blindly is a website that helps the blind to see through their ears. 
  - The website does this through uploading an image link to the Clarifai api. 
  - using AI, the api turns the Image into multiple words that describe the content of the image. 
  - then through a text to speech library we turn our api output to sound, enabling our users to hear their images. 
### model.py: 
  - Writing and initializing the table that will be stored in the database. 
  - I created a table that contains an id (primary key), a name, an image path and the content of the api response.
### database.py: 
  - This python file builds the database and defines every function that interacts with the database in order to be used in the app.py. 
  - examples: add blog, delete blog, edit blog.
### app.py: 
  Through Flask we are hosting our website and creating a route for every html page that is displayed in our website. 
  the website has 6 routes of which only 2 are apparent to the user, the rest are for website management (admin). 
  all the functionality of the website is defined in this file: 
      Clarifai api: I verified the account through an api key and did a post method to upload the image, the response contains all the words that describe the content and we store it in the databse. Admin: The website contains an option for the editor to change the content of the website manually, you can edit and delete the objects infront of you however you need, this is done through functions in the database.py file.
### Index.html: The page that opens on the initial route, it displayes all the blogs, and has a navbar which through it you can access the picture to sound.
### addImage.html: In this html file the user can transform any image link to sound, in the form they have a name and image link. after they submit the form 
