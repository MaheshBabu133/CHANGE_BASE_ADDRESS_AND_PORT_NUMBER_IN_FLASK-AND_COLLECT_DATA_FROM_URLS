from doctest import debug
from flask import Flask

FAI=Flask(__name__)


@FAI.route('/Renu')
def Renu():
    return '<center><h1>hii this is Renu<h1></center>'


@FAI.route('/maha/<na>')
def maha(na):
    return f'<center><h1>hii this is {na}<h1></center>'


if __name__=='__main__':
    FAI.run(debug=True,port=9000,host='192.168.2.108')