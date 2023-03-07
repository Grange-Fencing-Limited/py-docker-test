# Use Python 3.9.1
FROM python:3.9.1
# Copy everything to the app DIR
ADD . /app
# From now on we are referring to this DIR
WORKDIR /app
# Install module requirements
RUN pip install -r requirements.txt
# Run main.py using Python
CMD ["python", "main.py"]