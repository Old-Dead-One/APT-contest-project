# Golf Event Skins Games Project Development Plan

## Overview

The Golf Event Skins Games Management project aims to develop a web application for managing skins games in a golf event. The project will use FastAPI for the backend API development and React for the frontend user interface.

## Goals

- Allow players to create profiles with their first name, last name and email address.
- Allow players to select the local chapter to enter contests.
- Provide a list of available contests for players to enter.
- Display a summary of contests entered by players along with total entrance fees.
- Enable players to confirm their choices and receive payment instructions.

## Testing/Use

### Instalation

1. Initialize a Python virtual environment.
2. Clone repo https://github.com/Old-Dead-One/APT-contest-project.git
3. Install requirements.txt and other required dependencies.
4. Fill db with needed/relavent data either using existing endpoints or sql injection.

## Development Phases

### Phase 1: Backend Development with FastAPI

1. Set up the project directory structure.
2. Initialize a Python virtual environment.
3. Install requirements.txt and other required dependencies.
4. Define models for Player and Contest.
5. Implement API endpoints for player management.
6. Implement API endpoints for contest management.
7. Add data storage functionality to save player data with UUIDs.
8. Write unit tests for API endpoints.
9. Test data persistence and API functionality.

### Phase 2: Frontend Development with React

1. Set up a new React project using Vite.
2. Design and develop React components for user interface elements.
3. Implement forms for player creation and Venmo ID update.
4. Create a component to display available contests with checkboxes for selection.
5. Develop a component to display contest summaries and total entrance fees.
6. Implement data fetching to communicate with the backend API.
7. Style the frontend components using CSS or a CSS framework.
8. Test frontend components and user interactions.

### Phase 3: Integration and Testing

1. Integrate the frontend with the backend API endpoints.
2. Test the integrated application to ensure proper communication between frontend and backend.
3. Conduct end-to-end testing to verify all features and functionalities.
4. Gather feedback from users and stakeholders.
5. Iterate on the project based on feedback and make necessary adjustments.

### Phase 4: Documentation and Deployment

1. Write comprehensive documentation for setting up and running the project.
2. Document the API endpoints, their parameters, and expected responses.
3. Provide instructions for interacting with the frontend interface.
4. Deploy the backend API to a server using a service like Heroku.
5. Deploy the frontend application to a hosting service like Vercel or Netlify.
6. Configure deployment environments for security and performance.

## Timeline

- Phase 1: 6 weeks
- Phase 2: 8 weeks
- Phase 3: 4 week
- Phase 4: 4 week

## Resources and Tools

- Python: Programming language for backend development.
- FastAPI: Web framework for building APIs with Python.
- React: JavaScript library for building user interfaces.
- Axios: Promise-based HTTP client for making requests to the backend API.
- Git: Version control system for managing project code.
- GitHub: Hosting service for Git repositories.
- Visual Studio Code or any preferred code editor for development.

## Team Collaboration

- Use Git branches for feature development and pull requests for code review.
- Conduct regular team meetings to discuss progress and address any issues.
- Use project management tools like Trello or Jira for task tracking and prioritization.

## Glossary

### Player

- Definition: A participant in the golf event who creates a profile with a unique identifier (UUID) and enters their Venmo ID.
- Used in: Backend and Frontend development.

### Contest

- Definition: A competition or game within the golf event, which players can enter for a chance to win prizes.
- Used in: Backend and Frontend development.

### Backend

- Definition: The server-side portion of the application responsible for processing requests, managing data, and interacting with databases.
- Used in: Backend development.

### Frontend

- Definition: The client-side portion of the application responsible for presenting the user interface and interacting with users.
- Used in: Frontend development.

### Venmo ID

- Definition: The unique identifier associated with a player's Venmo account, used for receiving payments.
- Used in: Backend and Frontend development.

### UUID

