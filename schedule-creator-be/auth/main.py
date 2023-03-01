import uvicorn


if __name__ == '__main__':
    print("DB SERVICE INITIATING \n", flush=True)
    uvicorn.run('app:app', host="0.0.0.0", port=5000, reload=True)
