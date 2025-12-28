import React from 'react';
import { CheckCircle, AlertCircle, TrendingUp } from 'lucide-react';
import { MatchResult } from '../types';

interface ResultCardProps {
  result: MatchResult;
  recommendations: string[];
}

const ResultCard: React.FC<ResultCardProps> = ({ result, recommendations }) => {
  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-success';
    if (score >= 60) return 'text-yellow-400';
    return 'text-danger';
  };

  const getScoreBgColor = (score: number) => {
    if (score >= 80) return 'from-success/20 to-transparent';
    if (score >= 60) return 'from-yellow-500/20 to-transparent';
    return 'from-danger/20 to-transparent';
  };

  return (
    <div className="space-y-6 animate-slideUp">
      {/* Score Section */}
      <div className={`bg-gradient-to-br ${getScoreBgColor(result.match_score)} rounded-xl p-8 border border-primary/20`}>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-2xl font-bold text-white">Match Analysis</h2>
          <TrendingUp className={`w-8 h-8 ${getScoreColor(result.match_score)}`} />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center">
            <div className={`text-5xl font-bold ${getScoreColor(result.match_score)} mb-2`}>
              {result.match_score.toFixed(1)}%
            </div>
            <p className="text-gray-400">Overall Match Score</p>
          </div>

          <div className="text-center border-l border-r border-gray-700">
            <div className="text-3xl font-bold text-primary mb-2">
              {(result.similarity_score * 100).toFixed(1)}%
            </div>
            <p className="text-gray-400">Semantic Similarity</p>
          </div>

          <div className="text-center">
            <div className="text-3xl font-bold text-accent mb-2">
              {result.matched_skills.length}/{result.matched_skills.length + result.missing_skills.length}
            </div>
            <p className="text-gray-400">Skills Matched</p>
          </div>
        </div>
      </div>

      {/* Skills Section */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Matched Skills */}
        <div className="bg-secondary/50 rounded-xl p-6 border border-success/20">
          <div className="flex items-center gap-2 mb-4">
            <CheckCircle className="w-5 h-5 text-success" />
            <h3 className="text-lg font-semibold text-white">Matched Skills</h3>
          </div>
          <div className="flex flex-wrap gap-2">
            {result.matched_skills.length > 0 ? (
              result.matched_skills.map((skill, index) => (
                <span
                  key={index}
                  className="px-3 py-1 bg-success/20 text-success text-sm rounded-full border border-success/30"
                >
                  {skill.skill}
                </span>
              ))
            ) : (
              <p className="text-gray-400 text-sm">No matched skills</p>
            )}
          </div>
        </div>

        {/* Missing Skills */}
        <div className="bg-secondary/50 rounded-xl p-6 border border-danger/20">
          <div className="flex items-center gap-2 mb-4">
            <AlertCircle className="w-5 h-5 text-danger" />
            <h3 className="text-lg font-semibold text-white">Missing Skills</h3>
          </div>
          <div className="flex flex-wrap gap-2">
            {result.missing_skills.length > 0 ? (
              result.missing_skills.map((skill, index) => (
                <span
                  key={index}
                  className="px-3 py-1 bg-danger/20 text-danger text-sm rounded-full border border-danger/30"
                >
                  {skill}
                </span>
              ))
            ) : (
              <p className="text-gray-400 text-sm">All skills matched!</p>
            )}
          </div>
        </div>
      </div>

      {/* Explanation */}
      <div className="bg-secondary/50 rounded-xl p-6 border border-primary/20">
        <h3 className="text-lg font-semibold text-white mb-3">Analysis</h3>
        <p className="text-gray-300 leading-relaxed">{result.explanation}</p>
      </div>

      {/* Recommendations */}
      <div className="bg-secondary/50 rounded-xl p-6 border border-accent/20">
        <h3 className="text-lg font-semibold text-white mb-4">Recommendations</h3>
        <ul className="space-y-3">
          {recommendations.map((rec, index) => (
            <li key={index} className="flex gap-3 text-gray-300">
              <span className="text-accent font-bold">→</span>
              <span>{rec}</span>
            </li>
          ))}
        </ul>
      </div>

      {/* Metadata */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
        <div className="bg-secondary/50 rounded-lg p-4 border border-gray-700">
          <p className="text-2xl font-bold text-primary">
            {result.experience_match ? '✓' : '✗'}
          </p>
          <p className="text-xs text-gray-400 mt-2">Experience Match</p>
        </div>
        <div className="bg-secondary/50 rounded-lg p-4 border border-gray-700">
          <p className="text-2xl font-bold text-primary">
            {result.education_match ? '✓' : '✗'}
          </p>
          <p className="text-xs text-gray-400 mt-2">Education Match</p>
        </div>
        <div className="bg-secondary/50 rounded-lg p-4 border border-gray-700">
          <p className="text-2xl font-bold text-primary">
            {result.matched_skills.length}
          </p>
          <p className="text-xs text-gray-400 mt-2">Total Matched</p>
        </div>
        <div className="bg-secondary/50 rounded-lg p-4 border border-gray-700">
          <p className="text-2xl font-bold text-primary">
            {result.missing_skills.length}
          </p>
          <p className="text-xs text-gray-400 mt-2">Gap Areas</p>
        </div>
      </div>
    </div>
  );
};

export default ResultCard;
