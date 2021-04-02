from loguru import logger

# 输出日志到文件
'''
logger.add('文件名',格式化，级别)
'''
logger.add("a.log", format="{time} {level} {message}", level="INFO")
logger.debug("debug")
logger.info("info")


#字符串格式化
logger.info('hello{},hello,{}','python','java')



# 日志保存