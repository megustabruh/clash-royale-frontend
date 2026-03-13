# ClashRoyaleFrontend React App

This project is a React frontend created with Vite, intended for deployment on AWS (S3/CloudFront or Amplify). It is set up for integration with a backend script.

## Getting Started

1. **Install dependencies:**
   ```sh
   cd frontend
   npm install
   ```
2. **Start development server:**
   ```sh
   npm run dev
   ```
3. **Build for production:**
   ```sh
   npm run build
   ```

## AWS Deployment
- The `dist` folder contains the production build, ready for deployment to AWS S3/CloudFront or Amplify.
- Configure your AWS deployment pipeline to upload the contents of `dist`.

## Backend Integration
- Update API endpoints in your React app to point to your backend script as needed.

## Project Structure
- `frontend/` - React frontend source code
- `frontend/dist/` - Production build output

---

For more details, see the Vite and React documentation.
