FROM django
ADD . /loginMS
WORKDIR /loginMS
RUN pip install -r requirements.txt
CMD ["python3","./manage.py runserver 0.0.0.0:8000"]

# fra youtube video part 1
# FROM python: 3x
# COPY ./loginMS /loginMS
# WORKDIR /loginMS
# RUN pip install -r requirements.txt
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]