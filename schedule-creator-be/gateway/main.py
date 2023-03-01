import uvicorn
import pika

if __name__ == '__main__':
    print("DB SERVICE INITIATING \n", flush=True)
    uvicorn.run('app:app', host="0.0.0.0", port=8080, reload=True)
