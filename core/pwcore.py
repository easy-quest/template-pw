#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def ft():
    """Генерация рандомного имени файла"""
    code = ''
    for i in range(18):
        code += str(random.randint(0,9))
    return code