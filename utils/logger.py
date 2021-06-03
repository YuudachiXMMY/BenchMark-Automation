import os, time
import logging

def logger(logName, dir=''):
    '''
    Return a logger with name in format '%Y-%m-%d-%H.%M' under "./Logs/" folder

    @param:
    - format: logName.log
    - location: ./Logs/%Y-%m-%d-%H.%M

    @RETURN:
        - A logger for logging.
        - None - EXCEPTION occurred.
    '''
    try:
        ####################################################################################################
        ## Logging
        # 第一步，创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.NOTSET)
        # 第二步，创建一个handler，用于写入日志文件
        rq = time.strftime('%Y-%m-%d-%H.%M.%S', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/' + rq

        if dir != '':
            log_path = log_path + '/' + dir + '/'
        # 判断结果
        if not os.path.exists(log_path):
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(log_path)

        fh = logging.FileHandler(log_path + "_" + logName + '.log', mode='w')
        fh.setLevel(logging.WARNING) # 输出到file的log等级的开关
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)  # 输出到console的log等级的开关
        # 第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        # 第四步，将logger添加到handler里面
        logger.addHandler(fh)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        # # 日志
        # logger.debug('this is a logger debug message')
        # logger.info('this is a logger info message')
        # logger.warning('this is a logger warning message')
        # logger.error('this is a logger error message')
        # logger.critical('this is a logger critical message')
        ####################################################################################################
        return logger
    except Exception:
        logger.error("Exception Occurred", exc_info=True)
        return None