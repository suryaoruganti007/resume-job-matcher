import axios, { AxiosInstance } from 'axios';
import { FileUploadResponse, MatchResponse } from '../types';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

class APIService {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Response interceptor
    this.client.interceptors.response.use(
      response => response,
      error => {
        console.error('API Error:', error.response?.data || error.message);
        throw error;
      }
    );
  }

  async uploadResume(file: File): Promise<FileUploadResponse> {
    const formData = new FormData();
    formData.append('file', file);

    const response = await this.client.post<FileUploadResponse>(
      '/upload/resume',
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    return response.data;
  }

  async uploadJob(file: File): Promise<FileUploadResponse> {
    const formData = new FormData();
    formData.append('file', file);

    const response = await this.client.post<FileUploadResponse>(
      '/upload/job',
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }
    );

    return response.data;
  }

  async matchResumeToJob(
    resumeId: string,
    jobId: string
  ): Promise<MatchResponse> {
    const response = await this.client.post<MatchResponse>(
      '/match/analyze',
      {
        resume_id: resumeId,
        job_id: jobId,
      }
    );

    return response.data;
  }

  async healthCheck(): Promise<any> {
    const response = await this.client.get('/match/health');
    return response.data;
  }
}

export default new APIService();
