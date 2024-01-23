from extensions.injection_module import register_ioc
from process import Process


if __name__ == '__main__':
    register_ioc()
    p = Process()
