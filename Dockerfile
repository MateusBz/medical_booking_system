FROM python:3.6.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /home/mateusz/django_projects/medical_booking_system

# Install dependencies
COPY Pipfile Pipfile.lock /home/mateusz/django_projects/medical_booking_system/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /home/mateusz/django_projects/medical_booking_system/
