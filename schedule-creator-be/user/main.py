import uvicorn
from dotenv import load_dotenv
load_dotenv()


if __name__ == '__main__':
    print("USER SERVICE INITIATING \n", flush=True)
    uvicorn.run('app:app', host="0.0.0.0", port=8000, reload=True)