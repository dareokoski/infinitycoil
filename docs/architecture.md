infinitycoil/
├── client/               # Godot Project (Frontend)
│   ├── ui/              # UI Scenes (Main UI, Post Feed, Profile)
│   ├── scripts/         # GDScript Files
│   │   ├── network/     # Handles API Requests
│   │   ├── ui/          # UI Handling Scripts
│   │   ├── auth.gd      # Login & Signup Handling
│   │   ├── feed.gd      # Fetch & Display Posts
│   ├── assets/          # Images, Icons, Sounds
│   ├── scenes/          # Godot Scenes
│   │   ├── main.tscn    # Main App Scene
│   │   ├── login.tscn   # Login Screen
│   │   ├── feed.tscn    # Post Feed UI
│   │   ├── profile.tscn # User Profile UI
│   ├── project.godot    # Godot Project File
│   ├── config.json      # Stores API URL & Settings
│
├── server/              # Backend API Server
│   ├── api/             # API Routes
│   │   ├── auth.py      # User Authentication
│   │   ├── posts.py     # Post Handling
│   │   ├── feed.py      # Fetching Posts
│   ├── database/        # Database Files
│   ├── app.py           # Main API Server File (FastAPI or Node.js)
│   ├── requirements.txt # Python Dependencies
│
├── LICENSE
├── README.md
└── .gitignore