# Contributing to NASA APOD Viewer

Thank you for considering contributing to this project! Here's how you can help improve the NASA APOD Viewer application.

## Development Environment Setup

1. **Fork and clone the repository**
   ```
   git clone https://github.com/YOUR-USERNAME/Final-project.git
   cd Final-project
   ```

2. **Set up a virtual environment**
   ```
   # For Windows:
   python -m venv .venv
   .venv\Scripts\activate

   # For macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```
   cd FinalCopy
   pip install -r Requirements.txt
   ```

4. **Running the application for development**
   ```
   # From the FinalCopy directory
   python -m src.main  # or python3 -m src.main
   ```

## Coding Guidelines

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions small and focused on a single task
- Write cross-platform code that works on Windows, macOS, and Linux

## Pull Request Process

1. Create a new branch for your feature or bugfix
   ```
   git checkout -b feature/your-feature-name
   ```

2. Make your changes, following the coding guidelines

3. Test your changes on multiple platforms if possible

4. Update the README.md if needed, especially if you've added new features or dependencies

5. Commit your changes with clear commit messages
   ```
   git commit -m "Add feature: brief description of what you did"
   ```

6. Push to your fork
   ```
   git push origin feature/your-feature-name
   ```

7. Open a Pull Request against the main repository

## Testing

Before submitting a pull request, please test your changes:

- Ensure the application runs without errors
- Test any UI changes to make sure they display correctly
- Verify that images load and save properly
- If possible, test on multiple platforms (Windows/macOS/Linux)

## Feature Ideas for Contributors

Here are some ideas for features you could add to improve the application:

- Add the ability to browse previous days' images
- Implement a favorites system
- Add a settings page to customize the UI
- Create a dark/light theme toggle
- Add ability to share images to social media
- Implement keyboard shortcuts for common actions

Thank you for contributing to the NASA APOD Viewer project!
