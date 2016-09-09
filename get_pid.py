ps -ef | grep 'python analysis.py' | grep -v "grep" | awk '{print $2}' > server.pid
ps -ef | grep 'celery -A com.analysis' | grep -v "grep" | awk '{print $2}' > celery.pid
