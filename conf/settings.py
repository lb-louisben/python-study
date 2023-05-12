# -*- coding: UTF-8 -*-
"""
@Project    : python-study 
@File       : settings.py
@Author     : louis
@Date       : 5/12/23 12:36 
"""
import os
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
LOG_PATH = rf'{BASE_PATH}/log'


LOGGING_DIR = {
    'version': 1.0,
    'disable_existing_loggers': False,
    # log format
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(threadName)s:%(thread)d [%(name)s] %(levelname)s [%(pathname)s:%(lineno)d] %(message)s',
            'dateformat': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(asctime)s [%(name)s] %(levelname)s %(message)s',
            'dateformat': '%Y-%m-%d %H:%M:%S'
        },
        'test': {
            'format': '%(asctime)s %(message)s'
        },
    },

    'filters': {},

    # log manage
    'handlers': {
        'console_debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_info_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{LOG_PATH}/study.log',
            'maxBytes': 1024 * 1024 * 10,  # 10M
            'backupCount': 10,  # 最多 10 个文件
            'encoding': 'utf-8',
            'formatter': 'standard'
        },
        'file_debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/test.log',
            'encoding': 'utf-8',
            'formatter': 'test'
        }
    },

    # log recoder
    'loggers': {
        'logger1': {
            'handlers': ['console_debug_handler'],
            'level': 'DEBUG',  # 日志级别 DEBUG
            'propagate': False  # 向上更高级别传递logger, 默认为否
        },
        'logger2': {
            'handlers': ['console_debug_handler', 'file_debug_handler'],
            'level': 'DEBUG',  # 日志级别 DEBUG
            'propagate': False  # 向上更高级别传递logger, 默认为否
        },
        'logger3': {
            'handlers': ['console_debug_handler', 'file_info_handler'],
            'level': 'DEBUG',  # 日志级别 DEBUG
            'propagate': False  # 向上更高级别传递logger, 默认为否
        },
    }
}
