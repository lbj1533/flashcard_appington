## Setup Instructions

1. Clone the repository:
   git clone https://github.com/lbj1533/flashcard_appington.git
   cd flashcard_appington

2. Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Run the application
    python -m flashcard_appington.main

5. Create Flashcards

    This project requires a `flashcards` directory where you can store your own flashcard files. Create a directory structure similar to the one below:
    
    flashcards/ 
    ├── language1/ 
    │   ├── topic1/ 
    │   ├── topic2/ 
    └── language2/ 
        ├── topic1/ 
        └── topic2/