# Seeing Blindly
### Video Demo:  <URL HERE>
### Description: 
  - Seeing Blindly is a website that helps the blind to see through their ears. 
  - The website does this through uploading an image link to the Clarifai api. 
  - Using AI, the api turns the Image into multiple words that describe the content of the image. 
  - Then through a text to speech library we turn our api output to sound, enabling our users to hear their images. 
### model.py: 
  - Writing and initializing the table that will be stored in the database. 
  - I created a table that contains an id (primary key), a name, an image path and the content of the api response.
### database.py: 
  - This python file builds the database and defines every function that interacts with the database in order to be used in the app.py. 
  - Examples: add blog, delete blog, edit blog.
### app.py: 
  - Through Flask we are hosting our website and creating a route for every html page that is displayed in our website. 
  - The website has 6 routes of which only 2 are apparent to the user, the rest are for website management (admin). 
  - All the functionality of the website is defined in this file: 
    - Clarifai api: 
      - I verified the account through an api key and did a post method to upload the image.
      - The response contains all the words that describe the content and we store it in the databse. 
    - Text to Speech:
      - I used a library called pyttsx3.
      - First you initialize, then you simply put a string in the function and it starts speaking.
    - Admin: 
      - The website contains an option for the editor to change the content of the website manually.
      - you can edit and delete the objects infront of you however you need, this is done through functions in the database.py file.
### Index.html: 
  - The page that opens on the initial route.
  - It displayes all the blogs, and has a navbar which through it you can access the picture to sound.
  - The form of addImage.html is submitted to the route of this html file, and there we post to the api and turn all the words to sound.
### addImage.html: 
  - In this html file the user can transform any image link to sound.
  - In the form they have a name and image link. 
  - After they submit the form it turns the image to speech and the blog is added to the database.
### admin.html: 
  - A sign in page for the editor to be able to edit the website.
  - The username and password are static and saved in the app.py.
### management.html:
  - Here you can edit the objects in the database or delete them.
  - All the objects are in a numbered list.
### blog_management:
  - you have an input box for each attribute of the object so you can edit them.
  - after you submit the object is updated in the database.
  - We know which object we're editing by making a variable route that takes the id of the object as an input.
  
###### I used a template for the frontend aspect of the project, ofcourse with a lot of changes.
