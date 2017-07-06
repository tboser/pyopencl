CL_TRACE = False
CL_ENABLE_GL = False
CL_USE_SHIPPED_EXT = True
CL_PRETEND_VERSION = '1.1'
CL_INC_DIR = []
CL_LIB_DIR = [
        '/opt/intelFPGA/16.1/hld/board/s5_ref/linux64/lib', 
        '/opt/intelFPGA/16.1/hld/host/linux64/lib']
CL_LIBNAME = ['alteracl', 'alterahalmmd', 'elf', 'OpenCL']
CXXFLAGS = ['-std=c++0x']
LDFLAGS = ['-Wl,--no-as-needed']
