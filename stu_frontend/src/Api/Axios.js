import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Set your backend API base URL
  timeout: 5000, // Optional: Set a timeout for requests
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
