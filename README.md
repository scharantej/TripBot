## Flask Application Design for Travel Planning and Record

### HTML Files

- **home.html**: This file will serve as the main page of the application. It will contain a form for users to enter travel plan details, including destination, travel dates, and activities.
- **success.html**: This file will be displayed after a user successfully submits the travel plan. It will provide a summary of the plan and allow users to edit or save it.
- **error.html**: This file will be displayed if an error occurs during plan submission. It will provide information on the error and allow users to try again.

### Routes

- **index**: This route will render the home.html file, which displays the form for entering travel plan details.
- **submit_plan**: This route will handle the submission of the travel plan form. It will validate the input and, if valid, save the plan to the database and redirect to the success.html file.
- **edit_plan**: This route will allow users to edit an existing travel plan. It will receive the plan ID as a parameter, retrieve the plan from the database, and render a form with the pre-populated plan details.
- **delete_plan**: This route will allow users to delete an existing travel plan. It will receive the plan ID as a parameter and delete the plan from the database.
- **display_plan**: This route will allow users to view a specific travel plan. It will receive the plan ID as a parameter, retrieve the plan from the database, and render a page displaying the plan details.
- **error**: This route will handle any errors that occur during the application execution. It will render the error.html file, which provides information about the error and allows users to try again.