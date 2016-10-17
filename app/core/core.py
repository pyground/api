import os
from datetime import datetime
import subprocess


PATH = os.path.dirname(os.path.abspath(__file__))

UPLOAD_PATH = os.path.join(PATH, 'uploads')

PYTHON_VERSIONS = {
    'python276': 'python2',
    'python343': 'python3',
}


class ModuleHandler(object):

    def check_integraty(self, text_as_module):
        """
        TODO
        """
        return True

    def clean_stdout(self, stdout):
        """
        TODO
        """
        return stdout

    def clean_stderr(self, stderr):
        """
        TODO
        """
        return stderr

    def run_as_module(self, text_as_module, interpreter='python3'):
        """
        -----------------------------------
        STDERR
        -----------------------------------
        def test():
            new_list = []
            for i in range(1, 10000):
                new_list.append(i*5-1)

        result = test()
        for i in result:
            print('OBA OBA: {}'.format(i))

        -----------------------------------
        STDOUT
        -----------------------------------
        def test():
            new_list = []
            for i in range(1, 10000):
                new_list.append(1*5-1)
            return new_list

        result = test()
        for i in result:
            print('OBA OBA: {}'.format(i))

        """

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        module_name = '{}.py'.format(timestamp)
        module_path = os.path.join(UPLOAD_PATH, module_name)

        with open(module_path, 'w') as f:
            self.check_integraty(text_as_module)
            f.write(text_as_module)

        python_interpreter = PYTHON_VERSIONS.get(interpreter, interpreter)

        popen = subprocess.Popen(
            [python_interpreter, module_path],
            bufsize=2,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        stdout, stderr = popen.communicate(timeout=5)

        stderr = self.clean_stderr(stderr)
        if stderr:
            return stderr

        stdout = self.clean_stdout(stdout)
        return stdout
