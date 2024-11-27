FROM python:3.10 as builder

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"


COPY requirements.txt ./

RUN pip install -r requirements.txt

FROM python:3.10-slim

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

COPY --from=builder /opt/venv/ /opt/venv

EXPOSE 8000

CMD python main.py