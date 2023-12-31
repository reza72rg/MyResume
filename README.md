# My Personal Render Template Website
This is my personal render template website built using the Django framework. It serves as a platform to showcase my skills, projects, and blog posts. The website includes several pages such as the index, contact, about, and skill pages, along with additional features like login, password recovery, and a blog section.

## Features

- **User Authentication**: Users can register, log in, and recover their passwords. Both email and username can be used for login.
- **Blog Section**: Users can view and interact with blog posts, including reading post details, liking posts, and adding comments.
- **Contact Page**: Users can send messages through the contact page, and the website owner can receive and respond to these messages.
- **Skill Page**: A dedicated page to showcase skills and expertise.
- **MySQL Database**: Data, including user information, blog posts, and messages, is stored in a MySQL database.
- **jQuery Integration**: jQuery is used for various functionalities, including displaying messages, handling likes, and refreshing CAPTCHA.

- ## Installation

1. Clone this repository to your local machine:

   bash
   git clone https://github.com/reza72rg
   2. Install the required dependencies:

   bash
   pip install -r requirements.txt
   3. Set up the MySQL database by creating a new database and updating the database settings in the `settings.py` file.

4. Apply database migrations:

   bash
   python manage.py migrate
   5. Start the development server:

   bash
   python manage.py runserver
   6. Open the website in your web browser at `http://localhost:8000`.
  
  ## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
