.
├── README.md
├── apps
│   ├── auth
│   │   ├── main.py
│   │   ├── models
│   │   │   ├── share_users.py
│   │   │   ├── shared_user_sessions.py
│   │   │   └── users.py
│   │   ├── routers
│   │   │   ├── oauth.py
│   │   │   └── sign_up.py
│   │   └── utils
│   │       └── jwt_handler.py
│   ├── aws
│   │   ├── main.py
│   │   ├── routers
│   │   │   └── files.py
│   │   └── utils
│   │       ├── file_handler.py
│   │       └── kms_handler.py
│   ├── core
│   │   ├── celery
│   │   │   ├── config.py
│   │   │   ├── tasks.py
│   │   │   └── utils.py
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── main.py
│   │   └── utils
│   │       └── redis_handler.py
│   ├── rbac
│   │   ├── config
│   │   ├── main.py
│   │   ├── middlewares
│   │   │   └── casbin_middleware.py
│   │   ├── models
│   │   │   ├── models.py
│   │   │   └── shared_models.py
│   │   ├── routers
│   │   │   ├── groups.py
│   │   │   ├── policies.py
│   │   │   └── roles.py
│   │   └── utils
│   └── sast
│       ├── crud
│       ├── dependencies
│       │   └── verify_token.py
│       ├── main.py
│       ├── models
│       │   ├── models.py
│       │   └── shared_models.py
│       ├── routers
│       │   ├── organisations.py
│       │   ├── projects.py
│       │   ├── repositories.py
│       │   └── scans.py
│       ├── schemas
│       └── utils
│           └── celery_tasks.py
├── migrations
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── templates
└── tests
    ├── conftest.py
    └── userflows
        ├── test_auth.py
        └── test_create_org.py

28 directories, 41 files
