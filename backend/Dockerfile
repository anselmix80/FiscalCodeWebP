FROM python:3.13-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /backend
ENV HOME=/backend
WORKDIR $HOME
RUN mkdir $HOME/static
ADD requirements.txt /backend/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY scripts/start*.sh /
ADD . /backend/
EXPOSE 8000
CMD ["sh", "/start_prd.sh"]