# Vue Music Player

This project is a music player website created for practice purposes. Anyone can register, upload MP3 files, and play MP3 files on this platform.

You can test the project using the provided [DEMO](https://music-player.de-website.com/)

The project mainly utilizes Vue 3, FastAPI, and MongoDB Atlas. The DEMO is deployed using AWS S3 and Lambda.

## Local Testing

If you want to test this project locally, simply clone the repository and configure the .env files:

1. Configure the .env file for FastAPI located in `/backend`.
   Environment variables include:

   - MONGODB_URI={your_mongodb_uri}
   - SECRET_KEY={any_secret}
   - ALGORITHM={HS256}

   After configuration, navigate to `/backend` and run:

   ```bash
   pip install -r requirements.txt
   uvicorn main:app
   ```

   This will start the backend server.

2. Configure the .env file for Vite located in the root directory.
   Environment variables include:

   - VITE_API_URL={`http://localhost:8000`}

   After configuration, run:

   ```bash
   npm install
   npm run dev
   ```

   This will start the frontend server. You can access the project at `http://localhost:5173/`.

## Contact

If you have any questions or feedback, feel free to contact me.
