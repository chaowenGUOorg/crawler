FROM python:slim
RUN ["apt", "update"]
RUN ["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"]
RUN ["apt", "install", "-y", "--no-install-recommends", "./google-chrome-stable_current_amd64.deb"]
COPY main.py /usr/local/src/
RUN ["pip", "install", "selenium"]
ENTRYPOINT ["python", "main.py"]
