import sys
import os
from packages.crazylib import crazylib


def deploy_to_pypi():
    from packages.crazylib import crazylib

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

def git_config_user_info(user_name,user_passwd):
    from packages.crazylib import crazylib

    git_user_info_str=crazylib.ReadLines2OneLine("docs/git-credentials")
    git_user_info_str = git_user_info_str.replace("{username}",user_name)
    git_user_info_str = git_user_info_str.replace("{password}",user_passwd)

    envs_dict = os.environ
    home_path= envs_dict["HOME"]
    user_info_file = os.path.join(home_path,".git-credentials")
    crazylib.WriteStringLine(user_info_file,git_user_info_str)


    print("write git_user_info_str = ",git_user_info_str)
    info_str = crazylib.ReadLines2OneLine(user_info_file)
    print("read info_str = ",info_str)

def deploy_link_to_annconda(src_path,dst_name):

    envs_dict = os.environ
    home_path= envs_dict["HOME"]

    conda_dirs=[".conda","anaconda3"]
    for conda_dir in conda_dirs:
        conda_root=os.path.join(home_path,conda_dir)
        envs = os.path.join(conda_root,"envs")
        envs_dirs = crazylib.list_curren_dir(envs)

        for env_dir in envs_dirs:
            lib_dir=os.path.join(envs,env_dir,"lib")

            python_dir = crazylib.list_curren_dir(lib_dir,"python")
            site_package_dir = os.path.join(lib_dir,python_dir,"site-packages")

            dst_dir = os.path.join(site_package_dir, dst_name)

            cmd_rm ="rm -rf " +dst_dir
            cmd_link = "ln -s " + src_path +" " +dst_dir
            print(cmd_rm)
            print(cmd_link)

            os.system(cmd_rm)
            os.system(cmd_link)

def local_deploy():

    this_path = crazylib.get_file_dir(__file__)
    src_path = os.path.join(this_path, "../", "packages/crazylib/crazylib")
    dst_name="crazylib"
    deploy_link_to_annconda(src_path,dst_name)
    # git_config_user_info(user_name="",
    #                      user_passwd="")

def build_cpplib():
    this_path = crazylib.get_this_path(__file__)

    CPP_LIB_DIR="packages/CrazyCPPs"
    PYTHON_LIB_DIR="packages/crazylib"

    CPP_BUILD_DIR=os.path.join(CPP_LIB_DIR,"build")

    # os.system("rm -rf "+CPP_BUILD_DIR)
    # crazylib.makedirs(CPP_BUILD_DIR)


    os.chdir(CPP_BUILD_DIR)
    os.system("pwd")
    os.system("cmake -DCMAKE_BUILD_TYPE=RELEASE ..")
    os.system("make install -j8")


    print("----------build_cpplib done-----------")

def main():
    local_deploy()
    # build_cpplib()




