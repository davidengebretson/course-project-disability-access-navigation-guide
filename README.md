CSCI 597T/497T -- WWU
Winter 2023

# Disability Access Navigation Guide  

##This project is split into two teams with the following team members:

###1) Data Visualization
   <ul>
   <li> Emma Geary, gearye2@wwu.edu </li>
   <li>Benjamin Clay, clayb@wwu.edu </li>
   <li> Ryan Rapoport, rapopor@wwu.edu </li>
   </ul>

###Contributions R1
   <dl>
      <dt>Emma Geary</dt>
      <dd>Created filter.css, implemented building lists, implemented sample classroom, implemented all South Campus buildings and related content</dd>
      <dt>Benjamin Clay</dt>
      <dd>Implemented Mid Campus information (Region buildings, pictures, alt-text, buttons, and SampleFloor page)</dd>
      <dt>Ryan Rapoport</dt>
      <dd>Implemented North Campus information (Region buildings, pictures, alt-text and buttons)</dd>
   </dl>

###Features Implemented R1:
   <ul>
   <li> Filtering done by region and building
   <li> All pages for buildings include images (placeholders in some cases)
   <li> Communications Facility floors, complete with basement classrooms listed
   <li> Sample classroom information page created
   </ul>

###Contributions R2
   <dl>
      <dt>Emma Geary</dt>https://dl.acm.org/doi/10.1145/2596695.2596715
      <dd>Adding buildings accessibility information, finished SMATE and CF, added floorplans to remaining buildings, edited some aesthetic issues, fixed alt text, fixed page headers</dd>
      <dt>Benjamin Clay</dt>
      <dd>Implemented basic search bar, finished linking MidCampus floor buttons to sample floor, and each floor to sample classroom</dd>
      <dt>Ryan Rapoport</dt>
      <dd>Implemented Academic West classrooms</dd>
   </dl>

###Features Implemented R2:
   <ul>
   <li> Finished Communications Facility, Academic West, SMATE
   <li> Bond Hall has sample classrooms for all classrooms
   <li> Every building has building accessibility information
   <li> Search bar partially implemented
   <li> Every floor of every building has a floorplan
   </ul>

##To Do:
   <ul>
   <li> Link crowd sourcing functionality to data visualization portion
   <li> Add classrooms to remaining buildings
   </ul>

##Crowd Sourcing
<ul>
   <li> Don Strong - strongd5@wwu.edu </li>
   <li> Katie Taylor - taylo230@wwu.edu </li>
   <li> Nikita Rana- ranan@wwu.edu </li>
   <li> Thuan Nguyen- nguye404@wwu.edu </li>
</ul>

###Features Implemented R1:
   <ul>
   <li> Home page with navbar, main content page for navigation, footer with external reference to Github project. </li>
   <li> Upload form to capture data from users. </li>
   <li> Server that facilitates navigation, error checking of uploaded data </li>
   <li> Placeholder pages for data upload success and failed attempts </li>
   </ul>
   
   ###Contributions R1
   <dl>
      <dt>Don Strong</dt>
         <dd>Created template app for crowd sourcing and data visualization teams using HTML/CSS, Flask, Jinja.</dd>
         <dd>Created upload form for data entries.</dd>
         <dd>Created placeholder upload success and upload failure pages and implemented client and server side upload-requirements checking.</dd>
      <dt>Katie Taylor</dt>
      <dd></dd>
      <dt>Nikita Rana</dt>
      <dd>Worked on success and faliure pages, helped design layout features, made questions for survey, documentation</dd>
      <dt>Thuan Nguyen</dt>
         <dd>Created a survey form and implemented the survey with WWU students for the functional design requirement</dd>
         <dd>Designed the layout for the About and Contact Page</dd>
   </dl>
   
   ###Features Implemented R2:
   <ul>
   <li> Connected Flask to MongoDB for data storage and retrieval. </li>
   <li> Various UI bug fixes (inconsistent height with smaller screens, unresponsive buttons, etc).</li>
   <li> Deployed app on AWS EC2 instance for public access. </li>
   <li> Created local storage on server for file uploads. </li>
   <li> Redesigned upload successful page to show user confirmation of uploaded data </li>
   </ul>
   
   ##Contributions R2
   <dl>
      <dt>Don Strong</dt>
      <dd>UI Bug fixes</dd>
      <dd>Created/incorporated MongoDB with server for user uploads.</dd>
      <dd>Added local storage on server for file uploads.</dd>
      <dd>Updated upload success page to provide upload confirmation.</dd>
      <dd>Configured/deployed on AWS for demo and public access.</dd>
      <dt>Katie Taylor</dt>
      <dd>UI Bug fixes, e.g. fix layout arrangement on upload page</dd>
      <dd>Conducted evaluations with two users</dd>
      <dd>Documentation</dd>
      <dt>Nikita Rana</dt>
      <dd>Implemented faliure page, worked on UI bugs,conducted accessibility evaluation with participant, documentation</dd>
      <dt>Thuan Nguyen</dt>
      <dd>Implemented the About Page, added some CSS styling</dd>
      <dd>Implemented the Contact Page. Received contact information from other members</dd>
       <dd>Conducted evaluations with one new WWU student, and gave suggestion features</dd>
      <dd></dd>
   </dl>

##To Do:
   <ul>
   <li> Connect data visualization with latest changes to render data uploads.</li>
   </ul>
Additional details regarding progress and design decisions/motivation can be found in "Disability Access Navigation Guide R1 Prototype -- Crowdsourcing Team.pdf" and "Disability Access Navigation Guide R2 Prototype -- Crowdsourcing Team.pdf"

##Dependencies
<ul>
   <li> Python </li>
   <li> Flask </li>
   <li>MongoDB</li>
</ul>

##To run this app:
<ol>
   <li> Clone repo to local directory </li>
   <li> cd to the directory where you cloned the repository</li>
   <li> flask run </li>
   <li> Open your web browser and navigate to localhost:5000 </li>
</ol>
