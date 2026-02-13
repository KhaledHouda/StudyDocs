#!/usr/bin/env python3

'''
@author: Christian Wressnegger and Stefan Czybik
'''
import datetime
import os
import unittest
import subprocess
import shlex
import uuid

unittest.TestLoader.sortTestMethodsUsing = None
PYTHON = "python3"
PYERROR = "For running your solutions we call '{}'.\nThe name might be different for your installation (e.g. on Windows)\n"


class Ex07(unittest.TestCase):
    TASKS = 0
    MY_DIR = os.path.dirname(os.path.abspath(__file__))
    MY_DIR = os.path.join(MY_DIR, '../')

    def vuln_read_urls(self, c):
        if c == "stack-c":
            program = "canary"
        else:
            program = "program2"
        try:
            cmd = None
            secret = str(uuid.uuid4())[0:8]
            file = os.path.join(self.MY_DIR, "{}.sh".format(c))
            with open(file, 'r') as f:
                for line in f:
                    cmd = line
                    break

            self.assertTrue(cmd and cmd.startswith("./{}".format(program)),
                            "Please start the command line from the local directory with './{}".format(program))
            self.assertTrue(cmd, "No command line string included :/")
            if c == "local-c":
                s_cmd = shlex.split(cmd)
                self.assertIn(s_cmd[1], ["'sl'", '"sl"', "sl"], "Don't try to start anything else then sl")

                t_cmd = cmd.split(s_cmd[1])
                if t_cmd[0][-1] in ["'", '"', " "]:
                    delimiter = t_cmd[0][-1]
                else:
                    self.assertTrue(False, "No correct Escape characters")
                if t_cmd[1][0] != delimiter:
                    self.assertTrue(False, "No correct Escape characters")
                if delimiter == " ":
                    cmd = cmd.replace(s_cmd[1], "'echo {}'".format(secret), 1)
                else:
                    cmd = cmd.replace(s_cmd[1], "echo {}".format(secret), 1)

            print(cmd)

            p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, shell=True, cwd="/{}".format(program))

            out, err = p.communicate()

            out_lines = [line.decode("utf-8") for line in out.split(b'\n')]
            err_lines = [line.decode("utf-8") for line in err.split(b'\n')]
            if c == "stack-c":
                self.assertEqual(p.returncode, 0, "Execution failes!\n{}".format(err.decode("utf-8")))
                self.assertEqual(out_lines, ['Superuser!', ''], "Attack not successful")
            elif c == "local-a":
                self.assertNotEqual(p.returncode, 0, "Program Exit successful!")
                self.assertIn('Segmentation fault (core dumped)', err_lines, "Successful Segmentation fault")
            elif c == "local-b":
                self.assertEqual(p.returncode, 0, "Execution failes!\n{}".format(err.decode("utf-8")))
                self.assertEqual(out_lines[2], out_lines[3])
                for i in 0, 1:
                    try:
                        datetime.datetime.strptime(out_lines[i], '%a %b %d %X %Z %Y')
                    except ValueError:
                        self.assertTrue(False, "")
            elif c == "local-c":
                self.assertEqual(p.returncode, 0, "Execution failes!\n{}".format(err.decode("utf-8")))
                self.assertIn(secret, out_lines, "Attack not successful!")

        except IOError:
            self.assertTrue(False, "Unable to read file")

    def test_01_stack_c(self):
        self.vuln_read_urls("stack-c")
        Ex07.TASKS += 1

    def test_02_local_a(self):
        self.vuln_read_urls("local-a")
        Ex07.TASKS += 1

    def test_02_local_b(self):
        self.vuln_read_urls("local-b")
        Ex07.TASKS += 1

    def test_02_local_c(self):
        self.vuln_read_urls("local-c")
        Ex07.TASKS += 1


if __name__ == "__main__":
    unittest.main()
