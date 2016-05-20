FROM slave4.wizeye.com.cn:5000/ubuntu-python
COPY disk.py /home/disk.py
CMD python /home/disk.py