import requests
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pytube import YouTube
from bs4 import BeautifulSoup

app = FastAPI()


@app.post("/youtube", tags=["OPTION DOWNLOAD"])
def download_videos_from_youtube(url: str, output_path: str = "D:/Testing photo/python/videos-download"):
    youtubeObject = YouTube(url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=output_path)
        return HTTPException(
            status_code=status.HTTP_200_OK,
            detail="Download is completed successfully",
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An error has occurred",
        )


@app.get("/", tags=["DEFAULT"])
def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status_code": status.HTTP_200_OK,
            "message": "running successfully!",
            "result": None
        }
    )
