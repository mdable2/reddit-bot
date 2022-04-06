FROM pytorch/pytorch:1.9.1-cuda11.1-cudnn8-runtime

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]