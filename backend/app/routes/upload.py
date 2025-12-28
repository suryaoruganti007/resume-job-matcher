from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.core.config import get_settings
from app.services.file_service import FileService
from app.services.nlp_service import NLPService
from app.models.schemas import FileUploadResponse
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

# Initialize services
file_service = FileService()
nlp_service = NLPService()

@router.post("/resume", response_model=FileUploadResponse)
async def upload_resume(file: UploadFile = File(...), settings = Depends(get_settings)):
    """Upload a resume file"""
    
    try:
        # Validate file
        if not FileService.allowed_file(file.filename):
            raise HTTPException(
                status_code=400,
                detail=f"File type not allowed. Allowed types: {FileService.ALLOWED_EXTENSIONS}"
            )
        
        # Read file content
        content = await file.read()
        
        if len(content) > FileService.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds limit (50MB)"
            )
        
        # Save file
        file_id, file_path = file_service.save_upload(
            settings.UPLOAD_DIR,
            content,
            file.filename
        )
        
        # Extract text
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        extracted_text = file_service.extract_text(file_path, file_ext)
        
        # Process with NLP
        nlp_result = nlp_service.process_document(extracted_text, "resume")
        
        logger.info(f"Resume uploaded and processed: {file_id}")
        
        return FileUploadResponse(
            file_id=file_id,
            filename=file.filename,
            file_type="resume",
            upload_timestamp=datetime.now(),
            extracted_text=extracted_text[:500]  # Return first 500 chars
        )
    
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error uploading resume: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/job", response_model=FileUploadResponse)
async def upload_job(file: UploadFile = File(...), settings = Depends(get_settings)):
    """Upload a job description file"""
    
    try:
        # Validate file
        if not FileService.allowed_file(file.filename):
            raise HTTPException(
                status_code=400,
                detail=f"File type not allowed. Allowed types: {FileService.ALLOWED_EXTENSIONS}"
            )
        
        # Read file content
        content = await file.read()
        
        if len(content) > FileService.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds limit (50MB)"
            )
        
        # Save file
        file_id, file_path = file_service.save_upload(
            settings.UPLOAD_DIR,
            content,
            file.filename
        )
        
        # Extract text
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        extracted_text = file_service.extract_text(file_path, file_ext)
        
        # Process with NLP
        nlp_result = nlp_service.process_document(extracted_text, "job_description")
        
        logger.info(f"Job description uploaded and processed: {file_id}")
        
        return FileUploadResponse(
            file_id=file_id,
            filename=file.filename,
            file_type="job_description",
            upload_timestamp=datetime.now(),
            extracted_text=extracted_text[:500]
        )
    
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error uploading job description: {e}")
        raise HTTPException(status_code=500, detail=str(e))
