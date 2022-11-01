Expenses Tracker


Expenses Tracker is an application that allows you to create your own profile (name, profile picture, and budget), create, edit, delete expenses and track your budget. You are also able to edit your profile data and delete your profile.

1.	Skeleton
You are provided with all the needed HTML pages, images, and CSS for the project.
2.	Database

You will need 2 models:

•	Profile
o	First name
	Character field, required.
	 It should have at least 2 characters and maximum - 15 characters.
	The name should consist only of letters. Otherwise, raise ValidationError with the message: "Ensure this value contains only letters."
o	Last name 
	Character field, required.
	It should have at least 2 characters and maximum - 15 characters.
	The name should consist only of letters. Otherwise, raise ValidationError with the message: "Ensure this value contains only letters."
o	Budget
	Float field, required. The budget is 0 by default.
	The budget should not be below 0, when created or edited.
o	Profile Image
	Image field, optional. The picture is user.png (located in the resources) by default; if no image is uploaded)
	The max size limit is 5MB (inclusive). Otherwise, raise ValidationError with the message: "Max file size is 5.00 MB"


•	Expense
o	Title
	Character field, required.
	 It should consist of a maximum of 30 characters.
o	Expense Image
	URL field, required.
o	Description
	Text field, optional.
o	Price
	Float field, required.


3.	Routes
•	http://localhost:8000/ - home page
•	http://localhost:8000/create/ - create expense page
•	http://localhost:8000/edit/<id>/ - edit expense page
•	http://localhost:8000/delete/<id>/ - delete expense page
•	http://localhost:8000/profile/ - profile page
•	http://localhost:8000/profile/edit/ - profile edit page
•	http://localhost:8000/profile/delete/ - delete profile page

4.	Pages
Home Page
Template files: "home-no-profile.html"; "home-with-profile.html"
If there is no profile created yet, the home page shows a form for profile creation. It consists of:
•	A "Budget:", a "First Name:", a "Last Name:", and a "Profile Image:" fields. 
o	Only the "Profile Image:" field uses a CSS style class called "form-file".
•	A button "Submit". 
o	When you click on it, if the profile is successfully created, you should be redirected to the home page, showing a template for a home page with a profile.
o	Otherwise, the form should show the appropriate validation errors.
There is also a button at the left side of the navigation bar called "Expenses Tracker". It leads to the home page. # base.py, hfer ex. Tracket put {% url….%}

 

When you click on the "Submit" button, if the profile is successfully created, you should be redirected to the same page, showing a template for a home page with a profile. 
In addition to the button "Expenses Tracker", on the right side of the navigation bar is a button "Profile"  that leads to the profile page. (if we have profile, in not profile –don’t show) 2:06
When there are no expenses created, you should only see the headline "My Expenses" and the button "Add Expense" that leads to the create expense page:


If there are a profile and expenses, the page should have the following:
•	A headline "Summary"
•	A summary of all your expenses - the first number (in blue) is your budget, the following numbers (in red) are the prices of each product, the last number (in green) is the budget left. All of them should be formatted to the second decimal point.
•	A headline "My Expensese"
•	A button "Add Expense" that leads to the create expense page.
•	A container for each expense showing the title, the image, the description (if any), and the price for the expense. In each container, there should be two buttons: 
o	"Edit" - leading to edit expense page.
o	"Delete" - leading to delete expense page.



Create Expense Page
Template file: "expense-create.html"
This page contains an expense creation form. The page should have the following:
•	A navigation bar containing "Expenses Tracker" and "Profile" buttons.
•	A headline "Create Expense".
•	A form for creating an expense with "Title:", "Description:", "Link to Image:", and "Price:" fields.
•	A button "Create". 
o	When you click on it, if the expense is successfully created, you should be redirected to the home page, showing a template for a home page with a profile.
o	Otherwise, the form should show the appropriate validation errors.

Edit Expense Page
Template file: "expense-edit.html"
On the page, the form must be filled with the data of the expense we want to edit. When you click on the "Edit" button:
•	If the expense is successfully edited, you should be redirected to the home page, showing a template for a home page with a profile 
•	Otherwise, the form should show the appropriate validation errors.


Delete Expense Page
Template file: "expense-delete.html"
On the page, the form must be filled with the data of the expense, and the fields should be disabled. When you click on the "Delete", the expense is deleted from the database, and you should be redirected to the home page, showing a template for a home page with a profile.
The deleted expense should be no longer visible in the app.


Profile Page
Template file: "profile.html"
This page contains the user data. It should have the following:
•	A navigation bar containing "Expenses Tracker" and "Profile" buttons.
•	A headline "Your Profile"
•	A container consisting of:
o	The user's full name (separated by a single space)
o	The profile image (if there is one, otherwise, show the default user.png image)
o	A paragraph "Total Items Bought: {total_number_of_items}" that shows the total number of items existing in the database.
o	A paragraph "Budget Left: {budget_left}$ " that shows the budget left after deduction of all expenses. It should be formatted to the second decimal point.
o	An "Edit Profile" button that leads to the edit profile page
o	A "Delete Profile" button that leads to the delete profile page


Edit Profile Page
Template file: "profile-edit.html"
On the page, the form must be filled with the data of the profile we want to edit. When you click on the "Edit" button:
•	If the profile is successfully edited, you should be redirected to the profile page, showing a template filled with edited profile data
•	Otherwise, the form should show the appropriate validation errors.


Delete Profile Page
Template file: "profile-delete.html"
Deleting a profile should delete the profile info and all expenses. After deletion, the user should be redirected to the home page with no profile.
