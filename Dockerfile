FROM python:3.6 
RUN pip install fastapi -i https://mirror.nju.edu.cn/pypi/web/simple 
RUN pip install psutil -i https://mirror.nju.edu.cn/pypi/web/simple 
RUN pip install uvicorn[standard] -i https://mirror.nju.edu.cn/pypi/web/simple 
COPY main.py / 
COPY tools.py / 
EXPOSE 8000 
CMD uvicorn main:app --host 0.0.0.0 --port 8000