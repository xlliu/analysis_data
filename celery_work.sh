#!/usr/bin/env bash
nohup celery -A com.analysis.tasks.data_analysis.celery worker -P eventlet -c 5 -Q default_analysis -n workAAAA --loglevel=info &