- Definition: Universally Unique Identifier, a 128-bit identifier used as a unique identifier for players in the system.
- Used in: Backend development for uniquely identifying players.
- Installation: No separate installation required as it's built into Python's standard library.

# Appendix: Dependencies

## Backend Dependencies (Python):

- FastAPI: Web framework for building APIs with Python.
  - Used for developing API endpoints for player and contest management.
  - Installation: `pip install fastapi`
  - Repository: [FastAPI GitHub](https://github.com/tiangolo/fastapi)
- uvicorn: ASGI server for running FastAPI applications.
  - Used for serving the FastAPI application.
  - Installation: `pip install uvicorn`
  - Repository: [uvicorn GitHub](https://github.com/encode/uvicorn)
- pydantic: Data validation and settings management using Python type annotations.
  - Used for defining models and validating input data in FastAPI endpoints.
  - Installation: `pip install pydantic`
  - Repository: [pydantic GitHub](https://github.com/samuelcolvin/pydantic)
- json: Built-in Python library for JSON manipulation.
  - Used for handling JSON data, such as saving player data to a JSON file.
  - No separate installation required.

# Appendix: Dependencies

## Backend Dependencies (Python):

- FastAPI: Web framework for building APIs with Python.
  - Used for developing API endpoints for player and contest management.
  - Installation: `pip install fastapi`
  - Repository: [FastAPI GitHub](https://github.com/tiangolo/fastapi)
- uvicorn: ASGI server for running FastAPI applications.
  - Used for serving the FastAPI application.
  - Installation: `pip install uvicorn`
  - Repository: [uvicorn GitHub](https://github.com/encode/uvicorn)
- pydantic: Data validation and settings management using Python type annotations.
  - Used for defining models and validating input data in FastAPI endpoints.
  - Installation: `pip install pydantic`
  - Repository: [pydantic GitHub](https://github.com/samuelcolvin/pydantic)
- json: Built-in Python library for JSON manipulation.
  - Used for handling JSON data, such as saving player data to a JSON file.
  - No separate installation required.

## Frontend Dependencies (React):

- React: JavaScript library for building user interfaces.
  - Used for developing frontend components and managing application state.
  - Installation: N/A (Included with Create React App)
  - Repository: [React GitHub](https://github.com/facebook/react)
- React Router: Library for routing in React applications.
  - Used for handling navigation between different pages or views in the frontend.
  - Installation: `npm install react-router-dom`
  - Repository: [React Router GitHub](https://github.com/ReactTraining/react-router)
- Axios: Promise-based HTTP client for making requests to the backend API.
  - Used for sending HTTP requests from the frontend to the backend API.
  - Installation: `npm install axios`
  - Repository: [Axios GitHub](https://github.com/axios/axios)
- Redux (optional): State management library for managing application state.
  - Used for managing complex application state across multiple components.
  - Installation: `npm install redux`
  - Repository: [Redux GitHub](https://github.com/reduxjs/redux)
- Redux Thunk (optional): Middleware for handling asynchronous actions in Redux.
  - Used for dispatching asynchronous actions in Redux, such as API requests.
  - Installation: `npm install redux-thunk`
  - Repository: [Redux Thunk GitHub](https://github.com/reduxjs/redux-thunk)
- React Bootstrap or Material-UI (optional): UI component libraries for styling React applications.
  - Used for quickly styling frontend components and creating a cohesive user interface.
  - Installation: For React Bootstrap: `npm install react-bootstrap bootstrap`, For Material-UI: `npm install @mui/material @emotion/react @emotion/styled`
  - Repositories: [React Bootstrap GitHub](https://github.com/react-bootstrap/react-bootstrap), [Material-UI GitHub](https://github.com/mui-org/material-ui)

## Additional Dependency:

- UUID: Universally Unique Identifier, a 128-bit identifier used as a unique identifier for players in the system.
  - Used in: Backend development for uniquely identifying players.
  - Installation: No separate installation required as it's built into Python's standard library.
