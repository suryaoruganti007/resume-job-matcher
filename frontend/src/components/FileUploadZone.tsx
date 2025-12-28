import React from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, CheckCircle, AlertCircle } from 'lucide-react';

interface FileUploadZoneProps {
  onFile: (file: File) => void;
  title: string;
  description: string;
  isUploading?: boolean;
  uploadSuccess?: boolean;
  fileName?: string;
  accept?: Record<string, string[]>;
}

const FileUploadZone: React.FC<FileUploadZoneProps> = ({
  onFile,
  title,
  description,
  isUploading = false,
  uploadSuccess = false,
  fileName,
  accept = { 'application/pdf': ['.pdf'], 'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'] },
}) => {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        onFile(acceptedFiles[0]);
      }
    },
    accept,
    disabled: isUploading,
  });

  return (
    <div
      {...getRootProps()}
      className={`relative border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all duration-300
        ${isDragActive
          ? 'border-primary bg-primary/10 scale-105'
          : 'border-gray-400 hover:border-primary hover:bg-primary/5'
        }
        ${isUploading ? 'opacity-60 cursor-not-allowed' : ''}
        ${uploadSuccess ? 'border-success bg-success/10' : ''}
      `}
    >
      <input {...getInputProps()} />

      <div className="flex flex-col items-center justify-center gap-3">
        {uploadSuccess ? (
          <>
            <CheckCircle className="w-12 h-12 text-success animate-bounce" />
            <div>
              <h3 className="text-lg font-semibold text-success mb-1">{fileName}</h3>
              <p className="text-sm text-gray-400">File uploaded successfully</p>
            </div>
          </>
        ) : isUploading ? (
          <>
            <div className="w-12 h-12 border-4 border-primary/30 border-t-primary rounded-full animate-spin" />
            <p className="text-sm text-gray-400">Uploading...</p>
          </>
        ) : (
          <>
            <Upload className="w-12 h-12 text-primary" />
            <div>
              <h3 className="text-lg font-semibold text-white mb-1">{title}</h3>
              <p className="text-sm text-gray-400">{description}</p>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default FileUploadZone;
