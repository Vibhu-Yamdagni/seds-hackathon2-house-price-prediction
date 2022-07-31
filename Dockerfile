FROM python:3.10
WORKDIR /opt/house_price_prediction
COPY requirements.txt /opt/house_price_prediction
EXPOSE 5000
RUN pip install -r ./requirements.txt
COPY . /opt/house_price_prediction
CMD ["python", "api.py"]