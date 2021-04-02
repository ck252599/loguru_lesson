# 导入
from loguru import logger
# 输出不同日志的级别
# 输出包含： 时间-级别-模块-内容
logger.debug('这是一条debug日志')
logger.info('这是一条info日志信息')  # 日志格式化
logger.warning('这是一条warning日志')
logger.success('这是一条success日志')
logger.error('这是一条erro日志')