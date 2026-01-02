FROM jupyter/base-notebook:python-3.10

WORKDIR /app

COPY services/jupyter/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

