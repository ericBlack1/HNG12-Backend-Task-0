# FastAPI Project

This is a simple FastAPI project that returns a JSON response with your email, the current datetime in ISO 8601 format (UTC), and a GitHub repository URL.

## Project Description

The project is a RESTful API built using **FastAPI**, a modern Python web framework. It responds to `GET` requests with a JSON object containing:
- Your email address.
- The current datetime in ISO 8601 format (UTC).
- A link to your GitHub repository.

This project demonstrates how to build and deploy a FastAPI application with proper documentation and deployment instructions.

---

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Git (optional, for version control)

### Steps to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/ericBlack1/HNG12-Backend-Task-0.git
   cd your-repo
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and visit:
   - **API Endpoint**: `http://127.0.0.1:8000/`
   - **Swagger UI Documentation**: `http://127.0.0.1:8000/docs`
   - **ReDoc Documentation**: `http://127.0.0.1:8000/redoc`

---

## API Documentation

### Endpoint
- **URL**: `GET /`
- **Response Format**:
  ```json
  {
     "email": "your-email@example.com",
     "current_datetime": "2025-01-30T09:30:00Z",
     "github_url": "https://github.com/yourusername/your-repo"
   }
  ```

### Fields
- `email`: Your email address.
- `current_datetime`: The current datetime in ISO 8601 format (UTC).
- `github_url`: The URL of your GitHub repository.

---

## Example Usage

### Using `curl`
1. Make a `GET` request to the root endpoint:
   ```bash
   curl http://127.0.0.1:8000/
   ```

2. Example response:
   ```json
   {
     "email": "your-email@example.com",
     "current_datetime": "2025-01-30T09:30:00Z",
     "github_url": "https://github.com/yourusername/your-repo"
   }
   ```

### Using a Browser
1. Visit the API endpoint:
   ```
   http://127.0.0.1:8000/
   ```

2. You’ll see the JSON response displayed in your browser.

---

## Deployment

The API is deployed to [Render](https://render.com) (or any other platform of your choice). You can access it at:
- **Live URL**: [https://hng12-backend-task-0.onrender.com](https://hng12-backend-task-0.onrender.com/)



This project was built using **Python** and **FastAPI**. If you're looking to hire skilled Python developers, check out:

👉 [Hire Python Developers at HNG](https://hng.tech/hire/python-developers)

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## Contact

For questions or feedback, please reach out to:
- **Email**: ericangeloawa@gmail.com
- **GitHub**: [ericBlack1](https://github.com/ericBlack1)


This link is relevant to the project's tech stack (Python and FastAPI) and provides value to readers looking to hire skilled developers.

---

Let me know if you need further adjustments! 🚀
