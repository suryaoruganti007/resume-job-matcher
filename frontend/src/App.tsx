import React, { useState } from 'react';
import { FileText, Briefcase, Zap } from 'lucide-react';
import FileUploadZone from './components/FileUploadZone';
import ResultCard from './components/ResultCard';
import APIService from './services/api';
import { useFileUpload } from './hooks/useFileUpload';
import { FileUploadResponse, MatchResponse, LoadingState } from './types';
import './App.css';

function App() {
  const [resumeFile, setResumeFile] = useState<FileUploadResponse | null>(null);
  const [jobFile, setJobFile] = useState<FileUploadResponse | null>(null);
  const [matchResult, setMatchResult] = useState<MatchResponse | null>(null);
  const [loading, setLoading] = useState<LoadingState>({ uploading: false, matching: false });
  const [error, setError] = useState<string | null>(null);

  const { uploading: resumeUploading, error: resumeError, uploadFile: uploadResume } = useFileUpload();
  const { uploading: jobUploading, error: jobError, uploadFile: uploadJob } = useFileUpload();

  const handleResumeUpload = async (file: File) => {
    const result = await uploadResume(file, 'resume');
    if (result) {
      setResumeFile(result);
      setError(null);
    } else {
      setError(resumeError);
    }
  };

  const handleJobUpload = async (file: File) => {
    const result = await uploadJob(file, 'job');
    if (result) {
      setJobFile(result);
      setError(null);
    } else {
      setError(jobError);
    }
  };

  const handleMatch = async () => {
    if (!resumeFile || !jobFile) {
      setError('Please upload both resume and job description');
      return;
    }

    try {
      setLoading({ ...loading, matching: true });
      setError(null);

      const result = await APIService.matchResumeToJob(
        resumeFile.file_id,
        jobFile.file_id
      );

      setMatchResult(result);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Matching failed. Please try again.');
    } finally {
      setLoading({ ...loading, matching: false });
    }
  };

  const handleReset = () => {
    setResumeFile(null);
    setJobFile(null);
    setMatchResult(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-secondary via-gray-900 to-secondary text-white">
      {/* Header */}
      <header className="border-b border-gray-800 sticky top-0 bg-secondary/80 backdrop-blur-sm z-50">
        <div className="max-w-6xl mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Zap className="w-8 h-8 text-primary" />
              <h1 className="text-3xl font-bold bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">
                Resume-Job Matcher
              </h1>
            </div>
            <span className="text-xs px-3 py-1 bg-primary/20 text-primary rounded-full">
              AI-Powered Matching
            </span>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-6 py-12">
        {/* Error Alert */}
        {error && (
          <div className="mb-8 p-4 bg-danger/20 border border-danger/50 rounded-lg text-danger animate-slideUp">
            <p className="font-semibold">Error: {error}</p>
          </div>
        )}

        {!matchResult ? (
          <div className="space-y-8">
            {/* Upload Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="flex flex-col gap-4">
                <div className="flex items-center gap-2">
                  <FileText className="w-6 h-6 text-primary" />
                  <h2 className="text-xl font-bold text-white">Resume</h2>
                </div>
                <FileUploadZone
                  onFile={handleResumeUpload}
                  title="Upload Resume"
                  description="Drag and drop your resume (PDF or DOCX)"
                  isUploading={resumeUploading}
                  uploadSuccess={!!resumeFile}
                  fileName={resumeFile?.filename}
                />
              </div>

              <div className="flex flex-col gap-4">
                <div className="flex items-center gap-2">
                  <Briefcase className="w-6 h-6 text-accent" />
                  <h2 className="text-xl font-bold text-white">Job Description</h2>
                </div>
                <FileUploadZone
                  onFile={handleJobUpload}
                  title="Upload Job Description"
                  description="Drag and drop the job description (PDF or DOCX)"
                  isUploading={jobUploading}
                  uploadSuccess={!!jobFile}
                  fileName={jobFile?.filename}
                />
              </div>
            </div>

            {/* Match Button */}
            <button
              onClick={handleMatch}
              disabled={!resumeFile || !jobFile || loading.matching}
              className={`w-full py-4 px-6 font-bold rounded-xl transition-all duration-300 transform
                ${resumeFile && jobFile && !loading.matching
                  ? 'bg-gradient-to-r from-primary to-accent hover:shadow-lg hover:shadow-primary/50 hover:scale-105 cursor-pointer'
                  : 'bg-gray-700 opacity-50 cursor-not-allowed'
                }
              `}
            >
              {loading.matching ? (
                <span className="flex items-center justify-center gap-2">
                  <div className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                  Analyzing...
                </span>
              ) : (
                <span className="flex items-center justify-center gap-2">
                  <Zap className="w-5 h-5" />
                  Analyze Match
                </span>
              )}
            </button>
          </div>
        ) : (
          <div className="space-y-8">
            {/* Results Section */}
            <ResultCard
              result={matchResult.results}
              recommendations={matchResult.recommendations}
            />

            {/* Action Buttons */}
            <div className="flex gap-4 justify-center">
              <button
                onClick={handleReset}
                className="px-8 py-3 bg-secondary border-2 border-primary text-primary font-bold rounded-lg hover:bg-primary hover:text-secondary transition-all duration-300"
              >
                Analyze Another
              </button>
              <button
                onClick={() => window.print()}
                className="px-8 py-3 bg-gradient-to-r from-primary to-accent text-secondary font-bold rounded-lg hover:shadow-lg hover:shadow-primary/50 transition-all duration-300"
              >
                Download Report
              </button>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-gray-800 mt-16 py-8 text-center text-gray-500">
        <p>© 2025 Resume-Job Matcher. Powered by AI & NLP.</p>
      </footer>
    </div>
  );
}

export default App;
