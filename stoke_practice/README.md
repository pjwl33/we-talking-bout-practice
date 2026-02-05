boltline-assessment/
├── README.md                  # <-- 1. Start here. Write how to run it.
├── .gitignore
├── /server                    # BACKEND (Express + Prisma + Postgres)
│   ├── package.json
│   ├── .env                   # Database URL goes here
│   ├── /prisma
│   │   ├── schema.prisma      # <-- Your Database Model (The "Contract")
│   │   └── /migrations        # Generated SQL history
│   └── /src
│       ├── app.ts             # Entry point (Express setup, CORS)
│       ├── /controllers       # Logic (e.g., partController.ts)
│       └── /routes            # Endpoints (e.g., partRoutes.ts)
│
└── /client                    # FRONTEND (React / Next.js)
    ├── package.json
    ├── next.config.js
    ├── /src
    │   ├── /app               # (If Next.js App Router)
    │   │   ├── page.tsx       # Main Dashboard View
    │   │   └── layout.tsx
    │   ├── /components        # Reusable UI
    │   │   ├── PartHeader.tsx
    │   │   ├── AuditList.tsx
    │   │   └── StatusBadge.tsx
    │   ├── /hooks             # Custom Hooks (usePartData)
    │   └── /types             # Typescript Interfaces (Mirror your Prisma models)
    └── /public                # Static assets (images, icons)

    Interviewer Note: "I'm keeping the controller logic in server.ts for speed during this assessment, but in a production app, I would separate these into /controllers and /services for testability."