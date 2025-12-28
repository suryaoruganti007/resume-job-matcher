export interface FileUploadResponse {
  file_id: string;
  filename: string;
  file_type: 'resume' | 'job_description';
  upload_timestamp: string;
  extracted_text?: string;
}

export interface SkillMatch {
  skill: string;
  matched: boolean;
  frequency?: number;
}

export interface MatchResult {
  match_score: number;
  similarity_score: number;
  matched_skills: SkillMatch[];
  missing_skills: string[];
  experience_match: boolean;
  education_match: boolean;
  explanation: string;
  timestamp: string;
}

export interface MatchResponse {
  resume_id: string;
  job_id: string;
  results: MatchResult;
  recommendations: string[];
}

export interface UploadProgress {
  resume: boolean;
  job: boolean;
}

export interface LoadingState {
  uploading: boolean;
  matching: boolean;
}
