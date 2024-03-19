FROM python:3.11

EXPOSE 5000

WORKDIR /app

COPY req.txt .
RUN pip install --no-cache-dir --upgrade -r req.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]