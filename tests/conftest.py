import pytest
import smtplib
import os
import sys

#sys.dont_write_bytecode = True

# @pytest.fixture(scope="function",autouse=True)
# def foo():
#     logger = Logger(logger="function setup").getlog()
#     logger.info(" function setup")
#     yield 100
#     logger = Logger(logger="function teardown").getlog()
#     logger.info(" function teardown")

# @pytest.fixture(scope="module")
# def smtp_connection():
#     return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)






# @pytest.fixture(scope="function")
# def log(request):
#     test_path = request.node.parent.name.strip(".py")
#     test_name = request.node.name
#     node_id = request.node.nodeid
#     print(test_path)
#     print(test_name)
#     print(node_id)

#     log_file_path = '%s/%s' % (logs_dir, test_path)
#     print(log_file_path)

#     if not os.path.exists(log_file_path):
#         os.makedirs(log_file_path)
#     logger_obj = logger.make_logger(test_name, log_file_path, node_id)
#     yield logger_obj
#     handlers = logger_obj.handlers
#     for handler in handlers:
#         handler.close()
#         logger_obj.removeHandler(handler)
