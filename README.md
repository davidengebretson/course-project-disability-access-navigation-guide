CSCI 597T/497T -- WWU
Winter 2023

# Disability Access Navigation Guide  

## This project is split into two teams with the following team members:

### 1) Data Visualization
   - Emma Geary, gearye2@wwu.edu
   - Benjamin Clay, clayb@wwu.edu
   - Ryan Rapoport, rapopor@wwu.edu

   ### Contributions R1
         Emma Geary
         : Created filter.css, implemented building lists, implemented sample classroom, implemented all South Campus buildings and related content
      Benjamin Clay
      : Implemented Mid Campus information (Region buildings, pictures, alt-text, buttons, and SampleFloor page)
      Ryan Rapoport
      : Implemented North Campus information (Region buildings, pictures, alt-text and buttons
   
### Features Implemented R1:
   - Filtering done by region and building
   - All pages for buildings include images (placeholders in some cases)
   - Communications Facility floors, complete with basement classrooms listed
   - Sample classroom information page created
   
### Contributions R2
         Emma Geary
         : https://dl.acm.org/doi/10.1145/2596695.2596715
      : Adding buildings accessibility information, finished SMATE and CF, added floorplans to remaining buildings, edited some aesthetic issues, fixed alt text, fixed page headers
      Benjamin Clay
      : Implemented basic search bar, finished linking MidCampus floor buttons to sample floor, and each floor to sample classroom
      Ryan Rapoport
      : Implemented Academic West classrooms
   
### Features Implemented R2:
   - Finished Communications Facility, Academic West, SMATE
   - Bond Hall has sample classrooms for all classrooms
   - Every building has building accessibility information
   - Search bar partially implemented
   - Every floor of every building has a floorplan
   
## To Do:
      - Link crowd sourcing functionality to data visualization portion
   - Add classrooms to remaining buildings
   
## Crowd Sourcing
   - Don Strong - strongd5@wwu.edu
  -  Katie Taylor - taylo230@wwu.edu
   - Nikita Rana- ranan@wwu.edu
   - Thuan Nguyen- nguye404@wwu.edu

### Features Implemented R1:
      - Home page with navbar, main content page for navigation, footer with external reference to Github project.
   - Upload form to capture data from users.
   - Server that facilitates navigation, error checking of uploaded data
   - Placeholder pages for data upload success and failed attempts
   
      ### Contributions R1
      Don Strong
         : Created template app for crowd sourcing and data visualization teams using HTML/CSS, Flask, Jinja.
         : Created upload form for data entries.
         : Created placeholder upload success and upload failure pages and implemented client and server side upload-requirements checking.
      Katie Taylor
      : 
      Nikita Rana
      : Worked on success and faliure pages, helped design layout features, made questions for survey, documentation
      Thuan Nguyen
         : Created a survey form and implemented the survey with WWU students for the functional design requirements
         : Designed the layout for the About and Contact Page
   
      ### Features Implemented R2:
   - Connected Flask to MongoDB for data storage and retrieval.
   - Various UI bug fixes (inconsistent height with smaller screens, unresponsive buttons, etc).
   - Deployed app on AWS EC2 instance for public access.
   - Created local storage on server for file uploads.
   - Redesigned upload successful page to show user confirmation of uploaded data
   
      ## Contributions R2
      Don Strong
      : UI Bug fixes
      : Created/incorporated MongoDB with server for user uploads.
      : Added local storage on server for file uploads.
      : Updated upload success page to provide upload confirmation.
      : Configured/deployed on AWS for demo and public access.
      Katie Taylor
      : UI Bug fixes, e.g. fix layout arrangement on upload page
      : Conducted evaluations with two users
      : Documentation
      Nikita Rana
      : Implemented faliure page, worked on UI bugs,conducted accessibility evaluation with participant, documentation
      Thuan Nguyen
      : Implemented the About Page, added some CSS styling
      : Implemented the Contact Page. Received contact information from other members
       : Conducted evaluations with one new WWU student, and gave suggestion features

## To Do:
   - Connect data visualization with latest changes to render data uploads.
   
   ## Additional Details
Additional details regarding progress and design decisions/motivation can be found in the file in your repository called "Disability Access Navigation Guide R1 Prototype -- Crowdsourcing Team.pdf"

## Dependencies
   - Python 
   - Flask 
   - MongoDB

## To run this app:
   1. Clone repo to local directory 
   2. cd to the directory where you cloned the repository
   3. flask run 
   4. Open your web browser and navigate to localhost:5000 
