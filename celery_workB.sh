#!/usr/bin/env bash
nohup celery -A com.analysis.tasks.data_analysis.celery worker -P eventlet -c 5 -n workBBBBB -Q default_analysis --loglevel=info &
