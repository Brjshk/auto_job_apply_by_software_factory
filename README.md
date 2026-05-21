# Auto Job Apply Application

## Overview
The Auto Job Apply Application is a web-based tool designed to automate the job application process. Users can input their job preferences, upload their resumes, and the application will automatically apply to selected job postings on various job boards. The application aims to save time and streamline the job search process for users.

## Features
- User Registration and Authentication
- User Profile Management (resume upload, job preferences)
- Job Search (fetching job postings based on user preferences)
- Auto-Application (apply to selected job postings)
- Application Status Tracking (view applied jobs and their statuses)
- Email Notifications (confirmation of applications)

## Technology Stack
- **Backend**: Python with FastAPI
- **Frontend**: HTML, CSS, JavaScript (with Fetch API)
- **Database**: SQLite for simplicity

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/auto-job-apply.git
   cd auto-job-apply
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn backend.main:app --reload
   ```
4. Access the frontend at `http://localhost:8000`.

## License
This project is licensed under the MIT License.