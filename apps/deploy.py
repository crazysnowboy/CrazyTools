from packages.Crazylib import crazylib
import sys
import os

def deploy_to_pypi():

    envs_dict = os.environ
    home_path= envs_dict["HOME"]
    # home_path="data"
    pypirc_file = os.path.join(home_path,".pypirc")
    pip_ini_file = os.path.join(home_path,".pip/pip.conf")
    config_str=crazylib.ReadLines2OneLine("docs/pypirc")
    crazylib.WriteStringLine(pypirc_file,config_str)


    info_str = crazylib.ReadLines2OneLine(pypirc_file)
    print("pypirc=")
    print(info_str)

    info_str = crazylib.ReadLines2OneLine(pip_ini_file)
    print("pip_conf=")
    print(info_str)


    package_dir="packages/crazylib"
    os.chdir(package_dir)

    # cmd0="python -m pip install --user --upgrade twine"
    # os.system(cmd0)

    cmd1="python setup.py sdist"
    os.system(cmd1)

    cmd2="twine upload dist/* --verbose"
    os.system(cmd2)
    #
    cmd_install="python3 -m pip install --index-url https://upload.pypi.org/legacy/ crazylib"
    # os.system(cmd_install)


def deploy_link_to_annconda():
    envs_dict = os.environ
    home_path= envs_dict["HOME"]

    conda_dirs=[".conda","anaconda3"]
    for conda_dir in conda_dirs:
        conda_root=os.path.join(home_path,conda_dir)
        envs = os.path.join(conda_root,"envs")
        envs_dirs = crazylib.list_curren_dir(envs)
        this_path = crazylib.get_file_dir(__file__)

        for env_dir in envs_dirs:
            lib_dir=os.path.join(envs,env_dir,"lib")

            python_dir = crazylib.list_curren_dir(lib_dir,"python")
            site_package_dir = os.path.join(lib_dir,python_dir,"site-packages")

            crazylib_dir = os.path.join(site_package_dir,"crazylib")
            local_crazylib_dir = os.path.join(this_path,"../","packages/Crazylib/crazylib")

            cmd_rm ="rm -rf " +crazylib_dir
            cmd_link = "ln -s " + local_crazylib_dir +" " +crazylib_dir
            print(cmd_rm)
            print(cmd_link)

            os.system(cmd_rm)
            os.system(cmd_link)

def self_git_commit_test():
    import crazylib

    cmd_list=[
        "git status",
        # "git add readme.md ",
        # "git status",
        # "git commit -m 'modified reame.md'",
        # "git status"
    ]
    crazylib.git_managing(cmd_list)


def main():
    # deploy_link_to_annconda()
    self_git_commit_test()

