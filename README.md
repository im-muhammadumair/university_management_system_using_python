
# University Management System using Python

## Description
The University Management System is a software application designed in Python by `MUHAMMAD UMAIR` to manage various aspects of a university, including students, teachers, courses, programs, and sub-campuses. It provides functionalities to add, remove, search, and view information about these entities.

## Features
- Manage students
- Manage teachers
- Manage courses
- Manage programs
- Manage sub-campuses

## Installation Instructions
Clone the repository :

   ```bash
   git clone https://github.com/yourusername/University-Management-System.git
   ```
Enter the project repository folder :

   ```bash
   cd University-Management-System
   ```

## Usage Instructions
Run the application:
```bash
python src/main.py
```

## Repository Structure
```
University-Management-System/
│
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point for the application
│   ├── models.py            # Contains class definitions (Member, Student, Teacher, Course, Program, SubCampus)
│   ├── university_management.py  # Contains UniversityManagementSystem class and related methods
│   ├── utils.py             # Any utility functions you might want to include
│   └── data/
│       ├── students.json    # Sample JSON file for student data
│       ├── teachers.json     # Sample JSON file for teacher data
│       ├── courses.json      # Sample JSON file for courses data
│       └── programs.json     # Sample JSON file for programs data
│
├── tests/
│   ├── __init__.py
│   ├── test_models.py        # Tests for models
│   ├── test_management.py     # Tests for the UniversityManagementSystem functionality
│   └── test_utils.py         # Tests for utility functions
│
├── docs/
│   ├── architecture.md        # Overview of the system architecture
│   ├── user_manual.md         # User manual for operating the system
│   └── api_reference.md       # API reference if applicable
│
├── requirements.txt           # Python package dependencies
├── README.md                  # Project overview, installation, usage, etc.
└── LICENSE                    # License information
```

## Contributing
If you'd like to contribute, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.