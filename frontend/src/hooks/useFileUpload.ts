import { useState } from 'react';
import APIService from '../services/api';
import { FileUploadResponse } from '../types';

interface UseFileUploadResult {
  uploading: boolean;
  error: string | null;
  uploadFile: (file: File, type: 'resume' | 'job') => Promise<FileUploadResponse | null>;
  clearError: () => void;
}

export const useFileUpload = (): UseFileUploadResult => {
  const [uploading, setUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const uploadFile = async (
    file: File,
    type: 'resume' | 'job'
  ): Promise<FileUploadResponse | null> => {
    try {
      setUploading(true);
      setError(null);

      const response = type === 'resume'
        ? await APIService.uploadResume(file)
        : await APIService.uploadJob(file);

      return response;
    } catch (err: any) {
      const errorMessage = err.response?.data?.detail || 'Upload failed';
      setError(errorMessage);
      return null;
    } finally {
      setUploading(false);
    }
  };

  const clearError = () => setError(null);

  return { uploading, error, uploadFile, clearError };
};
